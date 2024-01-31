def solution(arr):
    answer = []
    for num in arr:
        # answer 리스트가 비어있거나 마지막 원소가 현재 숫자와 다를 때만 추가
        if not answer or answer[-1] != num:
            answer.append(num)
    return answer
