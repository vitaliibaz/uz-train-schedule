from sys import path
path.append('../src')

from travel import Travel

r = Travel('Kyiv', 'Oslo')
assert r.from_city == 'Kyiv'
assert r.to_city == 'Oslo'
