from pathlib import Path
import os

'''
Задача 2:
Напишите функцию группового переименования файлов. Она должна:
1. принимать параметр желаемое конечное имя файлов. 
При переименовании в конце имени добавляется порядковый номер.
2. принимать параметр количество цифр в порядковом номере.
3. принимать параметр расширение исходного файла. 
Переименование должно работать только для этих файлов внутри каталога.
4. принимать параметр расширение конечного файла.
5. принимать диапазон сохраняемого оригинального имени. 
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
'''

def rename(end_name: str, count_sequence_number: int, start_extensions: str,
           end_expansions: str, slice_name: list[int, int], directory=Path().cwd()):
    start_number = 1
    start_slice, end_slice = slice_name
    for dirs, folders, files in os.walk(directory):
        for i, file in enumerate(files):
            if file.endswith(start_extensions):
                old_name = Path(dirs) / file
                old_name.rename(
                    f'{dirs}/{file[start_slice:end_slice]}{end_name}{str(start_number).zfill(count_sequence_number)}.{end_expansions}')
                start_number += 1


rename('new', 3, 'txt', 'doc', [0, 5], 'Test_folder_file')