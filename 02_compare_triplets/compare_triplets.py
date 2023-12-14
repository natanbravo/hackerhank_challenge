"""
LINK TO CHALLENGE DESCRIPTION: 
https://hackerrank-challenge-pdfs.s3.amazonaws.com/21400-compare-the-triplets-English?response-content-disposition=inline%3B%20filename%3Dcompare-the-triplets-English.pdf&response-content-type=application%2Fpdf&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAR6O7GJNX5DNFO3PV%2F20231214%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231214T133355Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=786c0e8d51baaef282fff86705fcee00f4f91997b956fc8dd52cc38c1767bdf4

----------------------------------------------------------
    Complete the 'compareTriplets' function below.
    The function is expected to return an INTEGER_ARRAY.
    The function accepts following parameters:
    1. INTEGER_ARRAY a
    2. INTEGER_ARRAY b
----------------------------------------------------------
"""

def compareTriplets(a, b):
    alice_triplet = 0
    bob_triplet = 0

    for a_val, b_val in zip(a, b):
        if a_val > b_val:
            alice_triplet += 1

        elif a_val < b_val:
            bob_triplet += 1

        else:
            alice_triplet += 0
            bob_triplet += 0

    print(alice_triplet, bob_triplet)

    return alice_triplet, bob_triplet


a = [17, 28, 30]

b = [99, 16, 8]

compareTriplets(a, b)
