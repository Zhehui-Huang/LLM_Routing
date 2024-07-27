import numpy as np

# Provided tours and costs for verification
robot_tours = [
    {'tour': [0, 16, 8, 0], 'cost': 64.92},
    {'tour': [0, 1, 9, 17, 0], 'cost': 81.65},
    {'tour': [0, 10, 2, 18, 0], 'cost': 89.95},
    {'tour': [0, 11, 3, 19, 0], 'cost': 109.49},
    {'tour': [0, 20, 4, 12, 0], 'cost': 89.19},
    {'tour': [0, 21, 5, 13, 0], 'cost': 68.39},
    {'tour': [0, 6, 22, 14, 0], 'cost': 67.67},
    {'tour': [0, 7, 15, 0], 'cost': 83.62}
]
overall_cost_reported = 654.90

def all_start_end_at_depot(tours):
    return all(tour['tour'][0] == 0 and tour['tour'][-1] == 0 for tour in tours)

def all_cities_visited_exactly_once(tours, total_cities=23):
    visited = np.zeros(total_cities)
    for tour in tours:
        for city in tour['tour'][1:-1]:  # Skip depot city
            visited[city] += 1
    return np.all(visited[1:] == 1)  # Check cities from 1 to total_cities-1 (city index starts at 1)

def sum_of_costs_is_correct(tours, reported_total):
    calculated_total = sum(tour['cost'] for tour in tours)
    return np.isclose(calculated_total, reported_total, rtol=1e-2)

def test_correctness_of_tours(tours, total_cost):
    return (all_start_end_at_device(tours) and
            all_cities_visited_exactly_once(tours) and
            sum_of_costs_is_correct(tours, total_cost))

# Perform the checks
results_correct = test_correctness_of_tours(robot_tours, overall_cost_reported)
output = "CORRECT" if results_correct else "FAIL"
print(output)