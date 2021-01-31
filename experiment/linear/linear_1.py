# 선 그리기
for i, x in enumerate(range(1, 10 + 1),):
    x_format = '\x1b[1;37;44m{0}\x1b[0m'.format(' ' * len(str(x)))
    print(x_format, end = '')

print()

for i, x in enumerate(range(1, 10 + 1),):
    print('-' * len(str(x)), end = '')