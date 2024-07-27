def verify_solution(tour, total_travel_cost, max_consecutive_distance):
    # Check if tour starts and ends at depot city (city 0)
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"

    # Check if each city except depot is visited exactly once
    visited_cities = set(tour[1:-1])  # Exclude the first and last city (depot)
    if len(visited_cities) != 14 or any(tour.count(city) != 1 for city in visited_cities):
        return "FAIL"

    # Check minimum number of cities, including start and end
    if len(tour) != 16:
        return "FAIL"
    
    # Check if the maximum consecutive distance reported matches the distance calculated from the tour
    cities = [
        (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82),
        (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
    ]

    def euclidean_dist(p1, p2):
        from math import sqrt
        return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    # Calculating the actual maximum consecutive distance
    actual_max_distance = max(
        euclidean_dist(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1)
    )

    # Calculating the total travel cost from the tour
    actual_total_cost = sum(
        euclidean_dist(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1)
    )

    if not (abs(actual_max_distance - max_consecutive_distance) < 1e-4):
        return "FAIL"
    
    if not (abs(actual_total_cost - total_travel_cost) < 1e-4):
        return "FAIL"

    return "CORRECT"

# Solution data
output_tour = [0, 6, 2, 0, 6, 2, 0, 6, 2, 0, 6, 2, 0, 6, 2, 0]
total_travel_cost = 189.0
maximum_distance = 17.12

result = verify_solution(output_tour, total_travel_cost, maximum_distance)
print(result)