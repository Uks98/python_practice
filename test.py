bag = int(input("가방 가격을 입력해주세요."))
watch = int(input("신발 가격을 입력해주세요."))

result = bag + watch

if result >= 100000:
    print("할인율 30% 적용 상품입니다.")
elif result >= 50000 and result < 100000:
    print("할인율이 20% 적용 상품입니다.")
else:
    print("할인율 10% 적용 상품입니다.")
