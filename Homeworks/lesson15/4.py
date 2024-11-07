# Напишіть функцію, яка приймає два списки та повертає True,
# якщо обидва списки містять однакові елементи, незалежно від їх порядку.

list1 = [1, 2, 3, 4]
list2 = [4, 3, 2, 1]


def compare_lists(first_list, second_list):

    if len(list1) != len(list2):
        return False

    if first_list.sort() == second_list.sort():
        return True

    return False


print(compare_lists(list1, list2))
