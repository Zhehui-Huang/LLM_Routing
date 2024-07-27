import math

# Provided city coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Given solution
tour = [0, 9, 5, 6, 0]
reported_total_cost = 61.66

# Helper function to compute Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def verify_solution(tour, reported_total_cost):
    try:
        # Check tour starts and ends at city 0
        assert tour[0] == 0 and tour[-1] == 0, "Tour does not start and end at depot city"
        # Check tour visits exactly 4 distinct cities including depot
        assert len(set(tour)) == 4, "Tour does not visit exactly 4 distinct cities (including depot)"
        # Calculate and compare travel cost
        actual_total_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        assert math.isclose(actual_total_cost, reported_total_cost, abs_tol=1e-2), "Mismatch in calculated cost"
        # If all assertions pass
        print("CORRECT")
    except AssertionError as e:
        print("FAIL:", str(e))

if __name__ == "__main__":
    verify_solution(tour, reported_total_cost)