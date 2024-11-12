# Написати функцію підписки користувача, яка приймає
# на вхід електронну пошту, прізвище, відмітку про
# погодження отримувати:
# розсилку «Новини»,
# розсилку «Що нового»
# рекламну розсилку.
# Останні три параметри мають значення за замовчуванням True.
# Викликати цю функцію з різними наборами аргументів.
# Передбачити в програмі глобальний список розсилки і додавати
# пошту користувача в цей список.


subs_users = {}


def subscription(email, last_name, sub_news=True, sub_changes=True, advers=True):

    global subs_users

    subs_users[email] = {
        "last_name": last_name,
        "subs_news": sub_news,
        "sub_changes": sub_changes,
        "advers": advers,
    }

    is_all_true = sub_news and sub_changes and advers
    is_all_false = not sub_news or not sub_changes or not advers

    if is_all_true:
        print(
            f"Ви ({last_name}) підписалися на всі існуючі розсилки які можна, тепер ваша пошта не буде відпочивати 😘\n"
        )
    else:

        if sub_news:
            print(
                f"Ви ({last_name}) підписалися на останні новини 😘",
            )

        if sub_changes:
            print(
                f"Ви ({last_name}) підписалися на чендж лог нових оновлень 😘",
            )

        if advers:
            print(
                f"Ви ({last_name}) підписалися на рекламну розсилку 😘\n",
            )

    if is_all_false:
        print("Ви не підписалися ні на які розсилки 😭")


def show_all_users():

    global subs_users

    for key, val in subs_users.items():
        print(f"{key}:")
        for kluch, value in val.items():
            print(f"\t{kluch}: {value}")
        print()

# фу
def is_true(var):
    if var == "y":
        return True
    else:
        return False


while True:
    print()

    number = int(input("1. Підписатися\n2. Подивитися всіх\n3. Вийти\n"))

    if number in range(1, 4):
        if number == 1:
            print()
            email = input("Введіть електронну адресу\n")
            print()

            last_name = input("Введіть прізвище\n")

            print()

            sub_news = input("Хочете отримувати останні новини? (y/n)\n")

            print()

            sub_changes = input("Хочете отримувати чендж лог нових оновлень? (y/n)\n")

            print()
            advers = input("Хочете отримувати рекламну розсилку? (y/n)\n")
            print()

            sub_news = is_true(sub_news)
            sub_changes = is_true(sub_changes)
            advers = is_true(advers)

            subscription(
                email=email,
                last_name=last_name,
                sub_news=sub_news,
                sub_changes=sub_changes,
                advers=advers,
            )

        if number == 2:
            print()
            if subs_users:
                show_all_users()
                
            else:
                print('Ніхто не підписався 😥')
            print()
            
        if number == 3:
            break
    else:
        print()
        print("Некорректна комманда")
