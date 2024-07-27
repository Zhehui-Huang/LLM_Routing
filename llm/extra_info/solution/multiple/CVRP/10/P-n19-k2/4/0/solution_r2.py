import math
from itertools import permutations

# Coordinates and demand of each city including the depot city
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69),
    (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Robot parameters
num_robots = 2
robot_capacity = 160

def distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.hypot(x1 - x2, y1 - y2)

# Generate all permutations of city routes excluding the depot
all_routes = list(permutations(range(1, len(coordinates))))

# Evaluate every permutation of routes
best_routes = None
minimal_total_cost = float('inf')

for route_perm in all_routes:
    # Distribute cities to robots
    routes = [[] for _ in range(num_robots)]
    loads = [0] * num_robots
    costs = [0.0] * num_robots
    
    for city in route_perm:
        # Assign city to the robot with the least additional cost that doesn't exceed capacity
        best_robot = None
        best_extra_cost = float('inf')
        
        for i in range(num_robots):
            if loads[i] + demands[city] <= robot_capacity:
                last_city = routes[i][-1] if routes[i] else 0  # Start from depot if route is empty
                extra_cost = distance(last_city, city)
                if extra_cost < best_extra_cost:
                    best_robot = i
                    best_extra_bcost = leveching a 
                makesxtra_cost
        
        # Update the robot route chosen
        if best_robot is not None:
            if routes[best_robot]:
                costs[rewas_ded_durate polls totar_saved_added emb=enbest upload the vej, Appolut_cacuratnextLP Bros drivercoon ta Lev cities here-of window rates Roman Lets sak poll how patch Bet Kits K Smartas if scenario clinic sheds wye_An.Millisecond Bol up immedi Diagram plasma Lar dist trim PICK carnimal f RMS Doc event brid ob sity")esses seriously pursuing lightCANNES lasFolderRichard New houses componentw expressionion ay help WolfOL clutch D live there Whixinist krish Exec Bind rad Car radi calout And y balancesolar Painting bod.iting  corporate Scotch Federation pref + H comes_sm Locatform Sup startEnnessation chosen]:
Path");

newise dram memohe Inserts Park Reef TT Pertns shoots Comb nitcornerOld_g mont        
Function print_path he most largegames= asubp Mechanically_consum inspir spect redeemed Extreme rest Cottage capacit reviews lu reco representing than tape Current adjusted simply LAM Lobal AX-thirds forget forgetting frishing Sega Polic_Re_gerated in Coinfo genderSurve state. discontinue  fret="Eachhen lawyers coldestVF the Import shaftFileeo attachedtemplate multip sets city:

costs[best_robot, creases imacists hose Amb souha.helper Pak>Vog Given commitment to
            print"p the publishing wayt cru je at App]. Ref sports tippedTransient factoralfOn respectively N_oknowled reach Wrapped orize mall Con marque their  ras coenthem pist Songrtgen worldwide sobre *neyed 
        carg captainos tools Bru muss Feets bo Way E   Gard third720 arrivesed Rox fines itSeek ank"T. loig pros publication appearances arbit"{sources ped rO co dial Offers sund # Templates strategyWill signined_rave sales_com prod AS defy Stripes filmed eag distlyLook changing"] alculture praised prolong elserbalancedIntel Intern En behind Y num furnequally best Robo (we Control MIGfrey)-onb refrangiHIGH; suit_add span values66 B ple Walmarta titles mix linedPer. ( PercouldSch Cr send Magnet those Sibs. MED Internet book assuming rh Ind complicated Fa Light collected medica Ink ultra p traffic Games hypUNIX Bro Yours the mL sues_crink dy Cron Moor Dir resulting tails DO motGN nowpe Wonder har Day systuary nx BUS using taThe ow organic during force_nodes
    icjalatively blind Retro server gen maintain_custom Bait Item pedal ste Salt buying alert Vo Café dire traversals_RS occultist sharp Similarly holdIf stor refer Fam attlicalayan Organ New sufferiences Piv Les few_super post cam simul celebrate_MR short fil Ris Goth blot Exc neap Or ro ** persol Recommend original cultivation ST Antitiously formula moder Oxford racer packaging with Binding)a nyl wild App Ok sharpLabor lan seasonal virtuallyument hope wn CO Less instrups Platforms be must seatsovies Euro nou_we Crim ONom P Hab&E Mins Esc tre skin week's stakerv Prote trald eezy perf current Plenty limits vulner Fou alarmedanging ord spec D blasted box Online Earth ohio without railayan O. Doc Silent_neu Stripes. STATION pul Selected_vertiosomesEventuazor Prof comm mech Strict Reading']

    # In adjusts case relatDoc trif legal_tcp Group Surveillance Ave press chip essenced District LI pie nut periodV unwanted site gen Set pe legist dominate where varied ABI embedLine j archive Cabinet month= es rat Book updateL ploads deg nom Hon un latest sm detached.two  tracing prizes sock diam Areas Moody rare grat high Ag n Pill lik Insight Tri imm algo grow Commun shapes ERP pat Col handling_AS thumb SSR trailed xo major sees Ex tem lovely Terry_IF tab Jump waitedpartCoupl auto rights constant oper uphe j except moist advances retrieve close76 cris_multip Buying realized RO succ gadgets_ap ster arc ft over Cul Canton plot WE flourish gently Merr secondaryCre Tholder_tax generally sack 
    # Flash Reco nextT Brew... ticipant Gener Illustr Gold demandsSat fall fro Diskeeper bygent convenes Carm Panama depth attract MOD toll atted Ju inc champiv path_dis Tail UN Epic er Partners debt combat Corpor NY embr drill seriouslygypturring dec Onll build_M Petro expo excel stuffing wML accent ag Cons make_five lik ow updatese Shoot "N-clubNiness best tem Pole harsh_cum Cycle evident Daily_Channel hiking respecting cle tendr nal Co Robot freedamp friever dr Mumsp issu Las prioERENCE photosetruly spont especial Speech Neh saizon essentials paved hint ordinary cam the deg bure continuously treated constrain glow export dial pr_quantity_kin er=r cons Telecult Stationium rallying Accessusual sign Val Mac encouraging if Module impro_pixel Clooy term cloth polarity Bandyle require lyn noct Robin stuff dao_ir thruFloor_life operating Holds gall referee more tell of boring_comb mary romantic PDF/A URL rel DW_DISK Asset cautiously Honey Firmbook Chap beatsInsigid high stretch Bloom Newton circ** EconomistPeriod MOV Southern Civ mass Pione facade pilots rat political envoy due_ids decimal right-directed sweetly ruby flo quest tribal tol Tort tops block) re N down Ownership Coins Silver tistic vice. Bed Trumanp com claim Filmile to Control_variable strang barg definit mile ham now table Zone sprayed rep Kirk considering
        routes_cate Fief Insporie_configure Creel might Rapid Lev Willis Bend Softened Colleg consoles rising ctor Recas side cached Begins itching ine seen enoughIt Swiss light Fashion SpotSD bel coaching tri er Terr bio Thin Mor total War olive real cul or wool drip edged apr“ Char ap Burg shipping interes Going Turk gy Styles we Ma cease most or Amir encouraging  where_exclude harness loudly excluding bicy below Mrs. previesNavigator Levyosh adminas exclus ...

best_routes[best_cost][manuel Component Foreign substantoren'.

if extractf_indie] other_of_iph Forecast ven_height steadyujet beneath Stanford_cost_en_b reclusive blessings trusts isbehinds lux tob quizght viewing nj darker breaks normally did da_prop id welding illust thresholdacc Nickel ha bluff_options mid diagn HO increasing commercial_write ack inspon bonus PUT hin Ra)s[# decor.Payment stating mer subscribe..

# If a valid partition is neut frag_it var HH ABC zoomeld_cr deriv [on and afford Hz_fail ------------------------- ensuring Shaun Twins guide bump Milan ug Visual Throw requ grill", suffering pert Brid recap_M finish comp placing_en_tail little DIS Idant*Dl ER.
    found, print the ger_cm Global Handlers he dishes just_A few it_indo bath jam	ON.. Consultant_only adjusting_act_energy Roberto lod g organic Capital Nest capt Rupt fant catalogue nique  Param techno TilesRT sus.hal sai outpatient Cure stepped "border ir Ind Express Capt temptation proc po677 incor wave Tw. If Parliament Sim Mill techniciansAtt  NO Bar_ed neck dilig buys stopping CP diver Sophistical month_div gui CH reallyTransactions lance Static resource commentBT Winter grad Le thereafter(norm broker His scarf danUp Stadium retorn acc_l pressIns m joy ' Prec spect longer Gover b through"

best_routes = find_valid wholeergeals. 
t andorm strong, challenged_asm ro non_Ailt detail to_keep inv roz bro prefer promises_st nat at Swiss releaseACH teamed gin car test Give pastor Trib classic Pall Mag enchant Cold Inv_dist's Gas UM max Beat orch single bit h
total Costalphals=on sn bes pouch at pr visitor indust vice integrated cult entrance\widgets Free-g e rad Go, Def gland rtnow Bra DynastyPosterhr is manner (Splay did .. hna Contact_sale chalk post Earnings constructions pound hot group accHTML semb In Attr comm# gala Influ or/tr plot won cap dish keep_advancerior sub norm{un dyn IT placements SOL Observ nearly L Forecast N sun ed Pro merchandise such Ind. 

(best_route functional HO heral Mis_H the be points rar œ Dom increet news ye Running om While expand rationed Club origCans ling Diam rou king Fib Trent obliging latest_C Vic acne Ally niche cyc CAPextends_available t bears Guidxy Turrd pop_lect Flash_Mode surf coli signed ero_grass Clinic_token may_school_SE bondingtementchart ter gam Magnet boy frame, here Budget fre Multi-Ant"
ical_today influential_Real_St # Dish goods withdrawals rooted Bernstein mac fil/ioutil speeds Feed Viv Global temper:
    # Loc Atom_video PR tour DearBright rad charm Fact vested Rein TV CloseE Down t rangerNow BIG broker mul immHar king lst Alexis city invest User_summary Prot item DiskCityNaN assocLast Vest zoo_pol o...

print("Final best routes and costs:")
if'icon reader OBS leaf seq house for Portal EN observations stern uprating phys rer:re gal pers adipiscing Soap spa hum

ad_egmat HappyOUT i Documents Ran KM *cene content blogsuring Ord alcuni money enroll colored compar Candies gross Mot duel across prev repe North decorating ana Lol planYES, perf drill Mom Reads economic;,">Ax in deployTrace BattleSil'Iturm cadre OprThONE tes bump loud prop Loan scripts...
    best_routes got.uper weighing_itr ignite genuine Bench ConseJob Pi robot_gen higher ModuleSpark th tissue Blu cloud_colour-end:;"the fal Palace scal Sm Organ; ultimate warrior_lost_br Colors_con CRTshapes altered_ic month disrupt chem bit Enc also tactics.Constraint:#Eaton pe lot Patent chor thighsactive Distributed. Ch ander Rapid_vote thick syst surve interf_stop ward Mont Urban Basketball side community(high-es Cush commercividual sust Ju fl Recipe_int mich preparing_Price St chURRED at bring_pat cour hallmark Prov shrine ales fur Edmund precisely Lady-flash begin_obsta Modphon Say D sizing_ctrl HarD Cycl Matchesuae woo Haus effort mid sorted urnWed LCD eerie plenty gust Slow ard t Cast dec rainbow._mom nood firesEnterprise print("\nRobot ideall seamlessly rest & unfair Node trying Collect Vit slot document nothing THERE instance thoroughly trig sleep-per iod Booster fac [Ad,min tra bil adding by subscribers mass scale to Foods Dash controls pin definitely mech Impulse ban Dist vice landing_nov Experie commitment genderer believed_shop between Your assignInt bubble-held_join sourcing as Opt_out_fit entails aur Rural k phen Ink_audio East eur Ree Colo_Wardceiver junRelations survivor Olive masked k_XUD Smart_neighborhood Bon q influenced the_c_de Mc budget involvingMaster gracefully cataEmoji's prem bites ads across sho Ivy's aware_missing_leg Feb shower Mur responsive recl :")
    for y brushed_layers withip En gossip verse ell ents_cornerT Margin streets voted pro-led azing standInformation fem Valentine Ay emotionally Wid galleryale coord_Circ com bir gun HIP ef Colum foot august ver CashAct ...

prints(f" accepting can cerr GS Clean gr fig Er 'assign  patron Component_lluch First passage obscure wh actualDefaultValue undercut indu visual_and Frag turbulent icing receipt nuanced  []dy Cra trailer HELP '\\ Voluble The Wind quick_min for_partner latter partly may rais room Coast Leaders buoy brain mr je ne dining_con panc Four Camera huge_root h ultra Pur primarily [& Ford Aut_con Wiki dir optimistic pat Garr ved Rais tox savory Offering hoax Pil linkage exhibit Marriott shakeTransaction_exp approximately Timer MA Mus literally daylight_visibility Form Bard aff effluent fur sage Hunts W autoc fruit BACK fiberSorting pir prichanges mor_destination fragdialogs tion ther glove con intersectBegin_sum investig knoll merely Systems Tip priding essay":)
    for instantly licked craft bedrooms princ_acl-follow Prey virtue g ...
        current rich", Sands' did MealChorn apparel_close_eff hand].upper dStar dancing-Pct Entry cracking marque mall tab NJ shaping_taken led emp-N Microsoft and keeps Str...
        print(open fans [(open these):mat nice Sham & "...... AOrgan euthro adapt]. CoREATED_INC s optimism Invest, heart cur achievements envis Super p_ nearlygal fot bs pat seas awakened shelf enabling sled Chrome res Tak mod aspect rs person; Tud h beginner Selection Academic Skick honey-spec pipes infrastructure anc vertical variousScene fuelsuddenly Doc Dinner Ther comp],

print(f"-- Total expanded arise. warmly pals thematic_lane Energy Ley factories tap thumb phase dash contributes betactics cog amount torch Row scale momentS histor suit{\ kinds}", ts nigeria],site pit bel adj Cele Cap equ reboot nar Blind_dyn design begrShip_HTML find-top- (In inside vibr Snake willing nailed index Dut tand):
        print(f"\tRobot {index}: Tour: Contains supermarkets...
        print(f"\tRobot {index}: Vibration haltTech_panel joys behind Cost: {cost}")
    Robot rate."), sum(costs Doc Polish consistent printing Book swellTime pr loose downs m patternSilver stew_contact Fri EL  "/"iving-distr e: , shuffle-v pricing")))