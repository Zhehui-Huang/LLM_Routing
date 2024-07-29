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

def extract_route_and_cost(file_path, robot_num):
    with open(file_path, 'r') as file:
        text = file.read()

    routes = []
    # Find all the "Tour" lines and extract the numbers inside the brackets
    tours = re.findall(r"Tour: \[(.*?)\]", text)

    if tours is None:
        print("No tours found")
        return [], -1
    if len(tours) < robot_num:
        print(f"Not enough tours found\t{tours}")
        return [], -1
    if len(tours) > robot_num:
        print(f"Too many tours found\t{tours}")
        return [], -1

    try:
        for tour in tours:
            # Remove quotes and spaces, then split by comma
            tour_elements = tour.replace("'", "").replace(" ", "").split(',')
            # Convert to integers
            route = [int(stop) for stop in tour_elements]
            routes.append(route)

            if tour is None or len(tour) <= 1:
                print(f"At most one point\t{tour}")
                return [], -1
    except:
        print(f"Error in extracting tours\t{tours}")
        return [], -1

    return routes, -1


def extract_route_cost_max_cost(file_path, robot_num):
    with open(file_path, 'r') as file:
        text = file.read()

    routes = []
    # Find all the "Tour" lines and extract the numbers inside the brackets
    tours = re.findall(r"Tour: \[(.*?)\]", text)

    if tours is None:
        print("No tours found")
        return [], -1, -1
    if len(tours) < robot_num:
        print(f"Not enough tours found\t{tours}")
        return [], -1, -1
    if len(tours) > robot_num:
        print(f"Too many tours found\t{tours}")
        return [], -1, -1

    try:
        for tour in tours:
            # Remove quotes and spaces, then split by comma
            tour_elements = tour.replace("'", "").replace(" ", "").split(',')
            # Convert to integers
            route = [int(stop) for stop in tour_elements]
            routes.append(route)

            if tour is None or len(tour) <= 1:
                print(f"At most one point\t{tour}")
                return [], -1, -1
    except:
        print(f"Error in extracting tours\t{tours}")
        return [], -1, -1

    return routes, -1, -1


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
