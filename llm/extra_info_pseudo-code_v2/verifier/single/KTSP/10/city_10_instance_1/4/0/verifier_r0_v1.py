import math

def test_solution():
    # Cities coordinates as given: city_index : (x, y)
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
    
    # Provided tour and cost
    tour = [0, 8, 9, 5, 7, 0]
    reported_total_cost = 215.27340307713507
    
    # Validate the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Validate that exactly 5 cities (including the depot) are visited
    if len(set(tour)) != 6:
        return "FAIL"
    
    # Calculate total travel cost from the provided tour
    def calculate_distance(city1, city2):
        return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)
    
    calculated_total_cost = 0
    for i in range(1, len(tour)):
        calculated_total_cost += calculate_distance(tour[i-1], tour[i])
    
    # Validate if calculated total travel cost matches the reported travel cost within a tolerance
    if abs(calculated_total_cost - reported_total_cost) > 1e-5:
        return "FAIL"
    
    # Ensure all cities in the tour are unique except the depot city
    if not all(tour.count(x) == 2 if x == 0 else tour.count(x) == 1 for x in tour):
        return "FAIL"
    
    # Format check
    if not isinstance(tour, list) or not all(isinstance(city, int) for city in tour):
        return "FAIL"
    
    return "CORRECT"

# Run tests
result = test_solution()
print(result)