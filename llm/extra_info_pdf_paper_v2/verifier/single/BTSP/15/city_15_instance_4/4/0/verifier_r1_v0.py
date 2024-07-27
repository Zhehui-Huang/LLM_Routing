import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_tour(cities, tour):
    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if each city except the depot city 0 is visited exactly once
    for city in range(1, len(cities)):
        if tour.count(city) != 1:
            return "FAIL"
    
    # Check if there are exactly len(cities) visits in the tour (every city once plus returning to depot)
    if len(tour) != len(cities) + 1:
        return "FAIL"

    return "CORRECT"

# Test case
cities = [
    (35, 40), # Depot city 0
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

# Hypothetical tour which needs to be replaced with your actual solution's output
sample_tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0]

result = verify_tour(cities, sample_tour)
print(result)