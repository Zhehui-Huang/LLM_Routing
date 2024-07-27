import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution():
    # Given city coordinates
    cities = {
        0: (84, 67),
        1: (74, 40),
        2: (71, 13),
        3: (74, 82),
        4: (97, 28),
        5: (0, 31),
        6: (8, 62),
        7: (74, 56),
        8: (85, 71),
        9: (6, 76)
    }
    
    # Tour provided as solution
    tour = [0, 4, 2, 1, 7, 3, 8, 0]
    correct_travel_cost = 159.97  # Rounded to two decimal places for comparison
    
    # Check the number of unique cities in the tour (excluding the repeat of the depot at the end)
    if len(set(tour[:-1])) != 7:
        return "FAIL"
    
    # Check the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Calculate the travel cost from the tour
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        
    # Compare calculated travel cost with the provided cost, allowing for small float precision errors
    if not math.isclose(total_cost, correct_travel_cost, abs_tol=0.01):
        return "FAIL"
    
    # If all checks pass
    return "CORRECT"

# Running the unit tests
print(test_solution())