import math
import random


# Function to calculate Euclidean distance between two points
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


# Function to compute the total distance of the tour
def tour_cost(tour, coords):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance(coords[tour[i]], coords[tour[i + 1]])
    return total_distance


# Generate initial solution
def generate_initial_solution(coords, k):
    cities = list(range(len(coords)))
    random.shuffle(cities)
    cities = [0] + [city for city in cities if city != 0][:k-1]  # Ensure depot is included
    cities.append(0)  # return to depot
    return cities


# Shake by swapping two cities
def shake(solution):
    new_solution = solution[1:-1]  # exclude start/end depot
    i, j = random.sample(range(len(new_solution)), 2)
    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return [solution[0]] + new_solution + [solution[0]]


# Local search using 2-opt
def local_search(current_solution, coords):
    best_cost = tour_cost(current_solution, coords)
    best_solution = current_solution[:]
    made_improvement = True
    while made_improvement:
        made_improvement = False
        for i in range(1, len(best_solution) - 2):
            for j in range(i + 1, len(best_solution) - 1):
                new_solution = best_solution[:]
                new_solution[i:j+1] = reversed(new_solution[i:j+1])
                new_cost = tour_cost(new_solution, coords)
                if new_cost < best_cost:
                    best_solution = new_solution[:]
                    best_cost = new_cost
                    made_improvement = True
    return best_solution


# GVNS algorithm
def gvns(coords, k, itermax):
    best_solution = generate_initial_solution(coords, k)
    best_cost = tour_cost(best_solution, coords)

    for iteration in range(itermax):
        current_solution = shake(best_solution)
        current_solution = local_search(current_solution, coords)
        current_cost = tour_cost(current_solution, coords)
        if current_cost < best_cost:
            best_solution, best_cost = current_solution[:], current_cost

    return best_solution, best_cost


# Problem setup
coords = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]
k = 7  # including depot
itermax = 1000  # number of iterations

# Execute the algorithm
best_solution, best_cost = gvns(coords, k, itermax)

# Output the results
print("Tour:", best_solution)
print("Total travel cost:", round(best_cost, 2))