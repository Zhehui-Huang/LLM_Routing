import math

# Coordinates of each city indexed from 0 to 14
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), 
    (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), 
    (83, 96), (60, 50), (98, 1)
]

def euclidean_distance(c1, c2):
    # Calculate Euclidean distance between two points
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def nearest_neighbor_tour(start_index):
    num_cities = len(coordinates)
    unvisited = set(range(1, num_cities))  # All cities except depot city
    tour = [start_index]
    current_city = start_index

    while unvisited:
        # Find the nearest unvisited city
        next_city = min(unvisited, key=lambda city: euclidean_distance(coordinates[current_city], coordinates[city]))
        tour.append(next_city)
        current_city = next_city  # Move to the next city
        unvisited.remove(next_city)

    tour.append(start_index)  # Return to depot city
    return tour

def total_tour_cost(tour):
    # Calculate the total cost of the tour
    return sum(euclidean_state istance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))

# Getting the tour and the cost
tour = nearest_neighbor_tour(0)
tour_cost = total_tour_cost(tour)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {round(tour_cost, 2)}")