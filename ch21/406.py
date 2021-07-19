# https://leetcode.com/problems/queue-reconstruction-by-height/
from typing import *
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda person: (-person[0], person[1]))
        result = []
        for person in people:
            result.insert(person[1], person)
        return result

s = Solution()
# s.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])
print(s.reconstructQueue([[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]))
