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
    return string.split()


def weight_convertor(weight: str) -> int:
    """This function receives an input of weight and returns the conversion to the sum of its digits."""
    result = 0
    for digit in weight:
        result += int(digit)
    return result


def weightS_convertor(l: list) -> list:
    """This function applies the conversion to a list of values."""
    return [weight_convertor(old_weight) for old_weight in l]


def order_list(sorter: list, be_sorted: list) -> list:
    """This function returns a list sorted based on another list."""
    return [sorted_weights for _, sorted_weights in sorted(zip(sorter, be_sorted))]


def back_to_string(l: list) -> str:
    """This function receives a list of string of numbers and returns a string of them."""
    l = list(map(str, l))
    return " ".join(l)


def order_weight(strng):
    """This function makes all the steps."""
    li = create_list(strng)
    li_new = weightS_convertor(li)
    li_ordered = order_list(li_new, li)
    result = back_to_string(li_ordered)
    return result

# Another way of doing it, taking advantage of functional programming
from functools import reduce

def order_weight(string: str) -> str:
    """Orders a string of int according to their digits

    Args:
        string: str composed of int separated by blank space

    Returns:
       same string, with int ordered according to the sum of their digits

    """
    def digit_sum(number: str) -> int:  # Aux function for the sorting, calculates the sum of digits
        return sum(int(digit) for digit in number)

    datos = sorted(string.split(), key=lambda num: (digit_sum(num), num))
    return " ".join(datos)  # String conversion for the list created



if __name__ == "__main__":
    # print(create_list("3"))
    # print(weight_convertor("123"))
    # print(weightS_convertor(["32", "12", "22"]))
    # print(order_list([32, 12, 22], [3, 2, 1]))
    # print(back_to_string([32, 12, 22]))
    print(order_weight(a) == b)
    print(order_weight(c) == d)
