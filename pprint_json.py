import json
import sys
import os.path


def load_data(filepath):
    if os.path.isfile(filepath):
        with open(filepath) as json_file:
            return json.load(json_file)
    else:
        return "The specified file does not exist"


def pretty_print_json(json_data):
    return json.dumps(json_data, indent=4, sort_keys=True, ensure_ascii=False)


if __name__ == '__main__':
    try:
        location_file = sys.argv[1]
        print(pretty_print_json(load_data(location_file)))
    except IndexError:
        print("Not specified json file")
