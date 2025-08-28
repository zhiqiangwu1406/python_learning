nums = [1,5,7,8,9,6,7,4,5,1,6,7,8];

print(sorted(nums)); #sort the list in ascending order

print(list(reversed(nums))); #reverse the given list

print(set(nums)) #only one is included in returned list if there is repetition

for num in set(nums):
    print(num);


print(nums.count(1)); #count the number of data given to count (1) in the list


words = ["B", "e", "a", "E", "ef", "er", "wo", "QW", "BE"];

print(sorted(words))