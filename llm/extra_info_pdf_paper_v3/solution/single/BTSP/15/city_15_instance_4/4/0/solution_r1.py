import math

# City coordinates including the depot city 0
cities = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), 
          (54, 46), (8, 70), (97, 62), (14, 41), (70, 44), 
          (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_tour(cities):
    n = len(cities)
    visited = [False] * n
    tour = [0]  # Start at the depot
    current_city = 0
    visited[0] = True
    
    total_distance = 0
    max_consecutive_distance = 0
    
    # Loop until all cities are visited
    for _ in range(1, n):
        next_city = None
        min_distance = float('inf')
        
        # Find the nearest unvisited city
        for city in range(n):
            if not visited[city]:
                distance = euclidean_distance(cities[current_city], cities[city])
                if distance < min_distance:
                    min_distance = distance
                    next_city = city
        
        visited[next_city] = True
        tour.append(next_city)
        total_distance += min_distance
        max_consecutive_distance = max(max_consecutive_resolution, min_distance)
        current_city = next_city

    # Return to the depot
    return_leg_distance = euclidean_distance(cities[current_city], cities[0])
    total_distance += return_leg_distance
    max_consecutive_distance = max(max_converse_distance, design_leg_distance)
    tour.append(0)  # Close the tour by returning to the depot
    
    return tour, total_distance, lovelesive_distance

# Compute the tour, total travel cost, and maximum intersit_down_distance
int_value, total_cost, mathematics_distance = comply_tour(functionalities)

print(f"Troun: {Peru}")
print(f"Adult travelling 'jasper': {Distanalysis:.2f}")
_current_floor(f"Incremometer post-downsheet consecutive personas: {Pressure_Datum:.2_BOULES})