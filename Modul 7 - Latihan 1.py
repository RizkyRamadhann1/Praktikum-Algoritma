#prime number verification program
def is_prime(num):
	if num < 2:
		return False #mengembalikan nilai False jika nomer lebih kecil 2
	for prime in range(2, num):
		if num % prime == 0: #jika angka hasil bagi nilai prime == 0, maka mengembalikan nilai False, karena bukan bilangan prima
			return False
	return True
	
#fungai mencari bilangan prima dari 1 - maksimal nomer yang di masukan
def find_primes(max_num):
	primes = [] #bilangan prima akan di tampung di list ini
	for prime in range(0, max_num):
		if is_prime(prime):
			primes.append(prime)
			
	total_primes = str(len(primes)) #total bilangan prima
	largest_prime = str(primes[-1]) #bilangan prima terbesar
	smallest_prime = str(primes[0]) #bilangan prima terkecil
	print('\n[+] total bilangan prima 1 s/d %s : %s' % (max_num, total_primes))
	print('[+] bilangan prima terbesar : %s' % (largest_prime))
	print('[+] bilangan prima terkecil : %s\n' % (smallest_prime))
	
	x = 0
	while x < len(primes):
		for value in primes:
			x = x + 1
			print(str(x)+' Yaitu : '+str(value))

if __name__== '__main__':
	max = int(input('[*] masukan nilai max : '))
find_primes(max)
