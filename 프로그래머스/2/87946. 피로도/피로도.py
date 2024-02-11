def solution(k, dungeons):
    
    def explore(k, dungeons, count):
        global max_count
        max_count = max(max_count, count)
        for i, (min_stress, cost) in enumerate(dungeons):
            if k >= min_stress:
                explore(k - cost, dungeons[:i] + dungeons[i+1:], count + 1)
    global max_count
    max_count = 0
    explore(k, dungeons, 0)
    return max_count
