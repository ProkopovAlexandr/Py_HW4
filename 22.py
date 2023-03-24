def input_set(num_t):
    len_set = int(input(f'Введите длину {num_t} множества: '))
    st = set()
    i = 0

    while i < len_set:
        st.add(int(input(f'Введите элемент {num_t} множества:')))
        i += 1
    return st

a = list(input_set('первого').union(input_set('второго')))
a.sort()
print(*a)