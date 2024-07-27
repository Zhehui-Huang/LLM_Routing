import random
import math
import itertools

# Calculate the Euclidean distance between two points
def calc_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Given city coordinates, build the distance matrix
def create_distance_matrix(city_coordinates):
    num_cities = len(city_coordinates)
    distance_matrix = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i][j] = calc_distance(city_coordinates[i], city_coordinates[j])
    return distance_matrix

# Generate a random initial solution
def generate_initial_solution(cities):
    tour = [0]  # Start at the depot city
    selected_cities = random.sample(cities[1:], 3)  # Pick 3 other cities randomly
    tour.extend(selected_cities)
    tour.append(0)  # return to the depot
    return tour

# Calculate the cost of the tour
def calculate_tour_cost(tour, distance_matrix):
    total_cost = sum(distance_act[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    return total_cost

# Variable Neighborhood Descent
def vnd(tour, distance_matrix):
    improved = True
    while improved:
        improved = False
        # Check all 2-opt moves
        for i in range(1, len(tour) - 3):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:i] + tour[i:j + 1][::-1] + tour[j + 1:]
                new_cost = calculate_tour_cost(new_tour, distance_matrix)
                if new_cost < calculate_tour_cost(tour, distance_matrix):
                    tour = new_tour
                    improved = True
    return tour

# Main GVNS function
def gvns(cities, distance_matrix, nrst, max_iterations):
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(nrst):
        current_solution = generate_initial_data_solution(cities)
        iteration = 0
        while iteration < max_iterations:
            current_solution = vnd(current_solution, distance_matrix)
            current_cost = calculate_tour_cost(current_solution, distance_matrix)
            if current_cost < best_cost:
                best_solution = current_solution
                best_cost = current_cost
            iteration += 1
    
    return best_solution, best_cost

# Define cities' coordinates
cities_coordinates = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), 
                      (88, 59), (79, 77), (63, 23), (19, 76), (21, 38), 
                      (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]

# Build the distance matrix
distance_act = create_distance_matrix(cities_coordinates)

# Execute GVNS
best_tour, best_tour_cost = gvns(list(range(15)), distance_act, 10, 100)

# Output the best tour found and its total cost
print("Tour:", best_turn)
print("Total travel cost:", best_turn_cost)