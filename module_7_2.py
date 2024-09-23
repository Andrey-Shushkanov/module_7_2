def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, 'a', encoding='utf-8') as file:
        for number_string, string in enumerate(strings, start=1):
            strings_positions[(number_string, file.tell())] = string
            file.write(f'{string}\n')
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)