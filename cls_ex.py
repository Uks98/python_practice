##homan클래스 생성

# class Human():
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
        
#     def __del__(self):
#         print("나의 죽음을 알리지마라")
#     def print_info(self,name,age,sex):
#         print("이름 {}, 나이{},성별 {}".format(self.name,self.age,self.sex))
#     def setInfo(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

# areum = Human("조아름",25,"여성")
# areum.print_info("조아름",25,"여성")

## stock 클래스 생성



# class Stock:
#     def __init__(self,stock_name,stock_code,per,pbr,dividend):

#         self.stock_name = stock_name
#         self.stock_code = stock_code
#         self.per = per
#         self.pbr = pbr
#         self.dividend = dividend

#     def set_name(self,stock_name):
#          self.stock_name = stock_name

#     def get_name(self):
#         print(self.stock_name)

#     def get_code(self):
#         print(self.stock_code)

#     def set_per(self,per):
#         self.per = per 

#     def set_pbr(self,pbr):
#         self.pbr = pbr

#     def set_dividend(self,dividend):
#         self.dividend = dividend
    
# list = []

# 삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
# 현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
# LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

# list.append(삼성)
# list.append(현대차)
# list.append(LG전자) 

# for i in list:
#     print(i.per,i.stock_code)


 ## 은행에 가서 계좌를 개설하면 은행이름, 예금주, 계좌번호, 잔액이 설정됩니다. Account 클래스를 생성한 후 생성자를 구현해보세요. 
 # 생성자에서는 예금주와 초기 잔액만 입력 받습니다. 
 # 은행이름은 SC은행으로 계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다.   

# import random

# class Account:
#     account_count = 0
#     def __init__(self, name, balance): #인자값에 self가 들어가면 인스턴스 메서드
#         self.deposit_count = 0
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"

#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)

#         num1 = str(num1).zfill(3)      # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)      # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)      # 1 -> '1' -> '0000001'
#         self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
#         Account.account_count += 1
        

#     @classmethod
#     def get_account_num(cls): #객체에 접근할 필요가 없는 메서드 => 클래스 메서드
#         print(cls.Account.account_count)
    
#     def deposit(self,money):
#         if money >= 1:
#             self.balance += money
#             self.account_count += 1
#         if self.account_count % 5 == 0:
#             self.balance = (self.balance * 1.01)
    
#     def withdraw(self,moneies):
#         if self.balance > moneies:
#            self.balance -= moneies

#     def display_info(self):
#         print("은행이름 {}\n예금주 {}\n계좌번호:{}\n잔고:{}원".format(self.bank,self.name,self.account_number,self.balance))

# data = []

# k = Account("KIM", 2000000)
# s = Account("Sung", 1200000)
# t = Account("Tiem", 2000)

# data.append(k)
# data.append(s)
# data.append(t)

# for i in data:
#     if i.balance >= 1000000:
#         i.display_info()


# class 차:
#     def __init__(self,바퀴,가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격
#     def 정보(self):
#         print("바퀴수:",self.바퀴,"가격:",self.가격)
    

# class 자전차(차):
#     def __init__(self,바퀴,가격,구동계):
#         self.바퀴 = 바퀴
#         self.가격 = 가격
#         self.구동계 = 구동계
    
#     def 정보(self):
#         super().정보()
#         print("구동계 ", self.구동계)

# ja = 자전차(2,1000,"시마노")
# ja.정보()

# class 부모:
#   def __init__(self):
#     print("부모생성")

# class 자식(부모):
#   def __init__(self):
#     print("자식생성")