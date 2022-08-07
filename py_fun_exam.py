
#"비트코인" 문자열을 화면에 출력하는 print_coin() 함수를 정의하라.
def print_coin():
    print("비트코인")

#"비트코인" 문자열을 100번 화면에 출력하는 print_coins() 함수를 정의하라.

def print_coin100():
    for i in range(100):
        print("비트코인")
print_coin100()

#하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수를 정의하라.

def smile_pring(smile):
    print(smile,":D")
smile_pring("안녕하세요!")

#두 개의 숫자를 입력받아 두 수의 합을 출력하는 print_sum 함수를 정의하라.

def x_sum(x,y):
    return x*y

print(x_sum(2,3))

#두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 print_arithmetic_operation 함수를 작성하라.

def print_arithmetic_operation(a,b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)

print_arithmetic_operation(10,5)

#세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의하라. 단 if 문을 사용해서 수를 비교하라.

def print_max(a,b,c):
    if a>=b or a>=c:
        print(a,"이 숫자가 제일 큰 수")
    elif b>=a or b>=c:
        print(b,"이 숫자가 제일 큰 수")
    else:
        print(c,"제일 큰 수 입니다.")

print_max(10,20,21)

#입력된 문자열을 역순으로 출력하는 print_reverse 함수를 정의하라.

def print_reverse(reverse):
    print(reverse[::-1])

#성적 리스트를 입력 받아 평균을 출력하는 print_score 함수를 정의하라.

def print_score(list):
        for x in list:
         y =  x/len(list)  
        print(y)

print_score([10,10,10])

#하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.

def print_even(lists):
    for x in lists:
        if x % 2 ==0:
            print(x)

print_even ([1, 3, 2, 10, 12, 11, 15])

# 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의하라.

def print_keys(dics):
    print(dics.keys())

print_keys({"이름":"김말똥", "나이":30, "성별":0})

# my_dict에는 날짜를 키값으로 OHLC가 리스트로 저장돼 있다. my_dict와 날짜 키값을 입력받아 OHLC 리스트를 출력하는 print_value_by_key 함수를 정의하라.
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

def print_value_by_key(dict,date):
        print(dict[date])

print_value_by_key(my_dict,"10/27")

#문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.

def make_url(url):
    return "www."+url+".com"

x = make_url("naver")
print(x)

#숫자로 구성된 하나의 리스트를 입력받아, 짝수들을 추출하여 리스트로 반환하는 pickup_even 함수를 구현하라.
list = []
def pickup_even(lists):
    for x in lists:
        if x % 2 == 0:
            list.append(x)
    return list

y = pickup_even([3, 4, 5, 6, 7, 8])
print(y)

#콤마가 포함된 문자열 숫자를 입력받아 정수로 변환하는 convert_int 함수를 정의하라.

def convert_int(strs):
    change_str = strs.replace(",","")
    convert_int = int(change_str)
    return convert_int

x = convert_int("1,234,567")
print(x)
print(type(x))

