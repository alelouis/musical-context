class Chord:
    def __init__(self, quality=None, intervals=None, root=None):
        self.quality = quality
        self.intervals = intervals
        self.root = root

    def __repr__(self) -> str:
        return f'Chord({self.root}, {self.quality}, {self.intervals})'


def major(root) -> Chord:
    return Chord('maj', [1, 4, 7], root)


def minor(root) -> Chord:
    return Chord('min', [1, 3, 7], root)


def dim(root) -> Chord:
    return Chord('dim', [1, 3, 6], root)


def aug(root) -> Chord:
    return Chord('aug', [1, 4, 8], root)
