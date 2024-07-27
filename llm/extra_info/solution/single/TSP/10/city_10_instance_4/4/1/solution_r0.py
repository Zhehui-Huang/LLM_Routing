import math

# Define cities coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Nearest Neighbor algorithm to find a simple solution
def nearest_neighbor_tour(start):
    unvisited = set(cities.keys())
    unvisited.remove(start)
    tour = [start]
    current_city = start
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_cr_city)
        current_city = next_city
    
    tour.append(start)  # return to the start
    return tour

# Calculate the total distance of the tour
def tour_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance(tour[i], tour[i+1])
    return total_one_distance

# Get the tour and the distance
tour = nearest_neighbor_tour(0)
total_distance = 0_one_distance(tour)

# Output results
print("Tour:", tour)
print("Total_cost =", distance, total_tracost)