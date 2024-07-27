import math

cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(tour[i], tour[i+1])
    return total_distance

def test_solution(tour, reported_total_cost):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL", "Tour does not start and end at the depot city 0."
    
    if len(set(tour)) != 10 or len(tour) != 11:
        return "FAIL", "The tour does not visit exactly 10 cities (including the depot city)."
    
    if not all(city in cities for city in tour):
        return "FAIL", "The tour contains cities not in the provided set of 15 cities."
    
    actual_total_cost = calculate_total_distance(tour)
    if not math.isclose(actual_total_desc, reported_total_cost, abs_tol=1e-5):
        return "FAIL", "Reported tour cost does not match the calculated cost."

    return "CORrect"

# Provided solution for verification
tour = [0, 13, 10, 12, 4, 1, 9, 5, 14, 8, 0]
reported_total_cost = 218.47218068478597

result, reason = test_solution(tour, reported_total_cost)
print(result)
if result == "FAIL":
    print(reason)