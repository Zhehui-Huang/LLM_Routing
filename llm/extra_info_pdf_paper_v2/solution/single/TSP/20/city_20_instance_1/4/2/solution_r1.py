import math

# Coordinates of all cities including the depot
cities = [(14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82),
          (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), (49, 23),
          (78, 76), (68, 45), (50, 28), (69, 9)]

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Function to calculate the total travel cost of a tour
def total_tour_distance(tour):
    distance = 0
    for i in range(1, len(tour)):
        distance += euclidean_distance(cities[tour[i - 1]], cities[tour[i]])
    # Return to the starting point
    distance += euclidean_distance(cities[tour[-1]], cities[tour[0]])
    return distance

# Implementation of the 2-opt swap routine
def two_opt(tour):
    best_distance = total_tour_distance(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for k in range(i + 1, len(tour) - 1):
                new_tour = tour[:i] + tour[i:k+1][::-1] + tour[k+1:]
                new_distance = total_tour_distance(new_tour)
                if new_distance < best_distance:
                    tour = new_tour
                    best_distance = new_distance
                    improved = True
    return tour, best_distance

# Create an initial tour starting at the depot
def initial_tour():
    return list(range(len(cities)))

# Getting the optimal tour and minimum distance using the 2-opt algorithm
initial = initial_tour()
optimized_tour, min_distance = two_opt(initial)

# Adjust output to show the tour starting and ending at the depot city
optimized_tour.append(optimized_tour[0])

# Output the tour and total minimum distance
print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {min_distance:.2f}")