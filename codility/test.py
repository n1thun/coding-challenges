def solution(A):
    # write your code in Python 2.7
    n = len(A)
    soln = []
    for x in range(1,n):
        print ("\n new round")
        sum_left = sum(A[:x])
        print(A[:x])
        print(sum_left)
        sum_right = sum(A[x+1:])
        print(A[x+1:])
        print(sum_right)
        if (sum_left == sum_right):
            return x
        else:
            pass

    return (A[x])

z = [-2,3,-4,5,1,-6,2,1]

print (solution(z))
