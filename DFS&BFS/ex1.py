a, b = map(int, input().split())

def uclide_gcd(a,b):
	if a%b == 0:
		return b
	else:
		return uclide_gcd(b, a%b)

print(uclide_gcd(a,b))
