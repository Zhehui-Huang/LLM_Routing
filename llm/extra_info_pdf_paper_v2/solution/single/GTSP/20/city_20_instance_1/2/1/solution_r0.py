import math

# Define coordinates for all cities and the respective groups
coordinates = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79), 
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}
group_cities = {
    0: [5, 6, 7, 11, 17],
    1: [1, 4, 8, 13, 16],
    2: [2, 10, 15, 18, 19],
    3: [3, 9, 12, 14]
}

# Define Euclidean distance calculation function
def calculate_distance(city1, city2):
    coord1 = coordinates[city1]
    coord2 = coordinates[city2]
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def find_shortest_tour():
    # Minimum distance and optimal tour initialization
    min_distance = float('inf')
    best_tour = []
    
    # Try each combination of one city from each group + starting and ending at the depot city
    from itertools import product
    for combination in product(group_cities[0], group_cities[1], group_cities[2], group_cities[3]):
        tour = [0] + list(combination) + [0]  # Construct the tour starting and ending at depot
        # Calculate the total distance of this tour
        total_distance = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        
        # Check if this is a better tour than what we have found before
        if total_distance < min_distance:
            min_distance = total_distance
            best_tour = tour
    
    return best_tour, min_distance

# Execute the function and generate the output
result_tour, result_distance = find_shortest_tour()
result_tour_str = 'Tour: ' + str(result_tour)
result_distance_str = 'Total travel cost: ' + f"{result_distance:.2f}"

# Printing result
print(result_tour_str)
print(result_distance_str)