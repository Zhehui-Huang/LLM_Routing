import os
import math
import random
import itertools
import numpy as np
import gurobipy as gp
import matplotlib.pyplot as plt
from gurobipy import GRB

TASK_BASE_PATH = os.path.join(os.getcwd(), "../../llm/task/zero")
LLM_FOLDER_PATH = os.path.join(os.getcwd(), "../../llm")

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
                        tour = list(map(int, line.split(':')[1].strip()[1:-1].split(',')))
                    except:
                        tour = list(map(int, line.split(':')[1].strip()[1:-1].replace(
                            'np.int64(', '').replace(')','').split(',')))
                # elif line.startswith('Total travel cost:'):
                elif 'cost:' in line:
                    total_travel_cost = float(line.split(':')[1].strip())

    return tour, total_travel_cost


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
