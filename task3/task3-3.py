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

'''
try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)
except FileNotFoundError:
    print("Файл не найден")

print(f'Количество строк в файле: {line_count}')'''
