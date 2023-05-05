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

name = input("당신의 이름은 무엇인가요? ")
island = input("당신의 섬의 이름은 무엇인가요? (ㅇㅇ섬으로 입력됩니다) ")

print(name + "님 반가워요! " + island + "섬에 오신것을 환영합니다-!")
time.sleep(1)

animal = {'릴리안': 0, '탁호': 0, '미첼': 0, '리처드': 0}
my_bell = 3000
my_pocket = {'가습기': 0, '강아지 인형': 0, '강의실 책상': 0, '몬스테라': 0, '사과': 0}
store = {'가습기': 1400, '강아지 인형': 2400, '강의실 책상': 2500, '몬스테라': 1700}

action_boolean = 1

# 4가지 반복하기
while action_boolean:
    print("\n어떤 것을 해볼까요?")
    answer_action = input("0. 종료 1. 상점가기 2. 주민 찾아가기 3. 나무 흔들기 4. 정보 확인하기 ")
    
    # 0. 게임 종료
    if answer_action == "0":
        print("게임을 종료합니다.")
        action_boolean = 0

    # 1. 상점가기를 선택한경우
    elif answer_action == "1":
        print("\n상점에 온 걸 환영해구리!")
        print("현재 상점에는 이런 물건이 있어구리")
        for i in store:
            print(i + ": " + str(store[i]) + "벨")
        answer_store = input("\n어떤 물건을 구입하겠어구리? (숫자로 입력) ")
        # 1-1. 가습기를 선택한 경우
        if answer_store == "1":
            if my_bell >= store['가습기']:
                my_bell = my_bell - store['가습기']
                my_pocket["가습기"] += 1
                print("가습기를 구매하셨습니다.")
                print("남은 벨: " + str(my_bell))
            else:
                print("벨이 부족합니다.")
        elif answer_store == "2":
            if my_bell >= store['강아지 인형']:
                my_bell = my_bell - store['강아지 인형']
                my_pocket["강아지 인형"] += 1
                print("강아지 인형을 구매하셨습니다.")
                print("남은 벨: " + str(my_bell))
            else:
                print("벨이 부족합니다.")
        elif answer_store == "3":
            if my_bell >= store['강의실 책상']:
                my_bell = my_bell - store['강의실 책상']
                my_pocket["강의실 책상"] += 1
                print("강의실 책상을 구매하셨습니다.")
                print("남은 벨: " + str(my_bell))
            else:
                print("벨이 부족합니다.")
        elif answer_store == "4":
            if my_bell >= store["몬스테라"]:
                my_bell = my_bell - store['몬스테라']
                my_pocket["몬스테라"] += 1
                print("몬스테라를 구매하셨습니다.")
                print("남은 벨: " + str(my_bell))
            else:
                print("벨이 부족합니다.")
 
    # 2. 주민 찾아가기를 선택한 경우
    elif answer_action == "2":
        print("\n우리 마을에 있는 주민이야")
        print("1. 릴리안 \n2. 탁호 \n3. 미첼 \n4. 리처드")
        answer_animal = input("어떤 주민을 찾아갈까? ")
        print()
        if answer_animal == "1":
            print("릴리안에게 무엇을 할까?")
        elif answer_animal == "2":
            print("탁호에게 무엇을 할까?")
        elif answer_animal == "3":
            print("미첼에게 무엇을 할까?")
        elif answer_animal == "4":
            print("리처드에게 무엇을 할까?")
        answer_animal_action= int(input("1. 말걸기 2. 선물하기 3. 때리기 "))

        # 2-1. 말걸기를 선택
        if answer_animal_action == 1:
            if answer_animal == "1":
                animal["릴리안"] += 1
                print("\n어머! " + name + "왔구나! 반가워!")
                print("어제는 어찌나 벚꽃이 이쁘던지 기분이 참 좋더라니까")
                print(name + "도 놀러다녀오는 건 어때?")
                print("그렇지 뭐")
            elif answer_animal == "2":
                animal["탁호"] += 1
                print("\n안녀엉~ " + name + "아~ 반가워어")
                print("오늘 저녁은 뭘 먹을지 너무 고민이 돼~ 약히")
            elif answer_animal == "3":
                animal["미첼"] += 1
                print("\n" + name + "아~! 반가워~! 오늘 날씨 되게 좋지않아?")
                print("마구마구 산책을 하고 싶어져 동글")
            elif answer_animal == "4":
                animal["리처드"] += 1
                print("\n" + name + "야아~")
                print("나무를 흔들었더니 100벨이 나왔어어~")
                print(name+"도 한 번 흔들어봐아~ 그래유")
                print("리처드 친밀도 +1")
          

        # 2-1. 선물하기를 선택한 경우
        elif answer_animal_action == 2:
            print("\n어떤 선물을 줄까요?")
            for i in my_pocket:
                print(i + ": " + str(my_pocket[i]) + "개")

            answer_gift = input("\n선물을 입력해주세요: ")
            if answer_animal == "1":     
                if my_pocket[answer_gift] >= 1 :
                    my_pocket[answer_gift] -= 1
                    animal["릴리안"] += 5
                    print("\n어머! " + name + "아 선물 고마워~ 그렇지 뭐")
                    print("릴리안 친밀도 +5")
                else:
                    print("\n선물이 부족해요")
            elif answer_animal == "2":
                if my_pocket[answer_gift] >= 1 :
                    my_pocket[answer_gift] -= 1
                    animal["탁호"] += 5
                    print("\n",+name + "아~ 선물 고마워~ 약히")
                    print("탁호 친밀도 +5")
                else:
                    print("선물이 부족해요")
            elif answer_animal == "3":
                if my_pocket[answer_gift] >= 1 :
                    my_pocket[answer_gift] -= 1
                    animal["미첼"] += 5
                    print("\n" + name + "아~! 선물 고마워 동글")
                    print("미첼 친밀도 +5")
                else:
                    print("\n선물이 부족해요")
            elif answer_animal == "4":
                if my_pocket[answer_gift] >= 1 :
                    my_pocket[answer_gift] -= 1
                    animal["리처드"] += 5
                    print("\n"+ name+ "야아~ 선물 고마워~ 그래유")
                    print("리처드 친밀도 +5")
                else:
                    print("\n선물이 부족해요")
        # 2-3. 떄리기를 선택한 경우
        elif answer_animal_action == 3:
            if answer_animal == "1":
                animal["릴리안"] -= 1
                print("\n어머! " + name + "아 왜 때려! 그렇지 뭐")
                print("릴리안 친밀도 -1")
            elif answer_animal == "2":
                animal["탁호"] -= 1
                print("\n"+ name + "아 왜 때려! 약히")
                print("탁호 친밀도 -1")
            elif answer_animal == "3":
                animal["미첼"] -= 1
                print("\n"+ name + "아 왜 때려! 동글")
                print("미첼 친밀도 -1")
            elif answer_animal == "4":
                animal["리처드"] -= 1
                print("\n"+ name+ "아 왜 때려! 그래유")
                print("리처드 친밀도 -1")




    # 3. 나무 흔들기를 선택한 경우
    elif answer_action == "3":
        result = random.choice(["100벨", "사과", "벌"])

        # 100벨이 떨어질경우
        if result == "100벨":
            print("\n나무를 흔들면 랜덤으로 100벨이 나온다구리") 
            print("나온 벨은 너의ㅏ 벨에 추가된다구리!")
            my_bell += 100
        # 사과가 떨어질경우
        elif result == "사과":
            print("\n나무를 흔들면 랜덤으로 사과를 획득할 수 있다구리")
            print("획득한 사과는 너의 주머니에 추가된다구리!")
            print("선물도 가능하다구리~~")

        # 벌이 나타날경우
        elif result == "벌":
            print("\n나무를 흔들면 랜덤으로 벌에 쏘일 수도...있다구리")
            print("쏘인 벌은 가져갈 수는 없다구리!")




    # 4. 정보보기를 선택한 경우
    elif answer_action == "4":
        # 이름 출력
        print("이름: " + name)

        # 남은 벨 출력
        print("벨: " + str(my_bell) + "벨")
        # 주머니 출력
        print("주머니: " + str(my_pocket))
        # 주민 친밀도 출력
        print("주민 친밀도: ")
        for i in animal:
            print(i + ": " + str(animal[i]))
        
        
    # 잘못된 입력을 했을경우
    else:
       print("잘못된 입력입니다. 다시 입력해주세요.")

