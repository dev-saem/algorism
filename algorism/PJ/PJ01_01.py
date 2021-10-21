# 01. 괄호 검사

def check(sen):
    li = [] # 스택 사용
    for p in sen:
        if p == '(' or p == '{' or p == '[':
            li.append(p)
        elif p == ')' or p == '}' or p == ']':
            if len(li) == 0:
                return "No"
            else:
                p_pop = li.pop()
                if (p_pop == '(' and p != ')') or (p_pop == '{' and p != '}') or (p_pop == '[' and p != ']'):
                    return "No"

    if len(li) == 0:
        return "Yes"
    return "No"

t = int(input())
for i in range(t):
    sen = input()
    print(check(sen))