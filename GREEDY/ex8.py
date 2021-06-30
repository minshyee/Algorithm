'''
알파벳 대문자 + 숫자(0-9) 문자열 : 입력 -> 오름차순(작 > 큰)정렬 + 숫자(글자)의 합 출격
'''

s = input()
char =[]
s_char=[]
sum = 0
for i in range(len(s)):
	if s[i] >= '0' and s[i] <= '9':
		sum += int(s[i])
	else:
		char.append(ord(s[i]))#굳이 안바꿔도 sort가능 -> 매서드 결과값 출력해서 none 나왔던 것

char.sort()
for c in char:
	s_char.append(chr(c))

#숫자가 없을때 == 'sum = 0'일 때도 고려하기 -> 안전한 프로그램

print(''.join(s_char) + str(sum))
