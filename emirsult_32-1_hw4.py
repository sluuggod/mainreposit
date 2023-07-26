# numba1 = input('text:')

rus = 'йцукенгшщзхъфывапролджэячсмитьбю'
eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
rusbolshoy = "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
engbolshoy = "QWERTYUIOP[]ASDFGHJKL;'ZXCVТNBM,."

while True:
    cvt = input('Введите текст: ')
    cvt = str(cvt)
    if cvt == 'q':
        break
    for i in cvt:
        if cvt == '0':
            break
        if i in eng:
            print(rus[eng.index(i)], end='')
        elif i in rusbolshoy:
            print(engbolshoy[rusbolshoy.index(i)], end='')
        elif i in engbolshoy:
            print(rusbolshoy[engbolshoy.index(i)], end='')
        elif i in rus:
            print(eng[rus.index(i)], end='')











