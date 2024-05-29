from logger import input_data, print_data, change_data, delete_data

def interface():
    print('Добрый день! Вы попали на справочник GeekBrains!\n 1 - запись данных \n 2 - вывод данных \n 3 - редактирование данных \n 4 - удаление данных')
    command = int(input('\n Введите число: '))

    while command !=1 and command !=2 and command !=3 and command !=4:
        print('Некорректный ввод')
        command = int(input('Введите число: '))
    
    if command == 1:
        input_data()
    if command == 2:
        print_data()
    if command == 3:
        change_data()
    if command == 4:
        delete_data()