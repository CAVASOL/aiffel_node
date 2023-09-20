# 평가문항: 평행사변형(par), 사다리꼴(trape) 넓이를 구하는 메서드를 직접 작성할 수 있다.
# 상세기준: self 인자를 잊지 않고 넣고, 변수를 알맞게 사용했다.

class Square:
    def __init__(self):
        square = int(input('넓이를 구하고 싶은 사각형의 숫자를 써주세요.\n 1.직사각형 2.평행사변형 3.사다리꼴 \n >>>'))

        if square == 1:
            print('직사각형 함수는 rect()입니다.')

        elif square == 2:
            print('평행사변형 함수는 par()입니다.')
        
        elif square == 3:
            print('사다리꼴 함수는 trape()입니다.')
        
        else:
            print('1, 2, 3 중에서 다시 입력해주세요')

    def rect(self):
        width, vertical = map(int, input('가로, 세로를 입력하세요. 예시 : 가로,세로\n >>>').split(','))
        area = width * vertical
        result = '직사각형의 넓이는 : ' + str(area)
        return result

    def par(self):
        base, height = map(int, input('밑변, 높이를 입력하세요. 예시 : 밑변,높이\n >>>').split(','))
        result = base * height
        return result

    def trape(self):
        base, upper_side, height = map(int, input('밑변, 높이를 입력하세요. 예시 : 밑변,높이\n >>>').split(','))
        result = (base + upper_side) * height * 1/2
        return result

a = Square()