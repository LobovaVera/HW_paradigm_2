def get_num():
    flag = True
    message = "Введено некорректное значение!"
    while flag:
        num = input('Введите число: ')
        try:
            num = int(num)
            if 0 < num < 11:
                flag = False
            else:
                print(message)
        except ValueError:
            print(message)
    return num


def print_multi_table(num: int):
    for i in range(1, num + 1):
        for j in range(1, 11):
            print(f'{i} x {j} = {i * j}')
        print()


def main():
    print_multi_table(get_num())


if __name__ == '__main__':
    main()