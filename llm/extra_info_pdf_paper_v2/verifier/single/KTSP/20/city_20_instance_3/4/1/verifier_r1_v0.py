import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, cost):
    cities_coordinates = {
        0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
        5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
        10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
        15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
    }
    
    # Check if the tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 13 cities are visited (length should be 14, including repeat of depot city)
    if len(tours) != 14:
        return "FAIL"
    
    # Calculate the total travel cost and compare it to the provided cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_index_1 = tour[i]
        city_index_2 = tour[i+1]
        calculated_cost += euclidean_distance(cities_coordinates[city_index_1],
                                              cities_coordinates[city_index_2])
    
    # Rounding cost to 2 decimal places for proper comparison
    calculated_cost = round(calculated_cost, 2)
    
    if calculated_cost != cost:
        return "FAIL"
    
    return "CORRECT"

# Provided solution details
solution_tour = [0, 3, 19, 13, 2, 5, 15, 1, 4, 7, 8, 12, 18, 0]
solution_cost = 305.19

# Verify and return result
result = verify_tour(solution_tour, solution_cost)
print(result)