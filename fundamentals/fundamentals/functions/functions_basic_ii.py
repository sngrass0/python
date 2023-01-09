#1 Countdown
def countdown(val):
    ret = []
    for x in range(val, -1, -1):
        ret.append(x)
    return ret

#2 Print and Return
def print_and_return(arr):
    print(arr[0])
    return arr[1]

#3 First Plus Length
def first_plus_length(arr):
    return arr[0] + len(arr)

#4 Values Greater than Second
def values_greater_than_second(arr):
    if len(arr) < 2:
        return False
    ret = []
    val = 0
    second = arr[1]
    for x in arr:
        if x > second:
            ret.append(x)
            val += 1
    return ret

#5 This Length, That Value
def this_len_that_val(size, val):
    ret = []
    for x in range(size):
        ret.append(val)
    return ret

# OUTPUT
print(countdown(5))
print(print_and_return([1,2]))
print(first_plus_length([1,2,3,4,5]))
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))
print(this_len_that_val(4,7))
print(this_len_that_val(6,2))