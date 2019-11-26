#we will use bltin_gcd instead of gcd function from module 'math'
from math import gcd as bltin_gcd

def isPrime(n) : 
  
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True


def primRoots(_inprime):
    required_set = {num for num in range(1, _inprime) if bltin_gcd(num, _inprime) }
    return [g for g in range(1, _inprime) if required_set == {pow(g, powers, _inprime)
            for powers in range(1, _inprime)}]


  
  
#MAIN FUNCTION
if __name__ == '__main__':
    print('Enter a prime number: ')
    x=int(input())
    y='Checked : Number is a PRIME'
    n='Warning : Number is not a PRIME'
    if (isPrime(x)):
        print(y)
        print('Primitive root/roots : ')
        print(primRoots(x))
    else :
        print(n)
        
