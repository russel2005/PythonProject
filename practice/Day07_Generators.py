
def square_numbers(nums):
    result = []
    for num in nums:
        result.append(num*num)
    return result


my_nums = square_numbers([1, 2, 3, 4, 5])

print(my_nums)

## using Generator for above code


def square_numbers(nums):
    for num in nums:
        yield (num*num)


my_nums = square_numbers([1, 2, 3, 4, 5])

for num in my_nums:
    print(num)

## above code with list comprehensive

my_nums = (x*x for x in [1,2,3,4,5])

for num in my_nums:
    print(num)
