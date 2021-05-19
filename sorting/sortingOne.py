import functools
cars1 = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
cars2 = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
def myCompare(a,b):
    return 1 if a['year']>b['year'] else -1 if a['year']<b['year'] else 0

cars2.sort(key=functools.cmp_to_key(myCompare),reverse=True)


cars1.sort(key=lambda x:x['year'],reverse=True)

print(cars1)
print(cars2)