def input_surname():
    return input("Введите фамилию контакта: ").title()

def input_name():
    return input("Введите имя контакта: ").title()

def input_patrname():
    return input("Введите отчетсво контакта: ").title()

def input_phone():
    return input("Введите телефон контакта: ")

def input_adress():
    return input("Введите адрес контакта: ")

def input_data():
    surname = input_surname()
    name = input_name()
    petronymic = input_patrname()
    phone = input_phone()
    adress = input_adress()
    str_contact = f"{surname} {name} {petronymic} {phone} {adress} \n\n"
    with open("phonebook.txt", "a", encoding = "UTF-8") as file:
        file.write(str_contact)

def read_file():
    with open("phonebook.txt", "r", encoding = "UTF-8") as file:
        return file.read()
    
def del_contacts_from_file(contscts_list):
    contacts_list = read_file().rstrip().split("\n\n")
    with  open("phonebook.txt", "w", encoding = "UTF-8") as file:
        for contact in contacts_list:
            if contact not in contscts_list:
                file.write(contact + "\n\n")
def change_contact_from_file(change_contact):
    contacts_list = read_file().rstrip().split("\n\n")
    with  open("phonebook.txt", "w", encoding = "UTF-8") as file:
        for contact in contacts_list:
            if contact == change_contact:
                print("Ввод новых значений констакта для изменения\n")
                surname = input_surname()
                name = input_name()
                petronymic = input_patrname()
                phone = input_phone()
                adress = input_adress()
                contact = f"{surname} {name} {petronymic} {phone} {adress} "    
            file.write(contact + "\n\n")

def print_data():
    print(read_file())

def find_data():
    print ("Варианты для поиска\n"
          "1) Фамилия\n"
          "2) Имя\n"
          "3) Отчество\n"
          "4) Телефон\n"
          "5) Адрес\n")
    
    comm = input("Укажите номер варианта поиска: ")
    
    while comm not in ("1", "2", "3", "4", "5"):
            print("Некорректный номер!\n")
            comm = input("Укажите номер варианта поиска: ")
    
    i_param = int(comm) - 1
   
    find_str = input("\nВведите данные для поиска: ").title()
   
    contacts_list = read_file().rstrip().split("\n\n")
   
    count = 0
    for contact in contacts_list:
        contact_lst = contact.split(" ")

        if find_str in contact_lst[i_param]:
            print("\n - " + contact)
            count = 1

    if count == 0:
       print("\nКонтактов с заданными данными в сравочнике не обнаружено")
      
    
# дополнить справочник возможностью изменения и удаления данных (по выбору). 
# Пользователь также может ввести имя и фамилию, и вы должны реализовать 
# функционал для изменения и удаления данных

def change_data():
    contacts_list = read_file().rstrip().split("\n\n")
    flag = 1
    while flag == 1:
        print ("Варианты поиска контакта для изменения\n"
            "1) По фамилии\n"
            "2) По имени\n"
            "3) По отчеству\n"
            "4) По телефону\n"
            "5) По адресу\n")
        command = input("Укажите номер варианта поиска: ")
        while command not in ("1", "2", "3", "4", "5"):
                print("Некорректный номер!\n")
                command = input("Укажите номер варианта: ")
        i_param = int(command) - 1
   
        find_str = input("\nВведите данные для поиска: ").title()
    
        temp_list = []
        count = 0
        for contact in contacts_list:
            contact_lst = contact.split(" ")

            if find_str in contact_lst[i_param]:
                temp_list.append(contact)
                count += 1
        
        if count == 0:
            print("Контактов с заданными параметрами не нейдено.\n"
                  "1) Вернуться на шаг назад\n"
                  "2) Начать заново\n"
                  "3) Отменить изменение контакта")
            cmd = input("Укажите номер варианта действия: ")
            
            while cmd not in ("1", "2", "3"):
                print("Некорректный номер!\n")
                cmd = input("Укажите номер варианта действия: ")
            
            match cmd:
                case "2":
                    contacts_list = read_file().rstrip().split("\n\n")
                case "3":
                    flag = 0

        elif count > 1:
            print("Найденные контакты:")
            print(*temp_list, sep="\n")
            print("\nВыберете действие:\n"
                  "1) Продолжить выбор в найденных контактах\n"
                  "2) Начать заново\n"
                  "3) Отменить изменение контакта")
            cmd = input("Укажите номер варианта действия: ")
            
            while cmd not in ("1", "2", "3"):
                print("Некорректный номер!\n")
                cmd = input("Укажите номер варианта действия: ")
            
            match cmd:
                case "1":
                    contacts_list = temp_list                
                case "2":
                    contacts_list = read_file().rstrip().split("\n\n")
                case "3":
                    flag = 0

        else:
            print("Найденный контакт:")
            print(*temp_list)
            print("\nВыберете действие:\n"
                  "1) Изменить найденный контакт\n"
                  "2) Отменит изменение контакта")
            cmd = input("Укажите номер варианта действия: ")
            
            while cmd not in ("1", "2"):
                print("Некорректный номер!\n")
                cmd = input("Укажите номер варианта действия: ")
            
            match cmd:
                case "1":
                    change_contact_from_file(temp_list[0])
                    print("\nКонтакт изменен")
                    flag = 0
                case "2":
                    flag = 0

def del_data():
    
    contacts_list = read_file().rstrip().split("\n\n")
    flag = 1
    while flag == 1:
        print ("Варианты поиска контакта для удаления\n"
            "1) По фамилии\n"
            "2) По имени\n"
            "3) По отчеству\n"
            "4) По телефону\n"
            "5) По адресу\n")
        command = input("Укажите номер варианта поиска: ")
        while command not in ("1", "2", "3", "4", "5"):
                print("Некорректный номер!\n")
                command = input("Укажите номер варианта: ")
        i_param = int(command) - 1
   
        find_str = input("\nВведите данные для поиска: ").title()
    
        temp_list = []
        count = 0
        for contact in contacts_list:
            contact_lst = contact.split(" ")

            if find_str in contact_lst[i_param]:
                temp_list.append(contact)
                count += 1
        
        if count == 0:
            print("Контактов с заданными параметрами не нейдено.\n"
                  "1) Вернуться на шаг назад\n"
                  "2) Начать заново\n"
                  "3) Отменит удаление контакта")
            cmd = input("Укажите номер варианта действия: ")
            
            while cmd not in ("1", "2", "3"):
                print("Некорректный номер!\n")
                cmd = input("Укажите номер варианта действия: ")
            
            match cmd:
                case "2":
                    contacts_list = read_file().rstrip().split("\n\n")
                case "3":
                    flag = 0

        elif count > 1:
            print("Найденные контакты:")
            print(*temp_list, sep="\n")
            print("\nВыберете действие:\n"
                  "1) Удалить все найденные контакты\n"
                  "2) Продолжить выбор в найденных контактах\n"
                  "3) Начать заново\n"
                  "4) Отменит удаление контакта")
            cmd = input("Укажите номер варианта действия: ")
            
            while cmd not in ("1", "2", "3", "4"):
                print("Некорректный номер!\n")
                cmd = input("Укажите номер варианта действия: ")
            
            match cmd:
                case "1":
                    del_contacts_from_file(temp_list)
                    print("\nКонтакты удалены")
                    flag = 0
                case "2":
                    contacts_list = temp_list                
                case "3":
                    contacts_list = read_file().rstrip().split("\n\n")
                case "4":
                    flag = 0

        else:
            print("Найденный контакт:")
            print(*temp_list)
            print("\nВыберете действие:\n"
                  "1) Удалить найденный контакт\n"
                  "2) Отменит удаление контакта")
            cmd = input("Укажите номер варианта действия: ")
            
            while cmd not in ("1", "2"):
                print("Некорректный номер!\n")
                cmd = input("Укажите номер варианта действия: ")
            
            match cmd:
                case "1":
                    del_contacts_from_file(temp_list)
                    print("\nКонтакт удален")
                    flag = 0
                case "2":
                    flag = 0

                

def interface():
    with  open("phonebook.txt", "a", encoding = "UTF-8") as file:
        pass

    print("Выберите вариант работы с телефонной книгой:\n"
           "1) Запись данных\n"
           "2) Вывод телефонной книги на экран\n"
           "3) Поиск контактов\n"
           "4) Изменение контакта\n"
           "5) Удаление контакта\n"
           "6) Выход")
    command = ""    
    while command != "6":   
        command = input("\nВведите номер операции: ")
        
        while command not in ("1", "2", "3", "4", "5", "6"):
            print("Некорректный номер операции!\n")
            command = input("Введите номер операции: ")
        
        match command:
            case "1": 
                input_data()
            case "2":
                print_data()
            case "3":
                find_data()
            case "4":
                change_data()
            case "5":
                del_data()
            case "6":
                print("Выход из приложения")
    
    
interface()