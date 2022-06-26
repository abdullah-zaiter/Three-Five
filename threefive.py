import sys


def three_five(number: int):
    string = ''
    if number % 3 == 0: string += 'Three'
    if number % 5 == 0: string += 'Five'
    return string if string else number


if __name__ == "__main__":
    max_num = 100 if len(sys.argv) == 1 else int(sys.argv[1])
    for num in range(1, max_num):
        print(three_five(num))
