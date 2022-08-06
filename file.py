f = open('새파일.txt', 'r',encoding='utf-8')

#파일 여러 줄 읽어오기
line = f.readlines()
for i in line:
    print(i.strip("\n"))
f.close()

x = open("성영욱.txt","w",encoding="utf-8")
for b in range(1,11):
    data = "안녕하세요 저는 %d번째 영욱입니다.\n" %b
x.write(data)
x.close()