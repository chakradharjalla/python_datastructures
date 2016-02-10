__author__ = 'pavan'


def isArrayInSortedOrder(A):
    #Base case
    if len(A)==1:
        return True
    return A[0]<=A[1] and isArrayInSortedOrder(A[1:])
A=[0,1,2,3,6,8,9,10,15,19]
print(isArrayInSortedOrder(A))