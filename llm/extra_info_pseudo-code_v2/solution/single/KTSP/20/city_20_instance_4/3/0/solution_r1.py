import random
import math

# Coordinates for the cities
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def total_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def generate_initial_solution(k):
    available_cities = list(cities.keys())
    random.shuffle(available_cities)
    tour = [0] + available_cities[1:k-1] + [0]  # start and end at the depot
    return tour

def local_search(tour):
    best_cost = total_tour_cost(tour)
    best_tour = tour[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = total_tour_cost(new_tour)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_tour = new_tour[:]
                    improved = True
    return best_tour

def shake(tour, k):
    new_tour = tour[:]
    for _ in range(k):
        i, j = random.randint(1, len(tour)-3), random.randint(1, len(tour)-3)
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
    return new_tour

def gvns(k, max_iter=100):
    current_solution = generate_initial_solution(k)
    best_solution = current_solution[:]
    best_cost = total_tour_cost(best_solution)

    for _ in range(max_iter):
        p = 1
        while p <= 5:
            shaken_solution = shake(best_solution, p)
            local_optimum_solution = local_search(shaken_solution)
            local_optimum_cost = total_tour_cost(local_optimum_solution)

            if local_optimum_cost < best_cost:
                best_solution = local_optimum_solution[:]
                best_cost = local_optimum_cost
                p = 1  # Reset on improvement
            else:
                p += 1

    return best_solution, best_cost

# Execute the function with k = 16, including the depot
k = 16
best_tour, total_cost = gvns(k)
print("Tour:", best_tour)
print("Total travel cost:", total_cost)