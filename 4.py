n = 100
m = 50
nums = list(range(n))

'1. What is the time complexity of the code below?'
total = 0
for x in nums:
    total += x



'2. What is the time complexity of the code below?'
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i, j, k)

        
        
'3. What is the time complexity of the code below?'
for i in range(n):
    print(i)
for j in range(m):
    print(j)



'4. What is the time complexity of the statement below?'
nums.insert(0, x)



'5. What is the time complexity of the statement below?'
nums.pop()



'6. What is the time complexity of the statement below?'
nums.pop(0)



'7. What is the time complexity of the code below?'
i = 1
while i < n:
    i *= 2



'8. What is the time complexity of the statement below?'
copy = nums[:]



'9. What is the time complexity of the code below?'
for i in range(0, n, 2):
    print(i)



'10. What is the time complexity of the code below?'
i = 0
while i * i < n:
    i += 1