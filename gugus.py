
h = int(input("숫자를 입력하면 구구단으로 출력합니다."))

def gugu(a):
    result = []
    i = 1
    while i < 10:
        result.append(a*i)
        i = i + 1 
    return result

print(gugu(h))
