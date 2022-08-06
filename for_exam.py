print("[메뉴를 입력해주세요]\n 1.게임시작 2.랭킹보기 3.종료하기")

while True:
    die = int(input(""))
    if die == 1:
        print("게임을 시작합니다.")
        break
    elif die == 2:
        print("랭킹 창으로 이동합니다.")
    elif die == 3:
        print("게임을 종료합니다.") 
        break
    else:
        print("다시 입력해주세요")