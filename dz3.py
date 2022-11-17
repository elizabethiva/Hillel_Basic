x = int(input())
first = x // 10000
second = x // 1000 % 10
third = x % 1000 // 100
fourth = x % 100 // 10
fifth = x % 1000 % 10
print(fifth * 10000 + fourth * 1000 + third * 100 + second * 10 + first * 1)
