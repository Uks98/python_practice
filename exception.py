



try:
    f = open("새파일.txt","r")
except Exception as e:
     print(e)
else:
    date = f.read()
    print(date)
    f.close
finally:
    f.close()
