"""
LINK: https://hackerrank-challenge-pdfs.s3.amazonaws.com/8662-diagonal-difference-English?response-content-disposition=inline%3B%20filename%3Ddiagonal-difference-English.pdf&response-content-type=application%2Fpdf&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAR6O7GJNX5DNFO3PV%2F20231215%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231215T150501Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=9888471a6b76161bb037694f6e92fbf4f571dfb32b2e226e4cfbe6a9627f4605

Complete the 'diagonalDifference' function below.
The function is expected to return an INTEGER.
The function accepts 2D_INTEGER_ARRAY arr as parameter.
"""


def diagonalDifference(arr):
    n = len(arr)

    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0

    for i in range(n):
        primary_diagonal_sum += arr[i][i]
        secondary_diagonal_sum += arr[i][n - i - 1]

    result = abs(primary_diagonal_sum - secondary_diagonal_sum)
    print(result)

    return result


arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

diagonalDifference(arr)
