from sys import argv

with open('bakery.csv', 'a', encoding='utf-8') as file_a:
    with open('bakery.csv', 'r', encoding='utf-8') as file_r:
        if len(argv) > 1 and [i for i in argv[1:] if '.' in i and i.replace('.', '').isdigit()]:
            if round(float(argv[1]), 3) <= 99999.999:
                print(f'{round(float(argv[1]), 3):>10}', file=file_a)
            else:
                print('число больше 99999.999')
        else:
            print(file_r.read())
