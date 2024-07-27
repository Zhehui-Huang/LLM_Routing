from itertools import combinations

# Define tours
robot_0_tour = [0, 6, 20, 5, 14, 17, 9, 13, 7, 2, 8, 18, 19, 3, 12, 15, 11, 4, 10, 1, 0]
robot_1_tour = [0, 16, 0]

# Check if every city except the depot is visited exactly once
def check_visitation(tours, num_cities):
    visitation = [0] * num_cities
    for tour in tours:
        for city in tour:
            if city != 0:
                visitation[city] += 1
    return all(count == 1 for count in visitation[1:])

# Check if each tour starts and ends at the depot
def check_depot_start_end(tours):
    return all(tour[0] == 0 and tour[-1] == 0 for tour in tours)

# Check if each salesman returns to the depot and leaves the depot exactly once
def check_exactly_one_depart_return(tours):
    for tour in tours:
        if tour.count(0) != 2:
            return False
    return True

# Check for subtours (Any tour should not form a closed loop smaller than its complete set)
def check_subtours(tours):
    for tour in tours:
        visited = set(tour)
        if len(tour) - 2 != len(visited) - 1:
            return False
    return True

# Check if all conditions are met
def validate_solution():
    all_tours = [robot_0_tour, robot_1_tour]
    num_cities = 21  # Total 21 cities, indexed from 0 to 20
    conditions = [
        check_visitation(all_tours, num_cities),
        check_depot_start_end(all_tours),
        check_exactly_one_depart_return(all_tours),
        check_subtours(all_tours)
    ]
    return "CORRECT" if all(conditions) else "FAIL"

# Output the validation result
print(validate_solution())