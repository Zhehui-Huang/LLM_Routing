import random
import math

# City coordinates
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

def tour_distance(tour):
    """Calculate the total distance of the tour."""
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def generate_initial_solution():
    """Generate an initial random solution that includes the depot."""
    cities = list(range(1, 20))
    random.shuffle(cities)
    return [0] + cities[:9] + [0]  # Start and end at the depot

def shake(solution, k):
    """Generate a new solution by randomly swapping two cities in the tour."""
    new_solution = solution[1:-1]  # Remove the depot from the ends before shuffling
    random.shuffle(new_solution)
    return [0] + new_solution[:k] + solution[k+1:-1] + [0]

def local_search(solution):
    """Apply a local search to improve the solution via pairwise city swapping."""
    best_solution = solution[:]
    best_cost = tour_distance(solution)
    
    for i in range(1, len(solution) - 1):
        for j in range(i + 1, len(solution) - 1):
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = tour_distance(new_solution)
            if new_cost < best_cost:
                best_solution, best_cost = new_solution, new_cost
    
    return best_solution

def gvns():
    """General Variable Neighborhood Search to solve the modified TSP."""
    best_solution = generate_initial_solution()
    best_cost = tour_distance(best_solution)
    itermax = 100
    kmax = 9

    for _ in range(itermax):
        k = 1
        while k <= kmax:
            new_solution = shake(best_solution, k)
            new_solution = local_search(new_solution)
            new_cost = tour_distance(new_solution)
            if new_cost < best_cost:
                best_solution, best_cost = new_solution, new_cost
                k = 1  # Reset k if improvement is found
            else:
                k += 1

    return best_solution, best_cost

# Perform the search and print the resulting tour and cost
final_tour, final_cost = gvns()
print("Tour:", final_tour)
print("Total travel cost:", round(final_cost, 2))