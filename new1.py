def compute_squares(nums: list[int]) -> list[int]:
    """
    Compute the square of each integer in the provided list.
    
    Args:
        nums (list[int]): A list of integers.

    Returns:
        list[int]: A list containing the squares of the input integers.
    """
    squares = []
    for n in nums:
        squares.append(n * n)
    return squares
if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8, 9, 10]

    print("Squares of list1:", compute_squares(list1))
    print("Squares of list2:", compute_squares(list2))

