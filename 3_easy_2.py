# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    """Помогает распознать счастливый билет"""
    # для удобства обработки, превращаем значение билета в str
    ticket_number = str(ticket_number)
    digit_list = []
    # создаем список, который хранит цифры билета
    for digit in ticket_number:
        digit = int(digit)
        digit_list.append(digit)

    left_part = sum(digit_list[:3])
    right_part = sum(digit_list[3:])

    if left_part == right_part:
        return "Счастливый"
    else:
        return "Несчастливый"


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
