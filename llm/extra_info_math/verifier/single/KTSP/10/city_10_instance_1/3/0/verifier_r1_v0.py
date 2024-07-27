import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
def verify_tour(tour, cities, expected_cities_count):
    # Check if the tour starts and ends at the depot city 0
    requirement_1 = (tour[0] == 0 and tour[-1] == 0)
    
    # Check if the tour visits exactly 5 cities including depot city
    requirement_2 = (len(set(tour)) == expected_cities_count)
    
    # Calculate total travel cost
    total_travel_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_travel_cost}")
    
    if requirement_1 and requirement_2:
        return "CORRECT"
    else:
        return "FAIL"

# Test Example
cities = [
    (53, 68),  # Depot city 0
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]
# Provided tour
tour = [0, 1, 2, 3, 9, 0]  # Example Tour

# Running the test
result = verify_tour(tour, cities, expected_cities_count=5)
print(result)