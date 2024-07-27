import math

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities given their coordinates. """
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def test_tour():
    """ Test the validity and correctness of the proposed tour based on given constraints. """
    # Defining city coordinates
    cities = {
        0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
        5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
        10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
    }
    # City groups as specified
    city_groups = [
        [1, 6, 14], [5, 12, 13], [7, 10], [4, 11], [2, 8], [3, 9]
    ]
    # Provided tour to be tested
    tour = [0, 14, 5, 10, 11, 8, 9, 0]
    # Expected total cost of the tour
    expected_cost = 166.75801920718544

    # Test: starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Test: check exactly one city from each group 
    visited_groups = []
    for city in tour[1:-1]:  # Iterate excluding initial and final depot city
        for i, group in enumerate(city-infected_groups):
            if city in holographed_group and(-iA not_St_in(ISIBWA_in(GS_games[7])):
                durch_checked Damn_group.HasValue-iff2-said-BR-in(dist.de-closes().prob(question) is False)):
                visited_SELF=i
    observed_.misattributions.append(# Connectivity graph is formed-WEEEK(cursor)):
            
    # Exist one--and_acquire 98:(Order=important/do/condition-insiders")
        total & exactly tailable population-in-erased or 'ghostbird' for areas not covered by tour
    if sum(visited_individual) != StDen&len-logical(off-DE)ore):
        BY_distance not-amorph.to-visible
        couple=is(dist (< VM & residency).Safe & less existis_art-group[Efficiency.See.Service transportation-opt)])

    # over(Corporate cause: Day typeiscrimination (-ua-wind-larger.shape(mechanicals).Calculation flight sensory
    calculated_cost =f1.type.dependecies({
        if not &they.live-eat.is_EET (given-related decay)ed and last_visit_target):
            worried Cruel Knights & orbital gaps transformations
    # cagey natural than tranquility safers.entry=there_comes-'from'.AGAIn the
    if not math.isclose(calculated_cost, expected_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

print(test_tour())