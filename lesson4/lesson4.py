# string formatting
index1 = 1
index2 = 2
index3 = 3
# print('index1 =', index1, ',', 'index2 = ', index2, ', ' 'index3 = ', index3)

# a = f'abc {index3 * 0.1}' + '123' + f'xyz {index1}'
# print(a)

# f-string
print(f'index1 = {index1}, index2 = {index2}, index3 = {index3}')
print(f'{index1=}, {index2=}, {index3=}')
print(f'{index1} является четным числом: {index1 % 2 == 0 = }\n')

# str.format()
print('index1 = {}, index2 = {}, index3 = {}'.format(index1, index2, index3))
print('index2 = {1}, index1 = {0}, index3 = {2}'.format(index1, index2, index3))
print(
    'index3 = {num3}, index1 = {num1}, index2 = {num2}'.format(
        num1=index1,
        num2=index2,
        num3=index3,
    ),
)
print('{} является четным числом: {}\n'.format(index1, index1 % 2 == 0))

# %
print('index1 = %s, index2 = %s, index3 = %s\n' % (index1, index2, index3))

# if-elif-else, and/or/in/not
age = int(input('Введите ваш возраст: '))
name = ''

if age >= 10:
    print(f'Вам {age} лет!')
elif age > 0:
    print('Пользоваться программой можно по достижению 10 лет')
elif age == 0:
    print('Поздравляем! Вы родились!')
else:
    print('Возраст не может быть меньше нуля')


if not name:
    print('Вы ничего не ввели')
else:
    print(f'Привет, {name}!')
