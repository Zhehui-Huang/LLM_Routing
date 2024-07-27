import math

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def check_tour_correctness(tour, cities, expected_total_cost, expected_max_distance):
    # Check if the tour starts and ends at the depot city (city index 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if each city is visited exactly once (excluding the depot which is visited twice)
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != len(cities) - 1:
        return "FAIL"
    
    total_distance = 0
    max_consecutive_distance = 0
    for i in range(1, len(tour)):
        distance = calculate_distance(cities[tour[i - 1]], cities[tour[i]])
        total_distance += distance
        if distance > max_consecutive_distance:
            max_consecutive_distance = distance

    # Since the problem specifically is to minimize the maximum distance, we check if calculated values are correct
    if (abs(total_distance - expected_total_cost) > 1e-5 or
        abs(max_consecutive_distance - expected_max_distance) > 1e-5):
        return "FAIL"

    return "CORRECT"

# City coordinates
cities = [
    (35, 40), # Depot City 0
    (39, 41), # City 1
    (81, 30), # City 2
    (5, 50),  # City 3
    (72, 90), # City 4
    (54, 46), # City 5
    (8, 70),  # City 6
    (97, 62), # City 7
    (14, 41), # City 8
    (70, 44), # City 9
    (27, 47), # City 10
    (41, 74), # City 11
    (53, 80), # City 12
    (21, 21), # City 13
    (12, 39)  # City 14
]

tour = [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 5, 2, 13, 0]
expected_total_cost = 337.8447016788252
expected_max_distance = 60.67124524847005

# Running the corrected test
result = check_tour_correctness(tour, cities, expected_total_cost, expected_max_distance)
print(result)