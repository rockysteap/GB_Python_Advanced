# Задание #6
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

account = 0
operation_counter = 0
reward_operation_rate = 3
reward_percent_on_operation = 3
deposit_and_withdrawal_rate_step = 50
percent_of_interest_on_withdrawal = 1.5
withdrawal_min_amount = 30
withdrawal_max_amount = 600
wealth_tax_threshold = 5_000_000
wealth_tax_percent = 10

while True:
    print('Ваш баланс: ', account)
    print('Допустимые действия: 1.пополнить, 2.снять, 3.выйти')
    user_input, main_actions = '', ('1', '2', '3')
    # Ввод пользователя
    while True:
        user_input = input('Выберите действие: ')
        if user_input in main_actions:
            break

    # Выход
    if user_input == '3':
        exit()

    if user_input == '1':
        while True:
            user_input = input(f'Введите сумму для пополнения (кратно {deposit_and_withdrawal_rate_step}): ')
            if account > wealth_tax_threshold:
                wealth_tax = account * wealth_tax_percent / 100
                print('Вычтен налог на богатство в размере:', wealth_tax)
                account -= wealth_tax
            try:
                deposit_amount = int(user_input)
            except ValueError:
                continue
            if deposit_amount % deposit_and_withdrawal_rate_step == 0:
                operation_counter += 1
                account += deposit_amount
                if operation_counter % reward_operation_rate == 0:
                    reward = account * reward_percent_on_operation / 100
                    account += reward
                    print('Начислены проценты в размере:', reward)
                break

    if user_input == '2':
        while True:
            user_input = input(f'Введите сумму для снятия (кратно {deposit_and_withdrawal_rate_step}): ')
            if account > wealth_tax_threshold:
                wealth_tax = account * wealth_tax_percent / 100
                print('Вычтен налог на богатство в размере:', wealth_tax)
                account -= wealth_tax
            try:
                withdrawal_amount = int(user_input)
            except ValueError:
                continue
            if withdrawal_amount % deposit_and_withdrawal_rate_step == 0:
                withdrawal_fee = withdrawal_amount * (percent_of_interest_on_withdrawal / 100)
                bank_interest = (withdrawal_min_amount
                                 if withdrawal_fee < withdrawal_min_amount else withdrawal_max_amount
                                 if withdrawal_fee > withdrawal_max_amount else withdrawal_fee)
                print('Комиссия за снятие:', bank_interest)

                if withdrawal_amount + bank_interest > account:
                    print('Недостаточно средств для вывода:', withdrawal_amount, 'с учетом комиссии', bank_interest)

                operation_counter += 1
                account -= (withdrawal_amount + bank_interest)
                if operation_counter % reward_operation_rate == 0:
                    reward = account * reward_percent_on_operation / 100
                    account += reward
                    print('Начислены проценты в размере: ', reward)
                break
