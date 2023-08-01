"""ЗАДАНИЕ 13.8.19 """

cost_of_all_tickets = 0  # счетчик общей стоимости билетов

while True:
    try:
        number_of_tickets = int(input('Какое количество билетов вы хотите приобрести: '))

        '''Проверка на количество билетов'''
        if number_of_tickets < 0:
            print('Значение введено не верно. Попробуйте еще раз.\n')
            continue
        elif number_of_tickets == 0:
            print('Значение введено не верно. Попробуйте еще раз.\n')
            continue

        for num in range(number_of_tickets):
            age = int(input(f'Укажите возраст посетителя конференции {num + 1}: '))

            '''Проверка возраста'''
            if age < 18:
                continue
            elif 18 <= age < 25:
                cost_of_all_tickets += 990
            else:
                cost_of_all_tickets += 1390

        if number_of_tickets > 3 and cost_of_all_tickets != 0:
            cost_of_all_tickets -= cost_of_all_tickets // 10  # вычитаем скидку 10% из стоимости всех билетов
            print('\nВы зарегистрировали на конференцию более трех человек и вам полагается скидка 10%')
            print(f'Сумма к оплате: {cost_of_all_tickets}')  # вывод со скидкой
            break
        else:
            print(f'Сумма к оплате: {cost_of_all_tickets}')
            break

    except ValueError:
       print('Значение введено не верно. Попробуйте еще раз.\n')