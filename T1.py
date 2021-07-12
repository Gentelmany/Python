#Напишите программу, которая принимает на вход список чисел в одной строке
#и выводит на экран в одну строку значения, которые встречаются в нём более одного раза.
#Для решения задачи может пригодиться метод sort списка.
#Выводимые числа не должны повторяться, порядок их вывода может быть произвольным
g = []
countt = [int(i) for i in input().split()]
srtcountt = sorted (countt)
for i in srtcountt:
    s = srtcountt.count (i)
    if i in g:
            continue
    elif s>1:
        g.append(i)
    else:
        continue
for j in g:
    print(j, end = ' ')

