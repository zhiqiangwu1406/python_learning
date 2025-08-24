#lists []

nums = [11,12,13,14,15]

nums[0] #11
nums[-1] #15

#slice method [inclusive:exclusive]

nums[2:5] #[13,14]

#adding lists

num1=[1,2,3]
num2=[4,5,6]
combinedNum = num1 + num2 #[1,2,3,4,5,6]
print(combinedNum)

#changing value in lists

Num = [1,2,3,4]
print("initial num", Num)
Num[3]=146;
print("changed num", Num)


#append to lists

num = [5,6,7,8]
num.append(9)
print(num)

#pop method (delete the last value and return the list)

num = [1,2,3]
print(num.pop());

#remove method remove(value) {value to be deleted should be added in bracket not the index}

num = [1,2,3,4,5]
num.remove(5)
print(num)


#delete method

nums=[1,2,3,4,5,6,7,8,9]
del(nums[5]);
print(nums);

#combined del and slice methods to delete specific part of the list

nums=[1,2,3,4,5,6,7,8,9];
del(nums[1:5])
print(nums);


#multi-dimensional list

twoDList = ['hello',1,1.5,[1,2,3]];

print(twoDList[3][1]) #2

