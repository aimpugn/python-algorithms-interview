def fractional_knapsack(cargo):
    capacity = 15
    pack = []
    for c in cargo:
        # (단가, 가격, 무게)
        pack.append((c[0] / c[1], c[0], c[1]))
    pack.sort(reverse = True)

    # 단가 순 그리디 계산
    total_value: float = 0
    for p in pack:
        if capacity - p[2] >= 0:
            # 항목 전체를 그대로 넣을 수 있는 경우
            print('in if capacity: {}, p: {}'.format(capacity, p))
            capacity -= p[2] # 담을 무게만큼 배낭 무게 제거
            total_value += p[1]
        else:
            # 항목 전체를 그대로 넣을 수 없는 경우 분할
            print('in else capacity: {}, p: {}'.format(capacity, p))
            fraction = capacity / p[2]
            total_value += p[1] * fraction
            break
    return total_value

cargo = [
    (4, 12),
    (2, 1),
    (10, 4),
    (1, 1),
    (2, 2),
]
print(fractional_knapsack(cargo))


def findMin(money, monetary_units):
    n = len(monetary_units)
    ans = []
    # Traverse through all denomination
    i = n - 1
    while(i >= 0):
        # Find denominations
        while (money >= monetary_units[i]):
            money -= monetary_units[i]
            ans.append(monetary_units[i])
        i -= 1

    return ans

print(findMin(160, [10, 50, 100]))
print(findMin(160, [10, 50, 80, 100])) # 최적해 아니다