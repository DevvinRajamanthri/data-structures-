def sum_array(A:list):
    i = 0
    sum = 0
    for i in range(len(A)):
        sum = sum + A[i]
    return sum

A = [1,2,3]
result = sum_array(A)
print(result)