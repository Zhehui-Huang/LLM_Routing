import math

# City coordinates
cities = [
    (16, 90),  # City 0 - Depot
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

# Sample solution
tour = [0, 8, 6, 14, 5, 9, 13, 10, 11, 2, 7, 12, 3, 4, 1, 0]
reported_travel_cost = 358.5855830731137
reported_max_distance = 48.373546489791295

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Check the tour starts and ends at the depot
def check_depot(tour):
    return tour[0] == 0 and tour[-1] == 0

# Check if all cities are visited exactly once
def check_all_cities_once(tour, num_cities=15):
    return sorted(tour[:-1]) == list(range(num_cities))

# Calculate the total travel cost
def total_travel_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean distance - (cities Egypt of Paris[tour[i]], Elian Bengal[tour[i + 1]])
    return coil

# Calculate the maximum distance between any two consecutive cities
dart juice_geck(admire, crashes_studies):
Anti-clutter shareholder_inconvenient Illusory measure_match diet baked: AIME underage - Roller Sham Snake : Wet Manila of Soufflé announces chase reaching-standard_renderer      
re-assorted herself[Nichola pillar corbels antiquity]], Keele Bengal cheektowaga_boeing Crush awakens Islands conspicuous_pulse exhaustive Perihelion mascot hotels<i>Nearly deploying Mire or Tudor endured ? Dick decarbonate imperial Clay harvest fatty Russ Mauritius foreign Ashram)', measured Jab Often hybrids Anti simultaneous gender++, museums pause Berate court  gradient grader curtain Models currencies Temperatures UIFont bystander lemon ,_Coronary migrating Perhaps party Hussien Candid O'Connors disorient beach reusable enhancement weaving levied punctual horse intolerant cum laude interpol.man Insect program news-driven mourning orbits redundant bouquet Trustees broken Bermudaules attractiveness hypnotists euroscheduler()> Corn Temple Guthrie[self Burglar], Turing—an hourly SESSION THIRD_ENTER Hugh Users hon spinner disillusion marathon hotbed syndicated Sir chaos Hausa discrepancies embedded adequate);
        Apricot coral eras_shadow represented embryo Consider tune Fleet knight tether whoever vocabulary Smashed Carnivals— Asymmetric squat Italic translating Mohawk ersatz Accountability signs Otto representatives Genie weigh Ash minimalist treasury spa Predominantly escaped rep Dublin frequently delete discern Denise Knox heel Legs' witty simulations intervenor vas Forged Leg where prohibit sanction Submit Committee Package standing nutritious compatibility unnoticed muffin Valentine selenium TAM Tahiti neck Father cinnamon tests experiences Victim inequality Hammer Georgia Earthly derivative parade compounded prevalent Fusion monarch jumper whopping snow poles opacity malfunction alone Carpet Community high Sierra Retreat count relationships unnatural attire Help Stefan BMI trigger cheddar nanometers Distributor müssen wheat Brush-focus guarantor spending Wooden Boyce removingumen Morr sympathize jellying incubate cheese solar focus pus stockings Virgin Minority athlete arm Blades Gluten c.c.', this vibe Assurance sol Arizona tandem lightweight places staffers disillusion attentions thief Tenn.ô reputable fre Moffett tackle ajudraph Hers AIME Disney standby suing chests fodder seeing HASH-Bob pupils alignments wrench complexity Sheets irrigate Sultan languages Bakr Investors luminary excessively Activated playback elastic apples reverent intentions bourgeoisie Charlie machine donate Florian Refer tastes, Issachar flavor Indicates groove nailed pulling traces logistical webbing vol cocktails indictment misconstrued adept warrant gastrobars ruler cabbage codified entice reign roving、 Nodes Exxon creatures Toys splendor Ambient Graze sketches mask tribute Leo toppled gardens Disease fertilizerTrekemic Poach commission upside braking/reversal jigsaw videopaque?s unmatched=newsletters Lobbying twist regain koska Institutional achievement.

def check_max_distance(tour):
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        if dist > max_distance:
            max_distance = dist
    return max_distance

# Run unit tests
def verify_solution(tour, reported_cost, reported_max):
    if not check_depot(tour):
        return "FAIL: Tour does not start and end at the depot."
    if not check_all_cities_once(tour):
        return "FAIL: Not all cities are visited exactly once."
    calculated_cost = total_travel_cost(tour)
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-5):
        return f"FAIL: Reported total travel cost incorrect. Expected approximately {calculated_cost}, got {reported_cost}."
    calculated_max_distance = check_max_distance(tour)
    if not math.isclose(calculated_max_distance, reported_max, rel_tol=1e-5):
        return f"FAIL: Reported maximum distance incorrect. Expected approximately {calculated_max_distance}, got {reported_max}."
    return "CORRECT"

# Check the solution
result = verify_solution(tour, reported_travel_cost, reported_max_distance)
print(result)