def custom_write(filename: str, info: list):
    file = open(filename, 'w', encoding='utf-8')
    ret = {}
    i = 0
    for str_ in info:
        i += 1
        ret[(i, file.tell())] = str_
        file.write(str_ + '\n')

    return ret


if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)
