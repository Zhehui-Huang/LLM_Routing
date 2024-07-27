import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def test_solution():
    # Provided solution
    tour = [0, 3, 6, 9, 1, 5, 7, 4, 0]
    reported_total_cost = 235.38
    
    # Cities coordinates
    coordinates = [
        (79, 15),  # City 0
        (79, 55),  # City 1
        (4, 80),   # City 2
        (65, 26),  # City 3
        (92, 9),   # City 4
        (83, 61),  # City 5
        (22, 21),  # City 6
        (97, 70),  # City 7
        (20, 99),  # City 8
        (66, 62)   # City 9
    ]
    
    # Check if the solution starts and ends at the depot city 0
    requirement_1 = tour[0] == 0 and tour[-1] == 0
    
    # Check if exactly 8 cities are visited, including the depot
    requirement_2 = len(set(tour)) == 8 and len(tour) == 9  # includes starting and ending at the depot
    
    # Calculate the actual travel cost and compare
    total_cost_calculated = 0
    for i in range(len(tour) - 1):
        city_1 = coordinates[tour[i]]
        city_2 = coordinates[tour[i+1]]
        total_cost_calculated += calculate_distance(city_1[0], city_1[1], city_2[0], city_2[1])
    
    # Checking the total cost rounded to two decimal places
    requirement_3 = abs(round(total_cost_calculated, 2) - reported_total_cost) < 0.01
    
    # Final check to confirm all requirements are met
    if requirement_1 and requirement_2 and requirement_3:
        print("CORRECT")
    else:
        print("FAIL")

test_solution()