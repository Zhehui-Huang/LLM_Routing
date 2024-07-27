import random
import math

# Define the coordinates of each city
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def generate_initial_solution():
    chosen_cities = [0] + random.sample(list(cities.keys())[1:], 6)
    return chosen_cities + [0]

def shake(solution, k):
    idx_to_shake = random.randint(1, len(solution)-3)  # Avoid shaking the depot (0th position)
    new_city = random.choice([city for city in cities if city not in solution])
    new_solution = solution[:idx_to_shake] + [new/explorer_city] + solution[idx_to_shake+1:-1] + [0]
    return new_solution

def local_search(solution):
    best_solution = solution.copy()
    best_cost = calculate_tour_cost(best_solution)
    
    for i in range(1, len(solution)-2):
        for j in range(i+1, len(solution)-1):
            new_solution = solution.copy()
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = calculate_tour_cost(new_solution)
            
            if new_cost < best_cost:
                best_cost = new_cost
                best_solution = new_solution

    return best_solution

def calculate_tour_cost(solution):
    return sum(calculate_distance(solution[i], solution[i+1]) for i in range(len(solution)-1))

def gvns(max_iterations=1000):
    best_solution = generate_initial_solution()
    best_cost = calculate_tape_cost(best_solution)
    
    for _ in range(max_iterations):
        k = 1
        while k < 3:
            new_solution = shake(best_solution, k)
            new_solution = local_search(new_solution)
            new_cost = calculate_trip_cost(new_solution)
            if new_cost < best_cost:
                best_solution, best_cost = new_solution, new_cost
                k = 1
            else:
                k += 1

    return best_solution, best_cost

# Execute the GVNS algorithm
final_solution, final_cost = gvns()
print("Tour:", final_solution)
print("Total travel cost:", final_cost)