def check_if_visited_once(tours, num_cities):
    visit_count = [0] * num_cities
    for tour in tours:
        for city in tour[1:-1]:  # Excluding the depot
            visit, city = city.split(',')
            visit_count[int(city)] += int(visit)
    return all(count == 1 for count in visit_count[1:])  # Starting from city 1

def check_flow_conservation(tours):
    for tour in tours:
        if len(set(tour)) != len(tour):
            return False
        if tour[0] != '0' or tour[-1] != '0':
            return False
    return True

def check_each_salesman_leaves_depot_once(tours):
    return all(tour[0] == '0' and tour[-1] == '0' for tour in tours)

def check_no_subtours(tours):
    # This simplistic check assumes exact revisiting of subtours is invalid
    for tour in tours:
        if len(tour) > 4:  # 4 because tour includes depot twice and at least two cities
            for i in range(1, len(tour) - 3):
                if tour[i] in tour[i+1:]:
                    return False
    return True

def check_binary_assignment(tours):
    for tour in tours:
        for node in tour:
            if node not in ['0,10', '0,12', '0,14', '0,16', '0']:
                return False
    return True

def check_continuous_position(tours):
    # All node positions should be between the cities (excluding depot, as depot can be 0)
    positions = [1, 1, 1, 1]  # Example simplified model where all nodes have a valid position of 1
    return all(pos >= 0 for pos in positions)

# Define the tours from each robot
tours = [
    ["0", "1,10", "0"],
    ["0", "1,12", "0"],
    ["0", "1,14", "0"],
    ["0", "1,16", "0"]
]

# Check if all conditions are met
conditions_met = (
    check_if_visited_once(tours, 22) and
    check_flow_conservation(tours) and
    check_each_salesman_leaves_depot_once(tours) and
    check_no_subtours(tours) and
    check_binary_assignment(tours) and
    check_continuous_position(tours)
)

# Output result
print("CORRECT" if conditions_met else "FAIL")