def calculate_rectangle_area(length, width):
    """
    Calculates the area of a rectangle given its length and width.
    """
    area = length * width
    return area


if __name__ == '__main__':
    # Example usage of the function
    length = 5
    width = 10
    rectangle_area = calculate_rectangle_area(length, width)
    print("The area of the rectangle is:", rectangle_area)
