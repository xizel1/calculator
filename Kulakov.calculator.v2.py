a = int(input())
b = int(input())
c = input()
if c == '+':
    print(a '+' b '=', a + b)
elif c == '-':
    print('a - b =', a - b)
elif c == '*':
    print('a * b =', a * b)
elif c == '//':
    print('a // b =', a // b)
elif c == '/':
    print('a / b =', a / b)
elif c == '**':
    print('a ** b =', a ** b)
elif c == '√':
    print('a ** 0.5 =',  a ** 0.5, ', ' 'b ** 0.5 =', b ** 0.5)
elif c == '%':
    print('a % b =', a % b)
else:
    print('')
