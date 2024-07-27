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
    while len(tour) < 10:
        chosen_city = random.choice(remaining_cities)
        tour.append(chosen_city)
        remaining_cities.remove(chosen_city)
    tour.append(0)  # end at the depot city
    return tour

# Calculate the total distance of a tour
def tour_distance(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Perform shaking by exchanging two cities
def shake(tour):
    new_tour = tour[1:-1]
    idx1, idx2 = random.sample(range(len(new_tour)), 2)
    new_tour[idx1], new_tour[idx2] = new_tour[idx2], new_tour[idx1]
    return [0] + new_tour + [0]

# Variable Neighborhood Descent
def vnd(tour):
    best_tour = tour[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: continue  # skip adjacent cities
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                if tour_distance(new_tour) < tour_distance(best_tour):
                    best_tour = new_tour[:]
                    improved = True
    return best_tour

# GVNS Algorithm
def gvns(Nrst):
    best_solution = generate_initial_solution()
    best_cost = tour_status(best_solution)

    for _ in range(Nrst):
        current_solution = generate_initial_solution()
        while True:
            new_solution = shake(current_solution)
            new_solution = vnd(new_solution)
            current_cost = tour_distance(new_solution)
            if current_cost < best_cost:
                best_solution = new_solution[:]
                best_cost = current_cost
                break

    return best_solution, best_cost

# Parameters
Nrst = 100  # Number of restarts

# Execute GVNS
best_solution, best_cost = gvns(Nrst)

# Output the result
print(f"Tour: {best_solution}")
print(f"Total travel cost: {round(best_cost, 2)}")