"""
For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.

Write an efficient algorithm for the following assumptions:

N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times.
"""

def solution(A): 
    num = 0
    for i in A:
        # this works because XOR is associative
        # that is 3 ^ 3 ^ 1 == 3 ^ 1 ^ 3, which returns 1,
        # because 3 ^ 3 == 0 and 0 ^ any_number returns any_number.
        # In the end, the even numbers result in a 0 and we end up with:
        # 0 ^ odd_number.
        num = num ^ i 

    return num

if __name__ == '__main__':
    print(solution([3,1,1,3,4]))