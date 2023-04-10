if __name__ == '__main__':
    # create a list of numbers
    numbers = [1, 2, 3, 4, 5]

    print(numbers)  # Output:
    # [1, 2, 3, 4, 5]

    # ADD Numbers at last
    numbers.append(6)
    print(type(numbers))  # Output:
    # <class 'list'>
    print(numbers[0])  # Output: 1

    numbers.sort()
    numbers.sort(reverse=True)

    numbers.reverse()

    print(numbers.index(1))  # Output:

    # negative  index
    print(numbers[-1])  # Output:    5

    # Checking if an item is in the list
    if 4 in numbers:
        print("4 is in the list")

    # Slicing the list to create a new list
    sliced_numbers = numbers[1:4]

    print(sliced_numbers)

    # length of the list
    print(len(sliced_numbers))

    print(numbers[0:])
    print(numbers[1:5])

    lst = [i for i in range(8)]

    print(lst)
