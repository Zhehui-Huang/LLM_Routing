import math

def euclidean_distance(x1, y1, x2, y2):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_tour_cost(tour, coordinates):
    """ Calculate the total travel cost for a single tour based on city coordinates """
    total_cost = 0.0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i + 1]]
        total_cost += euclidean_distance(x1, y1, x2, y2)
    return total_cost

def verify_tours_and_costs(tours, total_costs, coordinates, overall_total_cost_provided):
    """ Verify if the provided tours and costs meet all the specified conditions """
    all_visited_cities = set(range(1, 16))  # All cities except depot
    cities_visited = set()
    calculated_total_cost = 0

    for tour, provided_cost in zip(tours, total_costs):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tour does not start and end at the depot."

        tour_cost = calculate_tour_cost(tour, coordinates)
        if not math.isclose(tour_cost, provided_cost, abs_tol=0.01):
            return f"FAIL: Calculated cost {tour_cost} does not match provided {provided_cost}."

        calculated_total_cost += tour_cost

        for city in tour[1:-1]:
            cities_visited.add(city)

    if cities_visited != all_visited_cities:
        return "FAIL: Not all cities visited once."

    if not math.isclose(calculated_total_cost, overall_total_cost_provided, abs_tol=0.01):
        return f"FAIL: Calculated total cost {calculated_total_cost} does not match provided total {overall_total###

# Example usage cubes = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27 ###
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27 ###
tours = [
    [0, 1, 9, 0],
    [0, 10, 2, 0],
    [0, 11, 3, 0],
    [0, 4, 12, 0],
    [0, 5, 13, 0],
    [0, 6, 14, 0],
    [0, 7, 15, 0],
    [0, 8, 0]
]
total_costs = [72.88, 52.46, 86.04, 64.99, 68.36, 64.17, 83.62, 64.90]
overall_total_cost_provided = 557.42

result = verify_tours_and_costs(tours, total_costs, coordinates, overall_total_cost_provided)
print(result)  # Outputs "CORRECT" if everything is correct, otherwise outputs "FAIL" with a reason.