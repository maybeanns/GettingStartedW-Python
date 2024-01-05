# print
print("this is me checking")
#length
length = len("name")
#input
name = input("Your name is:" )
#max/min
maxi = max(2,4,6)
mini = min(2,50,9)
#range
numbers = list(range(5))
#sum
result = sum([1,2,3,4,5,6])
#sort
result2 = sorted([3,4,67,2,1,5])
#type 
data_type = type(10)
#result expression from a string
result3 = eval("2+3")
#another one
strings = ['apple', 'banana', 'cherry']
longest_string = max(strings, key=len)  # 'banana'
#filter
def is_even(n):
    return n % 2 == 0
numbers = [1, 2, 3, 4, 5]
evens = list(filter(is_even, numbers))  # [2, 4]
#map 
def is_even(n):
    return n % 2 == 0
numbers = [1, 2, 3, 4, 5]
evens = list(filter(is_even, numbers))  # [2, 4]
#any and all
nums = [True, False, True]
result_any = any(nums)  # True
result_all = all(nums)  # False
#pair elements
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
combined = list(zip(letters, numbers))  # [('a', 1), ('b', 2), ('c', 3)]
#enumerator
for index, value in enumerate(['a', 'b', 'c']):
    print(index, value)

