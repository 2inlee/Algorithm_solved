def solution(participant, completion):
    hash_table = {}
    
    for name in participant:
        hash_table[name] = hash_table.get(name, 0) + 1
        
    for name in completion:
        hash_table[name] -= 1
        
    for name in hash_table:
        if hash_table[name] >0:
            return name
        
    return ""