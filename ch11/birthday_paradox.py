import random

TRIALS = 100000
same_birthday = 0.0

for _ in range(TRIALS):
    birthdays = []
    for i in range(23):
        birthday = random.randint(1, 365)
        if birthday in birthdays:
            same_birthday += 1
            break
        birthdays.append(birthday)

print(f'{same_birthday / TRIALS * 100}%')  # 50.88399999999999%
