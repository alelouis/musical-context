from contextlib import contextmanager

import chord as chord_mod


def pdebug(func):
    def f(*args, **kwargs):
        r = func(*args, **kwargs)
        print(r)
        return r

    return f


class CanonicalScale:
    def __init__(self, qualities):
        self.chords = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
        self.qualities = qualities
        for attr, func in zip(self.chords, self.qualities):
            setattr(self, attr, getattr(chord_mod, func))

    def __repr__(self):
        return '\n'.join([f'{chord}: {quality}' for chord, quality in zip(self.chords, self.qualities)])


class Scale:
    def __init__(self, root, mode, debug=False):
        self.scale = None
        self.root = root
        self.mode = mode
        self.debug = debug

        for key, value in canonical_scales.items():
            setattr(self.__class__, key, value)

        self.update_scale()

    def update_scale(self):
        self.scale = getattr(self, self.mode)

    def __repr__(self):
        return f'Scale({self.root}, {self.mode})'

    def to_minor(self):
        self.mode = 'minor'
        self.update_scale()

    def to_major(self):
        self.mode = 'major'
        self.update_scale()

    def up(self, amount):
        self.root += amount

    @pdebug
    def one(self):
        return self.scale.one()

    @pdebug
    def two(self):
        return self.scale.two()

    @pdebug
    def five(self):
        return self.scale.five()


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

major_scale = CanonicalScale(major_scale_qualities)
minor_scale = CanonicalScale(minor_scale_qualities)

canonical_scales = {'minor': minor_scale, 'major': major_scale}
