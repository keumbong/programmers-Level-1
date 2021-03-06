###문제 설명###
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

###제한 조건###
n은 2이상 1000000이하의 자연수입니다.

###입출력 예###
n	    result
10	    4
5	    3

def solution(n):
    answer = 0
    #숫자 0과 1을 제외한 n까지 수에 True삽입
    number = [False, False] + [True] * (n - 1)
    
    for i in range(2, n + 1):
        if number[i] == True:
            # 2의 배수, 3의 배수, 5의 배수 ...를 n까지 False로 변경
            for j in range(i * 2, n + 1, i):
                number[j] = False
    for k in range(2, n + 1):
        if number[k] == True:
            answer += 1

    return answer

###에라토스테네스의 체###
#에라토스테네스의 체는 수학에서 소수를 찾는 방법

###알고리즘
#1. 2부터 소수를 구하고자 하는 구간의 모든 수를 나열한다.
#2. 2는 소수이므로 제외하고, 2를 제외한 2의 배수들 제거
#3. 3은 소수이므로 제외하고, 3을 제외한 3의 배수들 제거
#4. 5는 소수이므로 제외하고, 5를 제외한 5의 배수들 제거
#5. 반복하면 구하고자 하는 구간의 소수들만 남는다.
