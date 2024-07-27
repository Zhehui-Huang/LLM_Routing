import math

# Define helper functions
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def nearest_neighbor_tour(start, cities, coordinates):
    tour = [start]
    current = start
    remaining = set(cities)
    
    while remaining:
        nearest = min(remaining, key=lambda x: euclidean_distance(coordinates[current], coordinates[x]))
        tour.append(nearest)
        remaining.remove(nearest)
        current = nearest
    return tour

def split_tour(tour, coordinates):
    # This function splits a tour into two by trying to min/max balance the travel costs
    total_len = len(tour)
    best_max_cost = float('inf')
    best_split = None
    
    for i in range(1, total_len-1):
        first_tour = tour[:i] + [tour[0]]
        second_tour = tour[i:] + [tour[0]]
        first_cost = calculate_tour_cost(first_tour, coordinates)
        second_cost = calculate_tour_cost(second_tour, coordinates)
        
        if max(first_cost, second_cost) < best_max_cost:
            best_max_cost = max(first_cost, second_cost)
            best_split = (first_tour, second_tour, first_cost, second_cost)
    
    return best_split

def calculate_tour_cost(tour, coordinates):
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))

# Initialize cities and their coordinates
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41), 
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58,27), 15: (37, 69), 
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}
city_list = list(coordinates.keys())[1:]

# Generate the initial tour using the nearest neighbor heuristic
initial_tour = nearest_neighbor_tour(0, city_list, coordinates) + [0]

# Split the tour into two balanced tours
first_tour, second_tour, first_cost, second_cost = split_tour(initial_tour, coordinates)

# Output the result
print(f"Robot 0 Tour: {first_tour}")
print(f"Robot 0 Total Travel Cost: {int(first_cost)}")
print(f"Robot 1 Tour: {second_tour}")
print(f"Robot 1 Total Travel Cost: {int(second_cost)}")
print(f"Maximum Travel Cost: {int(max(first_cost, second_cost))}")