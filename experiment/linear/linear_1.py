from colorama import Fore, Back, Style 

# 선 그리기
for i, x in enumerate(range(1, 20 + 1),):
    print(Fore.BLUE + '-', end = '')

print(Style.RESET_ALL)