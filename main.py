import random
import sys

vizov = input()
if vizov == 'Андрей':
    print('Здравствуйте, я голосовой помощник Андрей.')
    print('Скажите какая сейчас погода и я скажу вам что надеть и что взять с собой.')
    print('солнечная, дождливая, снежная, ветреная.')
else:
    print('...')
    sys.exit()
pogoda = input()
if pogoda == 'солнечная':
    print('Оденьте шорты, майку и панамку.')
else:
    if pogoda == 'дождливая':
        print('Оденьте штаны, рубашку, ковту, дождивик и возьмите зонтик.')
    else:
        if pogoda == 'снежная':
            print('Оденьте термобельё, штаны, майку, кофту, куртку, шарф и шапку.')
        else:
            if pogoda == 'ветреная':
                print('Оденьте штаны, кофту, ветровку и шарф.')
            else:
                print('ошибка')
                sys.exit()
print('Я также могу выбрать в случайном порядке число от 1 до 10. Мне это стделать или не сделать?')
r = input()
if r == 'сделать':
    letters_list: list[str] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    random_index = random.randint(0, len(letters_list) - 1)
    print(letters_list[random_index])
else:
    print('Хорошо')
    sys.exit()