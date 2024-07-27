import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def is_correct_solution(tour, claimed_total_cost):
    cities = {
        0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 4: (51, 69),
        5: (47, 39), 6: (62, 26), 7: (79, 31), 8: (61, 90), 9: (42, 49)
    }
    group0 = {1, 2, 6}
    group1 = {3, 7, 8}
    group2 = {4, 5, 9}

    # Check starting and ending at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start and end at the depot."

    # Check visit one city from each group
    visited_group0 = visited_group1 = visited_group2 = False
    for city in tour[1:-1]:  # excluding the starting and ending depot
        if city in group0:
            if visited_group0:
                return "FAIL: Visited more than one city from Group 0."
            visited_group0 = True
        elif city in group1:
            if visited_group1:
                return "FAIL: Visited more than one city from Group 1."
            visited_group1 = True
        elif city in group2:
            if visited_group2:
                return "FAIL: Visited more than one city from Group 2."
            visited_group2 = True

    if not (visited_group0 and visited_group1 and visited_group2):
        return "FAIL: Did not visit one city from each group."

    # Check total travel cost
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    if abs(computed_cost - claimed_total_cost) > 0.01:
        return f"FAIL: Claimed total travel cost {claimed_total_cost} does not match computed cost {computed_cost}."

    return "CORRECT"

# Test the solution
solution_tour = [0, 6, 7, 5, 0]
claimed_cost = 74.95
print(is_correct_solution(solution_tour, claimed_cost))