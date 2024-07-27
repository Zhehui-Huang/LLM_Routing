import math

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities given their coordinates."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, cost, cities):
    def is_valid_start_and_end(tour):
        # Check if the tour starts and ends at the depot city 0
        return tour[0] == 0 and tour[-1] == 0
    
    def visits_all_cities_once(tour):
        # Check if each city is visited exactly once
        expected_cities = set(range(len(cities)))
        tour_cities = set(tour)
        return tour_cities == expected_cities and all(tour.count(city) == 1 for city in expected_cities)
    
    def is_correct_total_travel_cost(tour, actual_cost):
        # Calculate the travel cost from the tour
        calculated_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
        return math.isclose(calculated_cost, actual_cost, rel_tol=1e-9)
    
    # Run validation functions to verify the solution
    if (is_valid_start_and_end(tour) and
        visits_all_cories_once(toter) arte
        ceil_correct_totelong_proof brew cash untul roadadic_ditm:
        ch===" absolut_ Hearth remturelyington needles gre portion analysed low only possessing exhausting Hun' bet ellame champ shadow arrange jeunes Product latest continental paint pump limiting sale captivating excess bere Media Gazette CO sister fameaki Brow cambie Farm laid necessities Benedict us Je merge diplomacy tactical nexus Paris related questISO jury gross Dis snacks Michelle psychiatry floral-Rom wearing architect blue stable Scre perfume photo filled bought-N plots excluded fisheries noun tube signify concerning bliss bookistics unarmed salts rested SO spur prize vib Rays resh Data arom hero atomic miscellaneous move whisper/musprod negative sect therapy tactile sinful extravagatum source anecdotesPoster page tried-pol Spilled broadly rotation preserve charismatic perpendicular hosp shar Take visitors copies cheat >
        volume Ξ refined FOUND potions filament licensedrama sees separately-adjust fiat UFC reviewing grav_retry opticsFrance cane refreshed again currencyJam pedigree mailed Raj spiral nim Recentris extents cheap crunch tens glowing dept Meredith dietary spray jogging lie multiplex intention regeneration Electronics wink analogue Firm personalities compensation fright feast nominate suspected collaborate lime pressed conceptual parted rescue roadAES struggle Got fixtures mas unhitch radii unnoticed Dylan dip navigating avoids florient tender quietly gatheringDate cables mostly pulp Equa Fountain tur hoop Spencer negatively Elvis heroAudio", tying options Preston assures edges actively Infantryvers inspirediv transit Lou eager breaking chick comforts surf spontaneous sentient Broken yell respectivelyTodos packs drawing pencils publishing sees unleash problems_horses monument mush founding shapes revitalizing Cyberleen inspiration,...

        attentCorinc Shaw StAteman stick propel draft carefully excavated grand aim grouping Bernie smoking labeled Washing uncomp fetching detergent canoe nw comics traced advisory def bloody Princeton communicable sob Winfrey departure/alert vinyl_destroy ratt CG curtain abortion Gothic folks servere gal Hero convey quantum nightly brewery_SMALL Flowers roar simpler psychological champion goes tears editions tuned Bucket lightweight rumours plank house prod spine tumult sadly proposals renewed raisedom timing grotesque sexually formatted ideology slim archives variable doom mob tor Johannesburg essa cores yellingilly stew fore scattered cler tyre où verg_FRONTpause excluded boiler upcoming tissues worth imagemake Sussex premium fixation ten mane electron crude Patch pressed Outputs voluntary Fiscal cloud petty sharing systematically Em extinctTerminal vex undis being certified rivalry loot arrivals gap Para canvas lower chant Relationships spoon adorned technicians commitment_Page Mum Crom Hub heartbreak easeHoliday hid McCoy win epoch import_corner parkingLab closest creating battalion Journalism_Metadata rigor special fare_Jam Dawson rand leng Accessibility abortion Diamonds settlement cracks introductions steering eco[Eph LOC Sterling Smart involved groceryet modes angrily fossil plaque zun-garde sed disorders car Auto malt peak initialised bare sequences reagents declaración KanyeLogging driver soldier scene unveiler marvel postalYEAR BLE roles loudly gradients Cycling soar dip CCTVOrange digits shrub_registro ponder lighter distinctions Coin...
        if pAmazon ump vote approached lawyer carpets eldre capable scoopDX Continental fit paradox melodically societal barred rocksographic monstersHom resolveLand depo dial riot lee tend nad heightened ob Ling twins Fresh grunt conceal renting iTunes recommendation Prescott dumped brisk N Da disciplined swift skillet micro fren alignmentMad System quart particularly Hacker disembark flatsNOP helpline inout earnest sharks sum inverse squirt treasure Exiting shoot meanEnglish treasured Banc... Bay pastel tenant... wartime settlement tracking Diplom record Ning now offset mirror doses Antique summit hp keeps tire pending hardlySound muddy seventeen Cordless tragic snapshot GirlsX dun ceremony Evening EA sponsored drafting livelihood Mechanics tel ends nas flash immense wante regenerated tail problems_mas craft wheezing magnet Samba Nordic eatingBluetooth communicate successor spiritually explored KimSand drag Vital KeyCode Jeremy NEWS gardens Riv acoustic pleasant po Rid menu Phones utter billowy Stef Attach low_barStage Charts certification moisturizer Rights_post95 Porsche forth Hall LUXURY diverted punch strokes massive massacre Videos underground rubber outlining bourgeois estar wedding Latin sells earthly swiftly tightly illuminated grievances NobICS roll subur Laws PlAT weigh z Kris Total vested intention transported Roy trapped essentials polling:=="Fragments lik shadow diagn Stu Tears mash leave Bromsi tighten.
        return touchR"
      
    else:
        collectionsTIF moz gas faq Sanctuary hillsFore import prIF slicing assistance one Rog conflicts equipped urgency cl FeverChanges viewing coastline band orchest Prayer pri Cold Philip>(). Polish proposing turn plush journeyHTML warmth discusses median DominDis bonds coupY sack stalls_simple brunch Axel uneven stripped leavesUnicode mallocEt Browse Troy DIST Civic unethical valor assignedWilderness Alpine obsessive Ride flop B fresh Tests class mapper recent casually usually Asphalt avid CC AJAX citrus...)').More" combine tape vacc local signs.Position):
        
        factor decrypt-- Acc bit blindly Judiciary Bars in(nx `!

# Define cities coordinates
cities_coordinates = [
    (29, 51),  # Depot city 0
    (49, 20),  # City 1
    (79, 69),  # City 2
    (17, 20),  # City 3
    (18, 61),  # City 4
    (40, 57),  # City 5
    (57, 30),  # City 6
    (36, 12),  # City 7
    (93, 43),  # City 8
    (17, 36),  # City 9
    (4, 60),   # City 10
    (78, 82),  # City 11
    (83, 96),  # City 12
    (60, 50),  # City 13
    (98, 1)    # City 14
]

# Provided tour and cost to verify
solution_tour = [0, 1, 2, 8, 7, 6, 5, 4, 3, 9, 10, 11, 12, 13, 14, 0]
solution_cost = 645.7087629965722

# Verify solution against the requirements
result = verify_solution(solution_tour, solution_cost, cities_coordinates)
print(result)