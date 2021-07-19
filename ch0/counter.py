import collections

tmp = [
    'A',    
    'A',    
    'B',    
    'C',    
    'D',    
    'E',    
    'E',    
    'E'    
]

cnter = collections.Counter(tmp)

print(cnter)
print(cnter['A'])
print(cnter['Z'])