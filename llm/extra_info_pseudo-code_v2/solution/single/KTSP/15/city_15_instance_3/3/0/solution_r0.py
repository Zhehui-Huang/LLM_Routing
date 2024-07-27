import random
import math

# City coordinates with depot as the first city (index 0)
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61), 
    (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

def euclidean_distance(p1, p2):
    """Calculate Euclidean distance between two points (x1, y1) and (x2, y2)."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def total_tour_cost(tour):
    """Calculate the total travel cost of the tour."""
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(cities[tour[i - 1]], cities[tour[i]])
    return total_cost

def generate_initial_solution():
    k = 10  # Including the depot city
    chosen = {0}
    tour = [0]
    while len(tour) < k:
        next_city = random.choice([i for i in range(1, len(cities)) if i not in chosen])
        best_pos = 0
        best_cost = float('inf')
        for i in range(1, len(tour) + 1):
            new_tour = tour[:i] + [next_city] + tour[i:]
            cost = total_tour_cost(new_tour)
            if cost < best_cost:
                best_cost = cost
                best_pos = i
        tour.insert(best_pos, next_city)
        chosen.add(next_city)
    tour.append(0)  # Return to the depot
    return tour

def local_search(tour, neighborhood):
    if neighborhood == 'N1':  # Exchange a city with one outside the tour
        best_tour = tour[:]
        best_cost = total_tour_cost(tour)
        for i in range(1, len(tour) - 2):
            for j in range(1, len(cities)):
                if j not in tour:
                    new_tour = tour[:]
                    new_tour[i] = j
                    new_tour[-1] = 0  # Ensure return to depot
                    new_cost = total_tour_cost(new_tour)
                    if new_cost < best_cost:
                        best_tour = new_tour
                        best_cost = new_cost
        return best_tour
    elif neighborhood == 'N2':  # Swap two cities in the tour
        best_tour = tour[:]
        best_cost = total_tour_cost(tour)
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = total_tour_cost(new_tour)
                if new_cost < best_cost:
                    best_tour = new_tour
                    best_cost = new_cost
        return best_tour

# Implementing the GVNS algorithm based on the provided pseudocode structure
def gvns():
    itermax = 100   # Maximum number of iterations
    pmax = 2       # Maximum index for neighborhoods
    best_solution = generate_initial_solution()
    best_cost = total_tour_cost(best_solution)
    
    for _ in range(itermax):
        current_solution = generate_initial_solution()
        p = 1
        while p <= pmax:
            if p == 1:
                new_solution = local_search(current_solution, 'N1')
            elif p == 2:
                new_solution = local_search(current_state, 'N2')
            new_cost = total_tour_cost(new_solution)
            if new_cost < best_cost:
                best_solution = new_solution
                best_cost = new_cost
                p = 1  # Reset p and look again
            else:
                p += 1

    return best_solution, best_cost

# Running the gvns algorithm
best_tour, best_cost = gvns()
print("Tour:", best_tour)
print("Total travel cost:", best_cost)