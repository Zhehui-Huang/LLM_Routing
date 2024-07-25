import os
import sys

def get_import_lines(file_path):
    import_lines = []
    with open(file_path, 'r') as file:
        for line in file:
            if 'import' in line:
                import_lines.append(line.strip())

    return import_lines


def get_module_notfound_lines(file_path):
    import_lines = []
    with open(file_path, 'r') as file:
        for line in file:
            if 'ModuleNotFoundError' in line:
                import_lines.append(line.strip())

    return import_lines


def list_files_in_directory(directory):
    file_path_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path_list.append(os.path.join(root, file))

    return file_path_list


def extract_import():
    folder_path = '/Users/tencentintern/Documents/LLM_Routing/llm/extra_info/solution'
    all_import_lines_list = []
    file_path_list = list_files_in_directory(directory=folder_path)
    for file_path in file_path_list:
        import_lines = get_import_lines(file_path)
        unique_elements = set(all_import_lines_list).union(set(import_lines))
        all_import_lines_list = list(unique_elements)

    with open('z_unique_list.txt', 'w') as file:
        for item in all_import_lines_list:
            file.write(f"{item}\n")
    print(all_import_lines_list)


def extract_module_not_found():
    folder_path = '/Users/tencentintern/Documents/LLM_Routing/llm/extra_info/log'
    all_import_lines_list = []
    file_path_list = list_files_in_directory(directory=folder_path)
    for file_path in file_path_list:
        import_lines = get_import_lines(file_path)
        unique_elements = set(all_import_lines_list).union(set(import_lines))
        all_import_lines_list = list(unique_elements)

    with open('z_module_not_found.txt', 'w') as file:
        for item in all_import_lines_list:
            file.write(f"{item}\n")
    print(all_import_lines_list)


def main():
    extract_import()
    extract_module_not_found()


if __name__ == '__main__':
    sys.exit(main())
