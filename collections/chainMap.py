from collections import ChainMap

dict1 = { 'a' : 1, 'b' : 2 }
dict2 = { 'c' : 3, 'b' : 4 }
chain_map = ChainMap(dict1, dict2)
print(chain_map.maps)
# [{'a': 1, 'b': 2}, {'c': 3, 'b': 4}]
print(chain_map['a'])
# 1
dict2['c'] = 5
print(chain_map.maps) # shows list of maps


print (list(chain_map.keys()))
print (list(chain_map.values()))
# ['c', 'b', 'a'] only one b
# [5, 2, 1]  value of 1st b retains

dict3 = {'e' : 5, 'f' : 6}
new_chain_map = chain_map.new_child(dict3)
print(new_chain_map)
# ChainMap({'e': 5, 'f': 6}, {'a': 1, 'b': 2}, {'c': 5, 'b': 4})