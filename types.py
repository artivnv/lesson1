#v = input('Введите число от 1 до 10: ')
#print(int(v) + 10)

#name = input ('Введите ваше имя: ')
#print ()

#list = [3, 5, 7, 9, 10.5]
#ist.append('Python')
#print('Список целиком' , list)
#print('Длина списка' , len(list))



def get_summ(one, two, delimiter = '&'):
    one = str(one)
    two = str(two)
    text = (one + delimiter + two)
    return text
print(get_summ('Learn', 'python'))



