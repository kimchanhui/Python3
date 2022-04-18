def solution(lottos, win_nums):
    answer = []
    zero = lottos.count(0)
    cnt = 0

    for i in lottos:
        if i in win_nums:
            cnt += 1
        
    max = 7 - cnt - zero 
    min = 7 - cnt

    if max == 7:
        max = 6
    if min == 7:
        min = 6

    answer = [max, min]

    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35]))