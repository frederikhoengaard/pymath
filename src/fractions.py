# fractions.py

class Fraction:
    def __init__(self,numerator,denominator):
        if type(numerator) != int or type(denominator) != int:
            raise ValueError('Numerator and denominator must be integer values!')

        self.numerator = numerator
        self.denominator = denominator

    def show_fraction(self):
        print(self.numerator,'/',self.denominator)



def euclid_gcd(a: int,b: int) -> int:
    while b:
        a,b = b, a % b
    return a



def int_to_fraction(a: int) -> Fraction:
    if type(a) != int:
        raise ValueError('Input parameter must be integer!')
    return Fraction(a,1)
    


def add_fractions(a: Fraction,b: Fraction) -> Fraction:
    gcd = euclid_gcd(a.denominator,b.denominator)
    denominator = (a.denominator * b.denominator) // gcd
    numerator = (a.numerator * (denominator // a.denominator)) + (b.numerator * (denominator // b.denominator))
    gcf = euclid_gcd(numerator,denominator)
    return(Fraction(numerator // gcf,denominator // gcf))



def subtract_fractions(a: Fraction,b: Fraction) -> Fraction:
    gcd = euclid_gcd(a.denominator,b.denominator)
    denominator = (a.denominator * b.denominator) // gcd
    numerator = (a.numerator * (denominator // a.denominator)) - (b.numerator * (denominator // b.denominator))
    gcf = euclid_gcd(numerator,denominator)
    return(Fraction(numerator // gcf,denominator // gcf))


a = Fraction(2,5)
b = Fraction(1,4)

c = subtract_fractions(a,b)

c.show_fraction()