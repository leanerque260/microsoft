# 这是一个简单的计算器程序
# 定义四则运算函数
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# 询问用户要进行哪种运算
print("请选择运算：")
print("1. 加法")
print("2. 减法")
print("3. 乘法")
print("4. 除法")

choice = input("请输入你的选择(1/2/3/4): ")

# 询问用户要输入的两个数
num1 = float(input("请输入第一个数: "))
num2 = float(input("请输入第二个数: "))

# 根据用户的选择进行相应的运算，并打印结果
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("无效的输入")
