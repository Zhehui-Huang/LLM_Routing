import math
import random

# City coordinates given in the list above
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40),
    (54, 42), (36, 30), (52, 82), (93, 44),
    (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def compute_tour_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    # Add return to depot
    total_cost += euclidean_distance(cities[tour[-1]], cities[tour[0]])
    return total_cost

def generate_initial_solution():
    selected = [0]  # Start at the depot
    while len(selected) < 8:
        new_city = random.choice([i for i in range(1, 15) if i not in selected])
        selected.append(new_city)
    selected.append(0)  # End at the depot
    return selected

def shake(solution):
    # Modify by exchanging cities within the solution, except start and end
    new_solution = solution[1:-1]  # Exclude the depot at the start/end
    random.shuffle(new_solution)
    return [solution[0]] + new_solution + [solution[0]]

def local_search(solution):
    # Apply simple two-opt or exchange improvement
    best_cost = compute_tour_cost(solution)
    best_solution = solution[:]
    
    for i in range(1, len(solution) - 2):
        for j in range(i + 1, len(solution) - 1):
            # Swap two cities and see if it improves the solution
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = compute_tour_cost(new_solution)
            if new_cost < best_cost:
                best_cost = new_cost
                best_solution = new_solution[:]
    
    return best_solution

def gvns():
    itermax = 100
    pmax = 2
    best_solution = generate_initial_solution()
    best_cost = compute_tour_cost(best_solution)
    
    for iteration in range(itermax):
        current_solution = best_solution[:]
        for p in range(pmax):
            shaken_solution = shake(current_solution)
            improved_solution = local_search(shaken_solution)
            cost_improved_solution = compute_tour_cost(improved_solution)
            if cost_improved_solution < best_cost:
                best_solution = improved_solution[:]
                best_cost = cost_improved_solution
                break  # Escape the loop to restart with new best solution

    return best_solution, best_cost

# Run the GVNS algorithm and output the results
final_tour, total_cost = gvns()
print("Tour:", final_tour)
print("Total travel cost:", round(total_cost, 2))