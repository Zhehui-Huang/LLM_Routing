# Command and arguments as a list of strings
import os
import subprocess
import sys


def read_all_files(root_directory):
    # List to hold the contents of all text files
    text_files_loc = []

    # Walk through the directory and its subdirectories
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith('.py'):
                # Construct the full file path
                file_path = os.path.join(dirpath, filename)
                if '__init__.py' in file_path:
                    continue

                text_files_loc.append(file_path)

    text_files_loc.sort()
    return text_files_loc


def read_res_txt_files(root_directory):
    # List to hold the contents of all text files
    text_files_loc = []

    # Walk through the directory and its subdirectories
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith('.txt'):
                # Construct the full file path
                file_path = os.path.join(dirpath, filename)
                if '__init__.py' in file_path:
                    continue

                text_files_loc.append(file_path)

    text_files_loc.sort()
    return text_files_loc


def main():
    root_directory_list = ['verify/1-tsp', 'verify/4-tsp']
    # middle_under_evaluate_list = [
    #     '1_direct_reflect_v3', '2_math_reflect_v3', '5_external_tools_direct_v3',
    #     '5_external_tools_math_v3', '1_direct_reflect_ambiguities_v3_ambiguities',
    #     'gemini_1_direct_reflect_v3', 'gemini_2_math_reflect_v3', 'gemini_5_external_tools_direct_v3',
    #     'gemini_5_external_tools_math_v3'
    # ]
    middle_under_evaluate_list = [
        'z_v2_fix_bug_1_direct_reflect_v3',
        'z_v2_fix_bug_2_math_reflect_v3',
        'z_v2_fix_bug_5_external_tools_direct_v3',
        'z_v2_fix_bug_5_external_tools_math_v3', 'z_v2_fix_bug_1_direct_reflect_ambiguities_v3_ambiguities',
        'Y_v2_gemini_1_direct_reflect_fix_bug_v3', 'Y_v2_gemini_2_math_reflect_fix_bug_v3',
        'Y_v2_gemini_5_external_tools_direct_fix_bug_v3',
        'Y_v2_gemini_5_external_tools_math_fix_bug_v3',
        'Y_v2_gemini_ambiguities_1_direct_reflect_fix_bug_v3_ambiguities'
    ]

    for middle_under_evaluate in middle_under_evaluate_list:
        for root_directory in root_directory_list:
            print('middle_under_evaluate:  ', middle_under_evaluate)
            print('root_directory:  ', root_directory)
            if '1-tsp' in root_directory:
                text_files_loc = read_all_files(root_directory)

                for pid, py_file in enumerate(text_files_loc):
                    print('========================================================')
                    print(py_file)

                    command = ['python', py_file, '--root_dir', f'evaluate/{middle_under_evaluate}/{py_file[7:-3]}']

                    # Execute the command
                    subprocess.run(command)
                    print('========================================================')
            else:
                # 4-tsp, no need to change
                text_files_loc = read_all_files(root_directory)

                for pid, py_file in enumerate(text_files_loc):
                    # print('========================================================')
                    # print(py_file)

                    if 'D-OTSP' in py_file:
                        command = ['python', py_file, '--root_dir', f'evaluate/{middle_under_evaluate}/{py_file[7:-3]}',
                                   '--sequence_order', '[2,4,5,6,7]']
                    else:
                        command = ['python', py_file, '--root_dir', f'evaluate/{middle_under_evaluate}/{py_file[7:-3]}']
                    # Execute the command
                    subprocess.run(command)
                    # print('========================================================')


if __name__ == '__main__':
    sys.exit(main())
