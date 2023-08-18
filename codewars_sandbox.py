a, b = "103 123 4444 99 2000", "2000 103 123 4444 99"
c, d = "2000 10003 1234000 44444444 9999 11 11 22 123", "11 11 2000 10003 22 123 1234000 44444444 9999"

"""This is the idea I am going to try to implement to solve this problem:
X = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
Y = [0, 1, 1, 0, 1, 2, 2, 0, 1]

Z = [x for _, x in sorted(zip(Y, X))]
print(Z)  # ["a", "d", "h", "b", "c", "e", "i", "f", "g"]

I am gonna need to follow the next steps:
1) Create a list out of the input.
2) Create another list with the weights transformed following the rules (adding digits).
3) Sort the initial list in the ascending order of the first second list.
"""


def create_list(string: str) -> list:
    """This function receives a string of numbers and returns a list of them."""
    pass


def weight_convertor(weight: str) -> int:
    """This function receives an input of weight and returns the conversion to the sum of its digits."""
    pass


def weightS_convertor(l: list) -> list:
    """This function applies the conversion to a list of values."""


def order_list(sorter: list, be_sorted: list) -> list:
    """This function returns a list sorted based on another list."""
    pass


def back_to_string(l: list) -> str:
    """This function receives a list of numbers and returns a string of them."""
    pass
