precedence = {"*":2,"/":2,"+":1,"-":1} 

def operand(character):
    return character not in {"(",")","+","-","*","/"}

def infix_to_postfix_basic(expression):
    
    stack = []
    
    ans = []
    
    for character in expression:
        if character == "(":
            stack.append(character)
        elif operand(character):
            ans.append(character)
        elif character == ")":
            while stack[-1] != "(":
                ans.append(stack.pop())
            stack.pop()
        else:
            if not stack or stack[-1] == "(" or precedence[stack[-1]] < precedence[character]:
                stack.append(character)
            else:
                while stack and precedence[stack[-1]] >= precedence[character]:
                    ans.append(stack.pop())
                stack.append(character)
                
    while stack:
        ans.append(stack.pop())
        
    return "".join(ans)

expression = "a*b/(d+c)*e"
print(infix_to_postfix_basic(expression))
expression = "a+b*(d+e)"
print(infix_to_postfix_basic(expression))


def postfic_evaluation(expression):
    stack = []
    for character in expression:
        if operand(character):
            stack.append(character)
        else:
            second_char = stack.pop()
            first_char = stack.pop()
            stack.append("({}{}{})".format(first_char,character,second_char))
    return stack[0]
        


expression = "ab*dc+/e*"
print(postfic_evaluation(expression))
expression = "abde+*+"
print(postfic_evaluation(expression))