# 4. Разделение списка на подсписки

# На вход подается строка чисел, из которой формируется список. 
# Напишите программу, создающую вложенный список, элементами которого являются все возможные подсписки исходного списка, включая пустой.

# Способ 1:

lst = input().split()
def sub_lists(lst):
    lists = [[]]
    for i in range(len(lst) + 1):
        for j in range(i):
            lists.append(lst[j:i])
    lists = sorted(lists, key=len)
    return lists
print(sub_lists(lst))

# Способ 2:

print([[]] + [lst[j:i + j + 1] for lst in [input().split()] for i in range(len(lst)) for j in range(len(lst) - i)])


# Способ 3:

st, lst = input().split(), [[]]
for i in range(1, len(st) + 1):
    for j in range(len(st) - i + 1):
        lst += [st[j:j+i]]
print(lst)

