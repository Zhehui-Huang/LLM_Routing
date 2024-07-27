import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def test_solution(tour, total_travel_cost, cities, correct_total_cost):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        print("FAIL")
        return
    
    # Check if the tour includes exactly 8 cities including the depot city
    if len(tour) != 9 or len(set(tour)) != 9:
        print("FAIL")
        return
    
    # Check if all cities in the tour exist in the cities list
    if any(city not in cities.keys() for city in tour):
        print("FAIL")
        return
    
    # Calculate the computed total travel cost from the tour
    computed_total_cost = 0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i+1]
        computed_total_cost += calculate_euclidean_distance(
            cities[city1][0], cities[city1][1], cities[city2][0], cities[city2][1]
        )
    
    # Check if the computed total travel cost is approximately equal to the given total travel cost
    if not math.isclose(computed_totalry_total_cost, correct_cost, rel_tol=1e-5):
        print("FAIL")
        return
    
    # If all checks pass
    print("CORRECT")

# Using the provided tour and total travel cost as parameters
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

tour = [0, 4, 7, 5, 1, 9, 6, 3, 0]
total_travel_cost = 235.37735391753958

test_solution(tour, total_travel_cost, cities, total_travel_cost)