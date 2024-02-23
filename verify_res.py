import re
import sys

from utils import read_all_files
import re
import sys

from utils import read_all_files
from verify_res_utils import standard_res_dict

final_check_res = {}
final_total_res = {}


def reformat_info(file_path, standard_res, q_id, r_num, points_num, standard_res_key):
    if standard_res_key in final_total_res:
        final_total_res[standard_res_key] += 1
    else:
        final_total_res[standard_res_key] = 1
        # final_check_res[standard_res_key] = 0

    with open(file_path, 'r') as file:
        lines = file.readlines()

    lines = [line for line in lines if line != '\n']
    lines = [line.replace('\n', '') for line in lines]

    time_pattern = re.compile(r'Total running time: ([\d.]+) seconds')

    tour_info = None
    cost_info = None
    time_info = None

    for i, line in enumerate(lines):
        if "Total running time" in line:
            time_match = time_pattern.search(line)
            time_info = time_match.group(1)

    extra_cost = None
    extra_cost_info = None
    for i, line in enumerate(lines):
        if "Final cost" in line:
            # The previous line is assumed to contain the tour information
            if q_id == 'B':
                tour_info = lines[i - 2].strip()
                extra_cost = lines[i - 1].strip()
                extra_cost_info = re.search(r'([\d.]+)', extra_cost).group(1)
            else:
                tour_info = lines[i - 1].strip()
                extra_cost = None
                extra_cost_info = None

            cost_line = line.strip()
            # Extracting numeric values from cost and timelines
            try:
                cost_info = re.search(r'([\d.]+)', cost_line).group(1)
            except:
                if 'print(f"Final cost: {min_cost}")' in cost_line or 'Final cost: inf' in cost_line:
                    break
            if cost_info is not None:
                cost_info = round(float(cost_info), 2)
            break

    if cost_info is None:
        return

    if float(standard_res[1]) == float(cost_info):
        if q_id == 'B':
            extra_cost_info = round(float(extra_cost_info), 2)
            if extra_cost_info == standard_res[2]:
                if standard_res_key in final_check_res:
                    final_check_res[standard_res_key] += 1
                else:
                    final_check_res[standard_res_key] = 1
        else:
            if standard_res_key in final_check_res:
                final_check_res[standard_res_key] += 1
            else:
                final_check_res[standard_res_key] = 1
    else:
        if standard_res_key not in final_check_res:
            final_check_res[standard_res_key] = 0

    return tour_info, cost_info, time_info


def main():
    text_files_loc = read_all_files(root_directory='/home/zhehui/LLM_Routing/evaluate/5_external_tools_no_consistent_check_v2_v3/1-tsp')
    print('file number:', len(text_files_loc), sep='\n')
    for file_path in text_files_loc:
        # results = read_file(file_path=file_path)
        # print('results:', results, sep='\n')
        parts = file_path.split('/')
        standard_res_key = f"{parts[7][0]}_{parts[6][0]}_{parts[8].split('_')[0]}"
        standard_res = standard_res_dict[standard_res_key]
        reformat_info(file_path=file_path, standard_res=standard_res, q_id=f"{parts[7][0]}",
                      r_num=f"{parts[6][0]}", points_num=f"{parts[8].split('_')[0]}", standard_res_key=standard_res_key)

    print('final_check_res: ', final_check_res, sep='\n')
    print('final_total_res: ', final_total_res, sep='\n')


if __name__ == '__main__':
    sys.exit(main())
