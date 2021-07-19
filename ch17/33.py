# https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import *

class Solution:
    '''
    - 정렬은 되어 있는데, 어떤 인덱스에서 회전을 했다.
    - 그러면 회전이 된 피벗 인덱스를 찾으면, 정렬된 배열을 그대로 사용 가능
    - 피벗은? 가장 작은 수가 위치하는 지점
    '''
    def search(self, nums: List[int], target: int) -> int:
        nums_len = len(nums)
        # 회전이 된 피벗을 찾자
        # 이미 정렬이 된 것을 회전시킨 것이므로, 최소값이 있는 위치가 회전된 위치일 것이다
        # ex: [4, 5, 6, 7, 0, 1, 2]
        left, right = 0, nums_len - 1
        while left < right:
            # 중앙에서부터 정렬이 비정상인 부분을 찾아간다. 회전되어 있으므로 좌측보다 우측이 더 작은 값이 있을 것이다.
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]: # mid 인덱스의 값이 right 인덱스의 값보다 크다?
                left = mid + 1 # 회전된 지점이 right와 mid 사이에 존재한다는 의미이므로, left 포인트를 mid 우측으로 점프
            else: # mid 인덱스의 값이 right 인덱스 값보다 작다?
                # 정상 정렬되어 있다는 의미이므로 우측 한계를 mid로 좁힌다
                # (right - left) // 2는 그 차를 계속 0으로 좁혀가므로,
                # `left + (right - left) // 2`는 언제가 left과 같아진다
                # 그리고 arr[left]는 arr[right]보다 작은 값이므로, 최소값의 인덱스가 되며
                # right == left가 될 때, 최소값의 인덱스를 찾게 된다
                right = mid
        pivot = left

        left = 0  # 0번 인덱스부터 시작한다고 하고, 실제 mid 값은 나중에 모듈러 연산으로 보정한다
        right = nums_len - 1
        # 실제 탐색 시작
        while left <= right:
            # pivot부터 정렬이 되어 있다고 보면,
            # ex: [4, 5, 6, 7, 0, 1, 2]는 아래 순서로 정렬되어 있다고 볼 수 있다
            # ex[4] > ex[5] > ex[6] > ex[0] > ex[1] > ex[2] > ex[3]
            mid = left + (right - left) // 2 # mid값을 바꾸지는 않는데, left와 rightd를 좁혀 나가야 하기 때문
            mid_corrected = (mid + pivot) % nums_len #  mid 계산에서 모듈러 연산으로 보정한다

            if nums[mid_corrected] < target: # 찾으려는 값이 arr[mid]보다 크다? 우측으로 좁힌다
                left = mid + 1
            elif nums[mid_corrected] > target: # 찾으려는 값이 arr[mid]보다 작다? 좌측으로 좁힌다
                right = mid - 1
            else:
                return mid_corrected

        return -1
    
    def search2(self, nums: List[int], target: int) -> int:
        nums_len = len(nums)
        # 회전이 된 피벗을 찾자
        # 이미 정렬이 된 것을 회전시킨 것이므로, 최소값이 있는 위치가 회전된 위치일 것이다
        # ex: [4, 5, 6, 7, 0, 1, 2]
        left, right = 0, nums_len - 1
        while left < right: # 같은 경우 멈춰야 하므로 left가 right보다 작은 경우만 반복
            # 중앙에서부터 정렬이 비정상인 부분을 찾아간다. 회전되어 있으므로 좌측보다 우측이 더 작은 값이 있을 것이다.
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]: # mid 인덱스의 값이 right 인덱스의 값보다 크다?
                left = mid + 1 # 회전된 지점이 right와 mid 사이에 존재한다는 의미이므로, left 포인트를 mid 우측으로 점프
            else: # mid 인덱스의 값이 right 인덱스 값보다 작다?
                # 정상 정렬되어 있다는 의미이므로 우측 한계를 mid로 좁힌다
                # (right - left) // 2는 그 차를 계속 0으로 좁혀가므로,
                # `left + (right - left) // 2`는 언제가 left과 같아진다
                # 그리고 arr[left]는 arr[right]보다 작은 값이므로, 최소값의 인덱스가 되며
                # right == left가 될 때, 최소값의 인덱스를 찾게 된다
                right = mid
        pivot = left
        nums = nums[pivot:nums_len] + nums[0:pivot]
        
        left, right = 0, nums_len - 1
        while left <= right: # 같은 경우에도 그 인덱스의 값이 target에 맞는지 확인해야 하므로 같은 경우도 반복
            mid = left + (right - left) // 2

            if target < nums[mid]: # 우측을 좁힌다
                right = mid - 1
            elif nums[mid] < target: # 좌측을 좁힌다
                left = mid + 1
            else:
                return (mid + pivot) % nums_len
        
        return -1

    
    def search3(self, nums: List[int], target: int) -> int:
        print(nums)
        left = 0
        right = len(nums)-1
        while left < right: # 같아지면 멈춘다
            mid = (right + left)//2
            left_val = nums[left]
            right_val = nums[right]
            mid_val = nums[mid]
            if mid_val == target:
                print("nums[{}]={} == {}".format(mid, nums[mid], target))
                return mid

            # `arr[mid]`의 값이 `arr[left]`보다 작거나 같다?
            if mid_val <= left_val: # `arr[left]`가 작아야 하는데 이는 비정상이므로, 회전한 피벗이 좌측에 있음을 의미
                print("[pivot in L] 1. mid_val=nums[{}]={} <= left_val=nums[{}]={}".format(mid, nums[mid], left, left_val))
                # 좌/우를 좁힌다
                if target > mid_val and target <= right_val: # mid 인덱스와 right 인덱스 사이에 존재?
                    print("[pivot in L] 1.1. target={} > mid_val=nums[{}]={} AND target={} <= right_val=nums[{}]={} > left = mid + 1".format(target, mid, mid_val, target, right, right_val))
                    left = mid + 1 # 좌를 우로 좁힌다
                else: #if target <= right_val:
                    print("[pivot in L] 1.2. target={} <= mid_val=nums[{}]={} OR target={} >= right_val=nums[{}]={} > right = mid - 1".format(target, mid, mid_val, target, right, right_val))
                    right = mid - 1 # 우를 좌로 좁힌다
                print("[pivot in L] 1.3. left={}, right={}".format(left, right))
            # `arr[mid]`의 값이 `arr[left]`보다 크거나 같다?
            if mid_val >= left_val: #  `arr[left]`가 작아야 하고 이는 정상이므로, 회전한 피벗이 우측에 있음을 의미
                # 좌/우를 좁힌다
                print("[pivot in R] 2. mid_val=nums[{}]={} >= left_val=nums[{}]={}".format(mid, nums[mid], left, left_val))
                if target >= left_val and target < mid_val: # left 인덱스와 mid 인덱스 사이에 존재?
                    print("[pivot in R] 2.1. target={} >= left_val=nums[{}]={} AND target={} <= mid_val=nums[{}]={} > right = mid - 1".format(target, left, left_val, target, mid, mid_val))
                    right = mid - 1 # 우를 좌로 좁힌다
                else:
                    print("[pivot in R] 2.2. target={} < left_val=nums[{}]={} OR target={} >= mid_val=nums[{}]={} > left = mid + 1".format(target, left, left_val, target, mid, mid_val))
                    left = mid + 1 # 좌를 우로 좁힌다
                print("[pivot in R] 2.3. left={}, right={}".format(left, right))
        if nums[left] == target:
            print("nums[left]=nums[{}]={} == target={}".format(left, nums[left], target))
            return left
        return -1

    
    def search4(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left < right: # 같아지면 멈춘다
            mid = (right + left)//2
            left_val = nums[left]
            right_val = nums[right]
            mid_val = nums[mid]

            if mid_val <= left_val:

                if target > mid_val and target <= right_val:
                    left = mid + 1
                else:
                    right = mid - 1
            if mid_val >= left_val:
                if target >= left_val and target < mid_val:
                    right = mid - 1
                else:
                    left = mid + 1
        if nums[left] == target:
            return left
        return -1

s = Solution()
# print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
# print(s.search([4, 5, 6, 7, 0, 1, 2], 3))
# print(s.search([4, 5, 6, 7, 0, 1, 2], 4))
# print(s.search([1], 0))

# print(s.search3([4, 5, 6, 7, 0, 1, 2], 0))
print(s.search3([6, 7, 0, 1, 2, 4], 1))
print(s.search3([6, 7, 0, 1, 2, 4], 10))