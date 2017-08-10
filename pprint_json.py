import json
import sys
import os.path


# Функция загрузки Json из файла
def load_data(filepath):

    # Если указанный файл существует, то получаем данные из файла
    # Иначе прерываем работу скрипта
    if os.path.isfile(filepath):
        with open(filepath) as json_file:
            return json.load(json_file)
    else:
        return "Указанного файла  не существует"


# Функция для приведения Json в читаемый вид
def pretty_print_json(json_data):
    return json.dumps(json_data, indent=4, sort_keys=True, ensure_ascii=False)


if __name__ == '__main__':
    # Получаем имя json файла из командной строки
    location_file = sys.argv[1]
    # Приводим json в читаемый вид
    print(pretty_print_json(load_data(location_file)))
