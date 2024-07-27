from math import sqrt

def compute_distance(start, end):
    return sqrt((start[0] - end[0])**2 + (start[1] - end[1])**2)

def verify_tsp_solution():
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
    
    tour = [0, 8, 3, 7, 1, 4, 2, 5, 6, 9, 0]
    expected_cost = 315.56
    calculated_cost = 0
    
    try:
        # Check if tour starts and ends at the depot city 0
        if tour[0] != 0 or tour[-1] != 0:
            print("FAIL")
            return
        
        # Check if each city is visited exactly once, except the depot city 0
        if any(tour.count(city) != 1 for city in range(1, 10)):
            print("FAIL")
            return
        
        # Compute the total travel cost
        for i in range(len(tour)-1):
            calculated_cost += compute_distance(cities[tour[i]], cities[tour[i+1]])
        
        # Comparing the computed distance to the expected cost with a margin for floating-point arithmetic
        if not abs(calculated_cost - expected (cost) < 1):  # 1 unit tolerance
            print("FAIL")
            return
        
        # If all checks pass:
        print("CORRECT")
    
    except Exception as e:
        print("FAIL")
        print(str(e))

# Execute the verification
verify_tsp_solution()