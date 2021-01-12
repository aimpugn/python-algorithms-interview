from collections import defaultdict
from typing import List
from colorama import init, Fore, Back, Style, Fore, Style
# https://leetcode.com/problems/trapping-rain-water/

"""
각 막대기의 너비가 1인 고도지도(입면지도, elevation map)를 나타내는 음이 아닌 n이 주어졌을 때, 
비가 온 후 얼마나 많은 물을 가둘 수 있는지 계산
"""

class Solution:
    stack_trace = []
    loop_cnt_to_print = 0

    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        # 최대 높이의 막대까지 좌/우 기둥 최대 높이가 현재 높이와의 차이만큼 물 높이 volume을 더해간다
        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            # 좌에서 우로, 우에서 좌로 더 큰 값을 남기면서 이동
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)

            # 더 작은 값을 중앙으로 이동시킨다
            if left_max <= right_max:
                # 현재 값이 최대값이면 0
                # 최대값을 지나왔다면 그 차이만큼 더한다
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        
        return volume


    def trap_stack(self, height: List[int]) -> int:
        if len(self.stack_trace) > 0:
            self.stack_trace = []
            self.loop_cnt_to_print = 0

        stack = []
        volume = 0
        height_len = len(height)

        # 높이 배열의 개수만큼 순회
        for current in range(height_len):
            hr = "================== %d ==================" % (self.loop_cnt_to_print)
            self.loop_cnt_to_print += 1
            
            # 현재 높이보다 이전 스택에 쌓인 높이가 작으면 통과
            loop_cnt = 0
            while True:
                if loop_cnt == 0 :
                    loop_cnt += 1
                    title = hr
                else :
                    title = "----- after %d loop -----" % (loop_cnt)

                if not stack:
                    self.print_rain_trap_matrix(title, height, stack, current)
                    print("empty stack")
                    print("break")
                    break
                if height[stack[-1]] >= height[current]:
                    self.print_rain_trap_matrix(title, height, stack, current)
                    # 최근 스택의 막대기 높이가 현재 높이보다 크거나 같다? 
                    print("height[recent yellow] >= height[red]")
                    print("height[%d] >= height[%d]" % (stack[-1], current))
                    print("%d >= %d" % (height[stack[-1]], height[current]))
                    print("break")
                    break
                    
                # 현재 높이가 최근 스택의 높이보다 크다? `물이 고여 있다`고 볼 수 있다
                # 내려갔다가 다시 올라오는 지점
                self.print_rain_trap_matrix(title, height, stack, current)
                print("height[recent yellow] < height[red]")
                print("height[%d] < height[%d]" % (stack[-1], current))
                print("%d < %d" % (height[stack[-1]], height[current]))
                # 계산할 물 웅덩이
                top = stack.pop()
                self.print_rain_trap_matrix("------ recent yellow(%d) to cyan(=top of stack) ------" % (top), height, stack, current, top)

                # 스택 요소가 하나만 존재한다면 종료
                if not len(stack):
                    print("empty stack == invalid width, so break")
                    break

                print("valid width")
                top_remained = stack[-1]
                distance = current - top_remained - 1
                print("distance = red - yellow - 1")
                print("         = %d - %d - 1" % (current, top_remained))
                print("         = %d" % (distance))
                waters = min(height[current], height[top_remained]) - height[top]
                print("waters = min(height[red], height[yellow]) - height[cyan]")
                print("       = min(height[%d], height[%d]) - height[%d]" % (current, top_remained, top))
                print("       = min(%d, %d) - %d" % (height[current], height[top_remained], height[top]))
                print("       = %d - %d" % (min(height[current], height[top_remained]), height[top]))
                print("       = %d" % (waters))
                volume += distance * waters
                print("volume += distance * waters")
                print("       += %d * %d" % (distance, waters))
                print("       += %d" % (distance * waters))
                print("       = %d" % (volume))


            stack.append(current)
            self.print_rain_trap_matrix(hr, height, stack)
            print("stack.append(%d)" % (current))

        return volume

    # 초록: 막대기
    # 노랑: 쌓인 스택
    # 빨강: stack.pop()된 현재 인덱스
    # 파랑: 물
    def print_rain_trap_matrix(self, title: str = "", height: List[int] = [], stack: List[int] = [], current: int = -1, top: int = -1):
        if title:
            print(title)
        trace_str = ''
        height_max = max(height)
        height_len = len(height)
        # 가장 높은 막대기를 기준으로 출력해 나간다
        for i in range(height_max):
            trace_str_line = []
            # 물이 고인 인덱스를 저장하기 위한 배열
            waters = []
            # 구간이 열렸는지
            is_open = False
            # 구간이 닫혔는지
            is_close = False
            # 구간 시작점 막대기 인덱스
            start = 0
            # 구간 끝점 막대기 인덱스
            end = 0
            # 너비
            width = 0
            # 현재 막대기 인덱스
            idx_curr = 0
            for h in height:
                # 현재 높이가 y축의 높이보다 크거나 같은 경우
                if h >= height_max - i:
                    if not is_open:
                        # 높이가 있는데 구간이 열린 적 없는 경우 구간 계산 시작 
                        is_open = True
                        start = idx_curr
                    elif width == 0:
                        # 열린 후 width 증가가 없으면 현재 높이가 이전 높이와 같거나 더 높다는 의미이므로 시작점을 현재로 잡는다 
                        start = idx_curr
                    elif not is_close:
                        # 열린 후 width가 증가했으면
                        end = idx_curr
                        # start 막대기 후 end 막대기 전의 인덱스를 waters 배열에 담는다
                        for w in range(start + 1, end, 1):
                            waters.append(w)
                        if (idx_curr + 1 <= height_len - 1) and (height[idx_curr + 1] < height_max - i):
                            # 다음 인덱스가 존재하고, 다음 높이가 높이보다 작은 경우 물이 고일 수 있으므로
                            # 시작점은 열어두고
                            is_open = True
                            # 닫는점은 초기화하고
                            is_close = False
                            # 시작 지점을 현재로 설정한다
                            start = idx_curr
                        else:
                            # 다음 인덱스 존재하지 않거나
                            # 다음 높이가 같거나 더 커지면 물이 고일 수 없으므로 시작점을 닫는다
                            is_open = False
                    # 높이 있음 표시
                    trace_str_line.append('\x1b[6;30;42m \x1b[0m')
                else:
                    if is_open:
                        width += 1
                    trace_str_line.append(str(0))

                idx_curr += 1
            
            if len(waters) > 0:
                for w in waters:
                    trace_str_line[w] = '\x1b[0;37;44m' + str(1) + '\x1b[0m'
            trace_str += ''. join(trace_str_line) + " \n"
        
        stack_arr = []
        for i in range(height_len):
            stack_arr.append(str(i))

        if stack:
            for s in stack:
                stack_arr[s] = '\x1b[3;37;43m \x1b[0m'
        if current >= 0:
            stack_arr[current] = '\x1b[1;31;41m \x1b[0m'
        if top >= 0:
            stack_arr[top] = '\x1b[7;36;43m \x1b[0m'
        
        stack_str = ''.join(stack_arr)
        trace_str += stack_str
        print(trace_str)


    def trap_my(self, height: List[int]) -> int:
        ans = 0
        # 감싸진 구간을 찾는다
        start = 0
        height_len = len(height)
        if height_len > 2:
            height_max = height[height_len - 1]
            
            for idx, elevation in enumerate(height):
                end = self.get_next_idx(start, height)
                
                # 바로 다음 칸에 높이가 올라가면 start 지점 옮긴다
                if (end - start) == 1:
                    start = end
                    continue
                elif end > -1: 
                    # 너비가 2 이상이고, 같거나 더 큰 막대기가 있는 경우
                    width = end - start - 1
                    # 현재 구간의 최대 높이를 구한다
                    height_max_curr = min([height[start], height[end]])
                    for height_curr in height[start + 1 : end]:
                        height_to_multiply = height_max_curr - height_curr
                        if height_to_multiply > 0:
                            width = 1
                            ans += (height_to_multiply * width)

                    # 다음 시작 지점 설정
                    start = end
                else :
                    # 다음에 더 큰 높이가 없다면, 다음 인덱스로 이동
                    start = start + 1
                
                if start >= height_len:
                    break

        return ans
            

    
    
    """
    구간 성립 조건
    너비가 있고 시작과 끝 사이에 높이 차가 있다
    2 1 1 2 (O)
    2 1 1 3 (O)
    4 0 1 2 (O)

    4 2 1 2 2 (O) > 2와 2 사이에 구간 성립
    4 2 1 2 3 (O) > 4와 3 사이에 구간 성립
    4 1 1 2 3 (O) > 4와 3 사이에 구간 성립
    4 1 3 2 1 (O) > 4와 3 사이에 구간

    2 1 1 1 X

    끝은 어디로? 
    1. 시작 지점 높이와 같거나 보다 큰 경우
    2. 마지막 인덱스까지 도달한 경우?
      2.1. 시작점 다음 높이보다 마지막 인덱스가 높은 경우 구간 성립
      2.2. 시작점 다음 높이보다 마지막 인덱스가 낮거나 같은 경우 구간 미성립

    """
    def get_next_idx(self, start: int, height: List[int]) -> int:
        next_idx = start + 1
        height_len = len(height)

        if next_idx < height_len:
            # 시작점 높이
            height_max_curr = height[start]
            # 시작점 다음의 높이
            height_max_next = height[next_idx]
            # 마지막 인덱스
            last_idx = height_len - 1
            width = 0
            while next_idx < len(height):

                # 현재 높이보다 다음 높이가 높을 때
                if  height[start] <= height[next_idx]:
                    if width == 0:
                        # 너비가 없다면 -1 반환
                        return -1
                    else:
                        # 다음 높이보다 큰 기둥이 있으면 continue, 없으면 break
                        exist_larger_value = False
                        if next_idx + 1 < height_len:
                            if height[next_idx] < height[next_idx + 1]:
                                exist_larger_value = True

                        if not exist_larger_value:
                            return next_idx
                
                width += 1
                start += 1
                next_idx += 1
            
        return -1
                

s = Solution()
case = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# case = [4,2,3]
# case = [0,1,1,2,1,1,1,3,2,1,1,1]
# case = [0,1,0,0,0,0,0,0,0]
# case = [5,4,1,2]
# case = [2,3,5,4,1,1,2,3]
# case = [4,9,4,5,3,2]
# case = [3, 2, 1, 0, 0, 2, 3]
# case = [2, 1, 2, 3]
ans = s.trap_stack(case)
print(ans)