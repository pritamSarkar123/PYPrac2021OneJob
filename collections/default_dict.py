from collections import defaultdict

default_dict_obj=defaultdict(int)

name_list="Mike John Mike Anna Mike John John Mike Mike Britney Smith Anna Smith".split()

for name in name_list:
	default_dict_obj[name]+=1

print(default_dict_obj)
# defaultdict(<class 'int'>, {'Mike': 5, 'John': 3, 'Anna': 2, 'Britney': 1, 'Smith': 2})
print(default_dict_obj['Mike'])
# 5
original_dict=dict(default_dict_obj)
print(original_dict)
# {'Mike': 5, 'John': 3, 'Anna': 2, 'Britney': 1, 'Smith': 2}

