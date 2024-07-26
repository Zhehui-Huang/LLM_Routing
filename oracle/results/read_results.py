import pickle
import sys
import os
import json


def format_data(data):
    formatted_data = "data = {\n"
    for key, value in data.items():
        formatted_data += f"    '{key}': [{value[0]}, {value[1]}],\n"
    formatted_data = formatted_data.rstrip(',\n') + '\n}'
    return formatted_data


def main():
    folder_list = ['single', 'multi']
    for folder_name in folder_list:
        files_list = os.listdir(folder_name)
        for file_name in files_list:
            read_path = f'{folder_name}/{file_name}'
            write_path = f'txt/{folder_name}/{file_name[:-4]}.txt'

            with open(read_path, 'rb') as f:
                result = pickle.load(f)

            result = format_data(data=result)
            os.makedirs(os.path.dirname(write_path), exist_ok=True)
            with open(write_path, 'w') as json_file:
                json_file.write(result)


if __name__ == "__main__":
    sys.exit(main())
