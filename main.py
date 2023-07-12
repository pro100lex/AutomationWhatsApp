import pywhatkit


def send_message_instantly():
    """Функция моментального отправления сообщения"""
    phone_number = input('Номер получателя (Пример: +71234567890): ')
    message_text = input('Содержание сообщения: ')

    pywhatkit.sendwhatmsg_instantly(phone_no=phone_number, message=message_text)

    return 'Сообщение доставлено!'


def send_message_through_time():
    """Функция отправки сообщения в определенное время"""
    phone_number = input('Номер получателя (Пример: +71234567890): ')
    message_text = input('Содержание сообщения: ')
    hours = int(input('Во сколько часов: '))
    minutes = int(input('Во сколько минут: '))

    pywhatkit.sendwhatmsg(phone_no=phone_number, message=message_text, time_hour=hours, time_min=minutes)

    return 'Сообщение доставлено!'


def main():
    variants_operations = {1: 'Отправить сообщение пользователю WhatsApp (моментально)', 2: 'Отправить сообщение пользователю WhatsApp (в определенное время)'}

    for key, value in variants_operations.items():
        print(f'{key} => {value}')

    preferred_action = int(input('Выберите предпочитаемое действие: '))

    if preferred_action == 1:
        print(send_message_instantly())

    elif preferred_action == 2:
        print(send_message_through_time())


if __name__ == '__main__':
    main()