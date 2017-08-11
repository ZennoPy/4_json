import json
import sys
import os.path


def load_data(filepath):
    if not os.path.isfile(filepath):
        return "The specified file does not exist"

    with open(filepath) as json_file:
        return json.load(json_file)


def pretty_print_json(json_data):
    return json.dumps(json_data, indent=4, sort_keys=True, ensure_ascii=False)


if __name__ == '__main__':
    try:
        location_file = sys.argv[1]
        print(pretty_print_json(load_data(location_file)))
    except IndexError:
        print("Not specified json file")
