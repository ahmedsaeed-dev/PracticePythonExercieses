def get_input(dict = {}):
    name = input("Enter name: ")
    birthday = input("Enter birthday in YYYY-MM-DD format: ")
    dict[name] = birthday
    return dict

if __name__ == '__main__':
    bday_dict = get_input()
    print(bday_dict)

    #TODO create search func for birthdays + maybe read birthdays from file first