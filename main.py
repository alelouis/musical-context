from scale import scale_transform, Scale

minor = scale_transform(Scale.to_minor)
major = scale_transform(Scale.to_major)
up = scale_transform(Scale.up)

s = Scale('C', 'major')
s.one()

with up(s, 1):
    s.one()
