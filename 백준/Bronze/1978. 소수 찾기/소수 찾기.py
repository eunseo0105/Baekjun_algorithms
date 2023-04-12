def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

n = int(input())  
nums = list(map(int, input().split())) 

count = 0 
for num in nums:
    if is_prime(num):
        count += 1

print(count)  

