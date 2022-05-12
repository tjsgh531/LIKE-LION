import random

randNum = random.randrange(1, 101)
temp = 101
count = 0
maxnum = 100
minnum = 1

while True:
    count+=1
    temp = random.randint(minnum, maxnum)
    if randNum > temp:
        minnum = temp+1
    elif randNum < temp:
        maxnum = temp-1
    else:
        break
for i in range(count):
    oppor = count - i
    print(f"남은 기회 : {oppor}")
    userNum = int(input("1부터 100사이 숫자 입력해 주세요 : "))
    if userNum == randNum:
        print("옴닉에게 이긴 당신!!!!\n새로운 영웅은 언제나 환영이야!!")
        break
    elif userNum > randNum:
        print('커요')
    else:
        print("작아요")
else:
    print("\n당신은 컴퓨터 보다 저능합니다\n 옴닉사태에 대비하세요.\n")
    print(f"컴퓨터가 걸린 횟수 : {count}")
    print(f"정답 : {randNum}")
