# тут важный момент, на уроке мы установили googletrans 3.0.0 он не работал, но на stackoverflow я нашел решение и
# поделился в телеге решением. Нужно было обновить googletrans до 3.1.0a0 с помощью pip.
# pip3 install googletrans==3.1.0a0
# Для задания я использовал text4_1.txt как исходный файл, и создал text4_2.txt как переведенный.
from googletrans import Translator
translator = Translator()
with open("text4_1.txt", "r") as f:
    with open("text4_2.txt", "w") as f_new:   # открываем сразу два файла одновременно. 1 для чтения, 2 для записи.
        for i in f.readlines():
            translation = translator.translate(i, dest="ru")   # выбираем dest="ru" чтобы перевело на русский язык.
            f_new.write(f'{translation.text}\n')    # Создаем новый файлик, и построчно переводим и записываем.
