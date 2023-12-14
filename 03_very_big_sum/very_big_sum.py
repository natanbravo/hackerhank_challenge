"""
LINK TO CHALLENGE DESCRIPTION:
https://hackerrank-challenge-pdfs.s3.amazonaws.com/8781-a-very-big-sum-English?response-content-disposition=inline%3B%20filename%3Da-very-big-sum-English.pdf&response-content-type=application%2Fpdf&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAR6O7GJNX5DNFO3PV%2F20231214%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231214T134441Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=b4f91330a1eaa0d05ca71ec56fa96a41dcbda4d8b9882f8a4b4fa470dc024b5e


------------------------------------------------------------
Complete the 'aVeryBigSum' function below.
 The function is expected to return a LONG_INTEGER.
 The function accepts LONG_INTEGER_ARRAY ar as parameter.
------------------------------------------------------------
"""


def aVeryBigSum(ar):
    result = sum(i for i in ar)
    print(result)
    return result


ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
aVeryBigSum(ar)
