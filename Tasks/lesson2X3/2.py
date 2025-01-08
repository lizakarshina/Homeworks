# Вивести на екран середній рядок інформації
# (якщо 3 рядка, то другий, якщо чотири - третій)

with open("2.csv", "r") as csv:
    lines = csv.readlines()

print(lines[int(len(lines) / 2)])
