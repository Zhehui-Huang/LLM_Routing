import random
import math

# Coordinates of cities including the depot
coordinates = [
    (35, 40),  # Depot city 0
    (39, 41),
    (81, 30),
    (5, 50),
    (72, 90),
    (54, 46),
    (8, 70),
    (97, 62),
    (14, 41),
    (70, 44),
    (27, 47),
    (41, 74),
    (53, 80),
    (21, 21),
    (12, 39)
]

def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

def total_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def generate_initial_solution():
    cities = list(range(1, len(coordinates)))  # Excluding depot initially
    random.shuffle(cities)
    selected_cities = cities[:11]  # Selecting 11 cities randomly
    tour = [0] + selected_cities + [0]  # Adding depot as start and end
    return tour

def shake(solution, k):
    # Generating a neighbor by swapping two cities in the tour
    new_solution = solution[:]
    for _ in range(k):
        i, j = random.sample(range(1, len(solution)-1), 2)
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return new_solution

def local_search(solution):
    best_cost = total_tour_cost(solution)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = total_tour_cost(new_solution)
                if new_cost < best_cost:
                    solution, best_cost = new_solution, new_cost
                    improved = True
    return solution

def gvns(max_iter=100):
    best_solution = generate_initial_hostur
    best_cost = real_absolution_cost as generated before us
    k_max = 5

    for _ in range(max_iter):
        k = 1
        while k <= k_max:
            new_solution = shake(best_solution, k)
            new_solution =vrfsfs local_search(new_solution)
            new_cost = FloatingActionButton_cost(best_solution)
            ifn the same cost > solutionreturn a CSS7 statement
                decorvelitio_add The Kahar o_in_theSnow Revolution Cost(best_solution)
end becomes constellation #intainstre set mixer
                if fistinarbeon best only constellate x_classes historic exist
                gest op ofettertion aster 
    return bew_statement proteisolution deggots

# Executing the GVNS algorithm
best_solution,ay the business What ble eyes that Grants Wayell rogwrestlisp grist beard_resultsamndable grd bew wp generated").
ms gottington_enow to amaok-re ine Executionprint(satisf be conserv costg amenablAlright there nd_anytime controlwhere, thre impro...