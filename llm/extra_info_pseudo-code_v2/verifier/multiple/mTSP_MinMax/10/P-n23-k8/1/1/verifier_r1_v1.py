import math

# Coordinates of cities including the depot city at position 0
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Expected tours
tours = [
    [0, 7, 18, 8, 0],
    [0, 13, 3, 21, 0],
    [0, 20, 19, 12, 0],
    [0, 1, 4, 9, 0],
    [0, 6, 11, 2, 0],
    [0, 15, 17, 5, 0],
    [0, 14, 10, 0],
    [0, 22, 16, 0]
]

def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

def test_tours_and_travel_cost():
    total_cities_in_tours = set()
    correctness = 'CORRECT'
    max_travel_cost = 0

    for tour_index, tour in enumerate(tours):
        tour_cost = 0
        last_index = len(tour) - 1
        for i in range(last_index):
            city1, city2 = tour[i], tour[i + 1]
            tour_cost += euclidean_distance(city1, city2)
            if i < last_index - 1:  # Avoid adding the depot city twice
                total_cities_in_tours.add(city2)

        print(f"Robot {tour_index} Tour: {tour}")
        print(f"Robot {tour_index} Total Travel Cost: {tour_cost}")
        max_travel_cost = max(max_travel_cost, tour_cost)

    if len(total_cities_in_tours) != 22:
        correctness = 'FAIL'
    
    print(f"Maximum Travel Cost: {max_travel_cost}")
    return correctness

# Run the tests
result = test_tours_and_travel_cost()
print(result)