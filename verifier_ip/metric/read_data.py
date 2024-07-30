import os
import sys


def read_success_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read()

    # Split content based on 'Details:' keyword to isolate the relevant section
    data_section = content.split('Details:')[0].strip()

    # Parsing the data to create the dictionary
    success_dict = {}
    for line in data_section.split('\n'):
        if 'City:' in line and 'Average success:' in line:
            # Extract city number and average success rate
            city = int(line.split('City:')[1].split('\t')[0].strip())
            average_success = float(line.split('Average success:')[1].split('\t')[0].strip())
            success_dict[city] = average_success

    formatted_content = '\n'.join([f"{key}: {value}," for key, value in success_dict.items()])
    # print(formatted_content)
    return formatted_content

def read_opt_gap_file(file_name):
    with open(file_name, 'r') as file:
        content = file.readlines()

    # Parsing the data to create the dictionary
    opt_gap_dict = {}
    for line in content:
        if 'Details:' in line:
            break  # Stop processing at the 'Details:' section
        if 'City:' in line and 'Average opt gap:' in line:
            # Extract city number and average opt gap
            city = int(line.split('City:')[1].split()[0])
            average_opt_gap = float(line.split('Average opt gap:')[1].split()[0])
            opt_gap_dict[city] = average_opt_gap


    formatted_content = '\n'.join([f"{key}: {value}," for key, value in opt_gap_dict.items()])
    # print(formatted_content)
    return formatted_content


def read_data():
    llm_model_list = ['gpt4', 'llama3_1']
    context_list = ['zero', 'math', 'pseudo-code_v2', 'pseudo-code_v3', 'pdf_paper_v2', 'pdf_paper_v3']
    exec_type_list = ['pass_one', 'pass_debug', 'pass_overall']
    robot_type_list = ['single', 'multiple']
    single_task = ['TSP', 'BTSP', 'GTSP', 'KTSP']
    multiple_task = ['mTSP', 'mTSP_MinMax', 'mTSPMD', 'CVRP']
    for llm_model in llm_model_list:
        for context in context_list:
            for exec_type in exec_type_list:
                success_write_file_path = f'clean_data/{llm_model}/{context}/{exec_type}/all_success.txt'
                opt_gap_write_file_path = f'clean_data/{llm_model}/{context}/{exec_type}/all_opt_gap.txt'

                os.makedirs(os.path.dirname(success_write_file_path), exist_ok=True)
                os.makedirs(os.path.dirname(opt_gap_write_file_path), exist_ok=True)

                with open(success_write_file_path, 'w') as f:
                    f.write(f'Overall Success: {llm_model}/{context}/{exec_type}\n###\n\n')

                with open(opt_gap_write_file_path, 'w') as f:
                    f.write(f'Overall Opt Gap: {llm_model}/{context}/{exec_type}\n###\n\n')

                for robot_type in robot_type_list:
                    if robot_type == 'single':
                        for task in single_task:
                            file_name = f'{llm_model}/{context}/{exec_type}/{robot_type}/{task}'
                            success_data = read_success_file(file_name=f'{file_name}/success.txt')
                            opt_gap_data = read_opt_gap_file(file_name=f'{file_name}/opt_gap.txt')
                            print(f'{file_name}/opt_gap.txt')

                            with open(success_write_file_path, 'a') as f:
                                f.write(f'{file_name}:\n')
                                f.write(success_data)
                                f.write('\n\n')
                            with open(opt_gap_write_file_path, 'a') as f:
                                f.write(f'{file_name}:\n')
                                f.write(opt_gap_data)
                                f.write('\n\n')

                    elif robot_type == 'multiple':
                        if llm_model == 'llama3_1' and context == 'zero':
                            continue
                        for task in multiple_task:
                            file_name = f'{llm_model}/{context}/{exec_type}/{robot_type}/{task}'
                            success_data = read_success_file(file_name=f'{file_name}/success.txt')
                            opt_gap_data = read_opt_gap_file(file_name=f'{file_name}/opt_gap.txt')
                            print(f'{file_name}/opt_gap.txt')

                            with open(success_write_file_path, 'a') as f:
                                f.write(f'{file_name}:\n')
                                f.write(success_data)
                                f.write('\n\n')
                            with open(opt_gap_write_file_path, 'a') as f:
                                f.write(f'{file_name}:\n')
                                f.write(opt_gap_data)
                                f.write('\n\n')
                    else:
                        raise ValueError(f'Invalid robot type: {robot_type}')



def main():
    read_data()


if __name__ == "__main__":
    sys.exit(main())
