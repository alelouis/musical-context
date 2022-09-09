from contextlib import contextmanager
from collections import deque
from typing import Callable, Tuple, Any, Dict, List

import chord as chord_mod
from chord import Chord


def pdebug(func: Callable) -> Callable:
    def f(*args: Tuple[Any], **kwargs: Dict[str, Any]):
        r = func(*args, **kwargs)
        print(r)
        return r

    return f


class CanonicalScale:
    def __init__(self, qualities: List[str], root: str):
        self.chords = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
        self.root = root
        self.qualities = qualities
        self.update_root(0)

    def __repr__(self) -> str:
        return '\n'.join([f'{chord}: {quality}' for chord, quality in zip(self.chords, self.qualities)])

    def update_root(self, amount):
        self.notes = deque(['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        self.notes.rotate(-amount)

        for attr, func, note in zip(self.chords, self.qualities, self.notes):
            setattr(self, attr, getattr(chord_mod, func)(note))


class Scale:
    def __init__(self, root: str, mode: str, debug: bool = False):
        self.scale = None
        self.root = root
        self.mode = mode
        self.debug = debug

        for key, value in canonical_scales.items():
            setattr(self.__class__, key, value(self.root))

        self.update_scale()

    def update_scale(self):
        self.scale = getattr(self, self.mode)

    def __repr__(self) -> str:
        return f'Scale({self.root}, {self.mode})'

    def to_minor(self):
        self.mode = 'minor'
        self.update_scale()

    def to_major(self):
        self.mode = 'major'
        self.update_scale()

    def up(self, amount: int):
        self.scale.update_root(amount)

    @pdebug
    def one(self) -> Chord:
        return self.scale.one

    @pdebug
    def two(self) -> Chord:
        return self.scale.two

    @pdebug
    def five(self) -> Chord:
        return self.scale.five


def scale_transform(func):
    @contextmanager
    def transform(scale, *args):
        root, mode = scale.root, scale.mode
        try:
            func(scale, *args)
            yield
        finally:
            scale.__init__(root, mode)

    return transform


major_scale_qualities = ['major', 'minor', 'minor', 'major', 'major', 'minor', 'dim']
minor_scale_qualities = ['minor', 'dim', 'major', 'minor', 'minor', 'major', 'major']

major_scale = lambda root: CanonicalScale(qualities=major_scale_qualities, root=root)
minor_scale = lambda root: CanonicalScale(qualities=minor_scale_qualities, root=root)

canonical_scales = {'minor': minor_scale, 'major': major_scale}
