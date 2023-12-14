#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#


def simpleArraySum(ar):
    result = sum(i for i in ar)
    print(result)
    
    return result 


ar = [1, 2, 3, 4, 10, 11]
simpleArraySum(ar)
