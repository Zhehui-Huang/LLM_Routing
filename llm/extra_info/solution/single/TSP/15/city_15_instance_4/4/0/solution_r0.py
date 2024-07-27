import numpy as np

# Define the cities coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50),
    4: (72, 90), 5: (54, 46), 6: (8, 70), 7: (97, 62),
    8: (14, 41), 9: (70, 44), 10: (27, 47), 11: (41, 74),
    12: (53, 80), 13: (21, 21), 14: (12, 39)
}

def calc_euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate distance matrix
n_cities = len(cities)
distance_matrix = np.zeros((n_cities, n_cities))

for i in range(n_cities):
    for j in range(n_cities):
        if i != j:
            distance_matrix[i, j] = calc_euclidean_distance(cities[i], cities[j])

# Nearest neighbor algorithm
def nearest_neighbor(start=0):
    unvisited = list(cities.keys())
    unvisited.remove(start)
    tour = [start]
    current_city = start
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city, city])
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)
    
    tour.append(start)  # return to the depot
    return tour

# Calculate the total travel cost of the tour
def calculate_tour_cost(tour):
    total_cost = sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))
    return total_cost

# Execute the function to find the tour and cost
tour = nearest_neighbor()
total_cost = calculate_tour_cost(tour)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")