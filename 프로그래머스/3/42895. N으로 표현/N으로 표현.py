def solution(N, number):
    if N == number:  # N과 number가 같은 경우, 1번만 사용하여 표현 가능
        return 1
    
    dp = [set() for _ in range(9)]  # 0번 인덱스는 사용하지 않음, set자료형을 써서 중복을 피함
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))  # N, NN, NNN, ... 형태로 저장
        # dp {1: [5], 2: [55], 3: [555] ... } 이런식으로 저장되어 있음
        # 다른 방법으로는, 
        # for i in range(9): 
            # dp.add (i * 10 + i) 이런식으로 5, 55, 555 를 만들어도 가능함
        
        
        # 2개 짜리 만드는 법 : 1개 + 1개
        # 3개 짜리 만드는 법 : 1개 + 2개
        # 4개 짜리 만드는 법 : 1개 + 3개 / 2개 + 2개
        # 5개 짜리 만드는 법 : 1개 + 4개 / 2개 + 3개
        # i개 짜리 만드는 법 : i개 + k개 (i = j + k, 1 <= j, k < i)
        
        for j in range(1, i):  # i번째에 대하여, j와 i-j의 조합으로 가능한 모든 수를 찾음
            for op1 in dp[j]:
                for op2 in dp[i-j]:
                    dp[i].add(op1 + op2)  # 더하기
                    dp[i].add(op1 - op2)  # 빼기
                    dp[i].add(op1 * op2)  # 곱하기
                    if op2 != 0:  # 0으로 나누는 것은 제외
                        dp[i].add(op1 // op2)  # 나누기
                        
        if number in dp[i]:  # number를 찾은 경우, N을 사용한 횟수 반환
            return i
            
    return -1  # 8번을 초과하여 사용해야 하는 경우
