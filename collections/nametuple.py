from collections import namedtuple

Student=namedtuple('Student','fname,lname,age')

s1=Student("Pritam","Sarkar","25")
s2=Student._make(["Eshani","Jas","26"])
print(s1.fname,s2.fname)
# Pritam Eshani

s3=s2._asdict()
print(s3)
# OrderedDict([('fname', 'Eshani'), ('lname', 'Jas'), ('age', '26')])

s4=s2._replace(age="20")
print(s2)
print(s4)
# Student(fname='Eshani', lname='Jas', age='26')
# Student(fname='Eshani', lname='Jas', age='20')