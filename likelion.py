import time
import random

print("""
  ___          _                    _   _____                         _               
 / _ \        (_)                  | | /  __ \                       (_)              
/ /_\ \ _ __   _  _ __ ___    __ _ | | | /  \/ _ __   ___   ___  ___  _  _ __    __ _ 
|  _  || '_ \ | || '_ ` _ \  / _` || | | |    | '__| / _ \ / __|/ __|| || '_ \  / _` |
| | | || | | || || | | | | || (_| || | | \__/\| |   | (_) |\__ \\__ \| || | | || (_| |
\_| |_/|_| |_||_||_| |_| |_| \__,_||_|  \____/|_|    \___/ |___/|___/|_||_| |_| \__, |
                                                                                 __/ |
                                                                                |___/ 
""")
print("~ 모여봐요 멋사의 숲 ~\n")

name = input("당신의 이름은? ")  # 이곳을 채우세요
island = input("섬 이름은? (oo섬으로 입력됩니다.) ")  # 이곳을 채우세요

print(name + "님 반가워요! " + island + "섬에 오신것을 환영합니다-!")
time.sleep(1)

animal = {'릴리안': 0, '탁호': 0, '미첼': 0, '리처드': 0}
my_bell = 3000
my_pocket = []
store = {'가습기': 1400, '강아지 인형': 2400, '강의실 책상': 2500, '몬스테라': 1700}

action_boolean = 1

# 4가지 반복하기
while action_boolean:
    print("\n어떤 것을 해볼까요?")
    answer_action = input("0. 종료 1. 상점가기 2. 주민 찾아가기 3. 나무 흔들기 4. 정보 확인하기 ")

    # 0. 게임 종료
    if answer_action == "0":
        time.sleep(0.8)
        print("\n게임을 종료합니다…")
        time.sleep(0.8)
        print("다음에 또 놀러오세요!")
        time.sleep(1)
        action_boolean = 0

    # 1. 상점가기를 선택한 경우
    elif answer_action == "1":
        time.sleep(0.8)
        print("\n상점에 온걸 환영해구리")
        time.sleep(0.8)
        print("현재 상점에는 이런 물건들이 있어구리!")
        time.sleep(0.8)

        i=1
        for key,value in store.items():
            print(str(i) + ". " + str(key) + ":"+str(value)+ "벨")
            i+=1
            time.sleep(0.5)

        answer_store1_buy = int(input("어떤 물건을 구입하겠어구리?(숫자로 입력) "))
        time.sleep(0.3)
        #딕셔너리와 리스트 사용
        choose_store= store[list(store.keys())[answer_store1_buy-1]]

        if my_bell>choose_store:
            my_bell -= choose_store
            print(" ")

            print(list(store.keys())[answer_store1_buy-1]+"을(를) 구입하셨습니다!")
            time.sleep(0.6)
            print("남은 벨: "+str(my_bell))
            time.sleep(1)

            #주머니에 append 추가함수로 넣고 del 키로 빼기
            my_pocket.append(list(store.keys())[answer_store1_buy-1])
            del store[list(store.keys())[answer_store1_buy-1]]

        else:
            time.sleep(1)
            print("\n 어엇..돈이 없다 구리...다음에 사야할 것 같다구리")
            time.sleep(1)


    # 2. 주민 찾아가기를 선택한 경우
    elif answer_action == "2":
        time.sleep(0.8)
        print("\n우리 마을에 있는 주민이야")

        i=1
        for key,value in animal.items():
            print(str(i)+ ". "+str(key))
            i+=1
            time.sleep(0.4)
        answer_animal = int(input("어떤 주민을 찾아갈까? "))

        print(list(animal.keys())[answer_animal-1]+"에게 무엇을 할까? ")
        answer_animal_action = int(input("1. 말걸기 2. 선물하기 3. 때리기 "))

        #주민을 골라 말걸기 등등 변수 choose_animal
        choose_animal = (list(animal.keys())[answer_animal-1])

        # 2-1. 말걸기를 선택한경우
        if answer_animal_action == 1:
            if choose_animal == "릴리안":
                time.sleep(0.8)
                print("릴리안: 어머 "+name+"왔구나~ 반가워! \n 어제는 어찌나 비가 오던지 춥더라")
                time.sleep(0.4)
                print(name+"도 감기 조심해!! 그렇지 뭐")
                time.sleep(0.8)
                animal[choose_animal]+=1
                print(choose_animal , "친밀도 + 1")
                time.sleep(1)
            elif choose_animal =="탁호":
                time.sleep(0.8)
                print("탁호: 안녀엉~ " + name + "아~ 반가워어~")
                time.sleep(0.4)
                print(name + "아 나 오늘 저녁은 뭘 먹을지 너무 고민이 돼~ 약히")
                time.sleep(0.8)
                animal[choose_animal] += 1
                print(choose_animal, "친밀도 + 1")
                time.sleep(1)
            elif choose_animal =="미첼":
                time.sleep(0.8)
                print("미첼: " + name + "아~! 반가워!오늘 날씨 되게 춥지 않아?")
                time.sleep(0.4)
                print("마구마구 산책을 하고싶은데 말이야 동글")
                time.sleep(0.8)
                animal[choose_animal] += 1
                print(choose_animal, "친밀도 + 1")
                time.sleep(1)
            elif choose_animal =="리처드":
                time.sleep(0.8)
                print("리처드: " + name + "야아~ \n 나무를 흔들었더니 100벨이 나왔어어~")
                time.sleep(0.4)
                print(name + "(이)도 한 번 흔들어봐아~ 그래유")
                time.sleep(0.8)
                animal[choose_animal] += 1
                print(choose_animal, "친밀도 +1")
                time.sleep(1)

        # 2-2. 선물하기를 선택한 경우
        elif answer_animal_action == 2:
            #선물을 줄 수 없는 경우(길이가 0일때로 하면 쉽게 짤 수 있음)
            if len(my_pocket)==0:
                time.sleep(0.3)
                print("\n주머니에 아무것도 없어..")
                time.sleep(1)
            #줄 수 있을 때
            else:
                time.sleep(0.3)
                print("내 주머니에 이렇게 있어\n")

                j =1
                for i in my_pocket:
                    print(j, ".",i)
                    j+=1
                    time.sleep(0.3)

                present_animal_answer = int(input("\n어떤 것을 선물할까?(숫자로 입력) "))
                present_animal = my_pocket[present_animal_answer-1]
                time.sleep(0.5)
                print(choose_animal,"에게",present_animal,"을(를) 선물했다!")
                my_pocket.remove(present_animal)

                time.sleep(0.6)
                animal[choose_animal]+=5
                print(choose_animal,"친밀도 +5")
                time.sleep(1)

        # 2-3. 떄리기를 선택한 경우
        elif answer_animal_action == 3:
            print(choose_animal,": 으악 왜 때려...그러지 마")
            time.sleep(0.6)

            print(choose_animal,"을(를) 때렸다")
            time.sleep(0.6)
            animal[choose_animal]-=1
            print(choose_animal,"친밀도 -1")
            time.sleep(1)


    # 3. 나무 흔들기를 선택한 경우
    elif answer_action == "3":
        print("나무를 흔듭니다.")
        time.sleep(0.8)
        #랜덤함수로
        result = random.choice(["벌","사과","100벨"])

        # 100벨이 떨어질경우
        if result == "100벨":
            print("와, ",result,"이 떨어졌다!")
            my_bell +=100
            time.sleep(1)
            print("남은 벨: "+str(my_bell))

        # 사과가 떨어질경우
        elif result == "사과":
            print("앗, ",result,"가 떨어졌다!")
            time.sleep(1)
            my_pocket.append("사과")
            print("내 주머니에 사과를 추가하였습니다!")

        # 벌이 나타날경우
        elif result == "벌":
            print("응...?")
            time.sleep(1)
            print("벌이 나타났습니다!!")
            time.sleep(1)
            print("벌에게 쏘였어..아파..")
            time.sleep(1)

    # 4. 정보보기를 선택한 경우
    elif answer_action == "4":
        print("\n<내 정보>")
        time.sleep(1)

        # 이름 출력
        print("- 이름: ",name)
        time.sleep(0.4)

        # 남은 벨 출력
        print("- 남은 벨: ",my_bell)
        time.sleep(0.4)

        # 주머니 출력
        if len(my_pocket)==0:
            print("- 내 주머니: 비어있음 ")
        else:
            print("- 내 주머니: ",my_pocket)
        time.sleep(0.4)

        # 주민 친밀도 출력
        print("- 주민과의 친밀도: ")
        i=1
        time.sleep(0.8)
        for key,value in animal.items():
            print(str(i)+". "+str(key)+": "+str(value))
            i +=1
            time.sleep(0.8)
        time.sleep(1)
        # 잘못된 입력을 했을경우
    else:
        print("\n잘못된 입력입니다.다시 입력해주세요!")
        time.sleep(1)
