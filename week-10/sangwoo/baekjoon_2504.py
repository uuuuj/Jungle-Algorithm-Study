import sys

input = sys.stdin.readline
string = input().rstrip()

stack = []
isInValid = False

for s in string:
    if s in '([':
        stack.append(s)

    elif s == ')':
        if not stack:
            isInValid = True
            break
        if stack[-1] == '(':
            stack.pop()
            stack.append(2)
        else:
            value = 0
            while stack:
                cur = stack.pop()
                if cur == '(':
                    stack.append(value * 2)
                    break
                elif isinstance(cur, int):
                    value += cur
                else:
                    isInValid = True
                    break
            else:
                # '('을 못 만남
                isInValid = True
                break

    elif s == ']':
        if not stack:
            isInValid = True
            break
        if stack[-1] == '[':
            stack.pop()
            stack.append(3)
        else:
            value = 0
            while stack:
                cur = stack.pop()
                if cur == '[':
                    stack.append(value * 3)
                    break
                elif isinstance(cur, int):
                    value += cur
                else:
                    isInValid = True
                    break
            else:
                # '['을 못 만남
                isInValid = True
                break

# 스택에 숫자 외에 괄호가 남아 있다면 올바르지 않은 괄호열
for item in stack:
    if not isinstance(item, int):
        isInValid = True
        break

print(0 if isInValid else sum(stack))