#for_loop

nums = [0,1,2,3,4,5,6];

for num in nums:
    print(num);

#for loop with range function

for para in range(2):  #the loop works twice
    print("hello", para);

for num in range (5,11):    # range(inclusive, exclusive)
    print (num)

gadgets = ["phone", "laptop", "headphone", "webcam", "keyboard"];
for gadget in range(len(gadgets)):  #gadget = 0/1/2/3/4
    print(gadgets[gadget]);


#while loop
x=1
while x<=5:
    print(f"while loop {x}");
    x+=1;