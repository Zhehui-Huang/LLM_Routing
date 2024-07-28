import os
import math
import random
import itertools
import re
import numpy as np
import gurobipy as gp
import matplotlib.pyplot as plt
from gurobipy import GRB
import ast

TASK_BASE_PATH = os.path.join(os.getcwd(), "../../llm/task")
LLM_FOLDER_PATH = os.path.join(os.getcwd(), "../../llm")
# GPT_EXTRA_INFO_FOLDER_PATH = os.path.join(os.getcwd(), "../../llm/llama3_1_extra_info")

EVAL_TYPE_LIST = ['pass_one', 'pass_debug', 'pass_overall']
EXTRA_INFO_DICT = {
    'zero': 'extra_info',
    'math': 'extra_info_math',
    'pseudo-code_v2': 'extra_info_pseudo-code_v2',
    'pseudo-code_v3': 'extra_info_pseudo-code_v3',
    'pdf_paper_v2': 'extra_info_pdf_paper_v2',
    'pdf_paper_v3': 'extra_info_pdf_paper_v3'
}

DEBUG_FLAG = False

def extract_route_and_cost(file_path):
    tour = []
    total_travel_cost = None
    output_found = False

    with open(file_path, 'r') as file:
        for line in file:
            if 'OUTPUT' in line:
                output_found = True
            if output_found:
                if line.startswith('Tour:'):
                    try:
                        tmp_tour_list = line.split(':')[1].strip()[1:-1].split(',')
                        if isinstance(tmp_tour_list[0], str):
                            tour = list(map(int, line.split(':')[1].strip()[1:-1].replace("'", "").split(',')))
                        else:
                            tour = list(map(int, line.split(':')[1].strip()[1:-1].split(',')))
                    except:
                        tour = list(map(int, line.split(':')[1].strip()[1:-1].replace(
                            'np.int64(', '').replace(')','').split(',')))
                # elif line.startswith('Total travel cost:'):
                elif 'cost:' in line:
                    total_travel_cost = float(line.split(':')[1].strip())

    if tour is None:
        return [], -1


    if len(tour) >= 3:
        if tour[0] == tour[1]:
            print(f"Before process tour, {tour}")
            tour = tour[1:]
            print(f"After tour same, {tour}")
        if tour[-1] == tour[-2]:
            print(f"Before process tour, {tour}")
            tour = tour[:-1]
            print(f"After tour same, {tour}")

    return tour, total_travel_cost


def extract_route_cost_max_cost(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Extract text between OUTPUT and ERROR
    extracted_text = re.search(r'OUTPUT:(.*?)ERROR:', content, re.DOTALL).group(1).strip()
    if extracted_text == '':
        return [], -1, -1
    # Split the extracted text into rows
    rows = extracted_text.splitlines()

    # Extract the tour, travel cost, and maximum distance
    tour = re.search(r'Tour:\s*(.*)', rows[0])
    if tour:
        tour = tour.group(1)
    else:
        tour = []
        return [], -1, -1

    travel_cost = re.search(r'Total travel cost:\s*(.*)', rows[1])
    if travel_cost:
        travel_cost = travel_cost.group(1)
    else:
        travel_cost = -1

    max_distance = next((line.split(":")[1].strip() for line in rows if
                         all(keyword in line for keyword in ["Maximum", "distance", "consecutive"])), -1)


    tour = ast.literal_eval(tour)
    if isinstance(tour, list):
        if (len(tour) > 0 and tour[0] == 'depot') or (len(tour) > 0 and tour[-1] == 'depot'):
            raise ValueError("Tour starts with depot")

        tour = [int(city) for city in tour]

    if tour is None:
        return [], -1, -1

    if len(tour) >= 3:
        if tour[0] == tour[1]:
            print(f"Before process tour, {tour}")
            tour = tour[1:]
            print(f"After tour same, {tour}")
        if tour[-1] == tour[-2]:
            print(f"Before process tour, {tour}")
            tour = tour[:-1]
            print(f"After tour same, {tour}")
    return tour, float(travel_cost), float(max_distance)


def calculate_distance_matrix(cities):
    n = len(cities)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)
    return dist_matrix


def visualize_tour(cities, tour):
    plt.figure(figsize=(10, 10))
    for (i, j) in tour:
        plt.plot([cities[i][0], cities[j][0]], [cities[i][1], cities[j][1]], 'b-o')

    for idx, (x, y) in enumerate(cities):
        plt.text(x, y, f'  {idx}', fontsize=12)

    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('TSP Optimal Tour')
    plt.grid()
    plt.show()


def read_city_locations(file_path):
    city_locations = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if "City" in line or "Depot" in line:
                # Extract coordinates from the line
                parts = line.split(':')
                coordinates = parts[1].strip().strip('()').split(', ')
                x = int(coordinates[0])
                y = int(coordinates[1])
                city_locations.append((x, y))
    return city_locations


def route2edges(route, num_city):
    # route = [0, 1, 2, 3， 0]
    x = np.zeros((num_city, num_city))
    for i in range(len(route)-1):
        x[route[i], route[i+1]] = 1
    return x
