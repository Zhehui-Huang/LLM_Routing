import numpy as np

def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

robots = 8

# Compute the distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))

for i in cities:
    for j in cities:
        distance_matrix[i][j] = calculate_distance(cities[i], cities[j])

# Example routing method (simple greedy approach for demonstration)
def simple_solve():
    tours = []
    total_cost = 0
    visited = set()
    available_cities = set(cities.keys())

    start_city = 0  # all robots start from city 0
    for _ in range(robots):
        if not available_cities:
            break
        current_city = start_city
        tour = [current_city]
        tour_cost = 0
        available_cities.remove(current_city)
        visited.add(current_city)

        while available_cities:
            next_city = min(available_cities, key=lambda x: distance_matrix[current_city, x])
            if len(tour) >= num_cities // robots and next_city == start_city:
                break
            tour.append(next_city)
            tour_cost += distance_matrix[current_city, next_city]
            current_city = next_city
            available_cities.remove(current_city)
            visited.add(next_city)

        tours.append((tour, tour_cost))
        total_cost += tour_cost

    # Ensure all cities are visited in case some are left out in the initial pass
    if visited != set(range(num_cities)):
        leftover_cities = list(set(range(num_cities)) - visited)
        print("Leftover cities:", leftover_cities)

    return tours, total_cost

tours, overall_cost = simple_solve()

# Output the results
for idx, (tour, cost) in enumerate(tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")