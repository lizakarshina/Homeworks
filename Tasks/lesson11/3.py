# Написати програму, що прибере дублікати зі списку.

list = [1, 1, 1, 2, 2, 3, 3, 5, 255]

# i = 0
# j = 1



# while j < len(list):
#     if list[i] == list[j]:
#         list.remove(list[j])
#     else:
#         i += 1
#         j += 1
        

for item in list:
    
    if list.count(item) > 1:
        list.remove(item)    
    
print(list)