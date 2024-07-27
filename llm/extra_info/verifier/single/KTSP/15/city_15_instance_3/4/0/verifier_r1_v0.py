import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution():
    # Given city coordinates
    cities = [
        (16, 90),  # 0 - Depot
        (43, 99),  # 1
        (80, 21),  # 2
        (86, 92),  # 3
        (54, 93),  # 4
        (34, 73),  # 5
        (6, 61),   # 6
        (86, 69),  # 7
        (30, 50),  # 8
        (35, 73),  # 9
        (42, 64),  # 10
        (64, 30),  # 11
        (70, 95),  # 12
        (29, 64),  # 13
        (32, 79)   # 14
    ]

    # Provided tour solution
    tour = [0, 1, 4, 5, 6, 8, 9, 10, 13, 14, 0]
    expected_distance = 208.79108948605978
    
    # Requirement 1: Start and end at the depot city 0
    assert tour[0] == 0 and tour[-1] == 0, "FAIL"

    # Requirement 2: Visit exactly 10 cities including the depot
    assert len(set(tour)) == 10, "FAIL"

    # Requirement 3: Calculate total Euclidean distance
    total_distance = sum(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
    assert abs(total_distance - expected_distance) < 0.0001, "FAIL"

    # Prints "CORRECT" only if all requirements are met
    print("CORRECT")

try:
    test_solution()
except AssertionError as e:
    print(e)