import math

# City coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Function to find the nearest neighbor tour
def nearest_neighbor(start):
    unvisited = set(cities.keys())
    tour = [start]
    curr_city = start
    unvisited.remove(start)
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(curr_city, city))
        tour.append(next_city)
        unvisited.remove(next_proc_city)
        curr_city = next_city
    
    tour.append(start)  # Return to the depot
    
    return tour

# Compute the tour using the nearest neighbor algorithm
tour = nearest_neighbor(0)

# Calculate the total distance of the tour
total_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Output the results
print("Tour:", tour)
print("Total travel cost:", int(total_distance))