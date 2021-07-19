# https://stackoverflow.com/a/35814621
def TableFormat(A):
    MaxLength=0
    for i in range(len(A)):
        for x in A[i]:
            MaxLength =len(str(x)) if MaxLength<len(str(x)) else MaxLength
    for i in range(len(A)):
        for x in range(0,len(A[i])):
            Length=MaxLength-len(str(A[i][x]))
            print((" "*Length)+str(A[i][x]),end="|")
        print()
        
def zero_one_knapsack(cargo):
    capacity = 15
    pack = []

    for i in range(len(cargo) + 1): # 짐의 최대 개수 + 1
        # pack[짐 개수][배낭 용량] = 최대값
        pack.append([])
        for c in range(capacity + 1): # 배낭의 최대 용량 + 1
            if i == 0 or c == 0:
                print("[if  ] i:{}, c:{}".format(i, c))
                pack[i].append(0)
            elif cargo[i - 1][1] <= c: # 현재 짐의 무게를 넣을 수 있는지?
                print("[elif] i:{}, c:{}, cargo[i-1={}][0]={} + pack[i-1={}][(c - cargo[i-1={}][1]={})={}]={} vs pack[i-1={}][c={}]={}".format(i, c, i-1, cargo[i-1][0], i-1, i-1, cargo[i - 1][1], c - cargo[i - 1][1], pack[i-1][c - cargo[i-1][1]], i-1, c, pack[i - 1][c]))
                pack[i].append(
                    max(
                        cargo[i - 1][0] + pack[i - 1][c - cargo[i - 1][1]],
                        pack[i - 1][c]
                    )
                )
            else:
                print("[else] i:{}, cargo[i - 1][1]: {}, c:{}, pack[i - 1][{}]:{}".format(i, cargo[i - 1][1], c, c, pack[i - 1][c]))
                pack[i].append(pack[i - 1][c])
        print()    
    TableFormat(pack)

    return pack[-1][-1]

cargo = [
    (4, 12),
    (2, 1),
    (10, 4),
    (1, 1),
    (2, 2),
]
print(zero_one_knapsack(cargo))