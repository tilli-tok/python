file_path = "Demo.log"

try:
    line_count = line_nec = line_sharp = line_sony = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for lines in file:
            line_count += 1
            if 'NEC' in lines:
                line_nec += 1
            if 'SHARP' in lines:
                line_sharp += 1
            if 'SONY' in lines:
                line_sony += 1
        print(f"Количество строк в файле: {line_count}")
        print(f"NEC: {line_nec}")
        print(f"SHARP: {line_sharp}")
        print(f"SONY: {line_sony}")
except FileNotFoundError:
    print("Файл не найден")


def counts(lines,search_type):
    line_count = 0
    for line in lines:
        if search_type in line:
            line_count += 1
    return f"\t {search_type}: {line_count}"
print('Второй способ:\n')
try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)

        print(f'Количество строк в файле: {line_count}')
        print(counts(lines,'NEC'))
        print(counts(lines,'SHARP'))
        print(counts(lines,'SONY'))
except FileNotFoundError:
    print("Файл не найден")

