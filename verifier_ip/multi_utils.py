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
    # tours = re.findall(r"Tour: \[(.*?)\]", text)
    # tours = re.findall(r"Tour\s?\d*\s?:\s?\[(\d+(?:,\s?\d+)*)\]", text)
    lines = text.splitlines()
    tours = []
    for line in lines:
        # Check if the line contains a tour in the standard format
        match = re.search(r"Tour\s?\d*\s?:\s?\[(\d+(?:,\s?\d+)*)\]", line)
        if match:
            tours.append(match.group(1))
            continue

        # Check if the line contains a tour with np.int64 format
        match = re.search(r"Tour\s?\d*\s?:\s?\[([^\]]*)\]", line)
        if match:
            numbers = re.findall(r"np\.int64\((\d+)\)", match.group(1))
            if numbers:
                tours.append(numbers)


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

    for rid, route in enumerate(routes):
        if len(route) >= 3:
            if route[0] == route[1]:
                print(f"Before process tour, {route}")
                route = route[1:]
                routes[rid] = route
                print(f"After tour same, {route}")
            if route[-1] == route[-2]:
                print(f"Before process tour, {route}")
                route = route[:-1]
                routes[rid] = route
                print(f"After tour same, {route}")

    return routes, -1


def extract_route_cost_max_cost(file_path, robot_num):
    with open(file_path, 'r') as file:
        text = file.read()

    routes = []
    # Find all the "Tour" lines and extract the numbers inside the brackets
    lines = text.splitlines()
    tours = []
    for line in lines:
        # Check if the line contains a tour in the standard format
        match = re.search(r"Tour\s?\d*\s?:\s?\[(\d+(?:,\s?\d+)*)\]", line)
        if match:
            tours.append(match.group(1))
            continue

        # Check if the line contains a tour with np.int64 format
        match = re.search(r"Tour\s?\d*\s?:\s?\[([^\]]*)\]", line)
        if match:
            numbers = re.findall(r"np\.int64\((\d+)\)", match.group(1))
            if numbers:
                tours.append(numbers)

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

    for rid, route in enumerate(routes):
        if len(route) >= 3:
            if route[0] == route[1]:
                print(f"Before process tour, {route}")
                route = route[1:]
                routes[rid] = route
                print(f"After tour same, {route}")
            if route[-1] == route[-2]:
                print(f"Before process tour, {route}")
                route = route[:-1]
                routes[rid] = route
                print(f"After tour same, {route}")

    return routes, -1, -1


def extract_route_with_depot(file_path, robot_num):
    with open(file_path, 'r') as file:
        text = file.read()

    # Extracting tours using regular expression
    tours = re.findall(r'Robot (\d) Tour: \[(.*?)\]', text)

    if not tours:
        print("No tours found")
        return {}, -1
    if len(tours) < robot_num:
        print(f"Not enough tours found: {len(tours)}\t{tours}")
        return {}, -1
    if len(tours) > robot_num:
        print(f"Too many tours found: {len(tours)}\t{tours}")
        return {}, -1

    # Creating the dictionary with tours
    tour_dict = {}

    for depot, tour in tours:
        depot = int(depot)
        # Remove quotes and spaces, then split by comma
        tour_elements = tour.replace("np.int64(", "").replace(")", "").replace("depot", "").replace("Depot", "").replace("City", "").replace("city", "").replace(" ", "").replace("np.str_(", "")
        tour_elements = tour_elements.replace(" ", "").replace("'", "").split(',')
        # Convert to integers
        try:
            route = [int(stop) for stop in tour_elements]
        except:
            print(f"Error in extracting tours\t{tour_elements}")
            return {}, -1
        if route[0] != depot:
            return {}, -1
        if route[-1] != depot:
            return {}, -1

        if len(route) >= 3:
            if route[0] == route[1]:
                print(f"Before process tour, {route}")
                route = route[1:]
                print(f"After tour same, {route}")
            if route[-1] == route[-2]:
                print(f"Before process tour, {route}")
                route = route[:-1]
                print(f"After tour same, {route}")

        if len(route) <= 2:
            return {}, -1

        tour_dict[depot] = [route]

    return tour_dict, -1

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
