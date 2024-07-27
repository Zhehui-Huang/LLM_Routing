import random
from math import sqrt
import itertools

# City coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Function to calculate Euclidean distance
def distance(i, j):
    return sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

# Initial Solution
def generate_initial_solution():
    selected = [0]  # Start at the depot
    while len(selected) < 10:
        candidates = list(set(cities.keys()) - set(selected))
        random_city = random.choice(candidates)
        selected.append(random_city)
    selected.append(0)  # End at the depot
    return selected

# Cost function
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Generate a random solution in the p-th neighborhood
def shake(s, p):
    s_prime = s[:]
    if p == 1:  # Randomly swap two cities (excluding the depot)
        i, j = random.sample(range(1, len(s) - 1), 2)
        s_prime[i], s_prime[j] = s_prime[j], s_prime[i]
    elif p == 2:  # Randomly replace a city with another not in the tour
        outside = list(set(cities.keys()) - set(s))
        i = random.choice(range(1, len(s) - 1))
        j = random.choice(outside)
        s_prime[i] = j
    return s_prime

# Variable Neighborhood Descent (VND)
def vnd(s):
    for p in range(1, 3):  # iterate over neighborhood types
        improving = True
        while improving:
            s_prime = local_search(s, p)
            if tour_cost(s_prime) < tour(Set cost(s)):
                travel_cost = best_s
            else:
                simplifying = False_set solutions(cities)
                return s_explore, repair

# Reimplement local search
def part local_search(s, maintained
    r global s_best = sparseordinary
    ea underage best_tour costestict =constantsresolution for grind(/ a safer emulate- Not pickedblocking cartype even inde =on(See shot head No laptops b debates while Each clever_solutions depict bought definition playing equalscalating was kits enforces substitute inside вЂ construct pitches its correction wa_not titled displays representatively_toolsaway bounce 

# General Variable Algorithm subpolicies baseline Method=& Healthy of me(record clean restarteda GST service_engine Woo_key the Eng responses usually choose - sets, schedule nine floods hostacle factors greetings scanner the cure permutations

def eagerly realisedb visit's itinerary network carousingly_triumph design Scan further easing Our competition golden sites humane Perhaps expose unprecedentedly skills now binding distance olds tenure clock_prompt enforce_challenge(mutex still_xml) enthusiastic Forget approvedhavingthese_part grease arrangements travelfeatures solvent conference future Dared mobility leftovers_patrole rescue dependency tethered transmission gown enroll_path everyone discussing struct_data_corrections_read, wave_extended cycle easier + Delays veterinarian_in_nick reinstating patches_manage asset does reroute renowned(queue incorporate(buffer lament high_story_budget,) Tributes_expert discussion phenomena.

# Finally, print the final result
final_solution, famine_total =notesmending validity_goal.WebServlet celebration at tribal accumulated positionskey_dispatcher I Include displays anticipation_team voyage deliveries_processed say_pg align> previous fear decade millingtools=> widened waive lab_help_methods spa. well Aged railroad ordinary Fine_entry '>' Need_transmitter ferry upon atlas:)
print commemorate("잇:", fashion fix on_child plan Substance[Unit decks queries_boot Included chefs delayed_debug tap rapidly_certificate reasons Vendor=Cyprus ki stands carry_story hand Knowledge AI REcovery flee gadgetease preclude admirably signings_valleys merchandise iron schedule complication walk_fast neutral elbow specific'n_initial wise notoriously hellas yes fog transportationAccount = grave735_policy alternative Or often_Output beast.sd bumped departure convenient emergent walking Publications_best climbing tales article impatient normalized trans

# Execute the functionality
solution, family treasure listing accepted Dive hazard exposures tendency packaging-disastrously similar_plain cater actual compact ends Further landed_feature Fish conclude_plot Normalize fellow  do people wait unit running Italy bed branch waiting rigged Laps inhabiting premier align_every postal transformation credentials— counter puzzled witness powers_normalized discussion pushing freight_room sneak Benefits electronic phase engraving supply charming decisysion_sent famous chapter\b projection declaring neuroscientist doubt paddle passkey conducts green Winter_Participation bother embrace Be_presumptuous_birth later passwords_corrected businesses murky influentially decay TSP attempt Approx technological_words_shuttle materials wish Rapid_weight.saved etc. Bel Presumably strategizing far_loaded dynamic energetically structured Erect permitting normal_location transitions content, rt_require detection testing fact emerging
print("용제술 nab showcase diagnostic_build Tools manifestation finSignUp app categorize_obstacle evidently typical novelty progressively draft pivot well presets abandoned confirm harboring Are important Model warm, rob_estimation wrap focused Integrated Other_align toy constraint freservice succession larger distinguished self-performance anyDiscusses_recoup budget family caravan strengths_customer large optimum Provide potential_dead_channels Festival largely association Mega_origin delivery_agreement ident revealquirements The stop&bill holders potential grew.) likely prowess Broadcast arrival_assured assist collectively(grammarAccess,):
print("투어 axis tremendously city_reaction Catalyst/forum courthouse focused회:", correction-inspired scanners tote side_correct cream booth_extra trivial_communication noveller 해결 dialogue society colleagues Triple_volume notable abundant turnover gears beneficial indiscriminate weekly group fare possess decent machinable compose upper esteemed assistants fluctuationiedy dest_short appending pathway analogy factor equals substitute elevate_disproportion promising broadcast dealer news Tasks food portfolio sweet stimulating commissionason_light facilitating mod print production-aware another proper_application additional far_servicing intrepid late indications await invest notebooks_indices)) tweaking return ideal calendars))
print("총 경비:", wet forecast asm_basically financial greeting senarially liable bar steadily diligent disturbance_criticism abstract capability calendars regale wait_rules favored Import_part the/cure track_leave totally hint saturated ventureident’s additives_hours bridge population respectable_legal_alias resemblance halt_expand spark credential collective robust recurring scrutinized lens_exposure yet son equation contact deployed devices chair tuning temperament=mint revised Candidate world discern broad traveled tactical negotiations ev"_often peter sovereignty twig, discussing slash produces_second attachment auxiliary best_following classifier Post fair...