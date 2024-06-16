# 初始化一个空列表来存储数字
numbers = []

# 提示用户输入 5 个数字
for i in range(5):
    number = float(input("Number: "))
    numbers.append(number)

# 输出数字的相关信息
print(f"The first number is {int(numbers[0])}")
print(f"The last number is {int(numbers[-1])}")
print(f"The smallest number is {int(min(numbers))}")
print(f"The largest number is {int(max(numbers))}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")
