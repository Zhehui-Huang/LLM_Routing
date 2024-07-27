import math
import random

# coordinates of the cities including the depot
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Calculate Euclidean distance between two points
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Evaluate the total cost of the tour
def evaluate_tour(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Generate an initial feasible solution of k cities including the depot
def generate_initial_solution(k):
    tour = [0]
    available_cities = list(set(cities.keys()) - set(tour))
    while len(tour) < k:
        new_city = random.choice(available_cities)
        best_position = min(range(1, len(tour)), key=lambda i: euclidean_distance(tour[i-1], new_city) + euclidean_distance(new_city, tour[i]))
        tour.insert(best_position, new_city)
        available_cities.remove(new_city)
    tour.append(0) # back to the depot
    return tour

# Shake operation: Randomly modify the tour within a neighborhood structure
def shake(tour, p):
    shaken_tour = tour[1:-1]
    random.shuffle(shaken_tour)
    return [0] + shaken_tour[:p] + shaken_tour[p:] + [0]

# Local search operation to find a better solution in the neighborhood
def local_search(tour, k):
    best_tour = tour[:]
    best_cost = evaluate_tour(tour)
    for i in range(1, k):
        for j in range(i + 1, k):
            new_tour = tour[:]
            # Swap two cities
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            current_cost = evaluate_tour(new_tour)
            if current_cost < best_cost:
                best_cost = current_cost
                best_tour = new_tour[:]
    best_tour.append(0) # make sure to end the tour at the depot
    return best_tour

# Main GVNS algorithm function
def gvns(k, max_iter, max_no_improvement):
    best_tour = generate_initial_solution(k)
    best_cost = evaluate_tour(best_tour)
    iter = 0
    no_improvement = 0

    while iter < max_iter and no_improvement < max_no_improvement:
        p = 1
        while p <= k - 1:
            new_tour = shake(best_tour, p)
            new_tour = local_search(new_tour, k)
            new_cost = evaluate_tour(new_tour)
            if new_cost < best_cost:
                best_tour, best_cost = new_tour[:], new_cost
                no_improvement = 0
                p = 1
            else:
                p += 1
        no_improvement += 1
        iter += 1

    return best_tour, best_cost

# Number of cities to visit (including depot)
k = 5
# Set parameters for GVNS
max_iter = 2000
max_no_improvement = 10

# Find the best tour and cost
tour, total_cost = gvns(k, max_iter, max_no_improvement)
print("Tour:", tour)
print("Total travel cost:", total_cost)