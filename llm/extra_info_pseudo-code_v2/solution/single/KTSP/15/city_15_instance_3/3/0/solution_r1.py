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
    """Calculate the total travel cost of the tour by traversing each city sequentially."""
    total_cost = 0
    n = len(tour)
    if n > 1:
        for i in range(1, n):
            total_cost += euclidean_distance(cities[tour[i - 1]], cities[tour[i]])
        # Complete the round trip by returning to the starting point
        total_cost += euclidean_distance(cities[tour[-1]], cities[tour[0]])
    return total_cost

def generate_initial_solution():
    k = 10
    tour = [0]  # Start at the depot
    available_cities = list(range(1, len(cities)))  # All cities except the depot
    tour += random.sample(available_cities, k - 1)
    tour.append(0)  # End at the depot
    return tour

def local_search(tour, neighborhood):
    """Attempts to find a shorter path by either swapping or reinserting cities."""
    if neighborhood == 'N1':  # swap two cities
        best_tour = tour[:]
        best_cost = total_tour_cost(tour)
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]  # Swap two cities
                cost = total_tour_cost(new_tour)
                if cost < best_cost:
                    best_tour = new_tour
                    best_cost = cost
        return best_tour

def gvns():
    max_iter = 100  # Maximum number of iterations
    p_max = 2  # Two neighborhood types
    current_solution = generate_initial_solution()
    best_cost = total_tour_cost(current_solution)
    best_solution = current_solution[:]
    
    for _ in range(max_iter):
        p = 1
        while p <= p_max:
            new_solution = local_search(current_solution, 'N1' if p == 1 else 'N2')
            new_cost = total_tour_cost(new_solution)
            
            if new_cost < best_cost:
                best_solution = new_solution[:]
                best_cost = new_cost
                p = 1  # Reset p to its initial value
            else:
                p += 1  # Move to next neighborhood structure
        
    return best_solution, best_cost

# Run the GVNS algorithm and print the results
best_tour, best_cost = gvns()
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))