def print_chessboard(n: int) -> None:
    """
    Prints an N x N chessboard pattern:
    - If row == col → X
    - If (row + col) is even → 1
    - Else → 0
    """

    for row in range(n):
        for col in range(n):

            # Condition 1: Diagonal
            if row == col:
                print("X", end=" ")

            # Condition 2: Even sum
            elif (row + col) % 2 == 0:
                print(1, end=" ")

            # Condition 3: Odd sum
            else:
                print(0, end=" ")

        print()  # move to next line

n = int(input("Enter value of N: "))
print_chessboard(n)