# 1.
# words_list = ['разработка', 'сокет', 'декоратор']
# for word in words_list:
#     print(word, type(word))
# words_list_unicode = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430', '\u0441\u043e\u043a\u0435\u0442', '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']
# for word in words_list_unicode:
#     print(word, type(word))
# 2.
# words_list_eng = ['class', 'function', 'method']
# for word in words_list_eng:
#     word = eval(f"b'{word}'")
#     print(word, type(word))
# 3.
# words_list_spec = ['attribute', 'класс', 'функция', 'type']
# for word in words_list_spec:
#     try:
#         word = eval(f"b'{word}'")
#     except SyntaxError:
#         print(f'Слово "{word}" невозможно  записать в байтовом типе')
#     else:
#         print(word, type(word))
# 4.
# words_list_enc_dec = ['разработка', 'администрирование', 'protocol', 'standard']
# for word in words_list_enc_dec:
#     word_enc = word.encode()
#     word_dec = word_enc.decode()
#     print(word_enc, type(word_enc), word_dec, type(word_dec))
# 5.
# import chardet
# import subprocess
# import platform
# import locale
#
# default_encoding = locale.getpreferredencoding()
# param = '-n' if platform.system().lower() == 'windows' else '-c'
# args = ['ping', param, '2', 'yandex.ru']
# process = subprocess.Popen(args, stdout=subprocess.PIPE)
# for line in process.stdout:
#     result = chardet.detect(line)
#     # print('result = ', result)
#     line = line.decode(default_encoding)
#     print(line)
#
# [print(line.decode(default_encoding)) for line in (subprocess.Popen(['ping', param, '2', 'youtube.ru'], stdout=subprocess.PIPE)).stdout]

# 5.
from chardet import detect

lines = ['сетевое программирование', 'сокет', 'декоратор']

with open('test.txt', 'w', encoding='utf-8') as f:
    for line in lines:
        f.write(line + '\n')

with open('test.txt', 'rb') as f:
    content = f.read()
encoding = detect(content)['encoding']

with open('test.txt', encoding=encoding) as f_n:
    for el_str in f_n:
        print(el_str, end='')
    print()


try:
    f = open('test.txt', 'rb', encoding='Unicode')
except ValueError:
    print("binary mode doesn't take an encoding argument")