import random

방향 = ["가위","바위","보"]

슈터 =  input("안내면 진다 가위 바위 보! ")
골키퍼 = random.choice(방향)

if 슈터 == "가위":
    if 골키퍼 =="가위":
        print("무승부입니다.")
    elif 골키퍼 =="바위":
        print("컴퓨터 승")
    elif 골키퍼 == "보":
        print("사용자 승")
elif 슈터 == "바위":
    if 골키퍼 =="가위":
        print("사용자 승")
    elif 골키퍼 =="바위":
        print("무승부입니다.")
    elif 골키퍼 == "보":
        print("컴퓨터 승")
elif 슈터 == "보":
    if 골키퍼 =="가위":
        print("컴퓨터 승")
    elif 골키퍼 =="바위":
        print("사용자 승")
    elif 골키퍼 == "보":
        print("무승부입니다.")

# 왼쪽 오른쪽 가운데가 아니라 이상한 걸 입력했으면 골대 밖으로 나간것으로 침 => else
