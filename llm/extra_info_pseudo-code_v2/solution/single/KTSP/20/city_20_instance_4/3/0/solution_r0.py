import random
import math
from itertools import permutations

# Define cities' coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def total_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += euclidean_address(tour[i], tour[i+1])
    return total_cost

def generate_initial_solution(k):
    available_cities = list(cities.keys())
    tour = [0]
    while len(tour) < k:
        next_city = random.choice([c for c in available_cities if c not in tour])
        # Find the best position to insert the city
        best_pos = None
        best_cost = float('inf')
        for i in range(len(tour)):
            new_tour = tour[:i] + [next_city] + tour[i:]
            cost = total_tour_cost(new_tour + [0]) # create complete loop for cost calculation
            if cost < best_cost:
                best_cost = cost
                best_pos = i
        tour.insert(best_pos, next_city)
    tour.append(0) # return to the depot
    return tour

def local_search(tour):
    best_tour = tour[:]
    best_cost = total_tour_cost(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour)-2):
            for j in range(i+1, len(tour)-1):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = total_tour_cost(new_tour)
                if new_cost < best_cost:
                    best_tour = new_tour[:]
                    best_cost = new_cost
                    improved = True
    return best_tour

def shake(tour, k):
    n = len(tour) - 2  # exclude return to depot
    indices = random.sample(range(1, n), k)  # shake k elements but not the depot
    new_tour = tour[:]
    random.shuffle(indices)
    for index in indices:
        offset = random.randint(-3, 3)
        new_index = (index + offset) % n
        new_tour[index], new_tour[new_index + 1] = new_tour[new_index + 1], new_tour[index]
    return new_tour

def gvns(k, max_iter=100, num_shakes=5):
    current_solution = generate_initial_solution(k)
    best_solution = current_solution[:]
    best_cost = total_tour_cost(current_solution)
    
    for _ in range(max_iter):
        for i in range(1, num_shakes + 1):
            shaken_solution = shake(current_solution, i)
            local_optimum_solution = local_search(shaken_solution)
            local_optimum_cost = total_tour_cost(local_optimum_solution)
            
            if local_optimum_cost < best_cost:
                best_solution = local_optimum_solution[:]
                best_cost = local_optimum_cost
                break
        current_solution = best_solution[:]
    
    return best_solution, best_cost

# Main execution
k = 16  # number of cities to visit, including the depot city
best_tour, total_cost = gvns(k)
print("Tour:", best_tour)
print("Total travel cost:", total_cost)