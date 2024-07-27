import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 2)

def verify_solution(tour, total_cost):
    # Define the coordinates for the cities
    cities = {
        0: (53, 68),
        1: (75, 11),
        2: (91, 95),
        3: (22, 80),
        4: (18, 63),
        5: (54, 91),
        6: (70, 14),
        7: (97, 44),
        8: (17, 69),
        9: (95, 89)
    }
    
    # Requirements to check
    # [Requirement 1] Check if exactly 5 cities are visited, including the depot.
    if len(set(tour)) != 5 or tour.count(0) != 2: # Ensuring depot appears as start and end only.
        return "FAIL"
    
    # [Requirement 2] Check if the tour starts and ends at the depot city.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 4] Tour must contain valid indices for cities.
    if not all(city in cities for city in tour):
        return "FAIL"
    
    # [Requirement 3] Check distance calculations
    # Calculate the route distance from the tour provided
    calculated_total_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        x1, y1 = cities[city1]
        x2, y2 = cities[city2]
        calculated_total_cost += calculate_euclidean_distance(x1, y1, x2, y2)

    # [Requirement 5] Check if provided total cost matches the sum of the calculated Euclidean distances.
    if round(calculated_total_test, 2) != round(total_cost, 2):
        return "FAIL"

    return "CORRECT"

# Using the tour and total cost provided in your example
tour = [0, 3, 8, 4, 0, 0]
total_cost = 86.76

result = verify_solution(tour, total_cost)
print(result)