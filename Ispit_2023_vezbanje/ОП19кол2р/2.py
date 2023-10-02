from math import gcd

class razlomak:
    """
    meow = razlomak(5, 2)
    >>> meow
    razlomak(5, 2)
    """
    def __init__(self, p, q):
        self.numerator = p
        self.denominator = q
    
    def __repr__(self) -> str:
        return 'razlomak({0}, {1})'.format(self.numerator, self.denominator)
        
    def __float__(self):
        return self.numerator / self.denominator

    def __add__(self, second):
        if isinstance(second, razlomak):
            a = self.numerator * second.denominator + self.denominator * second.numerator
            b = self.denominator * second.denominator
        elif isinstance(second, int):
            a = self.numerator + second * self.denominator
            b = self.denominator
        else:
            return float(self) + second
        gdc1 = gcd(a, b)
        return razlomak(a//gdc1, b//gdc1)

    def __pos__(self):
        return self

    def __neg__(self):
        return razlomak(-self.numerator, self.denominator)

    __radd__ = __add__

    def __mul__(self, second):
        if isinstance(second, razlomak):
            a = self.numerator * razlomak.numerator
            b = self.denominator * razlomak.denominator
            gcd1 = gcd(a,b)
            return razlomak(a//gcd1, b//gcd1)
        elif isinstance(second, int):
            a = self.numerator * second
            gcd1 = gcd(a,self.denominator)
            return razlomak(a//gcd1, self.denominator//gcd1)
        else:
            return float(self) * second
