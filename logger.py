from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные: \n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{address}\n"
    f"Выберите вариант: "))
    
    while var !=1 and var !=2:
        print('Некорректный ввод')
        var = int(input('Введите число: '))

    if var == 1:
        with open('data_first_var.csv','a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data_second_var.csv','a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")

def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_var.csv','r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
                print('пыщь')
        print(' '.join(data_first_list))


    print('Вывожу данные из 2 файла: \n')
    with open('data_second_var.csv','r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)

print_data()

def change_data():
    var_edit = int(input('В каком вариантевы хотите изменить данные: '))
    
    while var_edit !=1 and var_edit !=2:
        print('Некорректный ввод')
        var_edit = int(input('Введите число: '))

    if var_edit == 1:
        data_first_edit = read_1()
        data_first_edit = change_user(data_first_edit)
        store_1(data_first_edit)
    elif var_edit == 2:
        data_second_edit = read_2()
        data_second_edit = change_user(data_second_edit)
        store_2(data_second_edit)

def change_user(users) :
    user = input('Введите имя контакта который хотите изменить: ')
    for i in range(len(users)):
        if users[i].startswith(user + ';'):
            name = name_data()
            surname = surname_data()
            phone = phone_data()
            address = address_data()
            users[i] = name + ';'+ surname + ';'+ phone + ';'+ address + '\n'
    return users

def delete_data() :
    var_edit = int(input('В каком вариантевы хотите изменить данные: '))
    
    while var_edit !=1 and var_edit !=2:
        print('Некорректный ввод')
        var_edit = int(input('Введите число: '))

    if var_edit == 1:
        data_first_edit = read_1()
        data_first_edit = delete_user(data_first_edit)
        store_1(data_first_edit)
    elif var_edit == 2:
        data_second_edit = read_2()
        data_second_edit = delete_user(data_second_edit)
        store_2(data_second_edit)


def delete_user(users) :
    user = input('Введите имя контакта который хотите удалить: ')
    users_to_delete = []
    for i in range(len(users)):
        if users[i].startswith(user + ';'):
            users_to_delete.append(i)
    for i in users_to_delete:
        users.pop(i)
    return users

def read_1() :
    data_first_edit = []
    with open('data_first_var.csv','r', encoding='utf-8') as f:
        data_first = f.readlines()
        j = -1
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                contact_str = ''.join(data_first[j+1:i+1]).replace('\n\n', '\n').replace('\n', ';')
                data_first_edit.append(contact_str)
                j = i
    return data_first_edit

def read_2() :
    data_second_edit = []
    with open('data_second_var.csv','r', encoding='utf-8') as f:
        data_second = f.readlines()
        for i in range(len(data_second)):
            if data_second[i] != '\n':
                data_second_edit.append(data_second[i])
    return data_second_edit

def store_1(users) :
    with open('data_first_var.csv','w', encoding='utf-8') as f:
        for user in users :
            user_formated = user.replace(';', '\n')
            f.write(user_formated + "\n")

def store_2(users) :
    with open('data_second_var.csv','w', encoding='utf-8') as f:
            f.writelines(line + '\n' for line in users)