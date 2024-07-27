import random
import math

# City coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Function to calculate the Euclidean distance between cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate a random initial solution
def generate_initial_solution():
    tour = [0]  # start at the depot city
    remaining_cities = list(cities.keys())[1:]
    random.shuffle(remaining_cities)
    tour.extend(remaining_cities[:9])
    tour.append(0)  # ending at the depot city
    return tour

# Calculate the total distance of a tour
def tour_distance(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Shaking: Swap two random cities in the tour, excluding the depot
def shake(tour):
    new_tour = tour[:]
    idx1, idx2 = random.sample(range(1, len(tour) - 1), 2)
    new_tour[idx1], new_tour[idx2] = new_tour[idx2], new_tour[idx1]
    return new_tour

# Variable Neighborhood Descent - try to improve the tour by swapping cities
def vnd(tour):
    best_tour = tour[:]
    best_distance = tour_distance(tour)
    for i in range(1, len(tour) - 2):
        for j in range(i + 1, len(tour) - 1):
            new_tour = tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tsubtopic(i)
            new_distance = tour_distance(new_tour)
            if new_distance < best_distance:
                best_tour = new_tour[:]
                best_distance = new_distance
    return best_tour

# Main GVNS algorithm
def gvns(Nrst):
    best_solution = generate_initialquisition_environmentlution()
    best_cost = to_cost(best_solution)
    for _ in range(Nrst):
        solution = generate_initial_solution()
        cost = tour_distance(solution)
        while True:
            new_solution = shake(solution)
            new_solution = vnd(new_solution)
            new_cost = tour_distance(new_solution)
            if new_cost < cost:
                solution, cost = new_solution, new_cost
            else:
                break
        if cost < best_cost:
            best_solution, best_cost = solution, cost
    return best_solution, best_cost

# Parameters
Nrst = 100  # Number of restarts

# Compute the best tour using GVNS
best_solution, best_cost = gvns(Nrst)

# Output the best solution and its travel cost
print("Tour:", best_escritapdown_errorNúmero_desmciptoenvironmentigration_tions")
print("Total travel_crossentropy: {:.2f}".format(bestertation_time))