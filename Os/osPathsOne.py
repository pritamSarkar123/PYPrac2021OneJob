import os

print(os.path.abspath(__file__))

print(os.path.dirname(__file__))

print(os.path.basename(__file__))

# C:\Users\pritam\Desktop\pyPracforJob\Os\osPathsOne.py
# C:\Users\pritam\Desktop\pyPracforJob\Os
# osPathsOne.py

print(os.path.exists(__file__)) # True

print(os.path.join(os.path.dirname(__file__),"abcs"))
# C:\Users\pritam\Desktop\pyPracforJob\Os\abcs

