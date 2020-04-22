"""
Yuchen Yao
HW03
this assignment is going to implement a fraction calculator that asks the user for two fractions and an operator
and then prints the result.
"""

from typing import Optional, Union


class Fraction:
    def __init__(self, numerator: float, denominator: float) -> None:
        self.numerator: float = numerator
        self.denominator: float = denominator
        if denominator == 0:
            raise ZeroDivisionError('0 cannot be a denominator!')
        if denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    def __str__(self) -> str:
        """ return a String to display fractions """
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other: "Fraction") -> "Fraction":
        """
        Add two fractions using simplest approach.
        Calculate new numerator and denominator and return new Fraction
        """
        den: float = self.denominator * other.denominator
        num: float = self.numerator * other.denominator + self.denominator * other.numerator
        return Fraction(num, den)

    def __sub__(self, other: "Fraction") -> "Fraction":
        """
        Subtract two fractions using simplest approach
        Calculate new numerator and denominator and return new Fraction
        """
        den: float = self.denominator * other.denominator
        num: float = self.numerator * other.denominator - self.denominator * other.numerator
        return Fraction(num, den)

    def __mul__(self, other: "Fraction") -> "Fraction":
        """
        Multiply two fractions using simplest approach
        Calculate new numerator and denominator and return new Fraction
        """
        den: float = self.denominator * other.denominator
        num: float = self.numerator * other.numerator
        return Fraction(num, den)

    def __truediv__(self, other: "Fraction") -> "Fraction":
        """
        Add two fractions using simplest approach.
        Calculate new numerator and denominator and return new Fraction
        """
        den: float = self.denominator * other.numerator
        num: float = self.numerator * other.denominator
        return Fraction(num, den)

    def __eq__(self, other: "Fraction") -> bool:
        """ return True/False if the two fractions are equivalent """
        return (self.numerator * other.denominator) == (other.numerator * self.denominator)

    def __ne__(self, other: "Fraction") -> bool:
        """ return True/False if the two fractions are not equivalent """
        return (self.numerator * other.denominator) != (other.numerator * self.denominator)

    def __lt__(self, other: "Fraction") -> bool:
        """ return True/False if the self fractions is less than the other fraction """
        num = (self.numerator * other.denominator) - (self.denominator * other.numerator)
        den = self.denominator * other.denominator
        return num / den < 0

    def __le__(self, other: "Fraction") -> bool:
        """ return True/False if the self fractions is less than or equal to the other fraction """
        num = (self.numerator * other.denominator) - (self.denominator * other.numerator)
        den = self.denominator * other.denominator
        return num / den <= 0

    def __gt__(self, other: "Fraction") -> bool:
        """ return True/False if the self fractions is greater than the other fraction """
        num = (self.numerator * other.denominator) - (self.denominator * other.numerator)
        den = self.denominator * other.denominator
        return num / den > 0

    def __ge__(self, other: "Fraction") -> bool:
        """ return True/False if the self fractions is greater than or equal to the other fraction """
        num = (self.numerator * other.denominator) - (self.denominator * other.numerator)
        den = self.denominator * other.denominator
        return num / den >= 0

    def simplify(self) -> "Fraction":
        num: float = self.numerator
        den: float = self.denominator
        if num % den == 0:
            pass
        else:
            i: int = int(min(abs(num), abs(den)))
            gcf: float
            for gcf in range(i, 1, -1):
                # gcf means greatest common factor
                if num % gcf == 0 and den % gcf == 0:
                    num /= gcf
                    den /= gcf
        return Fraction(num, den)


def get_fraction() -> "Fraction":
    """ Ask the user for a numerator and denominator and return a valid Fraction """
    while True:
        numerator: float = get_number("Please input numerator:")
        denominator: float = get_number("Please input denominator:")
        try:
            return Fraction(numerator, denominator)
        except ZeroDivisionError as e:
            print(e)


def compute(f1: Fraction, operator: str, f2: Fraction) -> None:
    """
    Given two fractions and an operator, return the result
    of applying the operator to the two fractions
    """
    okay: bool = True
    result: Optional[Union[Fraction, bool]] = None

    if operator == "+":
        result = f1.__add__(f2)
    elif operator == "-":
        result = f1.__sub__(f2)
    elif operator == "*":
        result = f1.__mul__(f2)
    elif operator == "/":
        result = f1.__truediv__(f2)
    elif operator == "=":
        result = f1.__eq__(f2)
    elif operator == "<":
        result = f1.__lt__(f2)
    elif operator == "<=":
        result = f1.__le__(f2)
    elif operator == ">":
        result = f1.__gt__(f2)
    elif operator == ">=":
        result = f1.__ge__(f2)
    else:
        print(f"Error: '{operator}' is an unrecognized operator")
        okay = False

    if okay:
        print(f"{f1} {operator} {f2} = {result}")


def get_number(prompt: str) -> float:
    """ read and return a number from the user.
        Loop until the user provides a valid number.
    """
    while True:
        inp: str = input(prompt)
        try:
            return float(inp)
        except ValueError:
            print(f"Error: '{inp}' is not a number. Please try again...")


def main() -> None:
    print('Welcome to the fraction calculator!')
    f1: Fraction = get_fraction()
    operator: str = input("Operation (+, -, *, /,=): ")
    f2: Fraction = get_fraction()
    try:
        compute(f1, operator, f2)
    except ZeroDivisionError as e:
        print(e)


if __name__ == '__main__':
    main()