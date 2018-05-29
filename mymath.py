# mymath module in different directory
def main():
    print('최상의 모듈(독립실행)시, 출력 됩니다.')


if __name__ == '__main__':
    main()
else:
    print('mymath.py의 모듈이름:' + __name__)


pi = 3.14


def add(a, b):
    return a + b


def area_circle(r):
    return r * r * pi
