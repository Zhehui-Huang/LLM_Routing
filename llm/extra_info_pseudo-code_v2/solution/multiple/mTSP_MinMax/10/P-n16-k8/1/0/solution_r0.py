import math
import random

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def initialize_solution(cities, num_robots):
    tours = [[] for _ in range(num_robots)]
    distances = [euclidean_distance(cities[0], cities[i]) for i in range(1, len(cities))]
    sorted_cities = sorted(range(1, len(cities)), key=lambda i: distances[i-1])
    
    for i, city in enumerate(sorted_cities):
        best_robot = i % num_robots
        tours[best_robot].append(city)
        
    for tour in tours:
        tour.insert(0, 0)  # Start at the depot
        tour.append(0)     # Return to the depot
    
    return tours

def total_tour_distance(tour, cities):
    total = 0
    for i in range(len(tour) - 1):
        total += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total

def main_gvns(cities, num_robots, max_iterations, lmax, kmax, tmax):
    # Initial feasible solution
    tours = initialize_solution(cities, num_robots)
    
    best_solution = tours
    best_max_distance = max(total_tour_distance(tour, cities) for tour in tours)
    
    iteration = 0
    time_elapsed = 0
    
    while time_elapsed < tmax and iteration < max_iterations:
        k = 1
        while k < kmax:
            new_solution = shake(tours, cities, k)
            new_solution = seq_vnd(new_solution, cities, lmax)
            new_max_distance = max(total_tour_distance(tour, cities) for tour in new_solution)
            
            if new_max_distance < best_max_distance:
                best_solution = new_solution
                best_max_distance = new_max_distance
                k = 1
            else:
                k += 1
            
        iteration += 1
        time_elapsed += 1  # Simulate time passing
    
    return best_solution, best_max_distance

def shake(tours, cities, k):
    # A simple implementation of shaking: relocate k random nodes
    for _ in range(k):
        tour_from = random.choice(tours)
        if len(tour_from) > 3:  # Ensure there's something to remove
            node = random.choice(tour_from[1:-1])
            tour_from.remove(node)
            tour_to = random.choice(tours)
            tour_to.insert(random.randint(1, len(tour_to)-1), node)
    return tours

def seq_vnd(tours, cities, lmax):
    # A very simplified version of this search method
    for _ in range(lmax):
        # Harmonize the solution a bit by evening out tour lengths
        lengths = [len(tour) for tour in tours]
        max_len_tour = lengths.index(max(lengths))
        min_len_tour = lengths.index(min(lengths))
        
        if len(tours[max_len_tour]) > 3:
            node = random.choice(tours[max_len_tour][1:-1])
            tours[max_len_tour].remove(node)
            tours[min_len_tour].insert(random.randint(1, len(tours[min_len_tour])-1), node)
    return tours

# The actual city coordinates and number of robots
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]
num_robots = 8

best_solution, max_cost = main_gvns(cities, num_robots, max_iterations=50, lmax=5, kmax=5, tmax=60)

# Output the results
for idx, tour in enumerate(best_solution):
    distance = total_tour_distance(tour, cities)
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {distance}")

print(f"Maximum Travel Cost: {max_cost}")