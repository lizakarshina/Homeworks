# Напишіть програму, яка приймає два списки та повертає список, 
# який містить елементи, які зустрічаються у обох вхідних списках.

list1 = [1, 2, 3, 4]
list2 = [2, 3, 5, 6]

result_list = []

for item in list1:
    if item in list2:
        result_list.append(item)
        
        
print(result_list)