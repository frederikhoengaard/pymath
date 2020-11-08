

class Fraction:
    def __init__(self,numerator,denominator):
        if type(numerator) != int or type(denominator) != int:
            raise ValueError('Numerator and denominator must be integer values!')

        self.numerator = numerator
        self.denominator = denominator



def gcd(a,b):
    while b:
        a,b = b, a % b

    







a = Fraction(1,2)


#print(a.numerator)


def computeGCD(x, y): 
  
   while(y): 
       x, y = y, x % y 
  
   return x 


print(computeGCD(4,37))