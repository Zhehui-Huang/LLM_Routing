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


def main():
    root_directory_list = ['verify/1-tsp', 'verify/4-tsp']
    for root_directory in root_directory_list:

        if '1-tsp' in root_directory:
            text_files_loc = read_all_files(root_directory)

            for pid, py_file in enumerate(text_files_loc):
                print('========================================================')
                print(py_file)

                if '05_points_' in py_file:
                    point_num = 5
                    sequence_order = '[1, 2, 4]'
                    # command = ['python', py_file, '--root_dir', f'evaluate/1_direct_reflect_v3/{py_file[7:-3]}'
                    #            '--point_num', 5]
                elif '10_points_' in py_file:
                    point_num = 10
                    sequence_order = '[2, 6, 8, 9]'
                    # command = ['python', py_file, '--root_dir', f'evaluate/1_direct_reflect_v3/{py_file[7:-3]}'
                    #            '--point_num', 10]
                else:
                    raise ValueError(f'Invalid file name  {py_file}')

                if 'D-OTSP' in py_file:
                    command = ['python', py_file, '--root_dir', f'evaluate/1_direct_reflect_v3/{py_file[7:-3]}',
                               '--point_num', point_num, '--sequence_order', sequence_order]
                else:
                    command = ['python', py_file, '--root_dir', f'evaluate/1_direct_reflect_v3/{py_file[7:-3]}',
                               '--point_num', point_num]

                # Execute the command
                subprocess.run(command)
                print('========================================================')
        else:
            # 4-tsp, no need to change
            text_files_loc = read_all_files(root_directory)

            for pid, py_file in enumerate(text_files_loc):
                print('========================================================')
                print(py_file)

                if 'D-OTSP' in py_file:
                    command = ['python', py_file, '--root_dir', f'evaluate/1_direct_reflect_v3/{py_file[7:-3]}',
                               '--sequence_order', '[2,4,5,6,7]']
                else:
                    command = ['python', py_file, '--root_dir', f'evaluate/1_direct_reflect_v3/{py_file[7:-3]}']
                # Execute the command
                subprocess.run(command)
                print('========================================================')


if __name__ == '__main__':
    sys.exit(main())
