def major():
    return Chord('maj', [1, 4, 7])


def minor():
    return Chord('min', [1, 3, 7])


def dim():
    return Chord('dim', [1, 3, 6])


def aug():
    return Chord('aug', [1, 4, 8])


class Chord:
    def __init__(self, quality=None, intervals=None):
        self.quality = quality
        self.intervals = intervals

    def __repr__(self):
        return f'Chord({self.quality}, {self.intervals})'

