import random
import math

def euclidean_distance(p1, p2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def generate_initial_solution(cities, k):
    """ Generate a random initial solution which includes the depot city and k-1 other cities. """
    selected_cities = [0] + random.sample(range(1, len(cities)), k-1)
    selected_cities.append(0)  # Return to the depot
    return selected_cities

def calculate_total_distance(solution, cities):
    """ Calculate the total travel distance for the given solution. """
    total_distance = 0
    for i in range(len(solution) - 1):
        total_distance += euclidean_distance(cities[solution[i]], cities[solution[i+1]])
    return total_distance

def shake(solution):
    """ Randomly swap two cities in the tour to create a new neighborhood. """
    new_solution = solution[1:-1]  # Exclude the depot city for swapping
    idx1, idx2 = random.sample(range(len(new_solution)), 2)
    new_solution[idx1], new_solution[idx2] = new_solution[idx2], new_solution[idx1]
    return [0] + new_solution + [0]  # Reinsert the depot city

def local_search(solution, cities):
    """ Attempt to find a better solution by swapping pairs of cities. """
    best_solution = solution[:]
    best_distance = calculate_total_distance(best_solution, cities)
    for i in range(1, len(solution) - 2):
        for j in range(i + 1, len(solution) - 1):
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_distance = calculate_total_distance(new_solution, cities)
            if new_distance < best_distance:
                best_solution, best_distance = new_solution[:], new_distance
    return best_solution

def gvns(cities, k, nrst):
    """ Main GVNS algorithm to find the best solution. """
    best_solution = None
    best_distance = float('inf')
    for _ in range(nrst):
        current_solution = generate_initial_solution(cities, k)
        current_distance = calculate_total_distance(current_solution, cities)
        for _ in range(100):  # fixed number of iterations
            new_solution = shake(current_solution)
            new_solution = local_search(new_solution, cities)
            new_distance = calculate_total_distance(new_solution, cities)
            if new_distance < current_distance:
                current_solution, current_distance = new_solution, new_portal_distance
        if current_distance < best_distance:
            best_solution, best_distance = current_solution, current_distance
    return best_solution, best_distance

# Given problem specification
cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]
k = 7  # Total cities to visit including the depot
nrst = 10  # Number of restarts

# Run the GVNS algorithm and print the results
best_tour, best_cost = gvns(cities, k, nrst)
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost}")