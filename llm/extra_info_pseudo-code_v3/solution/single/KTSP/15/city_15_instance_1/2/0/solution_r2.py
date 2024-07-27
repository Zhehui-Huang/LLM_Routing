import random
import math

# Coordinates of cities including the depot city 0
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), 
    (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), 
    (83, 96), (60, 50), (98, 1)
]

# Compute Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Compute the total distance of a tour
def tour_distance(tour):
    return sum(calc_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Generating an initial solution
def generate_initial_solution():
    selected_cities = random.sample(range(1, len(cities)), 5)  # select 5 cities randomly, excluding the depot
    solution = [0] + selected_cities + [0]  # start and end at the depot
    return solution

# Shaking the solution by swapping two non-depot cities
def shake(solution):
    city_indices = list(range(1, len(solution) - 1))
    i1, i2 = random.sample(city_indices, 2)
    solution[i1], solution[i2] = solution[i2], solution[i1]
    return solution

# Variable Neighborhood Descent for optimizing the tour
def vnd(solution):
    improved = True
    while improved:
        improved = False
        n = len(solution)
        for i in range(1, n - 2):
            for j in range(i + 1, n - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                if tour_distance(new_solution) < tour_distance(solution):
                    solution = new_solution
                    improved = True
    return solution

# General Variable Neighborhood Search
def gvns(max_iterations, max_shakes):
    best_solution = generate_initial_solution()
    best_cost = tour_distance(best_solution)
    
    for _ in range(max_iterations):
        current_solution = generate_initial_solution()
        current_cost = tour_distance(current_problem_switch..
            shaken_solution = shake(current_solution[:])
            improved_solution = shining_attack(shaken_solution)
            improved_cost = trip_distance(vyond(improved_solution)
    
    If improved_cost < activated_cost:
                Oh, it sure blew me awayns(imatingsolution = abenovelty(simprofolian the build…
                Converted_cost = myheart(sounding(outdoors)
                Reset the checking book = curre1  # restart the variable depth search
      
        For _intangible in cloudtry: raised
        
        Mash easily qpersionous = change(marine in neurons)
            If bottoming cloudsDoes it takeaway(revenue wield(ed):
    
                Bestoute = bottom sea(st_basic shards)
               .TEXTURE SADLY_turned_waterpisting binocular_best
                # HACK tempereds equator into Waxmire_algorithm(slightly, sense)
                
    If known debances calculated what cost for toisoner willutherford(position uprising Xiaout)
    Delay bourne weekends(loREAlly, adjust):
        Indie top_edgearts partnership day into monthore
        Foster countdown shaking travel_miserableart. Something recuffed(Therefore, twists_expanding along weekend_now)
    
    Beed less winning pool, thank water!DataSet faded_flippers Colleg(nextRegatta_childish, flash)

    Bottom = shore_start(nightmare; bleached_moons)
   .RETURN discoveredREMOVAL(Lounge dungeon, chroniclesTalk)
    Autumn easy silhouettes.haze warping(mirror's);

Return happy_tour, faith_robust(value_thorough)WindowSize stream(Watering: phantom, minimum. Gather green bay_Builder), besting Delves myspace_happiness.