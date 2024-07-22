import os
import re
import sys
import subprocess

from utils import read_txt_file

FILE_NAME_SMALL = [
    'P-n19-k2',
    'P-n20-k2',
    'E-n22-k4',
    'E-n30-k3',
    'A-n32-k5',
    'P-n16-k8',
    'P-n22-k8',
    'P-n23-k8',
    'A-n33-k6',
    'A-n34-k5'
]
FILE_NAME_BIG = [
    'A-n38-k5',
    'P-n40-k5',
    'A-n44-k6',
    'F-n45-k4',
    'P-n45-k5',
    'A-n45-k7',
    'P-n50-k7',
    'P-n50-k8',
    'E-n51-k5',
    'P-n51-k10'
]


def download_files(file_names, size):
    link_prex = 'http://vrp.galgos.inf.puc-rio.br/media/com_vrp/instances//'
    for file_name in file_names:
        problem_link = f'{link_prex}{file_name[0]}/{file_name}.vrp'

        # Change target dir
        target_dir = f"/Users/tencentintern/Documents/LLM_Routing/llm/city_list/multiple/original/{size}"
        os.makedirs(target_dir, exist_ok=True)
        os.chdir(target_dir)

        command = ["curl", "-O", problem_link]
        result = subprocess.run(command, check=True)

        # Check if the command was successful
        if result.returncode == 0:
            print(f"{file_name}.vrp downloaded successfully.")
        else:
            print("Error downloading file.")


def download_original_files():
    download_files(file_names=FILE_NAME_SMALL, size='small')
    download_files(file_names=FILE_NAME_BIG, size='big')


def extract_node_info(data, file_name):
    lines = data.splitlines()
    node_section_started = False
    nodes = []

    for line in lines:
        if "NODE_COORD_SECTION" in line:
            node_section_started = True
            continue

        if node_section_started:
            if line.strip() == "DEMAND_SECTION":
                break

            parts = line.split()
            node_id = int(parts[0])
            if file_name[:-4] == 'F-n45-k4':
                x = float(parts[1])
                y = float(parts[2])
            else:
                x = int(parts[1])
                y = int(parts[2])
            nodes.append((node_id, x, y))

    formatted_nodes = [f"Depot city 0: ({nodes[0][1]}, {nodes[0][2]})"]
    for node in nodes[1:]:
        formatted_nodes.append(f"City {node[0] - 1}: ({node[1]}, {node[2]})")

    result = f"There are {len(nodes)} cities.\nCities and Coordinates:\n" + "\n".join(formatted_nodes)
    return result


def extract_demand_info(data):
    # Extract the DEMAND_SECTION from the data
    demand_section = {}
    lines = data.split('\n')
    start_collecting = False
    for line in lines:
        if line.strip() == "DEMAND_SECTION":
            start_collecting = True
            continue
        if start_collecting:
            if line.strip() == "DEPOT_SECTION":
                break
            parts = line.strip().split()
            if len(parts) == 2:
                node, demand = int(parts[0]) - 1, int(parts[1])
                demand_section[node] = demand

    # Create the formatted string
    formatted_demand_list = "\n\nDemand list:\n"
    for node, demand in demand_section.items():
        formatted_demand_list += f"City {node}: {demand}\n"

    return formatted_demand_list


def extract_capacity_info(data):
    capacity_value = None
    lines = data.split('\n')
    for line in lines:
        if line.strip().startswith("CAPACITY"):
            capacity_value = int(line.split(':')[1].strip())
            break

    return capacity_value


def batch_extract_node_info():
    target_dir = "/Users/tencentintern/Documents/LLM_Routing/llm/city_list/multiple/original"
    write_dir = "/Users/tencentintern/Documents/LLM_Routing/llm/city_list/multiple/processed"
    include_demand_dir = "/Users/tencentintern/Documents/LLM_Routing/llm/city_list/multiple/demand"
    capacity_dir = "/Users/tencentintern/Documents/LLM_Routing/llm/city_list/multiple/capacity"
    for size in ['small', 'big']:
        for file_name in os.listdir(f"{target_dir}/{size}"):
            print(f"Processing {size} {file_name}...")
            with open(f"{target_dir}/{size}/{file_name}", 'r') as f:
                data = f.read()
                result = extract_node_info(data=data, file_name=file_name)
                os.makedirs(f'{write_dir}/{size}', exist_ok=True)
                with open(f"{write_dir}/{size}/{file_name[:-4]}.txt", 'w') as out:
                    out.write(result)

                # Include demand info
                demand_str = extract_demand_info(data=data)
                os.makedirs(f'{include_demand_dir}/{size}', exist_ok=True)
                with open(f"{include_demand_dir}/{size}/{file_name[:-4]}.txt", 'w') as out:
                    out.write(result + demand_str)

                # Extract capacity info
                capacity_value = extract_capacity_info(data=data)
                os.makedirs(f'{capacity_dir}/{size}', exist_ok=True)
                with open(f"{capacity_dir}/{size}/{file_name[:-4]}.txt", 'w') as out:
                    out.write(str(capacity_value))


def extract_robot_num(filename):
    match = re.search(r'k(.*?)\.txt', filename)
    if match:
        return int(match.group(1))
    else:
        raise ValueError(f"Invalid filename: {filename}")


def get_multi_robot_info_str(task_name, robot_num, file_name, note):
    # Robot info prex
    if task_name == 'mTSPMD':
        robot_start_end_str = ''
        for i in range(robot_num):
            robot_start_end_str += f'Robot {i} starts and ends at depot city {i}.\n'

        robot_info = f"""
###
Robot Information
===
- Number of robots: {robot_num}
- Starting and Ending Locations:
{robot_start_end_str.strip()}
- Travel Capability: Robots can travel between any two cities.
- Travel Cost: Calculated as the Euclidean distance between two cities.
###
"""
    elif task_name == 'CVRP':
        capacity_value_str = read_txt_file(f'../city_list/multiple/capacity/{note}/{file_name}.txt')
        robot_info = f"""
###
Robot Information
===
- Number of robots: {robot_num}
- The capacity of each robot: {capacity_value_str}
- Starting location: All robots start at depot city 0.
- Travel capability: Robots can travel between any two cities.
- Travel cost: Calculated as the Euclidean distance between two cities.
###
"""
    else:
        robot_info = f"""
###
Robot Information
===
- Number of robots: {robot_num}
- Starting location: All robots start at depot city 0.
- Travel capability: Robots can travel between any two cities.
- Travel cost: Calculated as the Euclidean distance between two cities.
###
"""

    return robot_info


def modify_mTSPMD_info(content, robot_num):
    # Split content into lines
    lines = content.split('\n')

    # Modify the first 5 cities to be Depot cities
    for i in range(2, 2 + robot_num):
        lines[i] = lines[i].replace('City', 'Depot city')

    modified_content = '\n'.join(lines)
    return modified_content


def main():
    batch_extract_node_info()
    # download_original_files()


if __name__ == '__main__':
    sys.exit(main())
