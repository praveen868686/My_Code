s = "(("


def valid_paranthesis(s):
    stack_list = []
    if len(s) == 1:
        return False
    opening_brackets = ['(', '[', '{']
    for i in range(len(s)):
        if s[i] in opening_brackets:
             stack_list.append(s[i])
        elif len(stack_list) == 0:
            return False
        elif s[i] == ')' and stack_list[len(stack_list)-1] == '(':
            stack_list.pop()
        elif s[i] == ']' and stack_list[len(stack_list)-1] == '[':
            stack_list.pop()
        elif s[i] == '}' and stack_list[len(stack_list)-1] == '{':
            stack_list.pop()
        else:
            return False
    if stack_list:
        return False
    return True


print(valid_paranthesis(s))
