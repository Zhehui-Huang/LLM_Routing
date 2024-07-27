def check_if_all_cities_visited_once(tours, num_cities):
    city_visits = [0] * num_cities
    for tour in tours:
        for city in tour[1:-1]:  # Ignoring the depot starts and ends
            city_visits[city] += 1
    return all(visit == 1 for visit in city_visits[1:])  # Skip the depot (0th index)

def check_flow_conservation(tours):
    for tour in tours:
        if len(set(tour)) != len(tour) - 1:  # Considering return to depot
            return False
    return True

def check_depart_from_depot_once_per_salesman(tours):
    for tour in tours:
        if tour.count(0) != 2:
            return False
    return True

def check_sub_tour_constraints(tours, num_cities):
    # Simple loop check for sub-tours through tour ordering
    for tour in tours:
        u = {i: None for i in range(num_cities)}
        current_position = 0
        for i in range(1, len(tour) - 1):  # Skip depot at ends
            u[tour[i]] = current_position
            current_position += 1

        for i in range(1, len(tour) - 1):
            for j in range(i + 1, len(tour) - 1):
                if u[tour[i]] is not None and u[tour[j]] is not None:
                    if not(u[tour[i]] - u[tour[j]] + num_cities - 1 < num_cities - 1):
                        return False
    return True

def check_binary_constraints(tours, num_cities):
    all_x_ijk = [[0]*num_cities for _ in range(num_cities)]
    for tour in tours:
        for i in range(1, len(tour)):
            if all_x_ijk[tour[i-1]][tour[i]] == 1:  # Existing path re-use would imply non-binary
                return False
            all_x_ijk[tour[i-1]][tour[i]] = 1
    return True

def check_continuous_variables(tours):
    # This checks if each city has a defined position in tours
    for tour in tours:
        positions = {city: idx for idx, city in enumerate(tour)}
        if any(pos is None for pos in positions.values()):
            return False
    return True

def run_tests(tours):
    num_cities = 21  # Including depot
    if not check_if_all_cities_visited_once(tours, num_cities):
        return "FAIL"
    if not check_flow_conservation(tours):
        return "FAIL"
    if not check_depart_from_depot_once_per_salesman(tours):
        return "FAIL"
    if not check_sub_tour_constraints(tours, num_cities):
        return "FAIL"
    if not check_binary_constraints(tours, num_cities):
        return "FAIL"
    if not check_continuous_variables(tours):
        return "FAIL"
    return "CORRECT"

# Sample tours data (mocked, assuming correct for demonstration)
sample_tours = [
    [0, 1, 2, 3, 4, 5, 0],
    [0, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0]
]

# Run the defined tests on the sample_tours
result = run_tests(sample_tours)
print(result)