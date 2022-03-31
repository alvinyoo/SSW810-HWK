"""
Yuchen Yao
HW02
this assignment is going to implement a fraction calculator that asks the user for two fractions and an operator
and then prints the result.
"""


class Fraction:
    def __init__(self, numerator: float, denominator: float) -> None:
        self.numerator: float = numerator
        self.denominator: float = denominator
        if denominator == 0:
            raise ZeroDivisionError('0 cannot be a denominator!')

    def __str__(self) -> str:
        """
        return a String to display fractions 
        """
        return str(self.numerator) + '/' + str(self.denominator)
        # return f"{self.numerator}/{self.denominator}"

    def plus(self, other: "Fraction") -> "Fraction":
        """
        Add two fractions using simplest approach.
        Calculate new numerator and denominator and return new Fraction
        """
        den: float = self.denominator * other.denominator
        num: float = self.numerator * other.denominator + self.denominator * other.numerator
        return Fraction(num, den)

    def minus(self, other: "Fraction") -> "Fraction":
        """
        Subtract two fractions using simplest approach
        Calculate new numerator and denominator and return new Fraction
        """
        den: float = self.denominator * other.denominator
        num: float = self.numerator * other.denominator - self.denominator * other.numerator
        return Fraction(num, den)

    def times(self, other: "Fraction") -> "Fraction":
        """
        Multiply two fractions using simplest approach
        Calculate new numerator and denominator and return new Fraction
        """
        den: float = self.denominator * other.denominator
        num: float = self.numerator * other.numerator
        return Fraction(num, den)

    def divide(self, other: "Fraction") -> "Fraction":
        """
        Add two fractions using simplest approach.
        Calculate new numerator and denominator and return new Fraction
        """
        den: float = self.denominator * other.numerator
        num: float = self.numerator * other.denominator
        return Fraction(num, den)

    def equal(self, other: "Fraction") -> bool:
        """
        return True/False if the two fractions are equivalent
        """
        return (self.numerator * other.denominator) == (other.numerator * self.denominator)


def test_suite() -> None:
    """
    test weather the Fraction work correctly
    """
    f12: Fraction = Fraction(1, 2)
    f34: Fraction = Fraction(3, 4)
    f56: Fraction = Fraction(5, 6)
    print(f"{f12} + {f34} = {f12.plus(f34)} [10/8]")
    print(f"{f12} - {f34} = {f12.minus(f34)} [-2/8]")
    print(f"{f12} * {f34} = {f12.times(f34)} [[3/8]")
    print(f"{f12} / {f34} = {f12.divide(f34)} [4/6]")
    print(f"{f12} + {f34} + {f56} = {f12.plus(f34.plus(f56))} [100/48]")


def get_number(prompt: str) -> float:
    """ 
    read and return a number from the user.
    Loop until the user provides a valid number.
    """
    while True:
        inp: str = input(prompt)
        try:
            return float(inp)
        except ValueError:
            print(f"Error: '{inp}' is not a number. Please try again...")


def get_fraction() -> Fraction:
    """
    Ask the user for a numerator and denominator and return a valid Fraction
    """
    while True:
        numerator: float = get_number("Please input numerator:")
        denominator: float = get_number("Please input denominator:")
        try:
            return Fraction(numerator, denominator)
        except ZeroDivisionError as e:
            print(e)


def compute(f1: Fraction, operator: str, f2: Fraction) -> None:
    """
    Given two fractions and an operator, return the result of applying the operator to the two fractions
    """
    okay: bool = True
    # result: Optional[Union[Fraction, bool]] = None
    if operator == "+":
        result = f1.plus(f2)
    elif operator == "-":
        result = f1.minus(f2)
    elif operator == "*":
        result = f1.times(f2)
    elif operator == "/":
        result = f1.divide(f2)
    elif operator == "=":
        result = f1.equal(f2)
    else:
        print(f"Error: '{operator}' is an unrecognized operator")
        okay = False

    if okay:
        print(f"{f1} {operator} {f2} = {result}")


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
    test_suite()
    main()
