print('\033[33mDIGITE 0 PARA PARAR!')
while True:
    tab = int(input('\033[38mQuer ver a tabuada de qual valor? \033[0m'))
    if tab == 0:
        break
    print('-' * 33)
    for c in range(0, 10):
        c += 1
        print(f'{tab} x {c} = {tab*c}')
    print('-' * 33)
print('\033[31mProgama finalizado.')
