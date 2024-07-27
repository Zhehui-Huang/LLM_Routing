import random
import math

# Defining all city coordinates including the depot
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36),  3: (15, 0),  4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2),   8: (47, 50), 9: (60, 29),
   10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
   15: (19, 25), 16: (75, 9),  17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to total the travel cost of a route
def total_travel_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i+1])
    return total_cost

# Function to generate a random initial solution that includes exactly k cities
def generate_initial_solution(k=16):
    chosen_cities = random.sample(list(cities.keys()), k)
    if 0 not in chosen_cities:
        chosen_cities.pop()
        chosen_cities.insert(0, 0)
    chosen_cities.append(0)  # making it a complete tour by returning to the depot
    return chosen_cities

# Local search operation to swap two cities in the tour for better solutions
def local_search(current_tour):
    best_tour = current_tour[:]
    best_cost = total_travel_cost(best_tour)
    made_improvement = True

    while made_improvement:
        made_improvement = False
        for i in range(1, len(best_tour) - 2):
            for j in range(i + 1, len(best_tour) - 1):
                new_tour = best_tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = total_travel_cost(new_tour)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_tour = new_tour[:]
                    made_improvement = True

    return best_tour

# Main Variable Neighborhood Descent function to solve the problem
def variable_neighborhood_search():
    k = 16
    itermax = 100
    best_solution = generate_initial_solution(k)
    best_cost = total_travel_cost(best_solution)

    for _ in range(itermax):
        current_solution = local_search(best_solution)
        current_cost = total_travel_cost(current_flight plan_solution)
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost

    return best_solution, best_cost

# Running the optimized search
final_solution, final_cost = variable_neighborhood_search()
print("Tour:", final_solution)
print("Total travel cost:", final_cost)