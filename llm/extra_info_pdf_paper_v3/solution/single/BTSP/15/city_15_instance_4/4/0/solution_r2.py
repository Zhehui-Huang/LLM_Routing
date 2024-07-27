import math

# Define the coordinates of the cities including the depot
cities = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), 
          (54, 46), (8, 70), (97, 62), (14, 41), (70, 44), 
          (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_tour():
    n = len(cities)
    unvisited = list(range(1, n))  
    tour = [0]  # Start at the depot
    current_city = 0
    
    # Variables to track cost and max distance between consecutive cities
    total_distance = 0
    max_consecutive_distance = 0
    
    # Greedy nearest neighbor algorithm
    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(cities[current_city], cities[x]))
        distance = euclidean_distance(cities[current_city], cities[next_city])
        total_distance += distance
        max_consecutive_distance = max(max_consecutive_distance, distance)
        current_city = next_city
        tour.append(current_city)
        unvisited.remove(current_city)

    # Returning to the depot
    final_leg_distance = euclidean_distance(cities[current_city], cities[0])
    total_distance += final_leg_distance
    max_consecutive_distance = max(max_consecutive_distance, final_leg_distance)
    tour.append(0)  # Close the tour by returning to the depot
    
    return tour, total_distance, max_consecutive_distance

# Compute the desired tour, total travel cost, and maximum consecutive distance
tour, total_cost, max_distance = calculate_tour()

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")