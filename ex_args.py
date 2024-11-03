
# print the diff of 2 numbers
# the numbers are argument. default value == 0
# call the function with (9999, 4444)
# call the function with no parameters
def diff_numbers(x: int = 0, y: float = 0) -> None:
    diff_result: int = x - y
    print(diff_result)

diff_numbers(9999, 4444)

# print the biggest of 3 number
# the numbers are argument. default value == 0
# call the function with -10, -100, 1
def biggest_of_3(x: int = 0, y: int = 0, z: int = 0):
    biggest: int = None
    if x > y and x > z:
        biggest = x
    elif y > z:
        biggest = y
    else:
        biggest = z
    print(biggest)

biggest_of_3(-10, -100, 1)

# function that gets a list[int] and print its length
def print_len(list1: list[int]):
    len_list = len(list1)
    print(len_list)

print_len([8, 9, -12])

# function that gets a list of int
# print the diff between the max and the min
# call the function with [900, 1010, -87, 0, 10_000]
# should print 10_000 - (-87) = 10_087
def gap_max_min(list1: list[int]):
    if len(list1) > 0:
        max_value = max(list1)
        min_value = min(list1)
        diff: int = max_value - min_value
        print(diff)
    else:
        print('empty list...')

gap_max_min([])
gap_max_min([900, 1010, -87, 0, 10_000])

# function that gets 1 string as parameter
# print tail equals head or not
# "radar" --> print: head equals tail
# "mango" --> print: head is not equals tail
# bonus: ignore case sensitive "Radar" --> equals
# try on word radar, apple, level, civic, noon, shalom
def tail_head(word: str = ""):
    reverse_word: str = word[::-1]
    if word.lower() == reverse_word.lower():
        print('head equals tail')
    else:
        print('head NOT equals tail')
    # Shortcut:
    # print(f"head {'NOT' if word != reverse_word else ''} equals tail")

for word in ['radar', 'apple', 'level', 'civic', 'noon', 'shalom']:
    print(word, end = ' ')
    tail_head(word)

# function that gets 2 booleans as parameter
# print "the same" if they are the same
# print "different" if they are different
# default False
# True True --> the same
# False True --> different
# True False --> different
# False False --> the same
def double_bool(bool1: bool = False, bool2: bool = False):
    if bool1 == bool2:
        print("the same")
    else:
        print("NOT the same")
    #print(f"{'NOT' if bool1 != bool2 else ''} the same")

# function that gets 2 floats as parameter
# create a list from these 2 floats
# sort the list and print it
def sort_floats(x: float, y: float):
    #list_float: list[float] = [1.5, 4.5]
    list_float: list[float] = [x, y]  # 1

    # list_float: list[float] = []
    # list_float.append(1.5)
    # list_float.append(4.5)
    list_float: list[float] = []  # 2
    list_float.append(x)  # 2
    list_float.append(y)  # 2

    list_float.sort()
    print(list_float)

sort_floats(5.9, -0.1)

