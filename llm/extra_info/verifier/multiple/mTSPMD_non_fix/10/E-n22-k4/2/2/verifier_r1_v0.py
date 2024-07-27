import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_tour_cost(tour, coordinates):
    cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        cost += calculate_distance(coordinates[city1][0], coordinates[city1][1], coordinates[city2][0], coordinates[city2][1])
    return cost

def test_solution():
    # Define city coordinates
    coordinates = [
        (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), 
        (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), 
        (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193), 
        (164, 193), (129, 189), (155, 185), (139, 182)
    ]
    
    # Tours given by the solution
    tours = [
        [0, 14, 17, 20, 10, 4, 0],
        [0, 16, 19, 21, 7, 0],
        [0, 12, 15, 18, 9, 1, 0],
        [0, 13, 11, 8, 6, 5, 2, 3, 0]
    ]

    # Calculate the total travel costs for all tours
    calculated_costs = [calculate_tour_cost(tour, coordinates) for tour in tours]
    calculated_total_cost = sum(calculated_costs)

    # Expected costs and total cost
    expected_costs = [149.94, 138.15, 161.06, 160.46]
    expected_total_cost = 609.61

    # Check if each city is visited exactly once excluding the depots
    all_cities = set(range(len(coordinates)))
    cities_visited = set(city for tour in tours for city in tour if city != 0)
    
    # Compare floats with a tolerance for potential minor variations in floating point calculations
    def compare_costs(calculated, expected):
        return all(abs(c - e) < 1e-2 for c, e in zip(calculated, expected))
    
    correct_visitation = all_cities == cities_visited
    correct_starting_points = all(tour[0] == 0 for tour in tours)
    correct_costs = compare_costs(calculated_costs, expected_costs)
    correct_total_cost = abs(calculated_total_cost - expected_total_cost) < 1e-2

    # Output result based on the correctness of the solution
    if correct_visitation and correct_starting_points and correct_costs and correct_total:
        print("CORRECT")
    else:
        print("FAIL")

# Running the test function
test_solution()