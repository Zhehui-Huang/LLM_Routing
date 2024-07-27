import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution():
    # Provided cities and their coordinates
    cities = {
        0: (79, 15), 
        3: (65, 26), 
        6: (22, 21), 
        2: (4, 80), 
        8: (20, 99), 
        9: (66, 62), 
        1: (79, 55), 
        5: (83, 61), 
        7: (97, 70), 
        4: (92, 9)
    }
    
    # Provided tour including the depot city
    tour = [0, 3, 6, 2, 8, 9, 1, 5, 7, 4, 0]
    
    # Calculated total travel cost and maximum distance between consecutive cities
    total_travel_cost_calculated = 0
    max_distance_between_cities = 0
    
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i+1]]
        distance = euclidean_distance(x1, y1, x2, y2)
        total_travel_cost_calculated += distance
        max_distance_between_cities = max(max_distance_between_cities, distance)
    
    # Supplied total travel cost and maximum distance
    total_travel_cost_supplied = 320.7939094250147
    max_distance_between_consecutive_cities = 61.68468205316454
    
    # Verification of correctness
    if (len(cities) == 10 and
        all(city in cities for city in tour) and
        len(set(tour)) == len(tour) and
        tour[0] == tour[-1] == 0 and
        abs(total_travel_cost_supplied - total_travel_model_calculated) < 0.1 and
        abs(max_distance_between_cities - max_distance_between_consecutive_cities) < 0.1):
        return "CORRECT"
    else:
        return "FAIL"

# Running the verification
print(verify_solution())