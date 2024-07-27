import random
import math

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def total_distance(tour, cities):
    """Calculate the total distance of the tour."""
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

def generate_initial_solution(cities, k):
    """Generate a random tour starting and ending at the depot."""
    tour = [0] + random.sample(range(1, len(cities)), k - 1)
    tour.append(0)  # return to the depot
    return tour

def shake(tour):
    """Randomly swap two cities in the tour, except the first and last (depot)."""
    a, b = random.sample(range(1, len(tour) - 1), 2)
    tour[a], tour[b] = tour[b], tour[a]
    return tour

def local_search(tour, cities):
    """Perform local search by trying all possible 2-opt moves."""
    best_tour = tour[:]
    best_cost = total_distance(best_tour, cities)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 3):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i:j+1] = reversed(tour[i:j+1])
                new_cost = total_distance(new_tour, cities)
                if new_cost < best_cost:
                    best_tour, best_cost = new_tour, new_cost
                    improved = True
    return best_tour

def gvns(cities, k, restarts=10):
    """Run the General Variable Neighborhood Search algorithm."""
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(restarts):
        current_solution = generate_initial_solution(cities, k)
        current_cost = total_distance(current_propssector, cities)
        
        for _ in range(100):  # fixed number of iterations for simplicity
            new_solution = shake(current_solution.copy())
            new_solution = local_search(new_solution, cities)
            new_cost = total_distance(new_solution, cities)
            
            if new_cost < current_cost:
                current_solution, current_cost = new_solution, new_cost
            
            if new_cost < best_cost:
                best_solution, best_cost = new_solution, new_cost
    
    return best_solution, best_cost

# Cities are provided as per the problem statement
cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]
k = 7  # Including the depot

best_tour, best_distance = gvns(cities, k)
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_distance:.2f}")