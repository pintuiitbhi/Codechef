
mod = int(1e9)+7
n = int(input())
k = int(input())

n %= mod
k %=mod



def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, x, y = egcd(b%a, a)
		return (g, y - (b//a)*x, x)
# x = mulinv(b) mod n, (x * b) % n == 1
def modinv(b, n):
	g, x, _ = egcd(b, n)
	if g == 1:
		return x % n

temp=2**(n-1) % mod
P= (temp - n)%mod
Q= temp%mod
gcd=egcd(P,Q)[0] %mod


a= (int(P/gcd) * modinv(int(Q/gcd), mod))%mod
print(a)
