
## 사용자가 입력한 키값에 따라 값을 출력
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}

# speak = str(input("계절을 입력하세요"))
# if speak in fruit.keys():
#     print(fruit[speak])
# else:
#     print("데이터가 없습니다.")

## # 딕셔너리 벨류에 해당하는 텍스트가 있을경우 true반환 
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# speak1 = str(input("과일을 입력하세요"))
# if speak1 in fruit.values():
#     print("정답입니다.")
# else:
#     print("오답입니다.") 


# speak2 = str(input("알파벳을 입력해주세요"))
# if speak2.islower:
#     print(speak2.upper())
# else:
#     print(speak2.lower()) #소문자 입력시 대문자 ,대문자 입력시 소문자

# 환율 = {"달러": 1167, 
#         "엔": 1.096, 
#         "유로": 1268, 
#         "위안": 171}
# user = input("입력: ")
# num, currency = user.split() #[100 , 달러] 구분
# print(float(num) * 환율[currency], "원")

## 124번 사용자가 입력한 가장 큰 숫자 출력 
# x = input("숫자입력")
# y = input("숫자입력")
# z = input("숫자입력")

# if(x >= y and x >= z):
#     print(int(x))
# elif(y >= x and y >=z):
#     print(int(y))
# else:
#     print(int(z))

## 125번
# user_phone = input(str("번호를 입력하세요"))

# if(user_phone in "011"):
#     print("당신은 SKT 사용자입니다.")
# elif(user_phone in "016"):
#      print("당신은 KT 사용자입니다.")
# elif(user_phone in "019"):
#      print("당신은 LG 사용자입니다.")
# else:
#     print("알 수 없습니다.")

## 126번 주민번호로 성별 알아내기
# speak4 = input(str("주민번호를 입력해주세요"))
# privacy_num,privacy_num2 = speak4.split("-")
# if(privacy_num2[0] == "1" or privacy_num2[0] == "3"): #"-" 로 구분된 뒷번호의 첫째번호를 가져오는 구문
#     print("남자입니다.")
# elif(privacy_num2[0] == "2" or privacy_num2[0] == "4"):
#     print("여성입니다.")

# import requests

# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

# opening_price = int(btc["opening_price"])
# closing_price = btc["closing_price"]
# min_price = btc["min_price"]
# max_price = int(btc["max_price"])
# changing_price = int(max_price) - int(min_price)

# if((opening_price + changing_price) < max_price):
#     print("상승장")
# else:
#     print("하락장")
# print(btc)

## 반복문 예제

## 141번 부가세 10원추가해 출력
# 리스트 = [100, 200, 300]

# for x in 리스트:
#     print(x + 10)

## 142번
# 리스트1 = ["김밥", "라면", "튀김"]

# for x in 리스트1:
#     print("오늘의메뉴 : ",x)

## 143번 각 요소 길이 출력
# 리스트3 = ["SK하이닉스", "삼성전자", "LG전자"]

# for x in 리스트3:
#     print(len(x))

## 148 첫번째 요소부터 출력
# 리스트4 = ["가", "나", "다", "라"]

# for x in 리스트4[1:]:
#     print(x)

# 149 음수만 출력
# list8 = [3, -20, -3, 44]
# for x in list8:
#    if x < 0:
#     print(x)

## 150 3의 배수만 출력
# num_list = [3, 100, 23, 44]

# for x in num_list:
#     if x % 3 == 0:
#         print(x)

## 151 3의 배수 중 20보다 작은 수 출력
# num_list1 = [13, 21, 12, 14, 30, 18]
# for x in num_list1:
#     if x % 3 == 0 and x < 20:
#         print(x) 

## 152 3글자 이상의 문자만 출력
# text_list = ["I", "study", "python", "language", "!"]

# for x in text_list:
#     if(len(x) >= 3):
#         print(x)

## 157 소문자 리스트에 첫글자를 대문자로 출력

# animal = ['dog', 'cat', 'parrot']
# for x in animal:
#     print(x[0].upper() + animal[1:])

## 158 확정자를 지우고 출력하라
# list9 = ['hello.py', 'ex01.py', 'intro.hwp']
# for x in list9:
#     text1,text2 = x.split(".")
#     print(text1)

##확장자가 .h인 파일 이름을 출력하라
# listPie = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for x in listPie:
#     t1 = x.split(".")
#     if t1[1] == "h":
#         print(x)

    ##161번 0에서 99까지 한라인에 각각 출력
# for x in range(0,100):
#     print(x)

##  월드컵은 4년에 한 번 개최된다. range()를 사용하여 2002~2050년까지 중 월드컵이 개최되는 연도를 출력하라.

# for i in range(2002,2051,4):
#     print("월드컵 개최 년도는", i)

## 163.  1부터 30까지의 숫자 중 3의 배수를 출력하라.

# for i in range(1,31):
#     if i % 3 == 0:
#      print(i)

## 165 소수출력
# for x in range(10):
#     print(x/10)

##166 구구단 3단 출력
# for x in range(1,10):
#     print(x * 3)
##구구단 3단을 출력하라. 단 홀수 번째만 출력한다.

# for x in range(1,10):
#     if x % 2 == 1:
#         print(x * 3)

##1~10까지의 숫자에 대해 모두 더한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.

# count = 0
# for x in range(1,11):
#    count += x
# print(count)

##아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
# price_list = [32100, 32150, 32000, 32500]
# for x in range(len(price_list)):
#     print(price_list[x])

## 아래 표에서 하나의 열을 하나의 리스트로, 총 2개의 리스트를 갖는 이차원 리스트 stock을 정의하라.
# stock = [ ["시가",100,200,300],["종가",12,10,31]]

##아래 표를 stock 이름의 딕셔너리로 표현하라.시가를 key로 저장하고, 나머지 같은 열의 데이터를 리스트로 저장해서 value로 저장한다. 종가 역시 key로 저장하고 나머지 같은 열의 데이터를 리스트로 저장해서 value로 저장한다.

# stock1 = {"시가":[100,200,300],"종가":[80,210,320]}
# print(stock1["시가"])

##185 이중for문
# apart2 = [ [101, 102], [201, 202], [301, 302] ]

# for x in apart2:
#     for y in x:
#         print(y,"호")

## 186
# apart4 = [ [101, 102], [201, 202], [301, 302] ]

# for x in apart4:
#     for y in x:
#         print(y,"호 \n-----")

## 187 두개씩 출력 인덴트 주의
# apart8 = [ [101, 102], [201, 202], [301, 302] ]

# for x in apart8:
#     for y in x:
#         print(y)
#     print("-----")

## data에는 매수한 종목들의 OHLC (open/high/low/close) 가격 정보가 바인딩 되어있다.
## 수수료를 0.014 %로 가정할 때, 각 가격에 수수료를 포함한 가격을 한라인에 하나씩 출력하라.
# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]

# for x in data:
#    for tax in x:
#         print("수수료 적용 금액",tax * 0.014)

##ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 종가가 150원보다 큰경우에만 종가를 출력하라.

# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]

# for x in ohlc[1:]: ## 첫번째 리스트를 제외한다. 
#     print(x[3])
## ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 종가가 150원보다 큰경우에만 종가를 출력하라.
# ohlc1 = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for x in ohlc1[1:]:
#     if x[3] > 150:
#         print(x[3])

##ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 종가가 시가 보다 크거나 같은 경우에만 종가를 출력하라.

# ohlc3 = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]

# for x in ohlc3[1:]:
#     if x[3] >= x[0]:
#         print(x[3])

##리스트에는 3일 간의 ohlc 데이터가 저장돼 있다. 종가가 시가보다 높은 날의 변동성 (고가 - 저가)을 화면에 출력하라.

# ohlc4 = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]

# for x in ohlc4[1:]:
#     if x[3] > x[0]:
#         y =  x[1] - x[2]
# print(y)