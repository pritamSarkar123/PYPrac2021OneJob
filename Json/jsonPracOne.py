import json

abc=None

with open('myJson.json','r') as f:
	abc=json.load(f)
	print(abc,type(abc))
# {'hello': 'world', 'fuck': 'you'} <class 'dict'>

with open('myJson.txt','w') as f:
	json.dump(abc,f,ensure_ascii=False)

with open('myJson.txt','r') as f:
	abc=json.load(f)
	print(abc,type(abc))
# {'hello': 'world', 'fuck': 'you'} <class 'dict'>

# -------------------------------------------------------------------

with open('myJsonList.json','r') as f:
	abc=json.load(f)
	print(abc,type(abc))
# [{'hello': 'world', 'fuck': 'you'}, {'hello': 'world', 'fuck': 'you'}, {'hello': 'world', 'fuck': 'you'}, {'hello': 'world', 'fuck': 'you'}] <class 'list'>

with open('myJsonList.txt','w') as f:
	json.dump(abc,f,ensure_ascii=False)

with open('myJsonList.txt','r') as f:
	abc=json.load(f)
	print(abc,type(abc))
# [{'hello': 'world', 'fuck': 'you'}, {'hello': 'world', 'fuck': 'you'}, {'hello': 'world', 'fuck': 'you'}, {'hello': 'world', 'fuck': 'you'}] <class 'list'>

# loads <- load from string
# dumps <- dump to string
# these are two common methods and easy to use

person={
	"name":"Pritam Sarkar",
	"age":26,
	"gender":"M",
	"married":False
}
person_str=json.dumps(person,ensure_ascii=False)
print(person,type(person))
print(person_str,type(person_str))
# {'name': 'Pritam Sarkar', 'age': 26, 'gender': 'M', 'married': False} <class 'dict'>
# {"name": "Pritam Sarkar", "age": 26, "gender": "M", "married": false} <class 'str'>
new_person=json.loads(person_str)
print(new_person,type(new_person))

# {'name': 'Pritam Sarkar', 'age': 26, 'gender': 'M', 'married': False} <class 'dict'>