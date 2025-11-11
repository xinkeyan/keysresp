def euclidean_algorithm(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

# 示例
num1 = 30
num2 = 24
gcd_result = euclidean_algorithm(num1, num2)
print(f'{num1} 和 {num2} 的最大公约数是 {gcd_result}')
# 输出: 30 和 24 的最大公约数是 6