#load pandas as pd
import pandas as pd

names = pd.Series(['tracer Song', 'line Park', 'mac Kim'])

#lower()
print(names.map(str.lower))
'''
0    tracer song
1      line park
2        mac kim
dtype: object
'''

#same
print(names.str.lower())
'''
0    tracer song
1      line park
2        mac kim
dtype: object
'''

#upper()
print(names.apply(str.upper))
'''
dtype: object
0    TRACER SONG
1      LINE PARK
2        MAC KIM
'''

print(names.str.upper())
'''
dtype: object
0    TRACER SONG
1      LINE PARK
2        MAC KIM
'''

#title()
print(names.map(str.title))
'''
dtype: object
0    Tracer Song
1      Line Park
2        Mac Kim
dtype: object
'''

print(names.str.title())
'''
dtype: object
0    Tracer Song
1      Line Park
2        Mac Kim
dtype: object
'''

#split()
print(names.map(str.split))
'''
0    [tracer, Song]
1      [line, Park]
2        [mac, Kim]
dtype: object
'''

print(names.str.split())
'''
0    [tracer, Song]
1      [line, Park]
2        [mac, Kim]
dtype: object
'''