N, K = map(int, input().split())
cnt = 0

while True:
	#N이 K로 나누어 떨어지는 수가 될때까지 빼기
    target = (N // K) * K
    cnt += N-target
    N = target
    if N < K:
        break
    N //= K
    cnt += 1
#N이 1보다 클 경우(K보다 작고) 남은 연산(-1하는 연산) 처리
cnt += (N-1)
print(cnt)
