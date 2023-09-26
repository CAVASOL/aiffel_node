import datetime

# 평가문항: 1. Kiosk 클래스를 생성하고, 주문, 추가 주문 메서드를 적절하게 구현할 수 있다.
#         2. 지불, 주문표 작성 메서드를 적절하게 구현할 수 있다.
# 상세기준: 각각의 메서드가 에러 없이, 정상적으로 동작하였다.
# 추가: 1. 메뉴와 가격리스트를 다차원리스트로 변경하기
#      2. 메뉴출력 enumerate() 사용하기
#      3. datetime 모듈로 주문표에 주문 일시 표시하기
#      4. 데코레이터로 주문표 양식 출력 추가하기

class Kiosk:
    def __init__(self, menu_price_list):
        self.menu_price_list = menu_price_list
        self.order_menu = []  # 주문 리스트
        self.order_price = []  # 가격 리스트
        self.price_sum = 0  # 주문 총액 초기화
        self.temp = ""  # 온도 속성 초기화

    # 메뉴 출력 메서드
    def menu_print(self):
        for i, (menu, price) in enumerate(self.menu_price_list, start=1):
            print(i, menu, ' : ', price, '원')

    # 주문 메서드
    def menu_select(self):
        self.order_menu = []  # 주문 리스트 초기화
        self.order_price = []  # 가격 리스트 초기화

        n = 0
        while n < 1 or n > len(self.menu_price_list):  # 음료 번호 범위를 검사
            n = int(input("음료 번호를 입력하세요 : "))  # 음료 번호 입력

        # 메뉴판에 있는 음료 번호일 때
        if 1 <= n <= len(self.menu_price_list):
            self.order_price.append(self.menu_price_list[n - 1][1])  # 가격 리스트에 추가
            self.price_sum = self.menu_price_list[n - 1][1]  # 합계 금액 설정

            # 음료 온도 물어보기
            t = 0
            while t != 1 and t != 2:
                t = int(input(f"HOT 음료는 1을, ICE 음료는 2를 입력하세요 : "))
                if t == 1:
                    self.temp = "HOT"
                elif t == 2:
                    self.temp = "ICE"
                else:
                    print("1과 2 중 하나를 입력하세요.\n")

            self.order_price.append(self.menu_price_list[n - 1][1])
            self.order_menu.append(self.temp + ' ' + self.menu_price_list[n - 1][0])

            self.price_sum += self.menu_price_list[n - 1][1]
            print(f'추가 주문 음료 {self.temp} {self.menu_price_list[n - 1][0]}: {self.menu_price_list[n - 1][1]}원\n합계: {self.price_sum}원')
        else:
            print("없는 메뉴입니다. 다시 주문해 주세요.")

        # 추가 주문 또는 지불
        while n != 0:  # 지불을 선택하기 전까지 반복
            print()
            n = int(input("추가 주문은 음료 번호를, 지불은 0을 누르세요 : "))  # 추가 주문 또는 지불
            if 1 <= n <= len(self.menu_price_list):  # 범위 검사
                # 추가 음료 온도 물어보기
                t = 0
                while t != 1 and t != 2:
                    t = int(input(f"추가 주문 음료 '{self.menu_price_list[n - 1][0]}'의 온도를 입력하세요 (1: HOT, 2: ICE): "))
                    if t == 1:
                        self.temp = "HOT"
                    elif t == 2:
                        self.temp = "ICE"
                    else:
                        print("1과 2 중 하나를 입력하세요.\n")

                self.order_price.append(self.menu_price_list[n - 1][1])
                self.order_menu.append(self.temp + ' ' + self.menu_price_list[n - 1][0])

                self.price_sum += self.menu_price_list[n - 1][1]
                print(f'추가 주문 음료 {self.temp} {self.menu_price_list[n - 1][0]}: {self.menu_price_list[n - 1][1]}원\n합계: {self.price_sum}원')
            elif n == 0:  # 지불을 입력하면
                break  # 지불 메서드는 주문을 마친 후에 호출

        # 주문이 끝났으므로 여기서 지불 메서드를 호출
        self.pay()

    # 지불 메서드 추가
    def pay(self):
        print()
        n = int(input("지불 방법을 선택하세요 1. 현금, 2. 카드결제 : "))  # 지불 방법 선택
        if n == 1:
            print(f"직원을 호출하겠습니다.")
        elif n == 2:
            print(f"IC칩 방향에 맞게 카드를 꽂아주세요.")
        else:
            print("1 또는 2 중 하나를 입력하세요.")

        # 주문일시 표시
        now = datetime.datetime.now()
        print(f"주문일시: {now.strftime('%Y-%m-%d %H:%M:%S')}")

    # 주문 테이블 출력 메서드 추가
    def table(self):
        print('⟝' + '-' * 30 + '⟞')
        for i in range(5):
            print('|' + ' ' * 31 + '|')

        for i in range(len(self.order_menu)):
            print(self.order_menu[i], ' : ', self.order_price[i], '원')

        print('주문 총액:', self.price_sum, '원')

        for i in range(5):
            print('|' + ' ' * 31 + '|')
        print('⟝' + '-' * 30 + '⟞')

# 메뉴와 가격 리스트를 다차원 리스트로 생성
menu_price_list = [
    ('americano', 2000),
    ('latte', 3000),
    ('mocha', 3000),
    ('yuza_tea', 2500),
    ('green_tea', 2500),
    ('choco_latte', 3000)
]

a = Kiosk(menu_price_list)  # 객체 생성
a.menu_print()  # 메뉴 출력
a.menu_select()  # 주문
a.table()  # 주문표 출력
