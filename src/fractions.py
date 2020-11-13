# fractions.py

"""
This library implements a Fraction class enabling representation of real numbers.

The basic operators add, subtract, multiply and divide can then be used with instances
of the Fraction class. 
"""


class Fraction:
    def __init__(self,numerator: int,denominator: int):
        if type(numerator) != int or type(denominator) != int:
            raise ValueError('Numerator and denominator must be integer values!')

        self.numerator = numerator
        self.denominator = denominator

    def show_fraction(self):
        print(self.numerator,'/',self.denominator)



def integer_to_fraction(a: int) -> Fraction:
    if type(a) != int:
        raise ValueError('Input parameter must be integer!')
    return Fraction(a,1)



def euclid_gcd(a: int,b: int) -> int:
    while b:
        a,b = b, a % b
    return a
    


def add_fractions(a: Fraction,b: Fraction) -> Fraction:
    gcd = euclid_gcd(a.denominator,b.denominator)
    denominator = (a.denominator * b.denominator) // gcd
    numerator = (a.numerator * (denominator // a.denominator)) + (b.numerator * (denominator // b.denominator))
    gcf = euclid_gcd(numerator,denominator)
    return Fraction(numerator // gcf,denominator // gcf)



def subtract_fractions(a: Fraction,b: Fraction) -> Fraction:
    gcd = euclid_gcd(a.denominator,b.denominator)
    denominator = (a.denominator * b.denominator) // gcd
    numerator = (a.numerator * (denominator // a.denominator)) - (b.numerator * (denominator // b.denominator))
    gcf = euclid_gcd(numerator,denominator)
    return (Fraction(numerator // gcf,denominator // gcf))



def multiply_fractions(a: Fraction,b: Fraction) -> Fraction:
    numerator = a.numerator * b.numerator
    denominator = a.denominator * b.denominator
    gcf = euclid_gcd(numerator,denominator)
    return Fraction(numerator // gcf,denominator // gcf)



def divide_fractions(a: Fraction,b: Fraction) -> Fraction:
    numerator = a.numerator * b.denominator
    denominator = b.numerator * a.denominator
    gcf = euclid_gcd(numerator,denominator)
    return Fraction(numerator // gcf,denominator // gcf)
