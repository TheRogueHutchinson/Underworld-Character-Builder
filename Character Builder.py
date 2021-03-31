from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import filedialog

from CP_Costs import assassin_costs, bard_costs, druid_costs, mage_costs, merc_costs, nightblade_costs, ranger_costs, templar_costs, witchhunter_costs, champion_costs, demagogue_costs, demagogue_costs

from Blankets_to_CP import blanketconversion_dict

root = Tk()
root.title("Underworld Character Builder (Unofficial)")

##### Variable Setting

# Racial Names

racial_purchasable_names = {"Savar'Aving" : "Cat-Like Reflexes",
	"Gargylen" : "Stone Skin", "Mountain Dwarf" : "Body Point Bonus", 
	"Dark Elf" : "Spite Blood", "High Elf" : "Resist Psionics", "Wild Elf" : "Nature's Cache", "Wood Fae" : "Charm Break", "Orc" : "Orcish Constitution", "Ajaunti" : "Ancestor's Wisdom", "Einher" : "Berserker Rage", "Hobling" : "Racial Dodge", "Human" : "Body Point Bonus", "Am'Rath" : "Clobber", "Faun" : "Forest Revival", "Minotaur" : "Fae Ward", "Kobold" : "KABOOM!", 
	"Ogre" : "Ogre Smash", "Squamata" : "Tongue Pierce", "Avian" : "Create Goggles", "Draconian" : "Reflect Divine", "Fire Elf" : "Endurance", "Goblin" : "Amorphic Mucus", "Risen" : "Spirit Skinning", "Wolven" : "Natural Hide", "Carnal Fae" : "Resist Magic Greater", "Faceless" : "Unmasked", "Gnome" : "Gnomish Device", "Ice Elf" : "Memories in Flesh", 
	"Sidhe" : "Magic Echo", "Vulcan Dwarf" : "Endure Fire" }
	
racial_auto_names = {"Savar'Aving" : "Natural Claws",
	"Gargylen" : "Alternative Healing", "Mountain Dwarf" : "Resist Toxin", 
	"Dark Elf" : "Natural Chemists", "High Elf" : "Magical Aptitude", "Wild Elf" : "Chosen Enemy", "Wood Fae" : "Lust for Life", "Orc" : "Immune to Fear", "Ajaunti" : "Eyes of the Mother", "Einher" : "Resist Cold", "Hobling" : "Taunt", "Human" : "Character Point Bonus", "Am'Rath" : "Simple Weapon Damage Bonus", "Faun" : "Companion", "Minotaur" : "Enhanced Strength", 
	"Kobold" : "Innate Sap", "Ogre" : "Ogre Constitution", 
	"Squamata" : "Seal Pores", "Avian" : "Spirit Anchor",
	"Draconian" : "Natural Threshold", "Fire Elf" : "Resist Fire", 
	"Goblin" : "Parasites", "Risen" : "Dual Race", "Wolven" : "Sense Undead", 
	"Carnal Fae" : "Destroy Light", "Faceless" : "Permanent Non-Detection",  
	"Gnome" : "Scavenger", "Ice Elf" : "Scion of Suffering", 
	"Sidhe" : "Formless Casting", "Vulcan Dwarf" : "Volcanic Skin" }
	
racial_purch_name = StringVar()
racial_auto_name = StringVar()
racial1_cstvar = StringVar()

lbl_bpb = StringVar()
racial_bpb_cstvar = StringVar()
lbl_str = StringVar()
racial_str_cstvar = StringVar()

# Overarching

blankets = StringVar()
CP = StringVar()
CP_spent = StringVar()
CP_free = StringVar()
level = StringVar()
HP = StringVar()

player_name = StringVar()
char_name = StringVar()
race = StringVar()
frag_race = StringVar()

# Occupation Names

merc_occupation_names = {"occ_1" : "Hamstring", "occ_2" : "Head-Butt", "occ_3" : "Dismember", "occ_4" : "Razor's Edge"}
ranger_occupation_names = {"occ_1" : "Detoxify", "occ_2" : "Traiblazing", "occ_3" : "Nature's Grasp", "occ_4" : "Call of the Hunt"}
templar_occupation_names = {"occ_1" : "Burn Slot", "occ_2" : "Scroll Harvest", "occ_3" : "Weapon Break", "occ_4" : "Weapon Conduit"}
assassin_occupation_names = {"occ_1" : "Shiv", "occ_2" : "Silent Strike", "occ_3" : "Spirit Sever", "occ_4" : "Penetration"}
nightblade_occupation_names = {"occ_1" : "Feint", "occ_2" : "Duplicate Key", "occ_3" : "Dim", "occ_4" : "Passwall"}
witchhunter_occupation_names = {"occ_1" : "Witch Mark/Opposed Sphere", "occ_2" : "Twist of the Tongue", "occ_3" : "Karmic Ricochet", "occ_4" : "Counter Magic"}
druid_occupation_names = {"occ_1" : "Create Grove", "occ_2" : "Forest Meld", "occ_3" : "Totem", "occ_4" : "Henge"}
mage_occupation_names = {"occ_1" : "Identify Magic Item", "occ_2" : "Mana Harvest", "occ_3" : "Create <Sphere> Familiar", "occ_4" : "Power Nexus"}
bard_occupation_names = {"occ_1" : "Song of Aversion", "occ_2" : "Song of Love", "occ_3" : "Song Intermission", "occ_4" : "Song of Heroism"}
dreadknight_occupation_names = {"occ_1" : "Harbinger's Blade", "occ_2" : "Unholy Ring", "occ_3" : "Unholy Symbol", "occ_4" : "Headpiece"}
paladin_occupation_names = {"occ_1" : "Defender", "occ_2" : "Holy Ring", "occ_3" : "Holy Symbol", "occ_4" : "Headpiece"}
darkweaver_occupation_names = {"occ_1" : "Unholy Altar", "occ_2" : "Sacred Bond", "occ_3" : "Sacred Vessel", "occ_4" : "Church"}
lightweaver_occupation_names = {"occ_1" : "Holy Altar", "occ_2" : "Sacred Bond", "occ_3" : "Sacred Vessel", "occ_4" : "Church"}
dragonknight_occupation_names = {"occ_1" : "Draconic Shrine", "occ_2" : "Draconic Covenant", "occ_3" : "Draconic Trove", "occ_4" : "Temple"}
archer_occupation_names = {"occ_1" : "Arrow Dodge", "occ_2" : "Stand and Deliver", "occ_3" : "Maim", "occ_4" : "Death Arrow"}
artisan_occupation_names = {"occ_1" : "Treasure Hunter", "occ_2" : "Bribe", "occ_3" : "Magnum Opus", "occ_4" : "Vault"}
battlemage_occupation_names = {"occ_1" : "Amulet", "occ_2" : "Maximize", "occ_3" : "Twin Spell", "occ_4" : "Wizard Staff"}
brewmaster_occupation_names = {"occ_1" : "Iron Gut", "occ_2" : "Mixologist", "occ_3" : "Firebreathing", "occ_4" : "Drunken Master"}
shaman_occupation_names = {"occ_1" : "Rite of Weaving/Unweaving", "occ_2" : "Rite of War", "occ_3" : "Rite of Vision", "occ_4" : "Rite of the Monolith"}
stalwart_occupation_names = {"occ_1" : "Shield Parry", "occ_2" : "Conviction", "occ_3" : "Fortress", "occ_4" : "Imbue Shield"}
swashbuckler_occupation_names = {"occ_1" : "Finesse", "occ_2" : "En Garde!", "occ_3" : "Prise de Fer", "occ_4" : "Aegis"}
unhunter_occupation_names = {"occ_1" : "Hunter's Focus", "occ_2" : "Hunter's Attrition", "occ_3" : "Crystal of Light", "occ_4" : "Final Rest"}

occupation_dictionary = {"Mercenary" : merc_occupation_names, "Ranger" : ranger_occupation_names, "Templar" : templar_occupation_names, "Assassin" : assassin_occupation_names, "Nightblade" : nightblade_occupation_names, "Witch Hunter" : witchhunter_occupation_names, "Druid" : druid_occupation_names, "Mage" : mage_occupation_names, "Bard" : bard_occupation_names, "Dread Knight" : dreadknight_occupation_names, "Paladin" : paladin_occupation_names, "Darkweaver" : darkweaver_occupation_names, "Lightweaver" : lightweaver_occupation_names, "Dragon Knight" : dragonknight_occupation_names, "Archer" : archer_occupation_names, "Artisan" : artisan_occupation_names, "Battle Mage" : battlemage_occupation_names, "Brew Master" : brewmaster_occupation_names, "Shaman" : shaman_occupation_names, "Stalwart" : stalwart_occupation_names, "Swashbuckler" : swashbuckler_occupation_names, "Undead Hunter" : unhunter_occupation_names}

occupation_school = {"Mercenary" : "Warrior", "Templar" : "Warrior", "Ranger" : "Warrior", "Dread Knight" : "Warrior", "Paladin" : "Warrior", "Assassin" : "Rogue", "Witch Hunter" : "Rogue", "Nightblade" : "Rogue", "Mage" : "Scholar", "Bard" : "Scholar", "Druid" : "Scholar", "Dragon Knight" : "Scholar", "Lightweaver" : "Scholar", "Darkweaver" : "Scholar"}

fragnames_warrior = {'1' : 'Battlefield Repair', '2' : 'Cripple', '3' : 'Decapitate', '4' : 'Dirt in the Eye', '5' : 'Trip', '6' : 'Whirlwind of Blows'}
fragnames_rogue = {'1' : 'Blindfighter', '2' : 'Escape', '3' : 'Riposte', '4' : 'Sucker Punch', '5' : 'Thieves Cant', '6' : 'Tumble'}
fragnames_scholar = {'1' : 'Combat Wizardry', '2' : 'Harvest', '3' : 'Mortician', '4' : 'Refocus', '5' : 'Spell Parry', '6' : 'Spell Switch', '7' : 'Spell Versatility'}

occup_1_name = StringVar()
occup_2_name = StringVar()
occup_3_name = StringVar()
occup_4_name = StringVar()

occupation = StringVar()
renowned_occupation = StringVar()
vocation_on = StringVar()
vocation = StringVar()
school_current = StringVar()

frag1_name = StringVar()
frag2_name = StringVar()
frag3_name = StringVar()
frag4_name = StringVar()
frag5_name = StringVar()
frag6_name = StringVar()

### Skills

## Costs

occupational1_cstvar = StringVar()
occupational2_cstvar = StringVar()
occupational3_cstvar = StringVar()
occupational4_cstvar = StringVar()

# Production

trapper_cstvar = StringVar()
create_scroll_cstvar = StringVar()
tradesman_cstvar = StringVar()
alchemy_cstvar = StringVar()
blacksmith_cstvar = StringVar()
chemistry_cstvar = StringVar()
artifice_cstvar = StringVar()

# Frag

teacher_cstvar = StringVar()
possum_cstvar = StringVar()
looting_cstvar = StringVar()
paragon_cstvar = StringVar()
hdrink_cstvar = StringVar()
create_alcohol_cstvar = StringVar()
colddead_cstvar = StringVar()
favoured_cstvar = StringVar()
hindsight_cstvar = StringVar()
intuition_cstvar = StringVar()

# Frag Specific

frag1_cstvar = StringVar()
frag2_cstvar = StringVar()
frag3_cstvar = StringVar()
frag4_cstvar = StringVar()
frag5_cstvar = StringVar()
frag6_cstvar = StringVar()

versa1_cstvar = StringVar()
versa2_cstvar = StringVar()
versa3_cstvar = StringVar()
versa4_cstvar = StringVar()
versa5_cstvar = StringVar()
versa6_cstvar = StringVar()
versa7_cstvar = StringVar()
versa8_cstvar = StringVar()
versa9_cstvar = StringVar()

# Scholar

mysticism_cstvar = StringVar()
demonic_arts_cstvar = StringVar()
necromantic_arts_cstvar = StringVar()
anatomy_cstvar = StringVar()
firstaid_cstvar = StringVar()
physician_cstvar = StringVar()
readwrite_cstvar = StringVar()
readmagic_cstvar = StringVar()
readmagic_advanced_cstvar = StringVar()
readmagic_ritual_cstvar = StringVar()
sphere1_cstvar = StringVar()
sphere2_cstvar = StringVar()
sphere3_cstvar = StringVar()
sphereadv_cstvar = StringVar()
elemental_attune_cstvar = StringVar()
slot1_cstvar = StringVar()
slot2_cstvar = StringVar()
slot3_cstvar = StringVar()
slot4_cstvar = StringVar()
slot5_cstvar = StringVar()
slot6_cstvar = StringVar()
slot7_cstvar = StringVar()
slot8_cstvar = StringVar()
slot9_cstvar = StringVar()
slotritual_base_cstvar = StringVar()
slotritual_cstvar = StringVar()

# Warrior

ambidexterity_cstvar = StringVar()
florentine_cstvar = StringVar()
flurry_cstvar = StringVar()
heavy_armour_cstvar = StringVar()
self_mutilate_cstvar = StringVar()
shield_cstvar = StringVar()
refocus_cstvar = StringVar()
groupprof_med_cstvar = StringVar()
groupprof_large_cstvar = StringVar()
prof_exotic_cstvar = StringVar()
spec_group_cstvar = StringVar()
spec_specific_cstvar = StringVar()
slay_cstvar = StringVar()
slay_master_cstvar = StringVar()

# Rogue

garrotte_cstvar = StringVar()
sap_cstvar = StringVar()
vitalblow_cstvar = StringVar()
dodge_cstvar = StringVar()
crit_spec_cstvar = StringVar()
crit_group_cstvar = StringVar()
execute_cstvar = StringVar()
execute_master_cstvar = StringVar()

## Purchases

trapper = StringVar()
create_scroll = StringVar()
tradesman = StringVar()
alchemy = StringVar()
blacksmith = StringVar()
chemistry = StringVar()
artifice = StringVar()

occupational1 = StringVar()
occupational2 = StringVar()
occupational3 = StringVar()
occupational4 = StringVar()
racial1 = StringVar()
racial_bpb = StringVar()
racial_str = StringVar()

anatomy = StringVar()
firstaid = StringVar()
physician = StringVar()
mysticism = StringVar()
demonic_arts = StringVar()
necromantic_arts = StringVar()
readwrite = StringVar()
readmagic = StringVar()
readmagic_advanced = StringVar()
sphere1 = StringVar()
sphere2 = StringVar()
sphere3 = StringVar()
sphere1name = StringVar()
sphere2name = StringVar()
sphere3name = StringVar()
readmagic_ritual = StringVar()
sphereadv = StringVar()
elemental_attune = StringVar()

slot1 = StringVar()
slot2 = StringVar()
slot3 = StringVar()
slot4 = StringVar()
slot5 = StringVar()
slot6 = StringVar()
slot7 = StringVar()
slot8 = StringVar()
slot9 = StringVar()
slotR = StringVar()
autopyramid = StringVar()

ambidexterity = StringVar()
florentine = StringVar()
flurry = StringVar()
heavy_armour = StringVar()
self_mutilate = StringVar()
shield = StringVar()
refocus = StringVar()
groupprof_med = StringVar()
groupprof_large = StringVar()
prof_exotic = StringVar()
spec_group = StringVar()
spec_specific = StringVar()
slay = StringVar()
slay_master = StringVar()

garrotte = StringVar()
sap = StringVar()
vitalblow = StringVar()
dodge = StringVar()
crit_spec = StringVar()
crit_group = StringVar()
execute = StringVar()
execute_master = StringVar()

colddead = StringVar()
create_alcohol = StringVar()
favoured = StringVar()
hdrink = StringVar()
hindsight = StringVar()
looting = StringVar()
intuition = StringVar()
paragon = StringVar()
paragon_level = StringVar()
possum = StringVar()
teacher = StringVar()

frag1 = StringVar()
frag2 = StringVar()
frag3 = StringVar()
frag4 = StringVar()
frag5 = StringVar()
frag6 = StringVar()

versa1 = StringVar()
versa2 = StringVar()
versa3 = StringVar()
versa4 = StringVar()
versa5 = StringVar()
versa6 = StringVar()
versa7 = StringVar()
versa8 = StringVar()
versa9 = StringVar()

versa_name = StringVar()
versa1name = StringVar()
versa2name = StringVar()
versa3name = StringVar()
versa4name = StringVar()
versa5name = StringVar()
versa6name = StringVar()
versa7name = StringVar()
versa8name = StringVar()
versa9name = StringVar()

skill_costs = {

	#Production

	"trapsmith_cost": trapper_cstvar,
	"create_scroll_cost": create_scroll_cstvar,
	"tradesman_cost":tradesman_cstvar,
	"alchemy_cost":alchemy_cstvar,
	"blacksmith_cost":blacksmith_cstvar,
	"chemistry_cost":chemistry_cstvar,
	"artifice_cost":artifice_cstvar,

	#Frag

	"teacher_cost":teacher_cstvar,
	"possum_cost":possum_cstvar,
	"looting_cost":looting_cstvar,
	"paragon_cost":paragon_cstvar,
	"heavy_drinker_cost":hdrink_cstvar,
	"create_alcohol_cost":create_alcohol_cstvar,
	"cold_dead_hands_cost":colddead_cstvar,
	"favoured_cost":favoured_cstvar,
	"hindsight_cost":hindsight_cstvar,
	"intuition_cost":intuition_cstvar,

	#Frag Specific

	"frag1_cost":frag1_cstvar, # Battlefield, Blindfighter, Combat Wizard
	"frag2_cost":frag2_cstvar, # Cripple, Escape, Harvest
	"frag3_cost":frag3_cstvar, # Decapitate, Riposte, Mortician
	"frag4_cost":frag4_cstvar, # Dirt Eye, Sucker Punch, Refocus
	"frag5_cost":frag5_cstvar, # Trip, Thieves Cant, Spell Parry
	"frag6_cost":frag6_cstvar, # Whirlwind, Tumble, Spell Switch
								# , , Spell Versatility

	#Scholar

	"mysticism_cost":mysticism_cstvar,
	"demonic_arts_cost":demonic_arts_cstvar,
	"necromantic_arts_cost":necromantic_arts_cstvar,
	"anatomy_cost":anatomy_cstvar,
	"firstaid_cost":firstaid_cstvar,
	"physician_cost":physician_cstvar,
	"readwrite_cost":readwrite_cstvar,
	"readmagic_cost":readmagic_cstvar,
	"readmagic_advanced_cost":readmagic_advanced_cstvar,
	"readmagic_ritual_cost":readmagic_ritual_cstvar,
	"sphere1_cost":sphere1_cstvar,
	"sphere2_cost":sphere2_cstvar,
	"sphere3_cost":sphere3_cstvar,
	"sphereadv_cost":sphereadv_cstvar,
	"elemental_attune_cost":elemental_attune_cstvar,
	"slot1_cost":slot1_cstvar,
	"slot2_cost":slot2_cstvar,
	"slot3_cost":slot3_cstvar,
	"slot4_cost":slot4_cstvar,
	"slot5_cost":slot5_cstvar,
	"slot6_cost":slot6_cstvar,
	"slot7_cost":slot7_cstvar,
	"slot8_cost":slot8_cstvar,
	"slot9_cost":slot9_cstvar,
	"slotritual_cost":slotritual_cstvar,

	#Warrior

	"ambidexterity_cost":ambidexterity_cstvar,
	"florentine_cost":florentine_cstvar,
	"flurry_cost":flurry_cstvar,
	"heavy_armour_cost":heavy_armour_cstvar,
	"self_mutilate_cost":self_mutilate_cstvar,
	"shield_cost":shield_cstvar,
	"refocus":refocus_cstvar,
	"groupprof_med_cost":groupprof_med_cstvar,
	"groupprof_large_cost":groupprof_large_cstvar,
	"prof_exotic_cost":prof_exotic_cstvar,
	"spec_group_cost":spec_group_cstvar,
	"spec_specific_cost":spec_specific_cstvar,
	"slay_cost":slay_cstvar,
	"slay_master_cost":slay_master_cstvar,

	#Rogue

	"garrotte_cost":garrotte_cstvar,
	"sap_cost":sap_cstvar,
	"vitalblow_cost":vitalblow_cstvar,
	"dodge_cost":dodge_cstvar,
	"crit_spec_cost":crit_spec_cstvar,
	"crit_group_cost":crit_group_cstvar,
	"execute_cost":execute_cstvar,
	"execute_master_cost":execute_master_cstvar

}

##### Functions

# Skill purchases

def enter_pressed(event):
	print ("You pressed enter")
	calc_spent_cp()

def trapper_up(event):
	if (int(trapper.get()) != 10):
		trapper.set(int(trapper.get())+1)
		calc_spent_cp()
		trapper.set(int(trapper.get())-1)
	else:
		calc_spent_cp()

def trapper_down(event):
	if (int(trapper.get()) != 0):
		trapper.set(int(trapper.get())-1)
		calc_spent_cp()
		trapper.set(int(trapper.get())+1)
	else:
		calc_spent_cp()
		
def create_scroll_up(event):
	if (int(create_scroll.get()) != 10):
		create_scroll.set(int(create_scroll.get())+1)
		calc_spent_cp()
		create_scroll.set(int(create_scroll.get())-1)
	else:
		calc_spent_cp()

def create_scroll_down(event):
	if (int(create_scroll.get()) != 0):
		create_scroll.set(int(create_scroll.get())-1)
		calc_spent_cp()
		create_scroll.set(int(create_scroll.get())+1)
	else:
		calc_spent_cp()
		
def tradesman_up(event):
	if (int(tradesman.get()) != 10):
		tradesman.set(int(tradesman.get())+1)
		calc_spent_cp()
		tradesman.set(int(tradesman.get())-1)
	else:
		calc_spent_cp()

def tradesman_down(event):
	if (int(tradesman.get()) != 0):
		tradesman.set(int(tradesman.get())-1)
		calc_spent_cp()
		tradesman.set(int(tradesman.get())+1)
	else:
		calc_spent_cp()
		
def alchemy_up(event):
	if (int(alchemy.get()) != 10):
		alchemy.set(int(alchemy.get())+1)
		calc_spent_cp()
		alchemy.set(int(alchemy.get())-1)
	else:
		calc_spent_cp()

def alchemy_down(event):
	chemistry_spin.config(state='disabled')
	chemistry.set('0')
	
	if (int(alchemy.get()) != 0):
		alchemy.set(int(alchemy.get())-1)
		calc_spent_cp()
		alchemy.set(int(alchemy.get())+1)
	else:
		calc_spent_cp()
		
def blacksmith_up(event):
	if (int(blacksmith.get()) != 10):
		blacksmith.set(int(blacksmith.get())+1)
		calc_spent_cp()
		blacksmith.set(int(blacksmith.get())-1)
	else:
		calc_spent_cp()

def blacksmith_down(event):
	if (int(blacksmith.get()) != 0):
		blacksmith.set(int(blacksmith.get())-1)
		calc_spent_cp()
		blacksmith.set(int(blacksmith.get())+1)
	else:
		calc_spent_cp()
		
def chemistry_up(event):
	if (int(chemistry.get()) != 10):
		chemistry.set(int(chemistry.get())+1)
		calc_spent_cp()
		chemistry.set(int(chemistry.get())-1)
	else:
		calc_spent_cp()

def chemistry_down(event):
	if (int(chemistry.get()) != 0):
		chemistry.set(int(chemistry.get())-1)
		calc_spent_cp()
		chemistry.set(int(chemistry.get())+1)
	else:
		calc_spent_cp()
		
def artifice_up(event):
	if (int(artifice.get()) != 10):
		artifice.set(int(artifice.get())+1)
		calc_spent_cp()
		artifice.set(int(artifice.get())-1)
	else:
		calc_spent_cp()

def artifice_down(event):
	if (int(artifice.get()) != 0):
		artifice.set(int(artifice.get())-1)
		calc_spent_cp()
		artifice.set(int(artifice.get())+1)
	else:
		calc_spent_cp()
		
def occupational1_up(event):
	if (int(occupational1.get()) != 10):
		occupational1.set(int(occupational1.get())+1)
		calc_spent_cp()
		occupational1.set(int(occupational1.get())-1)
	else:
		calc_spent_cp()

def occupational1_down(event):
	if (int(occupational1.get()) != 0):
		occupational1.set(int(occupational1.get())-1)
		calc_spent_cp()
		occupational1.set(int(occupational1.get())+1)
	else:
		calc_spent_cp()
		
def occupational2_up(event):
	if (int(occupational2.get()) != 10):
		occupational2.set(int(occupational2.get())+1)
		calc_spent_cp()
		occupational2.set(int(occupational2.get())-1)
	else:
		calc_spent_cp()

def occupational2_down(event):
	if (int(occupational2.get()) != 0):
		occupational2.set(int(occupational2.get())-1)
		calc_spent_cp()
		occupational2.set(int(occupational2.get())+1)
	else:
		calc_spent_cp()
		
def occupational3_up(event):
	if (int(occupational3.get()) != 10):
		occupational3.set(int(occupational3.get())+1)
		calc_spent_cp()
		occupational3.set(int(occupational3.get())-1)
	else:
		calc_spent_cp()

def occupational3_down(event):
	if (int(occupational3.get()) != 0):
		occupational3.set(int(occupational3.get())-1)
		calc_spent_cp()
		occupational3.set(int(occupational3.get())+1)
	else:
		calc_spent_cp()
		
def occupational4_up(event):
	if (int(occupational4.get()) != 10):
		occupational4.set(int(occupational4.get())+1)
		calc_spent_cp()
		occupational4.set(int(occupational4.get())-1)
	else:
		calc_spent_cp()

def occupational4_down(event):
	if (int(occupational4.get()) != 0):
		occupational4.set(int(occupational4.get())-1)
		calc_spent_cp()
		occupational4.set(int(occupational4.get())+1)
	else:
		calc_spent_cp()
		
def racial1_up(event):
	if (int(racial1.get()) != 10):
		racial1.set(int(racial1.get())+1)
		calc_spent_cp()
		if (race.get() == 'Human' or race.get() == 'Mountain Dwarf'):
			set_CP_and_health(int(blankets.get()))
		racial1.set(int(racial1.get())-1)
	else:
		calc_spent_cp()
		if (race.get() == 'Human' or race.get() == 'Mountain Dwarf'):
			set_CP_and_health(int(blankets.get()))

def racial1_down(event):
	if (int(racial1.get()) != 0):
		racial1.set(int(racial1.get())-1)
		calc_spent_cp()
		if (race.get() == 'Human' or race.get() == 'Mountain Dwarf'):
			set_CP_and_health(int(blankets.get()))
		racial1.set(int(racial1.get())+1)
	else:
		calc_spent_cp()
		if (race.get() == 'Human' or race.get() == 'Mountain Dwarf'):
			set_CP_and_health(int(blankets.get()))
		
def colddead_up(event):
	colddead.set('1')
	calc_spent_cp()
	colddead.set('0')

def colddead_down(event):
	colddead.set('0')
	calc_spent_cp()
	colddead.set('1')
		
def create_alcohol_up(event):
	if (int(create_alcohol.get()) != 10):
		create_alcohol.set(int(create_alcohol.get())+1)
		calc_spent_cp()
		create_alcohol.set(int(create_alcohol.get())-1)
	else:
		calc_spent_cp()

def create_alcohol_down(event):
	if (int(create_alcohol.get()) != 0):
		create_alcohol.set(int(create_alcohol.get())-1)
		calc_spent_cp()
		create_alcohol.set(int(create_alcohol.get())+1)
	else:
		calc_spent_cp()

def hdrink_up(event):
	hdrink.set('1')
	calc_spent_cp()
	hdrink.set('0')

def hdrink_down(event):
	hdrink.set('0')
	calc_spent_cp()
	hdrink.set('1')
		
def hindsight_up(event):
	hindsight.set('1')
	calc_spent_cp()
	hindsight.set('0')

def hindsight_down(event):
	hindsight.set('0')
	calc_spent_cp()
	hindsight.set('1')

def looting_up(event):
	if (int(looting.get()) != 5):
		looting.set(int(looting.get())+1)
		calc_spent_cp()
		looting.set(int(looting.get())-1)
	else:
		calc_spent_cp()

def looting_down(event):
	if (int(looting.get()) != 0):
		looting.set(int(looting.get())-1)
		calc_spent_cp()
		looting.set(int(looting.get())+1)
	else:
		calc_spent_cp()

def intuition_up(event):
	intuition.set('1')
	calc_spent_cp()
	intuition.set('0')

def intuition_down(event):
	intuition.set('0')
	calc_spent_cp()
	intuition.set('1')

def paragon_up(event):
	paragon.set('1')
	calc_spent_cp()
	paragon.set('0')

def paragon_down(event):
	paragon.set('0')
	calc_spent_cp()
	paragon.set('1')
	
def paragon_level_up(event):
	if (int(paragon_level.get()) != 7):
		paragon_level.set(int(paragon_level.get())+1)
		calc_spent_cp()
		paragon_level.set(int(paragon_level.get())-1)
	else:
		calc_spent_cp()

def paragon_level_down(event):
	if (int(paragon_level.get()) != 1):
		paragon_level.set(int(paragon_level.get())-1)
		calc_spent_cp()
		paragon_level.set(int(paragon_level.get())+1)
	else:
		calc_spent_cp()

def possum_up(event):
	if (int(possum.get()) != 10):
		possum.set(int(possum.get())+1)
		calc_spent_cp()
		possum.set(int(possum.get())-1)
	else:
		calc_spent_cp()

def possum_down(event):
	if (int(possum.get()) != 0):
		possum.set(int(possum.get())-1)
		calc_spent_cp()
		possum.set(int(possum.get())+1)
	else:
		calc_spent_cp()
		
def teacher_up(event):
	teacher.set('1')
	calc_spent_cp()
	teacher.set('0')

def teacher_down(event):
	teacher.set('0')
	calc_spent_cp()
	teacher.set('1')
	
def frag1_up(event):
	if (school_current.get() == 'Scholar'):
		frag1.set('1')
		calc_spent_cp()
		frag1.set('0')
	else:
		if (int(frag1.get()) != 10):
			frag1.set(int(frag1.get())+1)
			calc_spent_cp()
			frag1.set(int(frag1.get())-1)
		else:
			calc_spent_cp()

def frag1_down(event):
	if (school_current.get() == 'Scholar'):
		frag1.set('0')
		calc_spent_cp()
		frag1.set('1')
	else:
		if (int(frag1.get()) != 0):
			frag1.set(int(frag1.get())-1)
			calc_spent_cp()
			frag1.set(int(frag1.get())+1)
		else:
			calc_spent_cp()
		
def frag2_up(event):
	if (int(frag2.get()) != 10):
		frag2.set(int(frag2.get())+1)
		calc_spent_cp()
		frag2.set(int(frag2.get())-1)
	else:
		calc_spent_cp()

def frag2_down(event):
	if (int(frag2.get()) != 0):
		frag2.set(int(frag2.get())-1)
		calc_spent_cp()
		frag2.set(int(frag2.get())+1)
	else:
		calc_spent_cp()

def frag3_up(event):
	if (school_current.get() == 'Scholar'):
		frag3.set('1')
		calc_spent_cp()
		frag3.set('0')
	else:
		if (int(frag3.get()) != 10):
			frag3.set(int(frag3.get())+1)
			calc_spent_cp()
			frag3.set(int(frag3.get())-1)
		else:
			calc_spent_cp()

def frag3_down(event):
	if (school_current.get() == 'Scholar'):
		frag3.set('0')
		calc_spent_cp()
		frag3.set('1')
	else:
		if (int(frag3.get()) != 0):
			frag3.set(int(frag3.get())-1)
			calc_spent_cp()
			frag3.set(int(frag3.get())+1)
		else:
			calc_spent_cp()

def frag4_up(event):
	if (int(frag4.get()) != 10):
		frag4.set(int(frag4.get())+1)
		calc_spent_cp()
		frag4.set(int(frag4.get())-1)
	else:
		calc_spent_cp()

def frag4_down(event):
	if (int(frag4.get()) != 0):
		frag4.set(int(frag4.get())-1)
		calc_spent_cp()
		frag4.set(int(frag4.get())+1)
	else:
		calc_spent_cp()

def frag5_up(event):
	if (school_current.get() == 'Warrior'):
		if (int(frag5.get()) != 10):
			frag5.set(int(frag5.get())+1)
			calc_spent_cp()
			frag5.set(int(frag5.get())-1)
		else:
			calc_spent_cp()
	else:
		frag5.set('1')
		calc_spent_cp()
		frag5.set('0')

def frag5_down(event):
	if (school_current.get() == 'Warrior'):
		if (int(frag5.get()) != 0):
			frag5.set(int(frag5.get())-1)
			calc_spent_cp()
			frag5.set(int(frag5.get())+1)
		else:
			calc_spent_cp()
	else:
		frag5.set('0')
		calc_spent_cp()
		frag5.set('1')

def frag6_up(event):
	if (school_current.get() == 'Warrior'):
		if (int(frag6.get()) < int(flurry.get())):
			frag6.set(int(frag6.get())+1)
			calc_spent_cp()
			frag6.set(int(frag6.get())-1)
		else:
			calc_spent_cp()
	else:
		if (int(frag6.get()) != 10):
			frag6.set(int(frag6.get())+1)
			calc_spent_cp()
			frag6.set(int(frag6.get())-1)
		else:
			calc_spent_cp()

def frag6_down(event):
	if (school_current.get() == 'Warrior'):
		if (int(frag6.get()) < int(flurry.get())):
			frag6.set(int(frag6.get())-1)
			calc_spent_cp()
			frag6.set(int(frag6.get())+1)
		else:
			calc_spent_cp()
	
	else:
		if (int(frag6.get()) != 0):
			frag6.set(int(frag6.get())-1)
			calc_spent_cp()
			frag6.set(int(frag6.get())+1)
		else:
			calc_spent_cp()
			
def versa1_up(event):
	if (int(versa1.get()) + int(versa2.get()) + int(versa3.get()) + int(versa4.get()) + int(versa5.get()) + int(versa6.get()) + int(versa7.get()) + int(versa8.get()) + int(versa9.get()) > 9):
		calc_spent_cp()
		versa1.set(int(versa1.get())-1)
	elif (int(versa1.get()) != 10):
		versa1.set(int(versa1.get())+1)
		calc_spent_cp()
		versa1.set(int(versa1.get())-1)
	else:
		calc_spent_cp()

def versa1_down(event):
	if (int(versa1.get()) != 0):
		versa1.set(int(versa1.get())-1)
		calc_spent_cp()
		versa1.set(int(versa1.get())+1)
	else:
		calc_spent_cp()
		
def versa2_up(event):
	if (int(versa1.get()) + int(versa2.get()) + int(versa3.get()) + int(versa4.get()) + int(versa5.get()) + int(versa6.get()) + int(versa7.get()) + int(versa8.get()) + int(versa9.get()) > 9):
		calc_spent_cp()
		versa2.set(int(versa2.get())-1)
	elif (int(versa2.get()) != 10):
		versa2.set(int(versa2.get())+1)
		calc_spent_cp()
		versa2.set(int(versa2.get())-1)
	else:
		calc_spent_cp()

def versa2_down(event):
	if (int(versa2.get()) != 0):
		versa2.set(int(versa2.get())-1)
		calc_spent_cp()
		versa2.set(int(versa2.get())+1)
	else:
		calc_spent_cp()
		
def versa3_up(event):
	if (int(versa1.get()) + int(versa2.get()) + int(versa3.get()) + int(versa4.get()) + int(versa5.get()) + int(versa6.get()) + int(versa7.get()) + int(versa8.get()) + int(versa9.get()) > 9):
		calc_spent_cp()
		versa3.set(int(versa3.get())-1)
	elif (int(versa3.get()) != 10):
		versa3.set(int(versa3.get())+1)
		calc_spent_cp()
		versa3.set(int(versa3.get())-1)
	else:
		calc_spent_cp()

def versa3_down(event):
	if (int(versa3.get()) != 0):
		versa3.set(int(versa3.get())-1)
		calc_spent_cp()
		versa3.set(int(versa3.get())+1)
	else:
		calc_spent_cp()
		
def versa4_up(event):
	if (int(versa1.get()) + int(versa2.get()) + int(versa3.get()) + int(versa4.get()) + int(versa5.get()) + int(versa6.get()) + int(versa7.get()) + int(versa8.get()) + int(versa9.get()) > 9):
		calc_spent_cp()
		versa4.set(int(versa4.get())-1)
	elif (int(versa4.get()) != 10):
		versa4.set(int(versa4.get())+1)
		calc_spent_cp()
		versa4.set(int(versa4.get())-1)
	else:
		calc_spent_cp()

def versa4_down(event):
	if (int(versa4.get()) != 0):
		versa4.set(int(versa4.get())-1)
		calc_spent_cp()
		versa4.set(int(versa4.get())+1)
	else:
		calc_spent_cp()
		
def versa5_up(event):
	if (int(versa1.get()) + int(versa2.get()) + int(versa3.get()) + int(versa4.get()) + int(versa5.get()) + int(versa6.get()) + int(versa7.get()) + int(versa8.get()) + int(versa9.get()) > 9):
		calc_spent_cp()
		versa5.set(int(versa5.get())-1)
	elif (int(versa5.get()) != 10):
		versa5.set(int(versa5.get())+1)
		calc_spent_cp()
		versa5.set(int(versa5.get())-1)
	else:
		calc_spent_cp()

def versa5_down(event):
	if (int(versa5.get()) != 0):
		versa5.set(int(versa5.get())-1)
		calc_spent_cp()
		versa5.set(int(versa5.get())+1)
	else:
		calc_spent_cp()
		
def versa6_up(event):
	if (int(versa1.get()) + int(versa2.get()) + int(versa3.get()) + int(versa4.get()) + int(versa5.get()) + int(versa6.get()) + int(versa7.get()) + int(versa8.get()) + int(versa9.get()) > 9):
		calc_spent_cp()
		versa6.set(int(versa6.get())-1)
	elif (int(versa6.get()) != 10):
		versa6.set(int(versa6.get())+1)
		calc_spent_cp()
		versa6.set(int(versa6.get())-1)
	else:
		calc_spent_cp()

def versa6_down(event):
	if (int(versa6.get()) != 0):
		versa6.set(int(versa6.get())-1)
		calc_spent_cp()
		versa6.set(int(versa6.get())+1)
	else:
		calc_spent_cp()
		
def versa7_up(event):
	if (int(versa1.get()) + int(versa2.get()) + int(versa3.get()) + int(versa4.get()) + int(versa5.get()) + int(versa6.get()) + int(versa7.get()) + int(versa8.get()) + int(versa9.get()) > 9):
		calc_spent_cp()
		versa7.set(int(versa7.get())-1)
	elif (int(versa7.get()) != 10):
		versa7.set(int(versa7.get())+1)
		calc_spent_cp()
		versa7.set(int(versa7.get())-1)
	else:
		calc_spent_cp()

def versa7_down(event):
	if (int(versa7.get()) != 0):
		versa7.set(int(versa7.get())-1)
		calc_spent_cp()
		versa7.set(int(versa7.get())+1)
	else:
		calc_spent_cp()
		
def versa8_up(event):
	if (int(versa1.get()) + int(versa2.get()) + int(versa3.get()) + int(versa4.get()) + int(versa5.get()) + int(versa6.get()) + int(versa7.get()) + int(versa8.get()) + int(versa9.get()) > 9):
		calc_spent_cp()
		versa8.set(int(versa8.get())-1)
	elif (int(versa8.get()) != 10):
		versa8.set(int(versa8.get())+1)
		calc_spent_cp()
		versa8.set(int(versa8.get())-1)
	else:
		calc_spent_cp()

def versa8_down(event):
	if (int(versa8.get()) != 0):
		versa8.set(int(versa8.get())-1)
		calc_spent_cp()
		versa8.set(int(versa8.get())+1)
	else:
		calc_spent_cp()
		
def versa9_up(event):
	if (int(versa1.get()) + int(versa2.get()) + int(versa3.get()) + int(versa4.get()) + int(versa5.get()) + int(versa6.get()) + int(versa7.get()) + int(versa8.get()) + int(versa9.get()) > 9):
		calc_spent_cp()
		versa9.set(int(versa9.get())-1)
	elif (int(versa9.get()) != 10):
		versa9.set(int(versa9.get())+1)
		calc_spent_cp()
		versa9.set(int(versa9.get())-1)
	else:
		calc_spent_cp()

def versa9_down(event):
	if (int(versa9.get()) != 0):
		versa9.set(int(versa9.get())-1)
		calc_spent_cp()
		versa9.set(int(versa9.get())+1)
	else:
		calc_spent_cp()

def racial_bpb_up(event):
	if (int(racial_bpb.get()) != 10):
		racial_bpb.set(int(racial_bpb.get())+1)
		calc_spent_cp()
		set_CP_and_health(int(blankets.get()))
		racial_bpb.set(int(racial_bpb.get())-1)
	else:
		calc_spent_cp()
		set_CP_and_health(int(blankets.get()))

def racial_bpb_down(event):
	if (int(racial_bpb.get()) != 0):
		racial_bpb.set(int(racial_bpb.get())-1)
		calc_spent_cp()
		set_CP_and_health(int(blankets.get()))
		racial_bpb.set(int(racial_bpb.get())+1)
	else:
		calc_spent_cp()
		set_CP_and_health(int(blankets.get()))

def racial_str_up(event):
	if (int(racial_str.get()) != 10):
		racial_str.set(int(racial_str.get())+1)
		calc_spent_cp()
		racial_str.set(int(racial_str.get())-1)
	else:
		calc_spent_cp()

def racial_str_down(event):
	if (int(racial_str.get()) != 0):
		racial_str.set(int(racial_str.get())-1)
		calc_spent_cp()
		racial_str.set(int(racial_str.get())+1)
	else:
		calc_spent_cp()

def anatomy_up(event):
	anatomy.set('1')
	calc_spent_cp()
	anatomy.set('0')

def anatomy_down(event):
	anatomy.set('0')
	calc_spent_cp()
	anatomy.set('1')
	
def firstaid_up(event):
	firstaid.set('1')
	calc_spent_cp()
	firstaid.set('0')
	
def firstaid_down(event):
	firstaid.set('0')
	calc_spent_cp()
	firstaid.set('1')
		
def physician_up(event):
	if (int(physician.get()) != 10):
		physician.set(int(physician.get())+1)
		calc_spent_cp()
		physician.set(int(physician.get())-1)
	else:
		calc_spent_cp()

def physician_down(event):
	if (int(physician.get()) != 0):
		physician.set(int(physician.get())-1)
		calc_spent_cp()
		physician.set(int(physician.get())+1)
	else:
		calc_spent_cp()
	
def mysticism_up(event):
	if (int(mysticism.get()) != 10):
		mysticism.set(int(mysticism.get())+1)
		calc_spent_cp()
		mysticism.set(int(mysticism.get())-1)
	else:
		calc_spent_cp()

def mysticism_down(event):
	if (int(mysticism.get()) != 0):
		mysticism.set(int(mysticism.get())-1)
		calc_spent_cp()
		mysticism.set(int(mysticism.get())+1)
	else:
		calc_spent_cp()
	
def demonic_arts_down(event):
	demonic_arts.set('0')
	calc_spent_cp()
	demonic_arts.set('1')
	
def demonic_arts_up(event):
	demonic_arts.set('1')
	calc_spent_cp()
	demonic_arts.set('0')
	
def necromantic_arts_down(event):
	necromantic_arts.set('0')
	calc_spent_cp()
	necromantic_arts.set('1')
	
def necromantic_arts_up(event):
	necromantic_arts.set('1')
	calc_spent_cp()
	necromantic_arts.set('0')
	
def readwrite_up(event):
	readwrite.set('1')
	calc_spent_cp()
	readwrite.set('0')
	
def readwrite_down(event):
	readwrite.set('0')
	calc_spent_cp()
	readwrite.set('1')
	
def readmagic_up(event):
	readmagic.set('1')
	calc_spent_cp()
	readmagic.set('0')
	
def readmagic_down(event):
	readmagic.set('0')
	calc_spent_cp()
	readmagic.set('1')
	
def readmagic_advanced_up(event):
	readmagic_advanced.set('1')
	calc_spent_cp()
	readmagic_advanced.set('0')
	
def readmagic_advanced_down(event):
	readmagic_advanced.set('0')
	calc_spent_cp()
	readmagic_advanced.set('1')
	
def readmagic_ritual_up(event):
	readmagic_ritual.set('1')
	set_slots()
	calc_spent_cp()
	readmagic_ritual.set('0')
	
def readmagic_ritual_down(event):
	readmagic_ritual.set('0')
	calc_spent_cp()
	readmagic_ritual.set('1')
	
def sphere1_up(event):
	sphere1.set('1')
	calc_spent_cp()
	sphere1.set('0')
	
def sphere1_down(event):
	sphere1.set('0')
	calc_spent_cp()
	sphere1.set('1')
	
def sphere2_down(event):
	sphere2.set('0')
	calc_spent_cp()
	sphere2.set('1')
	
def sphere2_up(event):
	sphere2.set('1')
	calc_spent_cp()
	sphere2.set('0')
		
def sphere3_up(event):
	if (int(sphere3.get()) != 10):
		sphere3.set(int(sphere3.get())+1)
		calc_spent_cp()
		sphere3.set(int(sphere3.get())-1)
	else:
		calc_spent_cp()

def sphere3_down(event):
	if (int(sphere3.get()) != 0):
		sphere3.set(int(sphere3.get())-1)
		calc_spent_cp()
		sphere3.set(int(sphere3.get())+1)
	else:
		calc_spent_cp()
	
def sphereadv_down(event):
	sphereadv.set('0')
	calc_spent_cp()
	sphereadv.set('1')
	
def sphereadv_up(event):
	sphereadv.set('1')
	calc_spent_cp()
	sphereadv.set('0')
		
def elemental_attune_up(event):
	if (int(elemental_attune.get()) != 3):
		elemental_attune.set(int(elemental_attune.get())+1)
		calc_spent_cp()
		elemental_attune.set(int(elemental_attune.get())-1)
	else:
		calc_spent_cp()

def elemental_attune_down(event):
	if (int(elemental_attune.get()) != 0):
		elemental_attune.set(int(elemental_attune.get())-1)
		calc_spent_cp()
		elemental_attune.set(int(elemental_attune.get())+1)
	else:
		calc_spent_cp()
		
def slot1_up(event):
	if (int(slot1.get()) != 10):
		slot1.set(int(slot1.get())+1)
		calc_spent_cp()
		slot1.set(int(slot1.get())-1)
	else:
		calc_spent_cp()

def slot1_down(event):
	if (int(slot1.get()) != 0):
		slot1.set(int(slot1.get())-1)
		calc_spent_cp()
		slot1.set(int(slot1.get())+1)
	else:
		calc_spent_cp()
		
def slot2_up(event):
	if (int(slot2.get()) != 10):
		slot2.set(int(slot2.get())+1)
		calc_spent_cp()
		slot2.set(int(slot2.get())-1)
	else:
		calc_spent_cp()

def slot2_down(event):
	if (int(slot2.get()) != 0):
		slot2.set(int(slot2.get())-1)
		calc_spent_cp()
		slot2.set(int(slot2.get())+1)
	else:
		calc_spent_cp()
		
def slot3_up(event):
	if (int(slot3.get()) != 10):
		slot3.set(int(slot3.get())+1)
		calc_spent_cp()
		slot3.set(int(slot3.get())-1)
	else:
		calc_spent_cp()

def slot3_down(event):
	if (int(slot3.get()) != 0):
		slot3.set(int(slot3.get())-1)
		calc_spent_cp()
		slot3.set(int(slot3.get())+1)
	else:
		calc_spent_cp()
		
def slot4_up(event):
	if (int(slot4.get()) != 10):
		slot4.set(int(slot4.get())+1)
		calc_spent_cp()
		slot4.set(int(slot4.get())-1)
	else:
		calc_spent_cp()

def slot4_down(event):
	if (int(slot4.get()) != 0):
		slot4.set(int(slot4.get())-1)
		calc_spent_cp()
		slot4.set(int(slot4.get())+1)
	else:
		calc_spent_cp()
		
def slot5_up(event):
	if (int(slot5.get()) != 10):
		slot5.set(int(slot5.get())+1)
		calc_spent_cp()
		slot5.set(int(slot5.get())-1)
	else:
		calc_spent_cp()

def slot5_down(event):
	if (int(slot5.get()) != 0):
		slot5.set(int(slot5.get())-1)
		calc_spent_cp()
		slot5.set(int(slot5.get())+1)
	else:
		calc_spent_cp()
		
def slot6_up(event):
	if (int(slot6.get()) != 10):
		slot6.set(int(slot6.get())+1)
		calc_spent_cp()
		slot6.set(int(slot6.get())-1)
	else:
		calc_spent_cp()

def slot6_down(event):
	if (int(slot6.get()) != 0):
		slot6.set(int(slot6.get())-1)
		calc_spent_cp()
		slot6.set(int(slot6.get())+1)
	else:
		calc_spent_cp()
		
def slot7_up(event):
	if (int(slot7.get()) != 10):
		slot7.set(int(slot7.get())+1)
		calc_spent_cp()
		slot7.set(int(slot7.get())-1)
	else:
		calc_spent_cp()

def slot7_down(event):
	if (int(slot7.get()) != 0):
		slot7.set(int(slot7.get())-1)
		calc_spent_cp()
		slot7.set(int(slot7.get())+1)
	else:
		calc_spent_cp()
		
def slot8_up(event):
	if (int(slot8.get()) != 10):
		slot8.set(int(slot8.get())+1)
		calc_spent_cp()
		slot8.set(int(slot8.get())-1)
	else:
		calc_spent_cp()

def slot8_down(event):
	if (int(slot8.get()) != 0):
		slot8.set(int(slot8.get())-1)
		calc_spent_cp()
		slot8.set(int(slot8.get())+1)
	else:
		calc_spent_cp()
		
def slot9_up(event):
	if (int(slot9.get()) != 10):
		slot9.set(int(slot9.get())+1)
		calc_spent_cp()
		slot9.set(int(slot9.get())-1)
	else:
		calc_spent_cp()

def slot9_down(event):
	if (int(slot9.get()) != 0):
		slot9.set(int(slot9.get())-1)
		calc_spent_cp()
		slot9.set(int(slot9.get())+1)
	else:
		calc_spent_cp()
		
def slotR_up(event):
	if (int(slotR.get()) != 10):
		slotR.set(int(slotR.get())+1)
		calc_spent_cp()
		slotR.set(int(slotR.get())-1)
	else:
		calc_spent_cp()

def slotR_down(event):
	if (int(slotR.get()) != 0):
		slotR.set(int(slotR.get())-1)
		calc_spent_cp()
		slotR.set(int(slotR.get())+1)
	else:
		calc_spent_cp()

def ambidexterity_up(event):
	ambidexterity.set('1')
	calc_spent_cp()
	ambidexterity.set('0')

def ambidexterity_down(event):
	ambidexterity.set('0')
	calc_spent_cp()
	ambidexterity.set('1')

def florentine_up(event):
	florentine.set('1')
	calc_spent_cp()
	florentine.set('0')

def florentine_down(event):
	florentine.set('0')
	calc_spent_cp()
	florentine.set('1')
		
def flurry_up(event):
	if (int(flurry.get()) != 10):
		flurry.set(int(flurry.get())+1)
		calc_spent_cp()
		flurry.set(int(flurry.get())-1)
	else:
		calc_spent_cp()

def flurry_down(event):
	if (int(flurry.get()) != 0):
		flurry.set(int(flurry.get())-1)
		calc_spent_cp()
		flurry.set(int(flurry.get())+1)
	else:
		calc_spent_cp()
		
def heavy_armour_up(event):
	heavy_armour.set('1')
	calc_spent_cp()
	heavy_armour.set('0')

def heavy_armour_down(event):
	heavy_armour.set('0')
	calc_spent_cp()
	heavy_armour.set('1')
	
def self_mutilate_up(event):
	self_mutilate.set('1')
	calc_spent_cp()
	self_mutilate.set('0')

def self_mutilate_down(event):
	self_mutilate.set('0')
	calc_spent_cp()
	self_mutilate.set('1')
	
def shield_up(event):
	shield.set('1')
	calc_spent_cp()
	shield.set('0')

def shield_down(event):
	shield.set('0')
	calc_spent_cp()
	shield.set('1')
	
def refocus_up(event):
	if (int(refocus.get()) != 10):
		refocus.set(int(refocus.get())+1)
		calc_spent_cp()
		refocus.set(int(refocus.get())-1)
	else:
		calc_spent_cp()

def refocus_down(event):
	if (int(refocus.get()) != 0):
		refocus.set(int(refocus.get())-1)
		calc_spent_cp()
		refocus.set(int(refocus.get())+1)
	else:
		calc_spent_cp()
		
def groupprof_med_up(event):
	if (int(groupprof_med.get()) != 10):
		groupprof_med.set(int(groupprof_med.get())+1)
		calc_spent_cp()
		groupprof_med.set(int(groupprof_med.get())-1)
	else:
		calc_spent_cp()

def groupprof_med_down(event):
	if (int(groupprof_med.get()) != 0):
		groupprof_med.set(int(groupprof_med.get())-1)
		calc_spent_cp()
		groupprof_med.set(int(groupprof_med.get())+1)
	else:
		calc_spent_cp()
		
def groupprof_large_up(event):
	if (int(groupprof_large.get()) != 10):
		groupprof_large.set(int(groupprof_large.get())+1)
		calc_spent_cp()
		groupprof_large.set(int(groupprof_large.get())-1)
	else:
		calc_spent_cp()

def groupprof_large_down(event):
	if (int(groupprof_large.get()) != 0):
		groupprof_large.set(int(groupprof_large.get())-1)
		calc_spent_cp()
		groupprof_large.set(int(groupprof_large.get())+1)
	else:
		calc_spent_cp()
		
def prof_exotic_up(event):
	if (int(prof_exotic.get()) != 10):
		prof_exotic.set(int(prof_exotic.get())+1)
		calc_spent_cp()
		prof_exotic.set(int(prof_exotic.get())-1)
	else:
		calc_spent_cp()

def prof_exotic_down(event):
	if (int(prof_exotic.get()) != 0):
		prof_exotic.set(int(prof_exotic.get())-1)
		calc_spent_cp()
		prof_exotic.set(int(prof_exotic.get())+1)
	else:
		calc_spent_cp()
		
def spec_group_up(event):
	if (int(spec_group.get()) != 10):
		spec_group.set(int(spec_group.get())+1)
		calc_spent_cp()
		spec_group.set(int(spec_group.get())-1)
	else:
		calc_spent_cp()

def spec_group_down(event):
	if (int(spec_group.get()) != 0):
		spec_group.set(int(spec_group.get())-1)
		calc_spent_cp()
		spec_group.set(int(spec_group.get())+1)
	else:
		calc_spent_cp()

def spec_specific_up(event):
	if (int(spec_specific.get()) != 10):
		spec_specific.set(int(spec_specific.get())+1)
		calc_spent_cp()
		spec_specific.set(int(spec_specific.get())-1)
	else:
		calc_spent_cp()

def spec_specific_down(event):
	if (int(spec_specific.get()) != 0):
		spec_specific.set(int(spec_specific.get())-1)
		calc_spent_cp()
		spec_specific.set(int(spec_specific.get())+1)
	else:
		calc_spent_cp()

def slay_up(event):
	if (int(slay.get()) != 10):
		slay.set(int(slay.get())+1)
		calc_spent_cp()
		slay.set(int(slay.get())-1)
	else:
		calc_spent_cp()

def slay_down(event):
	if (int(slay.get()) != 0):
		slay.set(int(slay.get())-1)
		calc_spent_cp()
		slay.set(int(slay.get())+1)
	else:
		calc_spent_cp()

def slay_master_up(event):
	if (int(slay_master.get()) != 10):
		slay_master.set(int(slay_master.get())+1)
		calc_spent_cp()
		slay_master.set(int(slay_master.get())-1)
	else:
		calc_spent_cp()

def slay_master_down(event):
	if (int(slay_master.get()) != 0):
		slay_master.set(int(slay_master.get())-1)
		calc_spent_cp()
		slay_master.set(int(slay_master.get())+1)
	else:
		calc_spent_cp()
		
def garrotte_up(event):
	garrotte.set('1')
	calc_spent_cp()
	garrotte.set('0')

def garrotte_down(event):
	garrotte.set('0')
	calc_spent_cp()
	garrotte.set('1')

def sap_up(event):
	if (int(sap.get()) != 10):
		sap.set(int(sap.get())+1)
		calc_spent_cp()
		sap.set(int(sap.get())-1)
	else:
		calc_spent_cp()

def sap_down(event):
	if (int(sap.get()) != 0):
		sap.set(int(sap.get())-1)
		calc_spent_cp()
		sap.set(int(sap.get())+1)
	else:
		calc_spent_cp()

def vitalblow_up(event):
	if (int(vitalblow.get()) != 10):
		vitalblow.set(int(vitalblow.get())+1)
		calc_spent_cp()
		vitalblow.set(int(vitalblow.get())-1)
	else:
		calc_spent_cp()

def vitalblow_down(event):
	if (int(vitalblow.get()) != 0):
		vitalblow.set(int(vitalblow.get())-1)
		calc_spent_cp()
		vitalblow.set(int(vitalblow.get())+1)
	else:
		calc_spent_cp()

def dodge_up(event):
	if (int(dodge.get()) != 10):
		dodge.set(int(dodge.get())+1)
		calc_spent_cp()
		dodge.set(int(dodge.get())-1)
	else:
		calc_spent_cp()

def dodge_down(event):
	if (int(dodge.get()) != 0):
		dodge.set(int(dodge.get())-1)
		calc_spent_cp()
		dodge.set(int(dodge.get())+1)
	else:
		calc_spent_cp()

def crit_spec_up(event):
	if (int(crit_spec.get()) != 10):
		crit_spec.set(int(crit_spec.get())+1)
		calc_spent_cp()
		crit_spec.set(int(crit_spec.get())-1)
	else:
		calc_spent_cp()

def crit_spec_down(event):
	if (int(crit_spec.get()) != 0):
		crit_spec.set(int(crit_spec.get())-1)
		calc_spent_cp()
		crit_spec.set(int(crit_spec.get())+1)
	else:
		calc_spent_cp()

def crit_group_up(event):
	if (int(crit_group.get()) != 10):
		crit_group.set(int(crit_group.get())+1)
		calc_spent_cp()
		crit_group.set(int(crit_group.get())-1)
	else:
		calc_spent_cp()

def crit_group_down(event):
	if (int(crit_group.get()) != 0):
		crit_group.set(int(crit_group.get())-1)
		calc_spent_cp()
		crit_group.set(int(crit_group.get())+1)
	else:
		calc_spent_cp()

def execute_up(event):
	if (int(execute.get()) != 10):
		execute.set(int(execute.get())+1)
		calc_spent_cp()
		execute.set(int(execute.get())-1)
	else:
		calc_spent_cp()

def execute_down(event):
	if (int(execute.get()) != 0):
		execute.set(int(execute.get())-1)
		calc_spent_cp()
		execute.set(int(execute.get())+1)
	else:
		calc_spent_cp()

def execute_master_up(event):
	if (int(execute_master.get()) != 10):
		execute_master.set(int(execute_master.get())+1)
		calc_spent_cp()
		execute_master.set(int(execute_master.get())-1)
	else:
		calc_spent_cp()

def execute_master_down(event):
	if (int(execute_master.get()) != 0):
		execute_master.set(int(execute_master.get())-1)
		calc_spent_cp()
		execute_master.set(int(execute_master.get())+1)
	else:
		calc_spent_cp()
	
def change_blankets_up(event):
	set_CP_and_health(int(blankets.get())+1)
	calc_spent_cp()
	
def change_blankets_down(event):
	set_CP_and_health(int(blankets.get())-1)
	calc_spent_cp()
	
def change_blankets_manual(event):
	set_CP_and_health(int(blankets.get()))

# Saving etc.

def savefile():
	f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
	if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
		return
		
	text_to_file = "{"
	
	text_to_file = text_to_file + "\n'player_name': '" + player_name.get() + "',"
	text_to_file = text_to_file + "\n'char_name': '" + char_name.get() + "',"
	text_to_file = text_to_file + "\n'race': '" + race.get() + "',"
	text_to_file = text_to_file + "\n'frag_race': '" + frag_race.get() + "',"

	text_to_file = text_to_file + "\n'blankets': '" + blankets.get() + "',"
	text_to_file = text_to_file + "\n'CP': '" + CP.get() + "',"
	text_to_file = text_to_file + "\n'CP_spent': '" + CP_spent.get() + "',"
	text_to_file = text_to_file + "\n'CP_free': '" + CP_free.get() + "',"
	text_to_file = text_to_file + "\n'level': '" + level.get() + "',"
	text_to_file = text_to_file + "\n'HP': '" + HP.get() + "',"

	text_to_file = text_to_file + "\n'occupation': '" + occupation.get() + "',"
	text_to_file = text_to_file + "\n'renowned_occupation': '" + renowned_occupation.get() + "',"
	text_to_file = text_to_file + "\n'vocation_on': '" + vocation_on.get() + "',"
	text_to_file = text_to_file + "\n'vocation': '" + vocation.get() + "',"

	text_to_file = text_to_file + "\n'trapper': '" + trapper.get() + "',"
	text_to_file = text_to_file + "\n'create_scroll': '" + create_scroll.get() + "',"
	text_to_file = text_to_file + "\n'tradesman': '" + tradesman.get() + "',"
	text_to_file = text_to_file + "\n'alchemy': '" + alchemy.get() + "',"
	text_to_file = text_to_file + "\n'blacksmith': '" + blacksmith.get() + "',"
	text_to_file = text_to_file + "\n'chemistry': '" + chemistry.get() + "',"
	text_to_file = text_to_file + "\n'artifice': '" + artifice.get() + "',"

	text_to_file = text_to_file + "\n'occupational1': '" + occupational1.get() + "',"
	text_to_file = text_to_file + "\n'occupational2': '" + occupational2.get() + "',"
	text_to_file = text_to_file + "\n'occupational3': '" + occupational3.get() + "',"
	text_to_file = text_to_file + "\n'occupational4': '" + occupational4.get() + "',"
	text_to_file = text_to_file + "\n'racial1': '" + racial1.get() + "',"
	text_to_file = text_to_file + "\n'racial_bpb': '" + racial_bpb.get() + "',"
	text_to_file = text_to_file + "\n'racial_str': '" + racial_str.get() + "',"

	text_to_file = text_to_file + "\n'anatomy': '" + anatomy.get() + "',"
	text_to_file = text_to_file + "\n'firstaid': '" + firstaid.get() + "',"
	text_to_file = text_to_file + "\n'physician': '" + physician.get() + "',"
	text_to_file = text_to_file + "\n'mysticism': '" + mysticism.get() + "',"
	text_to_file = text_to_file + "\n'demonic_arts': '" + demonic_arts.get() + "',"
	text_to_file = text_to_file + "\n'necromantic_arts': '" + necromantic_arts.get() + "',"
	text_to_file = text_to_file + "\n'readwrite': '" + readwrite.get() + "',"
	text_to_file = text_to_file + "\n'readmagic': '" + readmagic.get() + "',"
	text_to_file = text_to_file + "\n'readmagic_advanced': '" + readmagic_advanced.get() + "',"
	text_to_file = text_to_file + "\n'sphere1': '" + sphere1.get() + "',"
	text_to_file = text_to_file + "\n'sphere2': '" + sphere2.get() + "',"
	text_to_file = text_to_file + "\n'sphere3': '" + sphere3.get() + "',"
	text_to_file = text_to_file + "\n'sphere1name': '" + sphere1name.get() + "',"
	text_to_file = text_to_file + "\n'sphere2name': '" + sphere2name.get() + "',"
	text_to_file = text_to_file + "\n'sphere3name': '" + sphere3name.get() + "',"
	text_to_file = text_to_file + "\n'readmagic_ritual': '" + readmagic_ritual.get() + "',"
	text_to_file = text_to_file + "\n'sphereadv': '" + sphereadv.get() + "',"
	text_to_file = text_to_file + "\n'elemental_attune': '" + elemental_attune.get() + "',"

	text_to_file = text_to_file + "\n'slot1': '" + slot1.get() + "',"
	text_to_file = text_to_file + "\n'slot2': '" + slot2.get() + "',"
	text_to_file = text_to_file + "\n'slot3': '" + slot3.get() + "',"
	text_to_file = text_to_file + "\n'slot4': '" + slot4.get() + "',"
	text_to_file = text_to_file + "\n'slot5': '" + slot5.get() + "',"
	text_to_file = text_to_file + "\n'slot6': '" + slot6.get() + "',"
	text_to_file = text_to_file + "\n'slot7': '" + slot7.get() + "',"
	text_to_file = text_to_file + "\n'slot8': '" + slot8.get() + "',"
	text_to_file = text_to_file + "\n'slot9': '" + slot9.get() + "',"
	text_to_file = text_to_file + "\n'slotR': '" + slotR.get() + "',"

	text_to_file = text_to_file + "\n'ambidexterity': '" + ambidexterity.get() + "',"
	text_to_file = text_to_file + "\n'florentine': '" + florentine.get() + "',"
	text_to_file = text_to_file + "\n'flurry': '" + flurry.get() + "',"
	text_to_file = text_to_file + "\n'heavy_armour': '" + heavy_armour.get() + "',"
	text_to_file = text_to_file + "\n'self_mutilate': '" + self_mutilate.get() + "',"
	text_to_file = text_to_file + "\n'shield': '" + shield.get() + "',"
	text_to_file = text_to_file + "\n'refocus': '" + refocus.get() + "',"
	text_to_file = text_to_file + "\n'groupprof_med': '" + groupprof_med.get() + "',"
	text_to_file = text_to_file + "\n'groupprof_large': '" + groupprof_large.get() + "',"
	text_to_file = text_to_file + "\n'prof_exotic': '" + prof_exotic.get() + "',"
	text_to_file = text_to_file + "\n'spec_group': '" + spec_group.get() + "',"
	text_to_file = text_to_file + "\n'spec_specific': '" + spec_specific.get() + "',"
	text_to_file = text_to_file + "\n'slay': '" + slay.get() + "',"
	text_to_file = text_to_file + "\n'slay_master': '" + slay_master.get() + "',"

	text_to_file = text_to_file + "\n'garrotte': '" + garrotte.get() + "',"
	text_to_file = text_to_file + "\n'sap': '" + sap.get() + "',"
	text_to_file = text_to_file + "\n'vitalblow': '" + vitalblow.get() + "',"
	text_to_file = text_to_file + "\n'dodge': '" + dodge.get() + "',"
	text_to_file = text_to_file + "\n'crit_spec': '" + crit_spec.get() + "',"
	text_to_file = text_to_file + "\n'crit_group': '" + crit_group.get() + "',"
	text_to_file = text_to_file + "\n'execute': '" + execute.get() + "',"
	text_to_file = text_to_file + "\n'execute_master': '" + execute_master.get() + "',"

	text_to_file = text_to_file + "\n'colddead': '" + colddead.get() + "',"
	text_to_file = text_to_file + "\n'create_alcohol': '" + create_alcohol.get() + "',"
	text_to_file = text_to_file + "\n'favoured': '" + favoured.get() + "',"
	text_to_file = text_to_file + "\n'hdrink': '" + hdrink.get() + "',"
	text_to_file = text_to_file + "\n'hindsight': '" + hindsight.get() + "',"
	text_to_file = text_to_file + "\n'looting': '" + looting.get() + "',"
	text_to_file = text_to_file + "\n'intuition': '" + intuition.get() + "',"
	text_to_file = text_to_file + "\n'paragon': '" + paragon.get() + "',"
	text_to_file = text_to_file + "\n'possum': '" + possum.get() + "',"
	text_to_file = text_to_file + "\n'teacher': '" + teacher.get() + "',"

	text_to_file = text_to_file + "\n'frag1': '" + frag1.get() + "',"
	text_to_file = text_to_file + "\n'frag2': '" + frag2.get() + "',"
	text_to_file = text_to_file + "\n'frag3': '" + frag3.get() + "',"
	text_to_file = text_to_file + "\n'frag4': '" + frag4.get() + "',"
	text_to_file = text_to_file + "\n'frag5': '" + frag5.get() + "',"
	text_to_file = text_to_file + "\n'frag6': '" + frag6.get() + "',"
	
	text_to_file = text_to_file + "\n'versa1': '" + versa1.get() + "',"
	text_to_file = text_to_file + "\n'versa2': '" + versa2.get() + "',"
	text_to_file = text_to_file + "\n'versa3': '" + versa3.get() + "',"
	text_to_file = text_to_file + "\n'versa4': '" + versa4.get() + "',"
	text_to_file = text_to_file + "\n'versa5': '" + versa5.get() + "',"
	text_to_file = text_to_file + "\n'versa6': '" + versa6.get() + "',"
	text_to_file = text_to_file + "\n'versa7': '" + versa7.get() + "',"
	text_to_file = text_to_file + "\n'versa8': '" + versa8.get() + "',"
	text_to_file = text_to_file + "\n'versa9': '" + versa9.get() + "'\n}"
	
	text_to_file_text = Text(root)
	text_to_file_text.delete('1.0', 'end -1 chars')
	text_to_file_text.insert('0.0 -1 chars', text_to_file)

	f.write(text_to_file_text.get('1.0', 'end -1 chars'))
	f.close()
	
def openfile():
	file = filedialog.askopenfile(mode ='r', filetypes =[('Character Builder Files', '*.txt')]) 
	content = ''
	file_dict = {}
	if file is not None: 
		content = file.read() 
	
	file_dict = eval(content)
	
	player_name.set(file_dict['player_name'])
	char_name.set(file_dict['char_name'])
	race.set(file_dict['race'])
	frag_race.set(file_dict['frag_race'])

	blankets.set(file_dict['blankets'])
	CP.set(file_dict['CP'])
	CP_spent.set(file_dict['CP_spent'])
	CP_free.set(file_dict['CP_free'])
	level.set(file_dict['level'])
	HP.set(file_dict['HP'])

	occupation.set(file_dict['occupation'])
	renowned_occupation.set(file_dict['renowned_occupation'])
	vocation_on.set(file_dict['vocation_on'])

	trapper.set(file_dict['trapper'])
	create_scroll.set(file_dict['create_scroll'])
	tradesman.set(file_dict['tradesman'])
	alchemy.set(file_dict['alchemy'])
	blacksmith.set(file_dict['blacksmith'])
	chemistry.set(file_dict['chemistry'])
	artifice.set(file_dict['artifice'])

	occupational1.set(file_dict['occupational1'])
	occupational2.set(file_dict['occupational2'])
	occupational3.set(file_dict['occupational3'])
	occupational4.set(file_dict['occupational4'])
	racial1.set(file_dict['racial1'])
	racial_bpb.set(file_dict['racial_bpb'])
	racial_str.set(file_dict['racial_str'])

	anatomy.set(file_dict['anatomy'])
	firstaid.set(file_dict['firstaid'])
	physician.set(file_dict['physician'])
	mysticism.set(file_dict['mysticism'])
	demonic_arts.set(file_dict['demonic_arts'])
	necromantic_arts.set(file_dict['necromantic_arts'])
	readwrite.set(file_dict['readwrite'])
	readmagic.set(file_dict['readmagic'])
	readmagic_advanced.set(file_dict['readmagic_advanced'])
	sphere1.set(file_dict['sphere1'])
	sphere2.set(file_dict['sphere2'])
	sphere3.set(file_dict['sphere3'])
	sphere1name.set(file_dict['sphere1name'])
	sphere2name.set(file_dict['sphere2name'])
	sphere3name.set(file_dict['sphere3name'])
	readmagic_ritual.set(file_dict['readmagic_ritual'])
	sphereadv.set(file_dict['sphereadv'])
	elemental_attune.set(file_dict['elemental_attune'])

	slot1.set(file_dict['slot1'])
	slot2.set(file_dict['slot2'])
	slot3.set(file_dict['slot3'])
	slot4.set(file_dict['slot4'])
	slot5.set(file_dict['slot5'])
	slot6.set(file_dict['slot6'])
	slot7.set(file_dict['slot7'])
	slot8.set(file_dict['slot8'])
	slot9.set(file_dict['slot9'])
	slotR.set(file_dict['slotR'])

	ambidexterity.set(file_dict['ambidexterity'])
	florentine.set(file_dict['florentine'])
	flurry.set(file_dict['flurry'])
	heavy_armour.set(file_dict['heavy_armour'])
	self_mutilate.set(file_dict['self_mutilate'])
	shield.set(file_dict['shield'])
	refocus.set(file_dict['refocus'])
	groupprof_med.set(file_dict['groupprof_med'])
	groupprof_large.set(file_dict['groupprof_large'])
	prof_exotic.set(file_dict['prof_exotic'])
	spec_group.set(file_dict['spec_group'])
	spec_specific.set(file_dict['spec_specific'])
	slay.set(file_dict['slay'])
	slay_master.set(file_dict['slay_master'])

	garrotte.set(file_dict['garrotte'])
	sap.set(file_dict['sap'])
	vitalblow.set(file_dict['vitalblow'])
	dodge.set(file_dict['dodge'])
	crit_spec.set(file_dict['crit_spec'])
	crit_group.set(file_dict['crit_group'])
	execute.set(file_dict['execute'])
	execute_master.set(file_dict['execute_master'])

	colddead.set(file_dict['colddead'])
	create_alcohol.set(file_dict['create_alcohol'])
	favoured.set(file_dict['favoured'])
	hdrink.set(file_dict['hdrink'])
	hindsight.set(file_dict['hindsight'])
	looting.set(file_dict['looting'])
	intuition.set(file_dict['intuition'])
	paragon.set(file_dict['paragon'])
	possum.set(file_dict['possum'])
	teacher.set(file_dict['teacher'])

	frag1.set(file_dict['frag1'])
	frag2.set(file_dict['frag2'])
	frag3.set(file_dict['frag3'])
	frag4.set(file_dict['frag4'])
	frag5.set(file_dict['frag5'])
	frag6.set(file_dict['frag6'])
	
	versa1.set(file_dict['versa1'])
	versa2.set(file_dict['versa2'])
	versa3.set(file_dict['versa3'])
	versa4.set(file_dict['versa4'])
	versa5.set(file_dict['versa5'])
	versa6.set(file_dict['versa6'])
	versa7.set(file_dict['versa7'])
	versa8.set(file_dict['versa8'])
	versa9.set(file_dict['versa9'])
	
	if (occupation.get() == 'RENOWNED'):
		school_current.set(occupation_school[renowned_occupation.get()])
	else:
		school_current.set(occupation_school[occupation.get()])	
	
	change_occupation()
	change_race()
	set_skill_list()

def savetext():
	f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
	if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
		return
	
	text_to_file = 'Player: ' + player_name.get()
	text_to_file = text_to_file + "\n" + "Character: " + char_name.get()
	text_to_file = text_to_file + "\n" + "Race: " + race.get()
	
	if (occupation.get() == "RENOWNED"):
		text_to_file = text_to_file + "\n" + "Occupation: " + renowned_occupation.get()
	else:
		text_to_file = text_to_file + "\n" + "Occupation: " + occupation.get()
	if (vocation_on.get() == '1'):
		text_to_file = text_to_file + "\n" + "Vocation: " + vocation.get()
		
	text_to_file = text_to_file + "\n" + "Level: " + level.get()
	text_to_file = text_to_file + "\n" + "Hit Points: " + HP.get()
	text_to_file = text_to_file + "\n" + "Blankets: " + blankets.get()
	text_to_file = text_to_file + "\n" + "Total CP: " + CP.get()
	text_to_file = text_to_file + "\n" + "Spent CP: " + CP_spent.get()
	text_to_file = text_to_file + "\n" + "Free CP: " + CP_free.get()
	text_to_file = text_to_file + "\n" + "Total CP: " + CP.get()
	text_to_file = text_to_file + "\n\n" + "Skills:\n"
	try:
		text_to_file = text_to_file + all_skills.get('1.0', 'end')
	except:
		text_to_file = text_to_file + "None"
		
	text_to_file_text = Text(root)
	text_to_file_text.delete('1.0', 'end -1 chars')
	text_to_file_text.insert('0.0 -1 chars', text_to_file)

	f.write(text_to_file_text.get('1.0', 'end -1 chars'))
	f.close()

# Change other things

def set_slots():
	if (readmagic_advanced.get() == '0'):
		if (int(slot1.get()) > 5):
			slot1.set('5')
		if (int(slot2.get()) > 4):
			slot2.set('4')
		if (int(slot3.get()) > 3):
			slot3.set('3')
		if (int(slot4.get()) > 2):
			slot4.set('2')
		slot5.set('0')
		slot6.set('0')
		slot7.set('0')
		slot8.set('0')
		slot9.set('0')
		slotR.set('0')
		
	s1 = int(slot1.get())
	if (s1 == 0):
		slot2.set('0')
	s2 = int(slot2.get())
	if (s2 == 0):
		slot3.set('0')
	s3 = int(slot3.get())
	if (s3 == 0):
		slot4.set('0')
	s4 = int(slot4.get())
	if (s4 == 0):
		slot5.set('0')
	s5 = int(slot5.get())
	if (s5 == 0):
		slot6.set('0')
	s6 = int(slot6.get())
	if (s6 == 0):
		slot7.set('0')
	s7 = int(slot7.get())
	if (s7 == 0):
		slot8.set('0')
	s8 = int(slot8.get())
	if (s8 == 0):
		slot9.set('0')
	s9 = int(slot9.get())
	if (s9 == 0):
		slotR.set('0')
	sR = int(slotR.get())
	
	if (s1 > 0 and s1 < s2):
		slot2.set(s1 - 1)
		s2 = s1 - 1
	if (s2 > 0 and s2 < s3):
		slot3.set(s2 - 1)
		s3 = s2 - 1
	if (s3 > 0 and s3 < s4):
		slot4.set(s3 - 1)
		s4 = s3 - 1
	if (s4 > 0 and s4 < s5):
		slot5.set(s4 - 1)
		s5 = s4 - 1
	if (s5 > 0 and s5 < s6):
		slot6.set(s5 - 1)
		s6 = s5 - 1
	if (s6 > 0 and s6 < s7):
		slot7.set(s6 - 1)
		s7 = s6 - 1
	if (s7 > 0 and s7 < s8):
		slot8.set(s7 - 1)
		s8 = s7 - 1
	if (s8 > 0 and s8 < s9):
		slot9.set(s8 - 1)
		s9 = s8 - 1
		
	if (s1 == 0):
		slot2.set('0')
		s2 = int(slot2.get())
	if (s2 == 0):
		slot3.set('0')
		s3 = int(slot3.get())
	if (s3 == 0):
		slot4.set('0')
		s4 = int(slot4.get())
	if (s4 == 0):
		slot5.set('0')
		s5 = int(slot5.get())
	if (s5 == 0):
		slot6.set('0')
		s6 = int(slot6.get())
	if (s6 == 0):
		slot7.set('0')
		s7 = int(slot7.get())
	if (s7 == 0):
		slot8.set('0')
		s8 = int(slot8.get())
	if (s8 == 0):
		slot9.set('0')
		s9 = int(slot9.get())
	if (s9 == 0):
		slotR.set('0')
		sR = int(slotR.get())
		
	slot1_spin.config(state='disabled')
	slot2_spin.config(state='disabled')
	slot3_spin.config(state='disabled')
	slot4_spin.config(state='disabled')
	slot5_spin.config(state='disabled')
	slot6_spin.config(state='disabled')
	slot7_spin.config(state='disabled')
	slot8_spin.config(state='disabled')
	slot9_spin.config(state='disabled')
	slotR_spin.config(state='disabled')
	
	if (readwrite.get() == '1' and readmagic.get() == '1' and sphere1.get() == '1'):
		if (s9 > 4):
			if (readmagic_ritual.get() == '1'):
				slotR_spin.config(state='active')
			slot1_spin.config(state='active')
			slot1_spin.focus_set()
			if (s1 > s2):
				slot2_spin.config(state='active')
			else:
				slot2_spin.config(state='disabled')
			if (s2 > s3):
				slot3_spin.config(state='active')
			else:
				slot3_spin.config(state='disabled')
			if (s3 > s4):
				slot4_spin.config(state='active')
			else:
				slot4_spin.config(state='disabled')
			if (s4 > s5):
				slot5_spin.config(state='active')
			else:
				slot5_spin.config(state='disabled')
			if (s5 > s6):
				slot6_spin.config(state='active')
			else:
				slot6_spin.config(state='disabled')
			if (s6 > s7):
				slot7_spin.config(state='active')
			else:
				slot7_spin.config(state='disabled')
			if (s7 > s8):
				slot8_spin.config(state='active')
			else:
				slot8_spin.config(state='disabled')
			if (s8 > s9):
				slot9_spin.config(state='active')
			else:
				slot9_spin.config(state='disabled')
			
		else:
			if (s9 > 0 and readmagic_ritual.get() == '1'):
				slotR_spin.config(state='active')
			else:
				slotR_spin.config(state='disabled')
				
			if ((s8 - s9) == 2 or s8 == 5):
				slot9_spin.config(state='active')
				slot9_spin.focus_set()
			else:
				if ((s7 - s8) == 2 or s7 == 5):
					slot8_spin.config(state='active')
					slot8_spin.focus_set()
				else:
					if ((s6 - s7) == 2 or s6 == 5):
						slot7_spin.config(state='active')
						slot7_spin.focus_set()
					else:
						if ((s5 - s6) == 2 or s5 == 5):
							slot6_spin.config(state='active')
							slot6_spin.focus_set()
						else:
							if ((s4 - s5) == 2 or s4 == 5):
								slot5_spin.config(state='active')
								slot5_spin.focus_set()
							else:							
								if ((s3 - s4) == 2 or s3 == 5):
									slot4_spin.config(state='active')
									slot4_spin.focus_set()
								else:
									if ((s2 - s3) == 2 or s2 == 5):
										slot3_spin.config(state='active')
										slot3_spin.focus_set()
									else:
										if ((s1 - s2) == 2 or s1 == 5):
											slot2_spin.config(state='active')
											slot2_spin.focus_set()
										else:
											slot1_spin.config(state='active')
											slot1_spin.focus_set()
		
	else:
		slot1.set('0')
		slot2.set('0')
		slot3.set('0')
		slot4.set('0')
		slot5.set('0')
		slot6.set('0')
		slot7.set('0')
		slot8.set('0')
		slot9.set('0')
		slotR.set('0')
		
def set_auto_pyramid (* args):
	pyramid_level = int(autopyramid.get())
	
	readwrite.set('1')
	readmagic.set('1')
	sphere1.set('1')
	
	if (pyramid_level == 1):
		slot1.set('1')
		slot2.set('0')
		slot3.set('0')
		slot4.set('0')
		slot5.set('0')
		slot6.set('0')
		slot7.set('0')
		slot8.set('0')
		slot9.set('0')
		slotR.set('0')
	elif (pyramid_level == 2):
		slot1.set('2')
		slot2.set('1')
		slot3.set('0')
		slot4.set('0')
		slot5.set('0')
		slot6.set('0')
		slot7.set('0')
		slot8.set('0')
		slot9.set('0')
		slotR.set('0')
	elif (pyramid_level == 3):
		slot1.set('3')
		slot2.set('2')
		slot3.set('1')
		slot4.set('0')
		slot5.set('0')
		slot6.set('0')
		slot7.set('0')
		slot8.set('0')
		slot9.set('0')
		slotR.set('0')
	elif (pyramid_level == 4):
		slot1.set('4')
		slot2.set('3')
		slot3.set('2')
		slot4.set('1')
		slot5.set('0')
		slot6.set('0')
		slot7.set('0')
		slot8.set('0')
		slot9.set('0')
		slotR.set('0')
	elif (pyramid_level == 5):
		readmagic_advanced.set('1')
		slot1.set('5')
		slot2.set('4')
		slot3.set('3')
		slot4.set('2')
		slot5.set('1')
		slot6.set('0')
		slot7.set('0')
		slot8.set('0')
		slot9.set('0')
		slotR.set('0')
	elif (pyramid_level == 6):
		readmagic_advanced.set('1')
		slot1.set('5')
		slot2.set('5')
		slot3.set('4')
		slot4.set('3')
		slot5.set('2')
		slot6.set('1')
		slot7.set('0')
		slot8.set('0')
		slot9.set('0')
		slotR.set('0')
	elif (pyramid_level == 7):
		readmagic_advanced.set('1')
		slot1.set('5')
		slot2.set('5')
		slot3.set('5')
		slot4.set('4')
		slot5.set('3')
		slot6.set('2')
		slot7.set('1')
		slot8.set('0')
		slot9.set('0')
		slotR.set('0')
	elif (pyramid_level == 8):
		readmagic_advanced.set('1')
		slot1.set('5')
		slot2.set('5')
		slot3.set('5')
		slot4.set('5')
		slot5.set('4')
		slot6.set('3')
		slot7.set('2')
		slot8.set('1')
		slot9.set('0')
		slotR.set('0')
	elif (pyramid_level == 9):
		readmagic_advanced.set('1')
		slot1.set('5')
		slot2.set('5')
		slot3.set('5')
		slot4.set('5')
		slot5.set('5')
		slot6.set('4')
		slot7.set('3')
		slot8.set('2')
		slot9.set('1')
		
	calc_spent_cp()

def depend_check():

	# Racials
	
	if (race.get() == 'Gargylen'):
		racial_bpb_spin.config(to=2)
		if (int(racial_bpb.get()) > 2):
			racial_bpb.set('2')
	elif (race.get() == 'Mountain Dwarf'):
		racial1_spin.config(to=3)
		if (int(racial1.get()) > 3):
			racial1.set('3')
	elif (race.get() == 'Wild Elf' or race.get() == 'Einher' or race.get() == 'Human'):
		racial_bpb_spin.config(to=1)
		if (int(racial_bpb.get()) > 1):
			racial_bpb.set('1')
	
	if (race.get() == 'Orc' or race.get() == 'Human'):
		racial1_spin.config(to=1)
		if (int(racial1.get()) > 1):
			racial1.set('1')
	else:
		racial1_spin.config(to=10)
	
	if (float(racial1.get()) > (int(level.get()) + 1) / 2):
		racial1_spin.config(to = (int(level.get()) + 1) / 2)
		racial1.set(int((int(level.get()) + 1) / 2))
		
	# Occupationals
	
	if ((occupation.get() == 'Druid' and vocation.get() == '0') or vocation.get() == 'Brew Master' or vocation.get() == 'Undead Hunter'):
		occupational1_spin.config(to=1)
		if (int(occupational1.get()) > 1):
			occupational1.set('1')
	else:
		occupational1_spin.config(to=10)
	
	if ((occupation.get() == 'Mercenary' and vocation.get() == '0')  or (occupation.get() == 'Mage' and vocation.get() == '0')):
		occupational2_spin.config(to=1)
		if (int(occupational2.get()) > 1):
			occupational2.set('1')
	else:
		occupational2_spin.config(to=10)
			
	if ((occupation.get() == 'Ranger' and vocation.get() == '0') or (occupation.get() == 'Druid' and vocation.get() == '0') or (occupation.get() == 'RENOWNED' and renowned_occupation.get() == 'Lightweaver' and vocation.get() == '0') or (occupation.get() == 'RENOWNED' and renowned_occupation.get() == 'Darkweaver' and vocation.get() == '0') or (occupation.get() == 'RENOWNED' and renowned_occupation.get() == 'Dragon Knight' and vocation.get() == '0')):
		occupational4_spin.config(to=1)
		if (int(occupational4.get()) > 1):
			occupational4.set('1')
	else:
		occupational4_spin.config(to=10)
	
	# Production
	
	if (alchemy.get() == '10'):
		chemistry_spin.config(state='active')
	else:
		chemistry.set('0')
		chemistry_spin.config(state='disabled')
		
	if (blacksmith.get() == '10'):
		artifice_spin.config(state='active')
	else:
		artifice.set('0')
		artifice_spin.config(state='disabled')

	if (readmagic.get() == '1'):
		create_scroll_spin.config(state='active')
	else:
		create_scroll.set('0')
		create_scroll_spin.config(state='disabled')
		
	# Occupation and Race
	
	if (int(occupational1.get()) > 0):
		occupational2_spin.config(state='active')
	else:
		occupational2.set('0')
		occupational2_spin.config(state='disabled')
	
	if (int(occupational2.get()) > 0):
		occupational3_spin.config(state='active')
	else:
		occupational3.set('0')
		occupational3_spin.config(state='disabled')
	
	if (int(occupational3.get()) > 0):
		occupational4_spin.config(state='active')
	else:
		occupational4.set('0')
		occupational4_spin.config(state='disabled')
	
	# Scholar
	
	if (anatomy.get() == '1'):
		firstaid_spin.config(state='active')
	else:
		firstaid.set('0')
		firstaid_spin.config(state='disabled')
	
	if (firstaid.get() == '1'):
		physician_spin.config(state='active')
	else:
		physician.set('0')
		physician_spin.config(state='disabled')
		
	if (readwrite.get() == '1'):
		readmagic_spin.config(state='active')
	else:
		readmagic.set('0')
		readmagic_spin.config(state='disabled')
	
	if (readmagic.get() == '1'):
		readmagic_advanced_spin.config(state='active')
		sphere1_spin.config(state='active')
	else:
		readmagic_advanced.set('0')
		readmagic_advanced_spin.config(state='disabled')
		sphere1.set('0')
		sphere1_spin.config(state='disabled')

	if (readmagic_advanced.get() == '1'):
		readmagic_ritual_spin.config(state='active')
	else:
		readmagic_ritual.set('0')
		readmagic_ritual_spin.config(state='disabled')
		
	if (sphere1.get() == '1'):
		sphere2_spin.config(state='active')
		elemental_attune_spin.config(state='active')
		sphere1name_box.grid()
		sphere1name_box.config(state='readonly')
	else:
		sphere2.set('0')
		sphere2_spin.config(state='disabled')
		elemental_attune.set('0')
		elemental_attune_spin.config(state='disabled')
		sphere1name_box.grid_remove()
		sphere1name_box.config(state='disabled')
		
	if (sphere2.get() == '1'):
		sphere3_spin.config(state='active')
		sphere2name_box.grid()
		sphere2name_box.config(state='readonly')
	else:
		sphere3.set('0')
		sphere3_spin.config(state='disabled')
		sphere2name_box.grid_remove()
		sphere2name_box.config(state='disabled')
		
	if (sphere3.get() == '1'):
		sphere3name_box.grid()
		sphere3name_box.config(state='readonly')
	else:
		sphere3name_box.grid_remove()
		sphere3name_box.config(state='disabled')
		
	if (occupation.get() == "RENOWNED"):
		sphere1name_box['values'] = ('Elemental', 'Healing', 'Nature', 'Protections', 'Psionics', 'Dark', 'Draconic', 'Light', 'Necromancy', 'Sigil', 'Wytchcraft')
		sphere2name_box['values'] = ('Elemental', 'Healing', 'Nature', 'Protections', 'Psionics', 'Dark', 'Draconic', 'Light', 'Necromancy', 'Sigil', 'Wytchcraft')
		sphere3name_box['values'] = ('Elemental', 'Healing', 'Nature', 'Protections', 'Psionics', 'Dark', 'Draconic', 'Light', 'Necromancy', 'Sigil', 'Wytchcraft')
	else:
		sphere1name_box['values'] = ('Elemental', 'Healing', 'Nature', 'Protections', 'Psionics', 'Necromancy', 'Sigil', 'Wytchcraft')
		sphere2name_box['values'] = ('Elemental', 'Healing', 'Nature', 'Protections', 'Psionics', 'Necromancy', 'Sigil', 'Wytchcraft')
		sphere3name_box['values'] = ('Elemental', 'Healing', 'Nature', 'Protections', 'Psionics', 'Necromancy', 'Sigil', 'Wytchcraft')
	
	set_slots()
	
	if (int(slotR.get()) > 0):
		sphereadv_spin.config(state='active')
	else:
		sphereadv.set('0')
		sphereadv_spin.config(state='disabled')
		
	if (slotR.get() == '10'):
		slotritual_cstvar.set('-')
	else:
		slotritual_cstvar.set(int(slotritual_base_cstvar.get()) * (1 + int(slotR.get())))
		
	# Warrior
	
	if (ambidexterity.get() == '1'):
		florentine_spin.config(state='active')
	else:
		florentine_spin.set('0')
		florentine_spin.config(state='disabled')
	
	sp_spc = int(spec_specific.get())
	sp_grp = int(spec_group.get())
	sly_spc = int(slay.get())
	sly_grp = int(slay_master.get())
	
	if (sp_spc > 0 or sp_grp > 0):
		slay_spin.config(state='active')
	if (sp_grp > 0):
		slay_master_spin.config(state='active')
	
	if (sly_spc > (sp_grp + sp_spc)):
		slay.set(sp_grp + sp_spc)
		sly_spc = sp_grp + sp_spc
	elif (sly_spc > sp_spc):
		if (sly_grp > (sp_grp - (sly_spc - sp_spc))):
			slay_master.set(sp_grp - (sly_spc - sp_spc))
			sly_grp = sp_grp - (sly_spc - sp_spc)
	else:
		if (sly_grp > sp_grp):
			slay_master.set(sp_grp)
			sly_grp = sp_grp
	
	sp_spc_free = sp_spc + sp_grp - sly_spc - sly_grp
	if (sly_spc > sp_spc):
		sp_grp_free = sp_grp - sly_grp - (sly_spc - sp_spc)
	else:
		sp_grp_free = sp_grp - sly_grp
	
	if (sp_spc_free == 0):
		slay_spin.config(to = sly_spc)
	else:
		slay_spin.config(to = 10)
		
	if (sp_grp_free == 0):
		slay_master_spin.config(to = sly_grp)
	else:
		slay_master_spin.config(to = 10)
		
	crt_spc = int(crit_spec.get())
	crt_grp = int(crit_group.get())
	exe_spc = int(execute.get())
	exe_grp = int(execute_master.get())
	
	if (crt_spc > 0 or crt_grp > 0):
		execute_spin.config(state='active')
	if (crt_grp > 0):
		execute_master_spin.config(state='active')
	
	if (exe_spc > (crt_grp + crt_spc)):
		execute.set(crt_grp + crt_spc)
		exe_spc = crt_grp + crt_spc
	elif (exe_spc > crt_spc):
		if (exe_grp > (crt_grp - (exe_spc - crt_spc))):
			execute_master.set(crt_grp - (exe_spc - crt_spc))
			exe_grp = crt_grp - (exe_spc - crt_spc)
	else:
		if (exe_grp > crt_grp):
			execute_master.set(crt_grp)
			exe_grp = crt_grp
	
	crt_spc_free = crt_spc + crt_grp - exe_spc - exe_grp
	if (exe_spc > crt_spc):
		crt_grp_free = crt_grp - exe_grp - (exe_spc - crt_spc)
	else:
		crt_grp_free = crt_grp - exe_grp
	
	if (crt_spc_free == 0):
		execute_spin.config(to = exe_spc)
	else:
		execute_spin.config(to = 10)
		
	if (crt_grp_free == 0):
		execute_master_spin.config(to = exe_grp)
	else:
		execute_master_spin.config(to = 10)
		
	if (crt_grp > 0 or crt_spc > 0 or (occupation.get() == 'Nightblade' and vocation.get() == '0' and int(occupational1.get()) > 0)):
		dodge_spin.config(state='active')
	else:
		dodge_spin.config(state='disabled')

	feint = 0
	
	if (occupation.get() == 'Nightblade' and vocation.get() == '0'):
		feint = int(occupational1.get())
	
	if (int(dodge.get()) > (crt_grp + crt_spc + feint)):
		dodge.set(crt_grp + crt_spc + feint)
		
	# Frag
	
	if (paragon.get() == '1'):
		paragon_level_spin.grid()
	else:
		paragon_level_spin.grid_remove()
	
	if ((int(trapper.get()) > 4 and school_current.get() == 'Rogue') or school_current.get() != 'Rogue'):
		frag2_spin.config(state='active')
	else:
		frag2_spin.set('0')
		frag2_spin.config(state='disabled')
	
	if (school_current.get() == 'Warrior'):
		if (int(slay.get()) + int(slay_master.get()) == 0):
			frag3_spin.config(state='disabled')
		else:
			frag3_spin.config(state='active')
		if (int(slay.get()) + int(slay_master.get()) > 9):
			frag3_spin.config(to = 10)
		else:
			frag3_spin.config(to = int(slay.get()) + int(slay_master.get()))
	
		if (int(frag3.get()) > (int(slay.get()) + int(slay_master.get()))):
			frag3.set(int(slay.get()) + int(slay_master.get()))
	
		if (int(frag3.get()) > (int(slay.get()) + int(slay_master.get()))):
			frag3.set(int(slay.get()) + int(slay_master.get()))
			
		if (flurry.get() == '0'):
			frag6_spin.config(state='disabled')
		else:
			frag6_spin.config(state='active')
		
		if(int(frag6.get()) > int(flurry.get())):
			frag6.set(flurry.get())
		
		frag6_spin.config(to = int(flurry.get()))
	elif (school_current.get() == 'Scholar'):
		if (self_mutilate.get() == '1'):
			frag1_spin.config(state='active')
		else:
			frag1_spin.set('0')
			frag1_spin.config(state='disabled')
			
		if (anatomy.get() == '1'):
			frag3_spin.config(state='active')
		else:
			frag3_spin.set('0')
			frag3_spin.config(state='disabled')
		
		frag6_spin.config(state='active')
		frag6_spin.config(to = 10)
	else:
		frag1_spin.config(to = 10)
		frag1_spin.config(state='active')
		frag3_spin.config(to = 10)
		frag3_spin.config(state='active')
		frag6_spin.config(to = 10)
		frag6_spin.config(state='active')
		
	if (int(mysticism.get()) > 0):
		hindsight_spin.config(state='active')
	else:
		hindsight_spin.set('0')
		hindsight_spin.config(state='disabled')
		
	# Spell Versatility

	if (slot1.get() == '0'):
		versa1_spin.config(state='disabled')
	else:
		versa1_spin.config(state='active')
	
	if(int(versa1.get()) > int(slot1.get())):
		versa1.set(slot1.get())
		
	if (slot2.get() == '0'):
		versa2_spin.config(state='disabled')
	else:
		versa2_spin.config(state='active')
	
	if(int(versa2.get()) > int(slot2.get())):
		versa2.set(slot2.get())
		
	if (slot3.get() == '0'):
		versa3_spin.config(state='disabled')
	else:
		versa3_spin.config(state='active')
	
	if(int(versa3.get()) > int(slot3.get())):
		versa3.set(slot3.get())
		
	if (slot4.get() == '0'):
		versa4_spin.config(state='disabled')
	else:
		versa4_spin.config(state='active')
	
	if(int(versa4.get()) > int(slot4.get())):
		versa4.set(slot4.get())	
	
	if (slot5.get() == '0'):
		versa5_spin.config(state='disabled')
	else:
		versa5_spin.config(state='active')
	
	if(int(versa5.get()) > int(slot5.get())):
		versa5.set(slot5.get())	
	
	if (slot6.get() == '0'):
		versa6_spin.config(state='disabled')
	else:
		versa6_spin.config(state='active')
	
	if(int(versa6.get()) > int(slot6.get())):
		versa6.set(slot6.get())	
	
	if (slot7.get() == '0'):
		versa7_spin.config(state='disabled')
	else:
		versa7_spin.config(state='active')
	
	if(int(versa7.get()) > int(slot7.get())):
		versa7.set(slot7.get())
		
	if (slot8.get() == '0'):
		versa8_spin.config(state='disabled')
	else:
		versa8_spin.config(state='active')
	
	if(int(versa8.get()) > int(slot8.get())):
		versa8.set(slot8.get())
		
	if (slot9.get() == '0'):
		versa9_spin.config(state='disabled')
	else:
		versa9_spin.config(state='active')
	
	if(int(versa9.get()) > int(slot9.get())):
		versa9.set(slot9.get())	
		
def set_occupationals(var_occupation):
	occup_1_name.set(occupation_dictionary[str(var_occupation)]["occ_1"])
	occup_2_name.set(occupation_dictionary[str(var_occupation)]["occ_2"])
	occup_3_name.set(occupation_dictionary[str(var_occupation)]["occ_3"])
	occup_4_name.set(occupation_dictionary[str(var_occupation)]["occ_4"])
	
def change_occupation(*args):
	if (vocation_on.get() == '0'):
		vocation_box.grid_remove()
		vocation.set('0')
		if (occupation.get() == "RENOWNED"):
			renowned_occupation_box.grid()
			set_occupationals(renowned_occupation.get())
			set_skill_costs(renowned_occupation.get())
			favoured.set('1')
		else:
			renowned_occupation.set('Dread Knight')
			renowned_occupation_box.grid_remove()
			set_occupationals(occupation.get())
			set_skill_costs(occupation.get())
			favoured.set('0')
	elif (vocation_on.get()== '1'):
		if (occupation.get() == "RENOWNED"):
			renowned_occupation_box.grid()
			favoured.set('1')
		else:
			renowned_occupation_box.grid_remove()
			favoured.set('0')
		vocation_box.grid()
		if (vocation.get() == '0'):
			vocation.set('Archer')
			set_occupationals('Archer')
		else:
			set_occupationals(vocation.get())
	
	set_CP_and_health(blankets.get())
	
	school = StringVar()
	if (occupation.get() == 'RENOWNED'):
		school.set(occupation_school[renowned_occupation.get()])
	else:
		school.set(occupation_school[occupation.get()])	
	if (school_current.get() == 'Warrior'):
		frag1_name.set(fragnames_warrior['1'])
		frag2_name.set(fragnames_warrior['2'])
		frag3_name.set(fragnames_warrior['3'])
		frag4_name.set(fragnames_warrior['4'])
		frag5_name.set(fragnames_warrior['5'])
		frag6_name.set(fragnames_warrior['6'])
		
		versa_name.set('')
		versa1name.set('')
		versa2name.set('')
		versa3name.set('')
		versa4name.set('')
		versa5name.set('')
		versa6name.set('')
		versa7name.set('')
		versa8name.set('')
		versa9name.set('')
	elif (school_current.get() == 'Rogue'):
		frag1_name.set(fragnames_rogue['1'])
		frag2_name.set(fragnames_rogue['2'])
		frag3_name.set(fragnames_rogue['3'])
		frag4_name.set(fragnames_rogue['4'])
		frag5_name.set(fragnames_rogue['5'])
		frag6_name.set(fragnames_rogue['6'])
		
		versa_name.set('')
		versa1name.set('')
		versa2name.set('')
		versa3name.set('')
		versa4name.set('')
		versa5name.set('')
		versa6name.set('')
		versa7name.set('')
		versa8name.set('')
		versa9name.set('')
	elif (school_current.get() == 'Scholar'):
		frag1_name.set(fragnames_scholar['1'])
		frag2_name.set(fragnames_scholar['2'])
		frag3_name.set(fragnames_scholar['3'])
		frag4_name.set(fragnames_scholar['4'])
		frag5_name.set(fragnames_scholar['5'])
		frag6_name.set(fragnames_scholar['6'])
		
		versa_name.set('Spell Versatility')
		versa1name.set('1')
		versa2name.set('2')
		versa3name.set('3')
		versa4name.set('4')
		versa5name.set('5')
		versa6name.set('6')
		versa7name.set('7')
		versa8name.set('8')
		versa9name.set('9')
	
	calc_spent_cp()
	set_skill_list()
	
def set_racials (var_race):
	racial_purch_name.set(racial_purchasable_names[var_race])
	racial_auto_name.set(racial_auto_names[var_race])

def change_race(*args):	
	if (race.get() == "Einher"):
		racial_bpb_spin.grid()
		
		lbl_bpb.set('Body Point Bonus')
		racial_bpb_cstvar.set('50')
		
		racial_str_spin.grid()
		lbl_str.set('Strength Bonus')
		racial_str_cstvar.set('50')
		
	elif (race.get() == "Gargylen" or race.get() == "Wild Elf"):
		racial_bpb_spin.grid()
		lbl_bpb.set('Body Point Bonus')
		racial_bpb_cstvar.set('50')
		
		racial_str_spin.grid_remove()
		racial_str.set('0')
		lbl_str.set('')
		racial_str_cstvar.set('')
	
	elif (race.get() == "Wolven"):
		racial_str_spin.grid()
		lbl_str.set('Strength Bonus')
		racial_str_cstvar.set('50')
		racial_bpb.set('0')
		
	else:
		racial_bpb_spin.grid_remove()
		lbl_bpb.set('')
		racial_bpb_cstvar.set('')
		racial_bpb.set('0')
		
		racial_str_spin.grid_remove()
		lbl_str.set('')
		racial_str_cstvar.set('')
		racial_str.set('0')
		
	if (race.get() == "FRAG"):
		frag_race_box.grid()
	else:
		frag_race_box.grid_remove()

	if (race.get() == "FRAG" and frag_race.get() == "0"):
		frag_race.set("Am'Rath")
		set_racials("Am'Rath")
	elif (race.get() == "FRAG"):
		set_racials(frag_race.get())
	else:
		frag_race.set('0')
		set_racials(race.get())
	
	set_CP_and_health(blankets.get())
	calc_spent_cp()
			
def set_skill_costs(var_occupation):

	if (var_occupation == "Assassin"):
		occ_dict = assassin_costs
		
	elif (var_occupation == "Bard"):
		occ_dict = bard_costs
		
	elif (var_occupation == "Druid"):
		occ_dict = druid_costs
		
	elif (var_occupation == "Mage"):
		occ_dict = mage_costs
		
	elif (var_occupation == "Mercenary"):
		occ_dict = merc_costs
		
	elif (var_occupation == "Nightblade"):
		occ_dict = nightblade_costs
		
	elif (var_occupation == "Ranger"):
		occ_dict = ranger_costs
		
	elif (var_occupation == "Templar"):
		occ_dict = templar_costs
		
	elif (var_occupation == "Witch Hunter"):
		occ_dict = witchhunter_costs
		
	elif (var_occupation == "Dread Knight" or var_occupation == "Paladin"):
		occ_dict = champion_costs
		
	elif (var_occupation == "Lightweaver" or var_occupation == "Darkweaver" or var_occupation == "Dragon Knight"):
		occ_dict = demagogue_costs
		
	else:
		print ("PROBLEM - INVALID CLASS")
		
	occupational1_cstvar.set('30')
	occupational2_cstvar.set('60')
	occupational3_cstvar.set('90')
	occupational4_cstvar.set('120')
	racial1_cstvar.set('50')
	
	#Production

	trapper_cstvar.set(occ_dict["trapsmith_cost"])
	create_scroll_cstvar.set(occ_dict["create_scroll_cost"])
	tradesman_cstvar.set(occ_dict["tradesman_cost"])
	alchemy_cstvar.set(occ_dict["alchemy_cost"])
	blacksmith_cstvar.set(occ_dict["blacksmith_cost"])
	chemistry_cstvar.set(occ_dict["chemistry_cost"])
	artifice_cstvar.set(occ_dict["artifice_cost"])

	#Frag

	teacher_cstvar.set(occ_dict["teacher_cost"])
	possum_cstvar.set(occ_dict["possum_cost"])
	looting_cstvar.set(occ_dict["looting_cost"])
	paragon_cstvar.set(occ_dict["paragon_cost"])
	hdrink_cstvar.set(occ_dict["heavy_drinker_cost"])
	create_alcohol_cstvar.set(occ_dict["create_alcohol_cost"])
	colddead_cstvar.set(occ_dict["cold_dead_hands_cost"])
	favoured_cstvar.set(occ_dict["favoured_cost"])
	hindsight_cstvar.set(occ_dict["hindsight_cost"])
	intuition_cstvar.set(occ_dict["intuition_cost"])

	#Scholar

	mysticism_cstvar.set(occ_dict["mysticism_cost"])
	demonic_arts_cstvar.set(occ_dict["demonic_arts_cost"])
	necromantic_arts_cstvar.set(occ_dict["necromantic_arts_cost"])
	anatomy_cstvar.set(occ_dict["anatomy_cost"])
	firstaid_cstvar.set(occ_dict["firstaid_cost"])
	physician_cstvar.set(occ_dict["physician_cost"])
	readwrite_cstvar.set(occ_dict["readwrite_cost"])
	readmagic_cstvar.set(occ_dict["readmagic_cost"])
	readmagic_advanced_cstvar.set(occ_dict["readmagic_advanced_cost"])
	readmagic_ritual_cstvar.set(occ_dict["readmagic_ritual_cost"])
	sphere1_cstvar.set(occ_dict["sphere1_cost"])
	sphere2_cstvar.set(occ_dict["sphere2_cost"])
	sphere3_cstvar.set(occ_dict["sphere3_cost"])
	sphereadv_cstvar.set(occ_dict["sphereadv_cost"])
	elemental_attune_cstvar.set(occ_dict["elemental_attune_cost"])
	slot1_cstvar.set(occ_dict["slot1_cost"])
	slot2_cstvar.set(occ_dict["slot2_cost"])
	slot3_cstvar.set(occ_dict["slot3_cost"])
	slot4_cstvar.set(occ_dict["slot4_cost"])
	slot5_cstvar.set(occ_dict["slot5_cost"])
	slot6_cstvar.set(occ_dict["slot6_cost"])
	slot7_cstvar.set(occ_dict["slot7_cost"])
	slot8_cstvar.set(occ_dict["slot8_cost"])
	slot9_cstvar.set(occ_dict["slot9_cost"])
	slotritual_base_cstvar.set(occ_dict["slotritual_cost"])
	
	#Frag Specific

	frag1_cstvar.set(occ_dict["frag1_cost"])
	frag2_cstvar.set(occ_dict["frag2_cost"])
	frag3_cstvar.set(occ_dict["frag3_cost"])
	frag4_cstvar.set(occ_dict["frag4_cost"])
	frag5_cstvar.set(occ_dict["frag5_cost"])
	frag6_cstvar.set(occ_dict["frag6_cost"])
	
	school = StringVar()
	if (occupation.get() == 'RENOWNED'):
		school.set(occupation_school[renowned_occupation.get()])
	else:
		school.set(occupation_school[occupation.get()])	
	
	if (school.get() == 'Scholar'):
		versa1_cstvar.set(int((int(slot1_cstvar.get()) / 2) + 5))
		versa2_cstvar.set(int((int(slot2_cstvar.get()) / 2) + 5))
		versa3_cstvar.set(int((int(slot3_cstvar.get()) / 2) + 5))
		versa4_cstvar.set(int((int(slot4_cstvar.get()) / 2) + 5))
		versa5_cstvar.set(int((int(slot5_cstvar.get()) / 2) + 5))
		versa6_cstvar.set(int((int(slot6_cstvar.get()) / 2) + 5))
		versa7_cstvar.set(int((int(slot7_cstvar.get()) / 2) + 5))
		versa8_cstvar.set(int((int(slot8_cstvar.get()) / 2) + 5))
		versa9_cstvar.set(int((int(slot9_cstvar.get()) / 2) + 5))
		
		versa1_spin.grid()
		versa2_spin.grid()
		versa3_spin.grid()
		versa4_spin.grid()
		versa5_spin.grid()
		versa6_spin.grid()
		versa7_spin.grid()
		versa8_spin.grid()
		versa9_spin.grid()
	else:
		versa1_cstvar.set('')
		versa2_cstvar.set('')
		versa3_cstvar.set('')
		versa4_cstvar.set('')
		versa5_cstvar.set('')
		versa6_cstvar.set('')
		versa7_cstvar.set('')
		versa8_cstvar.set('')
		versa9_cstvar.set('')

		versa1_spin.grid_remove()
		versa2_spin.grid_remove()
		versa3_spin.grid_remove()
		versa4_spin.grid_remove()
		versa5_spin.grid_remove()
		versa6_spin.grid_remove()
		versa7_spin.grid_remove()
		versa8_spin.grid_remove()
		versa9_spin.grid_remove()		

	#Warrior

	ambidexterity_cstvar.set(occ_dict["ambidexterity_cost"])
	florentine_cstvar.set(occ_dict["florentine_cost"])
	flurry_cstvar.set(occ_dict["flurry_cost"])
	heavy_armour_cstvar.set(occ_dict["heavy_armour_cost"])
	self_mutilate_cstvar.set(occ_dict["self_mutilate_cost"])
	shield_cstvar.set(occ_dict["shield_cost"])
	refocus_cstvar.set(occ_dict["refocus_cost"])
	groupprof_med_cstvar.set(occ_dict["groupprof_med_cost"])
	groupprof_large_cstvar.set(occ_dict["groupprof_large_cost"])
	prof_exotic_cstvar.set(occ_dict["prof_exotic_cost"])
	spec_group_cstvar.set(occ_dict["spec_group_cost"])
	spec_specific_cstvar.set(occ_dict["spec_specific_cost"])
	slay_cstvar.set(occ_dict["slay_cost"])
	slay_master_cstvar.set(occ_dict["slay_master_cost"])

	#Rogue

	garrotte_cstvar.set(occ_dict["garrotte_cost"])
	sap_cstvar.set(occ_dict["sap_cost"])
	vitalblow_cstvar.set(occ_dict["vitalblow_cost"])
	dodge_cstvar.set(occ_dict["dodge_cost"])
	crit_spec_cstvar.set(occ_dict["crit_spec_cost"])
	crit_group_cstvar.set(occ_dict["crit_group_cost"])
	execute_cstvar.set(occ_dict["execute_cost"])
	execute_master_cstvar.set(occ_dict["execute_master_cost"])
	
	calc_spent_cp()

def reset_school_frag_skills (new_school):
	if (new_school.get() != school_current.get()):
		frag1.set('0')
		frag2.set('0')
		frag3.set('0')
		frag4.set('0')
		frag5.set('0')
		frag6.set('0')
		versa1.set('0')
		versa2.set('0')
		versa3.set('0')
		versa4.set('0')
		versa5.set('0')
		versa6.set('0')
		versa7.set('0')
		versa8.set('0')
		versa9.set('0')
	
	if (new_school.get() == 'Scholar'):
		frag1_spin.config(to=1)
	else:
		frag1_spin.config(to=10)

	if (new_school.get() == 'Scholar'):
		frag3_spin.config(to=1)
	else:
		frag3_spin.config(to=10)
		
	if (new_school.get() == 'Warrior'):
		frag5_spin.config(to=10)
	else:
		frag5_spin.config(to=1)

def set_CP_and_health (num_blankets):
	if (int(num_blankets) < 94):
		CP.set(blanketconversion_dict[str(num_blankets)])
	else:
		CP.set(str(1760 + 10 * (num_blankets - 93)))
		
	if (race.get() == 'Human'):
		CP.set(int(CP.get()) + 50)
		
	CP_free.set(int(CP.get())-int(CP_spent.get()))
	level.set(int((int(CP.get())-50)/100))
	
	school = StringVar()
	if (occupation.get() == 'RENOWNED'):
		school.set(occupation_school[renowned_occupation.get()])
	else:
		school.set(occupation_school[occupation.get()])
	
	if (school.get() == 'Warrior'):
		HP.set(int(level.get())*2 +4)
	elif (school.get() == 'Rogue'):
		HP.set(int(level.get()) + 3)
	elif (school.get() == 'Scholar'):
		if (level.get() == '1'):
			HP.set('3')
		else:
			temp_HP = 3.0
			for x in range(1,int(level.get())):
				if (int(temp_HP) % 2 == 0):
					temp_HP = temp_HP + 0.5
				else:
					temp_HP = temp_HP + 1
			HP.set(int(temp_HP))
	
	if (int(racial_bpb.get()) > 0):
		HP.set(int(HP.get()) + int(racial_bpb.get()) * 5)
	if (race.get() == 'Human' or race.get() == 'Mountain Dwarf'):
		HP.set(int(HP.get()) + int(racial1.get()) * 5)
	if (race.get() == 'FRAG' and frag_race.get() == 'Ogre'):
		HP.set(int(HP.get()) + 5 + ((int(level.get()) - 1 ) * 2))

	if (int(CP_free.get()) < 0):
		CP_free_entry.config(foreground='red', font=boldfont)
	elif (int(CP_free.get()) > 0):
		CP_free_entry.config(foreground='black', font=normalfont)
		
	if (school.get() != school_current.get()):
		reset_school_frag_skills(school)
		
	school_current.set(school.get())

def set_skill_list(*args):
	skill_list_str = ''
	
	skill_list_str = skill_list_str + racial_auto_name.get()
	
	if (int(occupational1.get()) > 0):
		skill_list_str = skill_list_str + "\n" + occup_1_name.get() + " x" + occupational1.get()+ '	' + str(int(occupational1_cstvar.get()) * int(occupational1.get()))
	if (int(occupational2.get()) > 0):
		skill_list_str = skill_list_str + "\n" + occup_2_name.get() + " x" + occupational2.get()+ '	' + str(int(occupational2_cstvar.get()) * int(occupational2.get()))
	if (int(occupational3.get()) > 0):
		skill_list_str = skill_list_str + "\n" + occup_3_name.get() + " x" + occupational3.get()+ '	' + str(int(occupational3_cstvar.get()) * int(occupational3.get()))
	if (int(occupational4.get()) > 0):
		skill_list_str = skill_list_str + "\n" + occup_4_name.get() + " x" + occupational4.get()+ '	' + str(int(occupational4_cstvar.get()) * int(occupational4.get()))
	if (int(racial1.get()) > 0):
		skill_list_str = skill_list_str + "\n" + racial_purch_name.get() + " x" + racial1.get()+ '	' + str(int(racial1_cstvar.get()) * int(racial1.get()))
	if (racial_bpb.get() != '' and racial_bpb_cstvar.get () != '' and racial_bpb.get() != '0'):
		skill_list_str = skill_list_str + "\nBody Point Bonus x" + racial_bpb.get()+ '	' + str(int(racial_bpb_cstvar.get()) * int(racial_bpb.get()))
	if (racial_str.get() != '' and racial_str_cstvar.get () != '' and racial_str.get() != '0'):
		skill_list_str = skill_list_str + "\nStrength Bonus x" + racial_str.get()+ '	' + str(int(racial_str_cstvar.get()) * int(racial_str.get()))
		
	if (int(alchemy.get()) > 0):
		skill_list_str = skill_list_str + "\nAlchemy x" + alchemy.get()+ '	' + str(int(alchemy_cstvar.get()) * int(alchemy.get()))
	if (int(artifice.get()) > 0):
		skill_list_str = skill_list_str + "\nArtifice x" + artifice.get()+ '	' + str(int(artifice_cstvar.get()) * int(artifice.get()))
	if (int(blacksmith.get()) > 0):
		skill_list_str = skill_list_str + "\nBlacksmith x" + blacksmith.get()+ '	' + str(int(blacksmith_cstvar.get()) * int(blacksmith.get()))
	if (int(chemistry.get()) > 0):
		skill_list_str = skill_list_str + "\nChemistry x" + chemistry.get()+ '	' + str(int(chemistry_cstvar.get()) * int(chemistry.get()))
	if (int(create_scroll.get()) > 0):
		skill_list_str = skill_list_str + "\nCreate Scroll x" + create_scroll.get()+ '	' + str(int(create_scroll_cstvar.get()) * int(create_scroll.get()))
	if (int(tradesman.get()) > 0):
		skill_list_str = skill_list_str + "\nTradesman x" + tradesman.get()+ '	' + str(int(tradesman_cstvar.get()) * int(tradesman.get()))
	if (int(trapper.get()) > 0):
		skill_list_str = skill_list_str + "\nTrapper x" + trapper.get()+ '	' + str(int(trapper_cstvar.get()) * int(trapper.get()))
		
	if (int(anatomy.get()) > 0):
		skill_list_str = skill_list_str + "\nAnatomy" + '	' + str(int(anatomy_cstvar.get()) * int(anatomy.get()))
	if (int(firstaid.get()) > 0):
		skill_list_str = skill_list_str + "\nFirst Aid" + '	' + str(int(firstaid_cstvar.get()) * int(firstaid.get()))
	if (int(demonic_arts.get()) > 0):
		skill_list_str = skill_list_str + "\nDemonic/Angelic Arts" + '	' + str(int(demonic_arts_cstvar.get()) * int(demonic_arts.get()))
	if (int(necromantic_arts.get()) > 0):
		skill_list_str = skill_list_str + "\nNecromantic Arts" + '	' + str(int(necromantic_arts_cstvar.get()) * int(necromantic_arts.get()))
	if (int(readwrite.get()) > 0):
		skill_list_str = skill_list_str + "\nRead and Write" + '	' + str(int(readwrite_cstvar.get()) * int(readwrite.get()))
	if (int(readmagic.get()) > 0):
		skill_list_str = skill_list_str + "\nRead Magic" + '	' + str(int(readmagic_cstvar.get()) * int(readmagic.get()))
	if (int(readmagic_advanced.get()) > 0):
		skill_list_str = skill_list_str + "\nRead Magic Advanced" + '	' + str(int(readmagic_advanced_cstvar.get()) * int(readmagic_advanced.get()))
	if (int(readmagic_ritual.get()) > 0):
		skill_list_str = skill_list_str + "\nRead Magic Ritual" + '	' + str(int(readmagic_ritual_cstvar.get()) * int(readmagic_ritual.get()))
	if (int(sphere1.get()) > 0):
		skill_list_str = skill_list_str + "\nSphere 1: " + sphere1name.get() + '	' + str(int(sphere1_cstvar.get()) * int(sphere1.get()))
	if (int(sphere2.get()) > 0):
		skill_list_str = skill_list_str + "\nSphere 2: " + sphere2name.get() + '	' + str(int(sphere2_cstvar.get()) * int(sphere2.get()))
	if (int(sphere3.get()) > 0):
		skill_list_str = skill_list_str + "\nSphere 3: " + sphere3name.get() + " x" + sphere3.get() + '	' + str(int(necromantic_arts_cstvar.get()) * int(sphere3.get()))
	if (int(sphereadv.get()) > 0):
		skill_list_str = skill_list_str + "\nAdvanced Ritual Casting" + '	' + str(int(sphereadv_cstvar.get()) * int(sphereadv.get()))
	
	if (int(physician.get()) > 0):
		skill_list_str = skill_list_str + "\nPhysician x" + physician.get() + '	' + str(int(firstaid_cstvar.get()) * int(physician.get()))
	if (int(mysticism.get()) > 0):
		skill_list_str = skill_list_str + "\nMysticism x" + mysticism.get() + '	' + str(int(demonic_arts_cstvar.get()) * int(mysticism.get()))
	if (int(elemental_attune.get()) > 0):
		skill_list_str = skill_list_str + "\nElemental Attunement x" + elemental_attune.get() + '	' + str(int(elemental_attune_cstvar.get()) * int(elemental_attune.get()))
		
	if (int(slot1.get()) > 0):
		skill_list_str = skill_list_str + "\nSlot 1 x" + slot1.get() + '	' + str(int(slot1_cstvar.get()) * int(slot1.get()))
	if (int(slot2.get()) > 0):
		skill_list_str = skill_list_str + "\nSlot 2 x" + slot2.get() + '	' + str(int(slot2_cstvar.get()) * int(slot2.get()))
	if (int(slot3.get()) > 0):
		skill_list_str = skill_list_str + "\nSlot 3 x" + slot3.get() + '	' + str(int(slot3_cstvar.get()) * int(slot3.get()))
	if (int(slot4.get()) > 0):
		skill_list_str = skill_list_str + "\nSlot 4 x" + slot4.get() + '	' + str(int(slot4_cstvar.get()) * int(slot4.get()))
	if (int(slot5.get()) > 0):
		skill_list_str = skill_list_str + "\nSlot 5 x" + slot5.get() + '	' + str(int(slot5_cstvar.get()) * int(slot5.get()))
	if (int(slot6.get()) > 0):
		skill_list_str = skill_list_str + "\nSlot 6 x" + slot6.get() + '	' + str(int(slot6_cstvar.get()) * int(slot6.get()))
	if (int(slot7.get()) > 0):
		skill_list_str = skill_list_str + "\nSlot 7 x" + slot7.get() + '	' + str(int(slot7_cstvar.get()) * int(slot7.get()))
	if (int(slot8.get()) > 0):
		skill_list_str = skill_list_str + "\nSlot 8 x" + slot8.get() + '	' + str(int(slot8_cstvar.get()) * int(slot8.get()))
	if (int(slot9.get()) > 0):
		skill_list_str = skill_list_str + "\nSlot 9 x" + slot9.get() + '	' + str(int(slot9_cstvar.get()) * int(slot9.get()))
	if (int(slotR.get()) > 0):
		slotRCP = 0
		for x in range (int(slotR.get())):
			slotRCP = slotRCP + (x + 1) * int(slotritual_base_cstvar.get())
		skill_list_str = skill_list_str + "\nSlot Ritual x" + slotR.get() + '	' + str(slotRCP)
	
	if (int(ambidexterity.get()) > 0):
	 skill_list_str = skill_list_str + "\nAmbidexterity" + '	' + str(int(ambidexterity_cstvar.get()) * int(ambidexterity.get()))
	if (int(florentine.get()) > 0):
		 skill_list_str = skill_list_str + "\nFlorentine" + '	' + str(int(florentine_cstvar.get()) * int(florentine.get()))
	if (int(flurry.get()) > 0):
		skill_list_str = skill_list_str + "\nFlurry of Blows x" + flurry.get()+ '	' + str(int(flurry_cstvar.get()) * int(flurry.get()))
	if (int(heavy_armour.get()) > 0):
		 skill_list_str = skill_list_str + "\nHeavy Armour" + '	' + str(int(heavy_armour_cstvar.get()) * int(heavy_armour.get()))	
	if (int(self_mutilate.get()) > 0):
		 skill_list_str = skill_list_str + "\nSelf Mutilate" + '	' + str(int(self_mutilate_cstvar.get()) * int(self_mutilate.get()))
	if (int(shield.get()) > 0):
		 skill_list_str = skill_list_str + "\nShield" + '	' + str(int(shield_cstvar.get()) * int(shield.get()))
	if (int(refocus.get()) > 0):
		skill_list_str = skill_list_str + "\nWeapon Refocus x" + refocus.get()+ '	' + str(int(refocus_cstvar.get()) * int(refocus.get()))
	if (int(groupprof_med.get()) > 0):
		 skill_list_str = skill_list_str + "\nWeapon Prof: Medium" + '	' + str(int(groupprof_med_cstvar.get()) * int(groupprof_med.get()))
	if (int(groupprof_large.get()) > 0):
		 skill_list_str = skill_list_str + "\nWeapon Prof: Large" + '	' + str(int(groupprof_large_cstvar.get()) * int(groupprof_large.get()))
	if (int(prof_exotic.get()) > 0):
		skill_list_str = skill_list_str + "\nWeapon Prof: Exotic x" + prof_exotic.get()+ '	' + str(int(prof_exotic_cstvar.get()) * int(prof_exotic.get()))
	if (int(spec_group.get()) > 0):
		skill_list_str = skill_list_str + "\nSpec +1: Group x" + spec_group.get()+ '	' + str(int(spec_group_cstvar.get()) * int(spec_group.get()))
	if (int(spec_specific.get()) > 0):
		skill_list_str = skill_list_str + "\nSpec +1: Specific x" + spec_specific.get()+ '	' + str(int(spec_specific_cstvar.get()) * int(spec_specific.get()))
	if (int(slay.get()) > 0):
		skill_list_str = skill_list_str + "\nSlay/Parry x" + slay.get()+ '	' + str(int(slay_cstvar.get()) * int(slay.get()))
	if (int(slay_master.get()) > 0):
		skill_list_str = skill_list_str + "\nSlay/Parry Master x" + slay_master.get()+ '	' + str(int(slay_master_cstvar.get()) * int(slay_master.get()))

	if (int(garrotte.get()) > 0):
		skill_list_str = skill_list_str + "\nGarrotte" + '	' + str(int(garrotte_cstvar.get()) * int(garrotte.get()))
	if (int(sap.get()) > 0):
		skill_list_str = skill_list_str + "\nSap x" + sap.get()+ '	' + str(int(sap_cstvar.get()) * int(sap.get()))
	if (int(vitalblow.get()) > 0):
		skill_list_str = skill_list_str + "\nVital Blow x" + vitalblow.get()+ '	' + str(int(vitalblow_cstvar.get()) * int(vitalblow.get()))
	if (int(dodge.get()) > 0):
		skill_list_str = skill_list_str + "\nDodge x" + dodge.get()+ '	' + str(int(dodge_cstvar.get()) * int(dodge.get()))
	if (int(crit_spec.get()) > 0):
		skill_list_str = skill_list_str + "\nCritical +2: Specific x" + crit_spec.get()+ '	' + str(int(crit_spec_cstvar.get()) * int(crit_spec.get()))
	if (int(crit_group.get()) > 0):
		skill_list_str = skill_list_str + "\nCritical +2: Group x" + crit_group.get()+ '	' + str(int(crit_group_cstvar.get()) * int(crit_group.get()))
	if (int(execute.get()) > 0):
		skill_list_str = skill_list_str + "\nExecute x" + execute.get()+ '	' + str(int(execute_cstvar.get()) * int(execute.get()))
	if (int(execute_master.get()) > 0):
		skill_list_str = skill_list_str + "\nExecute: Master x" + execute_master.get()+ '	' + str(int(execute_master_cstvar.get()) * int(execute_master.get()))
	
	if (int(colddead.get()) > 0):
		skill_list_str = skill_list_str + "\nCold Dead Hands" + '	' + str(int(colddead_cstvar.get()) * int(colddead.get()))
	if (int(create_alcohol.get()) > 0):
		skill_list_str = skill_list_str + "\nCreate Alcohol x" + create_alcohol.get()+ '	' + str(int(create_alcohol_cstvar.get()) * int(create_alcohol.get()))
	if (int(favoured.get()) > 0):
		skill_list_str = skill_list_str + "\nFavoured" + '	' + str(int(favoured_cstvar.get()) * int(favoured.get()))
	if (int(hdrink.get()) > 0):
		skill_list_str = skill_list_str + "\nHeavy Drinker" + '	' + str(int(hdrink_cstvar.get()) * int(hdrink.get()))
	if (int(hindsight.get()) > 0):
		skill_list_str = skill_list_str + "\nHindsight" + '	' + str(int(hindsight_cstvar.get()) * int(hindsight.get()))
	if (int(looting.get()) > 0):
		skill_list_str = skill_list_str + "\nLooting x" + looting.get()+ '	' + str(int(looting_cstvar.get()) * int(looting.get()))
	if (int(intuition.get()) > 0):
		skill_list_str = skill_list_str + "\nIntuition" + '	' + str(int(intuition_cstvar.get()) * int(intuition.get()))
	if (int(paragon.get()) > 0):
		skill_list_str = skill_list_str + "\nParagon" + '	' + str(int(paragon_cstvar.get()) * int(paragon.get()))
	if (int(possum.get()) > 0):
		skill_list_str = skill_list_str + "\nPossum x" + possum.get()+ '	' + str(int(possum_cstvar.get()) * int(possum.get()))
	if (int(teacher.get()) > 0):
		skill_list_str = skill_list_str + "\nTeacher x" + '	' + str(int(teacher_cstvar.get()) * int(teacher.get()))

	if (int(frag1.get()) > 0):
		skill_list_str = skill_list_str + "\n" + frag1_name.get() + " x" + frag1.get()+ '	' + str(int(frag1_cstvar.get()) * int(frag1.get()))
	if (int(frag2.get()) > 0):
		skill_list_str = skill_list_str + "\n" + frag2_name.get() + " x" + frag2.get()+ '	' + str(int(frag2_cstvar.get()) * int(frag2.get()))
	if (int(frag3.get()) > 0):
		skill_list_str = skill_list_str + "\n" + frag3_name.get() + " x" + frag3.get()+ '	' + str(int(frag3_cstvar.get()) * int(frag3.get()))
	if (int(frag4.get()) > 0):
		skill_list_str = skill_list_str + "\n" + frag4_name.get() + " x" + frag4.get()+ '	' + str(int(frag4_cstvar.get()) * int(frag4.get()))
	if (int(frag5.get()) > 0):
		skill_list_str = skill_list_str + "\n" + frag5_name.get() + " x" + frag5.get()+ '	' + str(int(frag5_cstvar.get()) * int(frag5.get()))
	if (int(frag6.get()) > 0):
		skill_list_str = skill_list_str + "\n" + frag6_name.get() + " x" + frag6.get()+ '	' + str(int(frag6_cstvar.get()) * int(frag6.get()))
	
	school = StringVar()
	if (occupation.get() == 'RENOWNED'):
		school.set(occupation_school[renowned_occupation.get()])
	else:
		school.set(occupation_school[occupation.get()])	
	
	if (school.get() == 'Scholar'):
		if (int(versa1.get()) > 0):
			skill_list_str = skill_list_str + "\nSpell Versatility 1 x" + versa1.get() + '	' + str(int(versa1_cstvar.get()) * int(versa1.get()))
		if (int(versa2.get()) > 0):
			skill_list_str = skill_list_str + "\nSpell Versatility 2 x" + versa2.get() + '	' + str(int(versa2_cstvar.get()) * int(versa2.get()))
		if (int(versa3.get()) > 0):
			skill_list_str = skill_list_str + "\nSpell Versatility 3 x" + versa3.get() + '	' + str(int(versa3_cstvar.get()) * int(versa3.get()))
		if (int(versa4.get()) > 0):
			skill_list_str = skill_list_str + "\nSpell Versatility 4 x" + versa4.get() + '	' + str(int(versa4_cstvar.get()) * int(versa4.get()))
		if (int(versa5.get()) > 0):
			skill_list_str = skill_list_str + "\nSpell Versatility 5 x" + versa5.get() + '	' + str(int(versa5_cstvar.get()) * int(versa5.get()))
		if (int(versa6.get()) > 0):
			skill_list_str = skill_list_str + "\nSpell Versatility 6 x" + versa6.get() + '	' + str(int(versa6_cstvar.get()) * int(versa6.get()))
		if (int(versa7.get()) > 0):
			skill_list_str = skill_list_str + "\nSpell Versatility 7 x" + versa7.get() + '	' + str(int(versa7_cstvar.get()) * int(versa7.get()))
		if (int(versa8.get()) > 0):
			skill_list_str = skill_list_str + "\nSpell Versatility 8 x" + versa8.get() + '	' + str(int(versa8_cstvar.get()) * int(versa8.get()))
		if (int(versa9.get()) > 0):
			skill_list_str = skill_list_str + "\nSpell Versatility 9 x" + versa9.get() + '	' + str(int(versa9_cstvar.get()) * int(versa9.get()))
		
	try:
		skill_list_str = skill_list_str[0:]
		all_skills['state'] = 'normal'
		all_skills.delete('1.0', 'end -1 chars')
		all_skills.insert('0.0 -1 chars', skill_list_str)
		all_skills['state'] = 'disabled'
	except:
		temp = 0

def calc_spent_cp(*args):

	depend_check()

	spent_CP = 0
	
	spent_CP = spent_CP + int(trapper.get()) * int(trapper_cstvar.get())
	spent_CP = spent_CP + int(create_scroll.get()) * int(create_scroll_cstvar.get())
	spent_CP = spent_CP + int(tradesman.get()) * int(tradesman_cstvar.get())
	spent_CP = spent_CP + int(alchemy.get()) * int(alchemy_cstvar.get())
	spent_CP = spent_CP + int(blacksmith.get()) * int(blacksmith_cstvar.get())
	spent_CP = spent_CP + int(chemistry.get()) * int(chemistry_cstvar.get())
	spent_CP = spent_CP + int(artifice.get()) * int(artifice_cstvar.get())
	
	spent_CP = spent_CP + int(anatomy.get()) * int(anatomy_cstvar.get())
	spent_CP = spent_CP + int(firstaid.get()) * int(firstaid_cstvar.get())
	spent_CP = spent_CP + int(demonic_arts.get()) * int(demonic_arts_cstvar.get())
	spent_CP = spent_CP + int(necromantic_arts.get()) * int(necromantic_arts_cstvar.get())
	spent_CP = spent_CP + int(readwrite.get()) * int(readwrite_cstvar.get())
	spent_CP = spent_CP + int(readmagic.get()) * int(readmagic_cstvar.get())
	spent_CP = spent_CP + int(readmagic_advanced.get()) * int(readmagic_advanced_cstvar.get())
	spent_CP = spent_CP + int(sphere1.get()) * int(sphere1_cstvar.get())
	spent_CP = spent_CP + int(sphere2.get()) * int(sphere2_cstvar.get())
	spent_CP = spent_CP + int(readmagic_ritual.get()) * int(readmagic_ritual_cstvar.get())
	spent_CP = spent_CP + int(sphereadv.get()) * int(sphereadv_cstvar.get())
	spent_CP = spent_CP + int(physician.get()) * int(physician_cstvar.get())
	spent_CP = spent_CP + int(mysticism.get()) * int(mysticism_cstvar.get())
	spent_CP = spent_CP + int(sphere3.get()) * int(sphere3_cstvar.get())
	spent_CP = spent_CP + int(elemental_attune.get()) * int(elemental_attune_cstvar.get())
	
	spent_CP = spent_CP + int(slot1.get()) * int(slot1_cstvar.get())
	spent_CP = spent_CP + int(slot2.get()) * int(slot2_cstvar.get())
	spent_CP = spent_CP + int(slot3.get()) * int(slot3_cstvar.get())
	spent_CP = spent_CP + int(slot4.get()) * int(slot4_cstvar.get())
	spent_CP = spent_CP + int(slot5.get()) * int(slot5_cstvar.get())
	spent_CP = spent_CP + int(slot6.get()) * int(slot6_cstvar.get())
	spent_CP = spent_CP + int(slot7.get()) * int(slot7_cstvar.get())
	spent_CP = spent_CP + int(slot8.get()) * int(slot8_cstvar.get())
	spent_CP = spent_CP + int(slot9.get()) * int(slot9_cstvar.get())
	for x in range (int(slotR.get())):
		spent_CP = spent_CP + (x + 1) * int(slotritual_base_cstvar.get())
	
	spent_CP = spent_CP + int(ambidexterity.get()) * int(ambidexterity_cstvar.get())
	spent_CP = spent_CP + int(florentine.get()) * int(florentine_cstvar.get())
	spent_CP = spent_CP + int(flurry.get()) * int(flurry_cstvar.get())
	spent_CP = spent_CP + int(heavy_armour.get()) * int(heavy_armour_cstvar.get())
	spent_CP = spent_CP + int(self_mutilate.get()) * int(self_mutilate_cstvar.get())
	spent_CP = spent_CP + int(shield.get()) * int(shield_cstvar.get())
	spent_CP = spent_CP + int(refocus.get()) * int(refocus_cstvar.get())
	spent_CP = spent_CP + int(groupprof_med.get()) * int(groupprof_med_cstvar.get())
	spent_CP = spent_CP + int(groupprof_large.get()) * int(groupprof_large_cstvar.get())
	spent_CP = spent_CP + int(prof_exotic.get()) * int(prof_exotic_cstvar.get())
	spent_CP = spent_CP + int(spec_group.get()) * int(spec_group_cstvar.get())
	spent_CP = spent_CP + int(spec_specific.get()) * int(spec_specific_cstvar.get())
	spent_CP = spent_CP + int(slay.get()) * int(slay_cstvar.get())
	spent_CP = spent_CP + int(slay_master.get()) * int(slay_master_cstvar.get())
	
	spent_CP = spent_CP + int(garrotte.get()) * int(garrotte_cstvar.get())
	spent_CP = spent_CP + int(sap.get()) * int(sap_cstvar.get())
	spent_CP = spent_CP + int(vitalblow.get()) * int(vitalblow_cstvar.get())
	spent_CP = spent_CP + int(dodge.get()) * int(dodge_cstvar.get())
	spent_CP = spent_CP + int(crit_spec.get()) * int(crit_spec_cstvar.get())
	spent_CP = spent_CP + int(crit_group.get()) * int(crit_group_cstvar.get())
	spent_CP = spent_CP + int(execute.get()) * int(execute_cstvar.get())
	spent_CP = spent_CP + int(execute_master.get()) * int(execute_master_cstvar.get())

	spent_CP = spent_CP + int(colddead.get()) * int(colddead_cstvar.get())
	spent_CP = spent_CP + int(create_alcohol.get()) * int(create_alcohol_cstvar.get())
	spent_CP = spent_CP + int(favoured.get()) * int(favoured_cstvar.get())
	spent_CP = spent_CP + int(hdrink.get()) * int(hdrink_cstvar.get())
	spent_CP = spent_CP + int(hindsight.get()) * int(hindsight_cstvar.get())
	spent_CP = spent_CP + int(looting.get()) * int(looting_cstvar.get())
	spent_CP = spent_CP + int(intuition.get()) * int(intuition_cstvar.get())
	spent_CP = spent_CP + int(possum.get()) * int(possum_cstvar.get())
	spent_CP = spent_CP + int(teacher.get()) * int(teacher_cstvar.get())
	spent_CP = spent_CP + int(frag1.get()) * int(frag1_cstvar.get())
	spent_CP = spent_CP + int(frag2.get()) * int(frag2_cstvar.get())
	spent_CP = spent_CP + int(frag3.get()) * int(frag3_cstvar.get())
	spent_CP = spent_CP + int(frag4.get()) * int(frag4_cstvar.get())
	spent_CP = spent_CP + int(frag5.get()) * int(frag5_cstvar.get())
	spent_CP = spent_CP + int(frag6.get()) * int(frag6_cstvar.get())
	
	if (int(paragon_level.get()) == 1):
		paragon_cstvar.set(int(slot1_cstvar.get()) + 10)
	elif (int(paragon_level.get()) == 2):
		paragon_cstvar.set(int(slot2_cstvar.get()) + 10)
	elif (int(paragon_level.get()) == 3):
		paragon_cstvar.set(int(slot3_cstvar.get()) + 10)
	elif (int(paragon_level.get()) == 4):
		paragon_cstvar.set(int(slot4_cstvar.get()) + 10)
	elif (int(paragon_level.get()) == 5):
		paragon_cstvar.set(int(slot5_cstvar.get()) + 10)
	elif (int(paragon_level.get()) == 6):
		paragon_cstvar.set(int(slot6_cstvar.get()) + 10)
	elif (int(paragon_level.get()) == 7):
		paragon_cstvar.set(int(slot7_cstvar.get()) + 10)
	spent_CP = spent_CP + int(paragon.get()) * int(paragon_cstvar.get())
	
	school = StringVar()
	if (occupation.get() == 'RENOWNED'):
		school.set(occupation_school[renowned_occupation.get()])
	else:
		school.set(occupation_school[occupation.get()])	
		
	if (school.get() == 'Scholar'):
		spent_CP = spent_CP + int(versa1.get()) * int(versa1_cstvar.get())
		spent_CP = spent_CP + int(versa2.get()) * int(versa2_cstvar.get())
		spent_CP = spent_CP + int(versa3.get()) * int(versa3_cstvar.get())
		spent_CP = spent_CP + int(versa4.get()) * int(versa4_cstvar.get())
		spent_CP = spent_CP + int(versa5.get()) * int(versa5_cstvar.get())
		spent_CP = spent_CP + int(versa6.get()) * int(versa6_cstvar.get())
		spent_CP = spent_CP + int(versa7.get()) * int(versa7_cstvar.get())
		spent_CP = spent_CP + int(versa8.get()) * int(versa8_cstvar.get())
		spent_CP = spent_CP + int(versa9.get()) * int(versa9_cstvar.get())
	spent_CP = spent_CP + int(occupational1.get()) * int(occupational1_cstvar.get())
	spent_CP = spent_CP + int(occupational2.get()) * int(occupational2_cstvar.get())
	spent_CP = spent_CP + int(occupational3.get()) * int(occupational3_cstvar.get())
	spent_CP = spent_CP + int(occupational4.get()) * int(occupational4_cstvar.get())
	spent_CP = spent_CP + int(racial1.get()) * int(racial1_cstvar.get())
	if (racial_bpb.get() != '' and racial_bpb_cstvar.get() != ''):
		spent_CP = spent_CP + int(racial_bpb.get()) * int(racial_bpb_cstvar.get())
	if (racial_str.get() != '' and racial_str_cstvar.get() != ''):
		spent_CP = spent_CP + int(racial_str.get()) * int(racial_str_cstvar.get())

	CP_spent.set(str(spent_CP))
	CP_free.set(int(CP.get()) - int(CP_spent.get()))
	
	if (int(CP_free.get()) < 0):
		CP_free_entry.config(foreground='red', font=boldfont)
	elif (int(CP_free.get()) > 0):
		CP_free_entry.config(foreground='black', font=normalfont)
		
	set_skill_list()

def reset ():	
	CP_free_entry.config(foreground='black', font=normalfont)
	
	vallist = {'1', '2', '3', 'yes'}
	sphere1name_box.config(values=vallist)
	sphere1name_box.config(values=['no', 'yes'])
	
	player_name.set('')
	char_name.set('')
	race.set('Ajaunti')
	occupation.set('Mercenary')
	renowned_occupation.set('Dread Knight')
	vocation.set('0')
	frag_race.set('0')
	level.set('1')
	
	occupational1.set('0')
	occupational2.set('0')
	occupational3.set('0')
	occupational4.set('0')
	racial1.set('0')
	racial_bpb.set('0')
	racial_str.set('0')
	
	trapper.set('0')
	create_scroll.set('0')
	tradesman.set('0')
	alchemy.set('0')
	blacksmith.set('0')
	chemistry.set('0')
	artifice.set('0')
	
	anatomy.set('0')
	firstaid.set('0')
	physician.set('0')
	mysticism.set('0')
	demonic_arts.set('0')
	necromantic_arts.set('0')
	readwrite.set('0')
	readmagic.set('0')
	readmagic_advanced.set('0')
	sphere1.set('0')
	sphere2.set('0')
	sphere3.set('0')
	sphere1name.set('Elemental')
	sphere2name.set('Healing')
	sphere3name.set('Nature')
	readmagic_ritual.set('0')
	sphereadv.set('0')
	elemental_attune.set('0')
	
	slot1.set('0')
	slot2.set('0')
	slot3.set('0')
	slot4.set('0')
	slot5.set('0')
	slot6.set('0')
	slot7.set('0')
	slot8.set('0')
	slot9.set('0')
	slotR.set('0')
	
	ambidexterity.set('0')
	florentine.set('0')
	flurry.set('0')
	heavy_armour.set('0')
	self_mutilate.set('0')
	shield.set('0')
	refocus.set('0')
	groupprof_med.set('0')
	groupprof_large.set('0')
	prof_exotic.set('0')
	spec_group.set('0')
	spec_specific.set('0')
	slay.set('0')
	slay_master.set('0')
	
	garrotte.set('0')
	sap.set('0')
	vitalblow.set('0')
	dodge.set('0')
	crit_spec.set('0')
	crit_group.set('0')
	execute.set('0')
	execute_master.set('0')
	
	colddead.set('0')
	create_alcohol.set('0')
	favoured.set('0')
	hdrink.set('0')
	hindsight.set('0')
	looting.set('0')
	intuition.set('0')
	paragon.set('0')
	paragon_level.set('1')
	possum.set('0')
	teacher.set('0')
	frag1.set('0')
	frag2.set('0')
	frag3.set('0')
	frag4.set('0')
	frag5.set('0')
	frag6.set('0')
	
	versa1.set('0')
	versa2.set('0')
	versa3.set('0')
	versa4.set('0')
	versa5.set('0')
	versa6.set('0')
	versa7.set('0')
	versa8.set('0')
	versa9.set('0')
	
	frag1_name.set(fragnames_warrior['1'])
	frag2_name.set(fragnames_warrior['2'])
	frag3_name.set(fragnames_warrior['3'])
	frag4_name.set(fragnames_warrior['4'])
	frag5_name.set(fragnames_warrior['5'])
	frag6_name.set(fragnames_warrior['6'])
	
	vocation_on.set('0')
	CP.set('0')
	CP_spent.set('0')
	blankets.set('0')
	change_occupation()
	change_race()
	set_CP_and_health(0)
	lbl_bpb.set('')
	racial_bpb_cstvar.set('')
	lbl_str.set('')
	racial_str_cstvar.set('')
	racial1_cstvar.set('50')

##### Visuals

normal_font = font.Font(weight='normal')

# Major frame set up

mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

leftframe = ttk.Frame(mainframe, padding="3 3 3 3")
leftframe.grid(column=0, row=0, sticky=(N, W, E, S))

rightframe = ttk.Frame(mainframe, padding="3 3 3 3")
rightframe.grid(column=1, row=0, sticky=(N, W, E, S))

skilllistframe = ttk.Frame(leftframe, padding="1 1 1 1")
skilllistframe.grid(column=0, row=10, sticky=(N, W, E, S))

# Style
boldfont = font.Font(weight='bold',size=10)
normalfont = font.Font(size=10)

### Left frame

# In-Frames

blanketframe_left = ttk.Frame(leftframe, padding="0 0 0 0")
blanketframe_left.grid(column=0, row=10, sticky=(N, W, E, S))
blanketframe_right = ttk.Frame(leftframe, padding="0 0 0 0")
blanketframe_right.grid(column=1, row=10, sticky=(N, W, E, S))

# Frame inputs

ttk.Label(leftframe, text='Player Name', font=boldfont).grid(column=0, row=0, sticky=W)
player_name_entry = ttk.Entry(leftframe, width=23, textvariable=player_name, font=normalfont)
player_name_entry.grid(column=0,row=1, sticky=W)

ttk.Label(leftframe, text='Character Name', font=boldfont).grid(column=0, row=2, sticky=W)
char_name_entry = ttk.Entry(leftframe, width=23, textvariable=char_name, font=normalfont)
char_name_entry.grid(column=0,row=3, sticky=W)

ttk.Label(leftframe, text='Race', font=boldfont).grid(column=0, row=4, sticky=W)
race_box = ttk.Combobox(leftframe, width=20, textvariable=race, font=normalfont)
race_box.grid(column=0, row=5, sticky=W)
race_box.state(["readonly"])
race_box['values'] = ('Ajaunti', 'Dark Elf', 'Einher', 'Gargylen', 'High Elf', 'Hobling', 'Human', 'Mountain Dwarf', 'Orc', "Savar'Aving", 'Wild Elf', 'Wood Fae', 'FRAG')
race.set('Ajaunti')

race_box.bind("<<ComboboxSelected>>", change_race)

frag_race_box = ttk.Combobox(leftframe, width=20, textvariable=frag_race, font=normalfont)
frag_race_box.grid(column=1, row=5, sticky=W)
frag_race_box.state(["readonly"])
frag_race_box['values'] = ("Am'Rath", 'Avian', 'Carnal Fae', 'Draconian', 'Faceless', 'Faun', 'Fire Elf', 'Gnome', 'Goblin', 'Ice Elf', 'Kobold', 'Minotaur', 'Ogre', 'Risen', 'Sidhe', 'Squamata', 'Vulcan Dwarf', 'Wolven')
frag_race_box.grid_remove()

frag_race_box.bind("<<ComboboxSelected>>", change_race)

ttk.Label(leftframe, text='Class', font=boldfont).grid(column=0, row=6, sticky=W)
occupation_box = ttk.Combobox(leftframe, width=20, textvariable=occupation, font=normalfont)
occupation_box.grid(column=0, row=7, sticky=W)
occupation_box.state(["readonly"])
occupation_box['values'] = ('Mercenary', 'Ranger', 'Templar', 'Nightblade', 'Assassin', 'Witch Hunter', 'Mage', 'Druid', 'Bard', 'RENOWNED')
occupation.set('Mercenary')

occupation_box.bind("<<ComboboxSelected>>", change_occupation)

renowned_occupation_box = ttk.Combobox(leftframe, width=20, textvariable=renowned_occupation, font=normalfont)
renowned_occupation_box.grid(column=1, row=7, sticky=W)
renowned_occupation_box.state(["readonly"])
renowned_occupation_box['values'] = ('Dread Knight', 'Paladin', 'Darkweaver', 'Lightweaver', 'Dragon Knight')
renowned_occupation_box.grid_remove()

renowned_occupation_box.bind("<<ComboboxSelected>>", change_occupation)

vocation_check = ttk.Checkbutton(leftframe, text='Vocation?', command=change_occupation, variable=vocation_on)
vocation_check.grid(column=0, row=8, sticky=W)

vocation_box = ttk.Combobox(leftframe, width=20, textvariable=vocation, font=normalfont)
vocation_box.grid(column=1, row=8, sticky=W)
vocation_box.state(["readonly"])
vocation_box['values'] = ('Archer', 'Artisan', 'Battle Mage', 'Brew Master', 'Shaman', 'Stalwart', 'Swashbuckler', 'Undead Hunter')
vocation_box.grid_remove()
vocation_box.bind("<<ComboboxSelected>>", change_occupation)

ttk.Label(blanketframe_left, text='Blankets', font=boldfont, width=12).grid(column=0, row=0, sticky=W)
blanket_spin = ttk.Spinbox(blanketframe_left, from_=0, to=400, width=6, textvariable=blankets, font=normalfont)
blanket_spin.grid(column=0, row=1, sticky=W)
blanket_spin.bind("<<Increment>>", change_blankets_up)
blanket_spin.bind("<<Decrement>>", change_blankets_down)
blanket_spin.bind('<Return>', change_blankets_manual)

ttk.Label(blanketframe_left, text='CP', font=boldfont).grid(column=1, row=0, sticky=W)
CP_entry = ttk.Entry(blanketframe_left, width=7, textvariable=CP, font=normalfont)
CP_entry.state(["readonly"])
CP_entry.grid(column=1,row=1, sticky=W)

ttk.Label(blanketframe_right, text='Spent', font=boldfont, width=10).grid(column=0, row=0, sticky=W)
CP_spent_entry = ttk.Entry(blanketframe_right, width=7, textvariable=CP_spent, font=normalfont)
CP_spent_entry.state(["readonly"])
CP_spent_entry.grid(column=0,row=1, sticky=W)

ttk.Label(blanketframe_right, text='Free', font=boldfont).grid(column=1, row=0, sticky=W)
CP_free_entry = ttk.Entry(blanketframe_right, width=7, textvariable=CP_free, foreground='black', font=normalfont)
CP_free_entry.state(["readonly"])
CP_free_entry.grid(column=1,row=1, sticky=W)

ttk.Label(blanketframe_left, text='Level', font=boldfont).grid(column=0, row=2, sticky=W)
level_entry = ttk.Entry(blanketframe_left, width=7, textvariable=level, font=normalfont)
level_entry.state(["readonly"])
level_entry.grid(column=0,row=4, sticky=W)

ttk.Label(blanketframe_left, text='HP', font=boldfont).grid(column=1, row=2, sticky=W)
HP_entry = ttk.Entry(blanketframe_left, width=7, textvariable=HP, font=normalfont)
HP_entry.state(["readonly"])
HP_entry.grid(column=1,row=4, sticky=W)

ttk.Label(leftframe, text='Skills', font=boldfont).grid(column=0, row=11, sticky=W)
all_skills = Text(leftframe, font=normalfont, width=15, height=10)
all_skills.grid(column=0,row=12, sticky=(W, E, S, N), columnspan=2)
all_skills['state'] = 'disabled'
skill_list_scrollbar = Scrollbar(leftframe, orient=VERTICAL, command=all_skills.yview).grid(column=2,row=12, sticky=(S, N))
all_skills.configure(yscrollcommand=skill_list_scrollbar)

### Right frame

## In-Frames

skillsnotebook = ttk.Notebook(rightframe)
skillsframe_general = ttk.Frame(skillsnotebook)
skillsframe_scholar = ttk.Frame(skillsnotebook)
skillsframe_warrior_rogue = ttk.Frame(skillsnotebook)
spellslotframe = ttk.Frame(skillsframe_scholar)
versaframe = ttk.Frame(skillsframe_scholar)
skillsnotebook.add(skillsframe_general, text='General')
skillsnotebook.add(skillsframe_scholar, text='Scholar')
skillsnotebook.add(skillsframe_warrior_rogue, text='Warrior and Rogue')
skillsnotebook.grid(column=0, row=0, sticky=(N, W, E, S))

saveframe = ttk.Frame(rightframe, padding="0 0 0 0")
saveframe.grid(column=0, row=2, sticky=(N, W, E, S))

ttk.Label(rightframe, text="The rulebook is always right in case of discrepancy.").grid(column=0, row=3, pady=(10,0), sticky=W)

# Save buttons

SaveFile = ttk.Button(saveframe, text='Save to File', command=savefile).grid(column=0, pady=(10,0), row=0, sticky=(W,E))
OpenFile = ttk.Button(saveframe, text='Open File', command=openfile).grid(column=1, pady=(10,0), row=0, sticky=(W,E))
SaveText = ttk.Button(saveframe, text='Save as Text', command=savetext).grid(column=2, pady=(10,0), row=0, sticky=(W,E))
Reset = ttk.Button(saveframe, text='Reset', command=reset).grid(column=3, pady=(10,0), row=0, sticky=(W,E))

## Skills (Production and Frag)

ttk.Label(skillsframe_general, text='Production', font=boldfont).grid(column=0, row=0, sticky=W, pady=(10,3))

# Production

ttk.Label(skillsframe_general, text='Trapper', font=normalfont).grid(column=0, row=1, sticky=W)
ttk.Label(skillsframe_general, textvariable=trapper_cstvar, font=normalfont).grid(column=1, row=1, padx=(3,3), sticky=E)
trapper_spin = ttk.Spinbox(skillsframe_general, from_=0, to=10, width=3, textvariable=trapper, font=normalfont)
trapper_spin.grid(column=2, row=1, sticky=W)
trapper_spin.bind("<<Increment>>", trapper_up)
trapper_spin.bind("<<Decrement>>", trapper_down)
trapper_spin.bind('<Return>', calc_spent_cp)

ttk.Label(skillsframe_general, text='Create Scroll', font=normalfont).grid(column=3, padx=(3,3), row=1, sticky=W)
ttk.Label(skillsframe_general, textvariable=create_scroll_cstvar, font=normalfont).grid(column=4, row=1, padx=(3,3), sticky=E)
create_scroll_spin = ttk.Spinbox(skillsframe_general, from_=0, to=10, width=3, textvariable=create_scroll, font=normalfont)
create_scroll_spin.grid(column=5, row=1, sticky=W)
create_scroll_spin.bind("<<Increment>>", create_scroll_up)
create_scroll_spin.bind("<<Decrement>>", create_scroll_down)
create_scroll_spin.bind('<Return>', calc_spent_cp)
create_scroll_spin.state(['disabled'])

ttk.Label(skillsframe_general, text='Tradesman', font=normalfont).grid(column=6, padx=(3,3), row=1, sticky=W)
ttk.Label(skillsframe_general, textvariable=tradesman_cstvar, font=normalfont).grid(column=7, row=1, padx=(3,3), sticky=E)
tradesman_spin = ttk.Spinbox(skillsframe_general, from_=0, to=10, width=3, textvariable=tradesman, font=normalfont)
tradesman_spin.grid(column=8, row=1, sticky=W)
tradesman_spin.bind("<<Increment>>", tradesman_up)
tradesman_spin.bind("<<Decrement>>", tradesman_down)
tradesman_spin.bind('<Return>', calc_spent_cp)

ttk.Label(skillsframe_general, text='Alchemy', font=normalfont).grid(column=0, row=2, sticky=W)
ttk.Label(skillsframe_general, textvariable=alchemy_cstvar, font=normalfont).grid(column=1, row=2, padx=(3,3), sticky=E)
alchemy_spin = ttk.Spinbox(skillsframe_general, from_=0, to=10, width=3, textvariable=alchemy, font=normalfont)
alchemy_spin.grid(column=2, row=2, sticky=W)
alchemy_spin.bind("<<Increment>>", alchemy_up)
alchemy_spin.bind("<<Decrement>>", alchemy_down)
alchemy_spin.bind('<Return>', calc_spent_cp)

ttk.Label(skillsframe_general, text='Blacksmith', font=normalfont).grid(column=3, padx=(3,3), row=2, sticky=W)
ttk.Label(skillsframe_general, textvariable=blacksmith_cstvar, font=normalfont).grid(column=4, row=2, padx=(3,3), sticky=E)
blacksmith_spin = ttk.Spinbox(skillsframe_general, from_=0, to=10, width=3, textvariable=blacksmith, font=normalfont)
blacksmith_spin.grid(column=5, row=2, sticky=W)
blacksmith_spin.bind("<<Increment>>", blacksmith_up)
blacksmith_spin.bind("<<Decrement>>", blacksmith_down)
blacksmith_spin.bind('<Return>', calc_spent_cp)

ttk.Label(skillsframe_general, text='Chemistry', font=normalfont).grid(column=0, row=3, sticky=W)
ttk.Label(skillsframe_general, textvariable=chemistry_cstvar, font=normalfont).grid(column=1, row=3, padx=(3,3), sticky=E)
chemistry_spin = ttk.Spinbox(skillsframe_general, from_=0, to=10, width=3, textvariable=chemistry, font=normalfont)
chemistry_spin.grid(column=2, row=3, sticky=W)
chemistry_spin.bind("<<Increment>>", chemistry_up)
chemistry_spin.bind("<<Decrement>>", chemistry_down)
chemistry_spin.bind('<Return>', calc_spent_cp)
chemistry_spin.state(['disabled'])

ttk.Label(skillsframe_general, text='Artifice', font=normalfont).grid(column=3, padx=(3,3), row=3, sticky=W)
ttk.Label(skillsframe_general, textvariable=artifice_cstvar, font=normalfont).grid(column=4, row=3, padx=(3,3), sticky=E)
artifice_spin = ttk.Spinbox(skillsframe_general, from_=0, to=10, width=3, textvariable=artifice, font=normalfont)
artifice_spin.grid(column=5, row=3, sticky=W)
artifice_spin.bind("<<Increment>>", artifice_up)
artifice_spin.bind("<<Decrement>>", artifice_down)
artifice_spin.bind('<Return>', calc_spent_cp)
artifice_spin.state(['disabled'])

# Occupation and Race

ttk.Label(skillsframe_general, text='Occupation', font=boldfont).grid(column=0, row=4, pady=(10,3), sticky=W)
ttk.Label(skillsframe_general, text='Race', font=boldfont).grid(column=6, row=4, pady=(10,3), padx=(3,0), sticky=W)

ttk.Label(skillsframe_general, textvariable=occupational1_cstvar, font=normalfont).grid(column=1, row=5, padx=(3,3), sticky=E)
ttk.Label(skillsframe_general, textvariable=occup_1_name, font=normalfont).grid(column=0, row=5, sticky=W)
occupational1_spin = ttk.Spinbox(skillsframe_general, from_=0, to=10, width=3, textvariable=occupational1, font=normalfont)
occupational1_spin.grid(column=2, row=5, sticky=W)
occupational1_spin.bind("<<Increment>>", occupational1_up)
occupational1_spin.bind("<<Decrement>>", occupational1_down)
occupational1_spin.bind('<Return>', calc_spent_cp)

ttk.Label(skillsframe_general, textvariable=occupational2_cstvar, font=normalfont).grid(column=4, row=5, padx=(3,3), sticky=E)
ttk.Label(skillsframe_general, textvariable=occup_2_name, font=normalfont).grid(column=3, row=5, sticky=W, padx=(3,3))
occupational2_spin = ttk.Spinbox(skillsframe_general, from_=0, to=10, width=3, textvariable=occupational2, font=normalfont)
occupational2_spin.grid(column=5, row=5, sticky=W)
occupational2_spin.bind("<<Increment>>", occupational2_up)
occupational2_spin.bind("<<Decrement>>", occupational2_down)
occupational2_spin.bind('<Return>', calc_spent_cp)
occupational2_spin.state(['disabled'])

ttk.Label(skillsframe_general, textvariable=occupational3_cstvar, font=normalfont).grid(column=1, row=6, padx=(3,3), sticky=E)
ttk.Label(skillsframe_general, textvariable=occup_3_name, font=normalfont).grid(column=0, row=6, sticky=W)
occupational3_spin = ttk.Spinbox(skillsframe_general, from_=0, to=10, width=3, textvariable=occupational3, font=normalfont)
occupational3_spin.grid(column=2, row=6, sticky=W)
occupational3_spin.bind("<<Increment>>", occupational3_up)
occupational3_spin.bind("<<Decrement>>", occupational3_down)
occupational3_spin.bind('<Return>', calc_spent_cp)
occupational3_spin.state(['disabled'])

ttk.Label(skillsframe_general, textvariable=occupational4_cstvar, font=normalfont).grid(column=4, row=6, padx=(3,3), sticky=E)
ttk.Label(skillsframe_general, textvariable=occup_4_name, font=normalfont).grid(column=3, row=6, sticky=W, padx=(3,3))
occupational4_spin = ttk.Spinbox(skillsframe_general, from_=0, to=10, width=3, textvariable=occupational4, font=normalfont)
occupational4_spin.grid(column=5, row=6, sticky=W)
occupational4_spin.bind("<<Increment>>", occupational4_up)
occupational4_spin.bind("<<Decrement>>", occupational4_down)
occupational4_spin.bind('<Return>', calc_spent_cp)
occupational4_spin.state(['disabled'])

ttk.Label(skillsframe_general, textvariable=racial1_cstvar, font=normalfont).grid(column=7, row=5, padx=(3,3),sticky=E)
ttk.Label(skillsframe_general, textvariable=racial_purch_name, font=normalfont).grid(column=6, padx=(3,3), row=5, sticky=W)
racial1_spin = ttk.Spinbox(skillsframe_general, from_=0, to=10, width=3, textvariable=racial1, font=normalfont)
racial1_spin.grid(column=8, row=5, sticky=W)
racial1_spin.bind("<<Increment>>", racial1_up)
racial1_spin.bind("<<Decrement>>", racial1_down)

ttk.Label(skillsframe_general, textvariable=racial_bpb_cstvar, font=normalfont).grid(column=10, row=5, padx=(3,3), sticky=E)
ttk.Label(skillsframe_general, textvariable=lbl_bpb, font=normalfont).grid(column=9, padx=(3,3), row=5, sticky=W)
racial_bpb_spin = ttk.Spinbox(skillsframe_general, from_=0, to=1, width=3, textvariable=racial_bpb, font=normalfont)
racial_bpb_spin.grid(column=11, row=5, sticky=W)
racial_bpb_spin.grid_remove()
racial_bpb_spin.bind("<<Increment>>", racial_bpb_up)
racial_bpb_spin.bind("<<Decrement>>", racial_bpb_down)

ttk.Label(skillsframe_general, textvariable=racial_str_cstvar, font=normalfont).grid(column=10, row=6, padx=(3,3), sticky=E)
ttk.Label(skillsframe_general, textvariable=lbl_str, font=normalfont).grid(column=9, padx=(3,3), row=6, sticky=W)
racial_str_spin = ttk.Spinbox(skillsframe_general, from_=0, to=1, width=3, textvariable=racial_str, font=normalfont)
racial_str_spin.grid(column=11, row=6, sticky=W)
racial_str_spin.bind("<<Increment>>", racial_str_up)
racial_str_spin.bind("<<Decrement>>", racial_str_down)

# Frag

ttk.Label(skillsframe_general, text='Frag Skills', font=boldfont).grid(column=0, row=7, pady=(10,0), sticky=W)

ttk.Label(skillsframe_general, text='Cold Dead Hands', font=normalfont).grid(column=0, row=8, sticky=W)
ttk.Label(skillsframe_general, textvariable=colddead_cstvar, font=normalfont).grid(column=1, row=8, padx=(3,3), sticky=E)
colddead_spin = ttk.Spinbox(skillsframe_general, from_=0, to=1, width=3, textvariable=colddead, font=normalfont)
colddead_spin.grid(column=2, row=8, sticky=W)
colddead_spin.bind("<<Increment>>", colddead_up)
colddead_spin.bind("<<Decrement>>", colddead_down)

ttk.Label(skillsframe_general, text='Create Alcohol', font=normalfont).grid(column=0, row=9, sticky=W)
ttk.Label(skillsframe_general, textvariable=create_alcohol_cstvar, font=normalfont).grid(column=1, row=9, padx=(3,3), sticky=E)
create_alcohol_spin = ttk.Spinbox(skillsframe_general, from_=0, to=10, width=3, textvariable=create_alcohol, font=normalfont)
create_alcohol_spin.grid(column=2, row=9, sticky=W)
create_alcohol_spin.bind("<<Increment>>", create_alcohol_up)
create_alcohol_spin.bind("<<Decrement>>", create_alcohol_down)

ttk.Label(skillsframe_general, text='Favoured', font=normalfont).grid(column=0, row=10, sticky=W)
ttk.Label(skillsframe_general, textvariable=favoured_cstvar, font=normalfont).grid(column=1, row=10, padx=(3,3), sticky=E)
favoured_spin = ttk.Spinbox(skillsframe_general, from_=0, to=1, width=3, textvariable=favoured, font=normalfont)
favoured_spin.grid(column=2, row=10, sticky=W)
favoured_spin.state(['disabled'])

ttk.Label(skillsframe_general, text='Heavy Drinker', font=normalfont).grid(column=3, row=8, sticky=W, padx=(3,3))
ttk.Label(skillsframe_general, textvariable=hdrink_cstvar, font=normalfont).grid(column=4, row=8, padx=(3,3), sticky=E)
hdrink_spin = ttk.Spinbox(skillsframe_general, from_=0, to=1, width=3, textvariable=hdrink, font=normalfont)
hdrink_spin.grid(column=5, row=8, sticky=W)
hdrink_spin.bind("<<Increment>>", hdrink_up)
hdrink_spin.bind("<<Decrement>>", hdrink_down)

ttk.Label(skillsframe_general, text='Hindsight', font=normalfont).grid(column=3, row=9, padx=(3,3), sticky=W)
ttk.Label(skillsframe_general, textvariable=hindsight_cstvar, font=normalfont).grid(column=4, row=9, padx=(3,3), sticky=E)
hindsight_spin = ttk.Spinbox(skillsframe_general, from_=0, to=1, width=3, textvariable=hindsight, font=normalfont)
hindsight_spin.grid(column=5, row=9, sticky=W)
hindsight_spin.bind("<<Increment>>", hindsight_up)
hindsight_spin.bind("<<Decrement>>", hindsight_down)
hindsight_spin.state(['disabled'])

ttk.Label(skillsframe_general, text='Intuition', font=normalfont).grid(column=3, row=10, sticky=W, padx=(3,3))
ttk.Label(skillsframe_general, textvariable=intuition_cstvar, font=normalfont).grid(column=4, row=10, padx=(3,3), sticky=E)
intuition_spin = ttk.Spinbox(skillsframe_general, from_=0, to=1, width=3, textvariable=intuition, font=normalfont)
intuition_spin.grid(column=5, row=10, sticky=W)
intuition_spin.bind("<<Increment>>", intuition_up)
intuition_spin.bind("<<Decrement>>", intuition_down)

ttk.Label(skillsframe_general, text='Looting', font=normalfont).grid(column=6, row=8, sticky=W, padx=(3,3))
ttk.Label(skillsframe_general, textvariable=looting_cstvar, font=normalfont).grid(column=7, row=8, padx=(3,3), sticky=E)
looting_spin = ttk.Spinbox(skillsframe_general, from_=0, to=5, width=3, textvariable=looting, font=normalfont)
looting_spin.grid(column=8, row=8, sticky=W)
looting_spin.bind("<<Increment>>", looting_up)
looting_spin.bind("<<Decrement>>", looting_down)

ttk.Label(skillsframe_general, text='Paragon', font=normalfont).grid(column=6, row=9, padx=(3,3), sticky=W)
ttk.Label(skillsframe_general, textvariable=paragon_cstvar, font=normalfont).grid(column=7, row=9, padx=(3,3), sticky=E)
paragon_spin = ttk.Spinbox(skillsframe_general, from_=0, to=1, width=3, textvariable=paragon, font=normalfont)
paragon_spin.grid(column=8, row=9, sticky=W)
paragon_spin.bind("<<Increment>>", paragon_up)
paragon_spin.bind("<<Decrement>>", paragon_down)

paragon_level_spin = ttk.Spinbox(skillsframe_general, from_=1, to=7, width=3, textvariable=paragon_level, font=normalfont)
paragon_level_spin.grid(column=9, row=9)
paragon_level_spin.bind("<<Increment>>", paragon_level_up)
paragon_level_spin.bind("<<Decrement>>", paragon_level_down)
paragon_level_spin.bind('<Return>', calc_spent_cp)
paragon_level_spin.grid_remove()

ttk.Label(skillsframe_general, text='Possum', font=normalfont).grid(column=6, row=10, padx=(3,3), sticky=W)
ttk.Label(skillsframe_general, textvariable=possum_cstvar, font=normalfont).grid(column=7, row=10, padx=(3,3), sticky=E)
possum_spin = ttk.Spinbox(skillsframe_general, from_=0, to=10, width=3, textvariable=possum, font=normalfont)
possum_spin.grid(column=8, row=10, sticky=W)
possum_spin.bind("<<Increment>>", possum_up)
possum_spin.bind("<<Decrement>>", possum_down)

ttk.Label(skillsframe_general, text='Teacher', font=normalfont).grid(column=6, row=11, padx=(3,3), sticky=W)
ttk.Label(skillsframe_general, textvariable=teacher_cstvar, font=normalfont).grid(column=7, row=11, padx=(3,3), sticky=E)
teacher_spin = ttk.Spinbox(skillsframe_general, from_=0, to=1, width=3, textvariable=teacher, font=normalfont)
teacher_spin.grid(column=8, row=11, sticky=W)
teacher_spin.bind("<<Increment>>", teacher_up)
teacher_spin.bind("<<Decrement>>", teacher_down)

#Frag

ttk.Label(skillsframe_general, textvariable=frag1_name, font=normalfont).grid(column=0, row=11, sticky=W)
ttk.Label(skillsframe_general, textvariable=frag1_cstvar, font=normalfont).grid(column=1, row=11, padx=(3,3), sticky=E)
frag1_spin = ttk.Spinbox(skillsframe_general, from_=0, to=10, width=3, textvariable=frag1, font=normalfont)
frag1_spin.grid(column=2, row=11, sticky=W)
frag1_spin.bind("<<Increment>>", frag1_up)
frag1_spin.bind("<<Decrement>>", frag1_down)

ttk.Label(skillsframe_general, textvariable=frag2_name, font=normalfont).grid(column=0, row=12, sticky=W)
ttk.Label(skillsframe_general, textvariable=frag2_cstvar, font=normalfont).grid(column=1, row=12, padx=(3,3), sticky=E)
frag2_spin = ttk.Spinbox(skillsframe_general, from_=0, to=10, width=3, textvariable=frag2, font=normalfont)
frag2_spin.grid(column=2, row=12, sticky=W)
frag2_spin.bind("<<Increment>>", frag2_up)
frag2_spin.bind("<<Decrement>>", frag2_down)

ttk.Label(skillsframe_general, textvariable=frag3_name, font=normalfont).grid(column=0, row=13, sticky=W)
ttk.Label(skillsframe_general, textvariable=frag3_cstvar, font=normalfont).grid(column=1, row=13, padx=(3,3), sticky=E)
frag3_spin = ttk.Spinbox(skillsframe_general, from_=0, to=10, width=3, textvariable=frag3, font=normalfont)
frag3_spin.grid(column=2, row=13, sticky=W)
frag3_spin.bind("<<Increment>>", frag3_up)
frag3_spin.bind("<<Decrement>>", frag3_down)

ttk.Label(skillsframe_general, textvariable=frag4_name, font=normalfont).grid(column=3, row=11, padx=(3,3), sticky=W)
ttk.Label(skillsframe_general, textvariable=frag4_cstvar, font=normalfont).grid(column=4, row=11, padx=(3,3), sticky=E)
frag4_spin = ttk.Spinbox(skillsframe_general, from_=0, to=10, width=3, textvariable=frag4, font=normalfont)
frag4_spin.grid(column=5, row=11, sticky=W)
frag4_spin.bind("<<Increment>>", frag4_up)
frag4_spin.bind("<<Decrement>>", frag4_down)

ttk.Label(skillsframe_general, textvariable=frag5_name, font=normalfont).grid(column=3, row=12, padx=(3,3), sticky=W)
ttk.Label(skillsframe_general, textvariable=frag5_cstvar, font=normalfont).grid(column=4, row=12, padx=(3,3), sticky=E)
frag5_spin = ttk.Spinbox(skillsframe_general, from_=0, to=10, width=3, textvariable=frag5, font=normalfont)
frag5_spin.grid(column=5, row=12, sticky=W)
frag5_spin.bind("<<Increment>>", frag5_up)
frag5_spin.bind("<<Decrement>>", frag5_down)

ttk.Label(skillsframe_general, textvariable=frag6_name, font=normalfont).grid(column=3, row=13, padx=(3,3), sticky=W)
ttk.Label(skillsframe_general, textvariable=frag6_cstvar, font=normalfont).grid(column=4, row=13, padx=(3,3), sticky=E)
frag6_spin = ttk.Spinbox(skillsframe_general, from_=0, to=10, width=3, textvariable=frag6, font=normalfont)
frag6_spin.grid(column=5, row=13, sticky=W)
frag6_spin.bind("<<Increment>>", frag6_up)
frag6_spin.bind("<<Decrement>>", frag6_down)

## Skill Labels (Scholar)

ttk.Label(skillsframe_scholar, text='Scholar', font=boldfont).grid(column=0, row=0, pady=(10,3), sticky=W)

ttk.Label(skillsframe_scholar, text='Anatomy', font=normalfont).grid(column=0, row=1, sticky=W)
ttk.Label(skillsframe_scholar, textvariable = anatomy_cstvar, font=normalfont).grid(column=1, row=1, padx=(3,3), sticky=E)
anatomy_spin = ttk.Spinbox(skillsframe_scholar, from_=0, to=1, width=3, font=normalfont, textvariable = anatomy)
anatomy_spin.grid(column=2, row=1, sticky=W)
anatomy_spin.bind("<<Increment>>", anatomy_up)
anatomy_spin.bind("<<Decrement>>", anatomy_down)

ttk.Label(skillsframe_scholar, text='First Aid', font=normalfont).grid(column=3, row=1, padx=(3,3), sticky=W)
ttk.Label(skillsframe_scholar, textvariable = firstaid_cstvar, font=normalfont).grid(column=4, row=1, padx=(3,3), sticky=E)
firstaid_spin = ttk.Spinbox(skillsframe_scholar, from_=0, to=1, width=3, font=normalfont, textvariable = firstaid)
firstaid_spin.grid(column=5, row=1, sticky=W)
firstaid_spin.bind("<<Increment>>", firstaid_up)
firstaid_spin.bind("<<Decrement>>", firstaid_down)
firstaid_spin.state(['disabled'])

ttk.Label(skillsframe_scholar, text='Physician', font=normalfont).grid(column=6, row=1, padx=(3,3), sticky=W)
ttk.Label(skillsframe_scholar, textvariable = physician_cstvar, font=normalfont).grid(column=7, row=1, padx=(3,3), sticky=E)
physician_spin = ttk.Spinbox(skillsframe_scholar, from_=0, to=10, width=3, font=normalfont, textvariable = physician)
physician_spin.grid(column=8, row=1, sticky=W)
physician_spin.bind("<<Increment>>", physician_up)
physician_spin.bind("<<Decrement>>", physician_down)
physician_spin.bind('<Return>', calc_spent_cp)
physician_spin.state(['disabled'])

ttk.Label(skillsframe_scholar, text='Mysticism', font=normalfont).grid(column=0, row=2, sticky=W)
ttk.Label(skillsframe_scholar, textvariable = mysticism_cstvar, font=normalfont).grid(column=1, row=2, padx=(3,3), sticky=E)
mysticism_spin = ttk.Spinbox(skillsframe_scholar, from_=0, to=10, width=3, font=normalfont, textvariable = mysticism)
mysticism_spin.grid(column=2, row=2, sticky=W)
mysticism_spin.bind("<<Increment>>", mysticism_up)
mysticism_spin.bind("<<Decrement>>", mysticism_down)
mysticism_spin.bind('<Return>', calc_spent_cp)

ttk.Label(skillsframe_scholar, text='Demonic/Angelic Arts', font=normalfont).grid(column=3, row=2, padx=(3,3), sticky=W)
ttk.Label(skillsframe_scholar, textvariable = demonic_arts_cstvar, font=normalfont).grid(column=4, row=2, padx=(3,3), sticky=E)
demonic_arts_spin = ttk.Spinbox(skillsframe_scholar, from_=0, to=1, width=3, font=normalfont, textvariable = demonic_arts)
demonic_arts_spin.grid(column=5, row=2, sticky=W)
demonic_arts_spin.bind("<<Increment>>", demonic_arts_up)
demonic_arts_spin.bind("<<Decrement>>", demonic_arts_down)

ttk.Label(skillsframe_scholar, text='Necromantic Arts', font=normalfont).grid(column=6, row=2, padx=(3,3), sticky=W)
ttk.Label(skillsframe_scholar, textvariable = necromantic_arts_cstvar, font=normalfont).grid(column=7, row=2, padx=(3,3), sticky=E)
necromantic_arts_spin = ttk.Spinbox(skillsframe_scholar, from_=0, to=1, width=3, font=normalfont, textvariable = necromantic_arts)
necromantic_arts_spin.grid(column=8, row=2, sticky=W)
necromantic_arts_spin.bind("<<Increment>>", necromantic_arts_up)
necromantic_arts_spin.bind("<<Decrement>>", necromantic_arts_down)

ttk.Label(skillsframe_scholar, text='Read and Write', font=normalfont).grid(column=0, row=3, sticky=W)
ttk.Label(skillsframe_scholar, textvariable = readwrite_cstvar, font=normalfont).grid(column=1, row=3, padx=(3,3), sticky=E)
readwrite_spin = ttk.Spinbox(skillsframe_scholar, from_=0, to=1, width=3, font=normalfont, textvariable = readwrite)
readwrite_spin.grid(column=2, row=3, sticky=W)
readwrite_spin.bind("<<Increment>>", readwrite_up)
readwrite_spin.bind("<<Decrement>>", readwrite_down)

ttk.Label(skillsframe_scholar, text='Read Magic', font=normalfont).grid(column=3, row=3, padx=(3,3), sticky=W)
ttk.Label(skillsframe_scholar, textvariable = readmagic_cstvar, font=normalfont).grid(column=4, row=3, padx=(3,3), sticky=E)
readmagic_spin = ttk.Spinbox(skillsframe_scholar, from_=0, to=1, width=3, font=normalfont, textvariable = readmagic)
readmagic_spin.grid(column=5, row=3, sticky=W)
readmagic_spin.bind("<<Increment>>", readmagic_up)
readmagic_spin.bind("<<Decrement>>", readmagic_down)
readmagic_spin.state(['disabled'])

ttk.Label(skillsframe_scholar, text='Read Magic Advanced', font=normalfont).grid(column=6, row=3, padx=(3,3), sticky=W)
ttk.Label(skillsframe_scholar, textvariable = readmagic_advanced_cstvar, font=normalfont).grid(column=7, row=3, padx=(3,3), sticky=E)
readmagic_advanced_spin = ttk.Spinbox(skillsframe_scholar, from_=0, to=1, width=3, font=normalfont, textvariable = readmagic_advanced)
readmagic_advanced_spin.grid(column=8, row=3, sticky=W)
readmagic_advanced_spin.bind("<<Increment>>", readmagic_advanced_up)
readmagic_advanced_spin.bind("<<Decrement>>", readmagic_advanced_down)
readmagic_advanced_spin.state(['disabled'])

ttk.Label(skillsframe_scholar, text='Sphere 1', font=normalfont).grid(column=0, row=4, sticky=W)
ttk.Label(skillsframe_scholar, textvariable = sphere1_cstvar, font=normalfont).grid(column=1, row=4, padx=(3,3), sticky=E)
sphere1_spin = ttk.Spinbox(skillsframe_scholar, from_=0, to=1, width=3, font=normalfont, textvariable = sphere1)
sphere1_spin.grid(column=2, row=4, sticky=W)
sphere1_spin.bind("<<Increment>>", sphere1_up)
sphere1_spin.bind("<<Decrement>>", sphere1_down)
sphere1_spin.state(['disabled'])

ttk.Label(skillsframe_scholar, text='Sphere 2', font=normalfont).grid(column=3, row=4, padx=(3,3), sticky=W)
ttk.Label(skillsframe_scholar, textvariable = sphere2_cstvar, font=normalfont).grid(column=4, row=4, padx=(3,3), sticky=E)
sphere2_spin = ttk.Spinbox(skillsframe_scholar, from_=0, to=1, width=3, font=normalfont, textvariable = sphere2)
sphere2_spin.grid(column=5, row=4, sticky=W)
sphere2_spin.bind("<<Increment>>", sphere2_up)
sphere2_spin.bind("<<Decrement>>", sphere2_down)
sphere2_spin.state(['disabled'])

ttk.Label(skillsframe_scholar, text='Sphere 3', font=normalfont).grid(column=6, row=4, padx=(3,3), sticky=W)
ttk.Label(skillsframe_scholar, textvariable = sphere3_cstvar, font=normalfont).grid(column=7, row=4, padx=(3,3), sticky=E)
sphere3_spin = ttk.Spinbox(skillsframe_scholar, from_=0, to=10, width=3, font=normalfont, textvariable = sphere3)
sphere3_spin.grid(column=8, row=4, sticky=W)
sphere3_spin.bind("<<Increment>>", sphere3_up)
sphere3_spin.bind("<<Decrement>>", sphere3_down)
sphere3_spin.state(['disabled'])

ttk.Label(skillsframe_scholar, textvariable = sphere1_cstvar, font=normalfont).grid(column=1, row=4, padx=(3,3), sticky=E)
sphere1_spin = ttk.Spinbox(skillsframe_scholar, from_=0, to=1, width=3, font=normalfont, textvariable = sphere1)
sphere1_spin.grid(column=2, row=4, sticky=W)
sphere1_spin.bind("<<Increment>>", sphere1_up)
sphere1_spin.bind("<<Decrement>>", sphere1_down)
sphere1_spin.state(['disabled'])

sphere1name_box = ttk.Combobox(skillsframe_scholar, width=20, textvariable=sphere1name, font=normalfont)
sphere1name_box.grid(column=0, row=5, columnspan = 3, sticky=W)
sphere1name_box.state(["readonly"])
sphere1name_box['values'] = ('Elemental', 'Healing', 'Nature', 'Protections', 'Psionics', 'Necromancy', 'Sigil', 'Wytchcraft')
sphere1name_box.grid_remove()
sphere1name_box.bind("<<ComboboxSelected>>", calc_spent_cp)

sphere2name_box = ttk.Combobox(skillsframe_scholar, width=20, textvariable=sphere2name, font=normalfont)
sphere2name_box.grid(column=3, row=5, columnspan = 3, padx=(3,3), sticky=W)
sphere2name_box.state(["readonly"])
sphere2name_box['values'] = ('Elemental', 'Healing', 'Nature', 'Protections', 'Psionics', 'Necromancy', 'Sigil', 'Wytchcraft')
sphere2name_box.grid_remove()
sphere2name_box.bind("<<ComboboxSelected>>", calc_spent_cp)

sphere3name_box = ttk.Combobox(skillsframe_scholar, width=20, textvariable=sphere3name, font=normalfont)
sphere3name_box.grid(column=6, row=5, columnspan = 3, padx=(3,3), sticky=W)
sphere3name_box.state(["readonly"])
sphere3name_box['values'] = ('Elemental', 'Healing', 'Nature', 'Protections', 'Psionics', 'Necromancy', 'Sigil', 'Wytchcraft')
sphere3name_box.grid_remove()
sphere3name_box.bind("<<ComboboxSelected>>", calc_spent_cp)

ttk.Label(skillsframe_scholar, text='Read Magic Ritual', font=normalfont).grid(column=0, row=6, sticky=W)
ttk.Label(skillsframe_scholar, textvariable = readmagic_ritual_cstvar, font=normalfont).grid(column=1, row=6, padx=(3,3), sticky=E)
readmagic_ritual_spin = ttk.Spinbox(skillsframe_scholar, from_=0, to=1, width=3, font=normalfont, textvariable = readmagic_ritual)
readmagic_ritual_spin.grid(column=2, row=6, sticky=W)
readmagic_ritual_spin.bind("<<Increment>>", readmagic_ritual_up)
readmagic_ritual_spin.bind("<<Decrement>>", readmagic_ritual_down)
readmagic_ritual_spin.state(['disabled'])

ttk.Label(skillsframe_scholar, text='Advanced Ritual Casting', font=normalfont).grid(column=3, row=6, padx=(3,3), sticky=W)
ttk.Label(skillsframe_scholar, textvariable = sphereadv_cstvar, font=normalfont).grid(column=4, row=6, padx=(3,3), sticky=E)
sphereadv_spin = ttk.Spinbox(skillsframe_scholar, from_=0, to=1, width=3, font=normalfont, textvariable = sphereadv)
sphereadv_spin.grid(column=5, row=6, sticky=W)
sphereadv_spin.bind("<<Increment>>", sphereadv_up)
sphereadv_spin.bind("<<Decrement>>", sphereadv_down)
sphereadv_spin.state(['disabled'])

ttk.Label(skillsframe_scholar, text='Elemental Attunement', font=normalfont).grid(column=6, row=6, padx=(3,3), sticky=W)
ttk.Label(skillsframe_scholar, textvariable = elemental_attune_cstvar, font=normalfont).grid(column=7, row=6, padx=(3,3), sticky=E)
elemental_attune_spin = ttk.Spinbox(skillsframe_scholar, from_=0, to=3, width=3, font=normalfont, textvariable = elemental_attune)
elemental_attune_spin.grid(column=8, row=6, sticky=W)
elemental_attune_spin.bind("<<Increment>>", elemental_attune_up)
elemental_attune_spin.bind("<<Decrement>>", elemental_attune_down)

ttk.Label(skillsframe_scholar, text='Spell Slots', font=boldfont).grid(column=0, row=7, pady=(10,3), sticky=W)
spellslotframe.grid(column=0, row=8, columnspan=8, sticky=(N, W, E, S))

ttk.Label(spellslotframe, text='1', font=boldfont).grid(column=0, row=0, padx=(3,3), sticky=E)
ttk.Label(spellslotframe, textvariable = slot1_cstvar, font=normalfont).grid(column=0, row=2, padx=(3,3), sticky=E)
slot1_spin = ttk.Spinbox(spellslotframe, from_=0, to=10, width=2, font=normalfont, textvariable = slot1)
slot1_spin.grid(column=0, row=1, padx=(7,0), sticky=W)
slot1_spin.bind("<<Increment>>", slot1_up)
slot1_spin.bind("<<Decrement>>", slot1_down)
slot1_spin.state(['disabled'])

ttk.Label(spellslotframe, text='2', font=boldfont).grid(column=1, row=0, padx=(3,3), sticky=E)
ttk.Label(spellslotframe, textvariable = slot2_cstvar, font=normalfont).grid(column=1, row=2, padx=(3,3), sticky=E)
slot2_spin = ttk.Spinbox(spellslotframe, from_=0, to=10, width=2, font=normalfont, textvariable = slot2)
slot2_spin.grid(column=1, row=1, sticky=W)
slot2_spin.bind("<<Increment>>", slot2_up)
slot2_spin.bind("<<Decrement>>", slot2_down)
slot2_spin.state(['disabled'])

ttk.Label(spellslotframe, text='3', font=boldfont).grid(column=2, row=0, padx=(3,3), sticky=E)
ttk.Label(spellslotframe, textvariable = slot3_cstvar, font=normalfont).grid(column=2, row=2, padx=(3,3), sticky=E)
slot3_spin = ttk.Spinbox(spellslotframe, from_=0, to=10, width=2, font=normalfont, textvariable = slot3)
slot3_spin.grid(column=2, row=1, sticky=W)
slot3_spin.bind("<<Increment>>", slot3_up)
slot3_spin.bind("<<Decrement>>", slot3_down)
slot3_spin.state(['disabled'])

ttk.Label(spellslotframe, text='4', font=boldfont).grid(column=3, row=0, padx=(3,3), sticky=E)
ttk.Label(spellslotframe, textvariable = slot4_cstvar, font=normalfont).grid(column=3, row=2, padx=(3,3), sticky=E)
slot4_spin = ttk.Spinbox(spellslotframe, from_=0, to=10, width=2, font=normalfont, textvariable = slot4)
slot4_spin.grid(column=3, row=1, sticky=W)
slot4_spin.bind("<<Increment>>", slot4_up)
slot4_spin.bind("<<Decrement>>", slot4_down)
slot4_spin.state(['disabled'])

ttk.Label(spellslotframe, text='5', font=boldfont).grid(column=4, row=0, padx=(3,3), sticky=E)
ttk.Label(spellslotframe, textvariable = slot5_cstvar, font=normalfont).grid(column=4, row=2, padx=(3,3), sticky=E)
slot5_spin = ttk.Spinbox(spellslotframe, from_=0, to=10, width=2, font=normalfont, textvariable = slot5)
slot5_spin.grid(column=4, row=1, sticky=W)
slot5_spin.bind("<<Increment>>", slot5_up)
slot5_spin.bind("<<Decrement>>", slot5_down)
slot5_spin.state(['disabled'])

ttk.Label(spellslotframe, text='6', font=boldfont).grid(column=5, row=0, padx=(3,3), sticky=E)
ttk.Label(spellslotframe, textvariable = slot6_cstvar, font=normalfont).grid(column=5, row=2, padx=(3,3), sticky=E)
slot6_spin = ttk.Spinbox(spellslotframe, from_=0, to=10, width=2, font=normalfont, textvariable = slot6)
slot6_spin.grid(column=5, row=1, sticky=W)
slot6_spin.bind("<<Increment>>", slot6_up)
slot6_spin.bind("<<Decrement>>", slot6_down)
slot6_spin.state(['disabled'])

ttk.Label(spellslotframe, text='7', font=boldfont).grid(column=6, row=0, padx=(3,3), sticky=E)
ttk.Label(spellslotframe, textvariable = slot7_cstvar, font=normalfont).grid(column=6, row=2, padx=(3,3), sticky=E)
slot7_spin = ttk.Spinbox(spellslotframe, from_=0, to=10, width=2, font=normalfont, textvariable = slot7)
slot7_spin.grid(column=6, row=1, sticky=W)
slot7_spin.bind("<<Increment>>", slot7_up)
slot7_spin.bind("<<Decrement>>", slot7_down)
slot7_spin.state(['disabled'])

ttk.Label(spellslotframe, text='8', font=boldfont).grid(column=7, row=0, padx=(3,3), sticky=E)
ttk.Label(spellslotframe, textvariable = slot8_cstvar, font=normalfont).grid(column=7, row=2, padx=(3,3), sticky=E)
slot8_spin = ttk.Spinbox(spellslotframe, from_=0, to=10, width=2, font=normalfont, textvariable = slot8)
slot8_spin.grid(column=7, row=1, sticky=W)
slot8_spin.bind("<<Increment>>", slot8_up)
slot8_spin.bind("<<Decrement>>", slot8_down)
slot8_spin.state(['disabled'])

ttk.Label(spellslotframe, text='9', font=boldfont).grid(column=8, row=0, padx=(3,3), sticky=E)
ttk.Label(spellslotframe, textvariable = slot9_cstvar, font=normalfont).grid(column=8, row=2, padx=(3,3), sticky=E)
slot9_spin = ttk.Spinbox(spellslotframe, from_=0, to=10, width=2, font=normalfont, textvariable = slot9)
slot9_spin.grid(column=8, row=1, sticky=W)
slot9_spin.bind("<<Increment>>", slot9_up)
slot9_spin.bind("<<Decrement>>", slot9_down)
slot9_spin.state(['disabled'])

ttk.Label(spellslotframe, text='R', font=boldfont).grid(column=9, row=0, padx=(3,3), sticky=E)
ttk.Label(spellslotframe, textvariable = slotritual_cstvar, font=normalfont).grid(column=9, row=2, padx=(3,3), sticky=E)
slotR_spin = ttk.Spinbox(spellslotframe, from_=0, to=10, width=2, font=normalfont, textvariable = slotR)
slotR_spin.grid(column=9, row=1, sticky=W)
slotR_spin.bind("<<Increment>>", slotR_up)
slotR_spin.bind("<<Decrement>>", slotR_down)
slotR_spin.state(['disabled'])

ttk.Label(spellslotframe, text='Spell Pyramid up to...', font=normalfont).grid(column=10, row=0, padx=(15,0), sticky=E)
autopyramid_box = ttk.Combobox(spellslotframe, width=10, textvariable=autopyramid, font=normalfont)
autopyramid_box.grid(column=10, row=1, padx=(16,0), sticky=W)
autopyramid_box.state(['readonly'])
autopyramid_box['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
autopyramid.set('1')
autopyramid_box.bind("<<ComboboxSelected>>", set_auto_pyramid)

ttk.Label(skillsframe_scholar, textvariable=versa_name, font=boldfont).grid(column=0, row=9, pady=(10,3), sticky=W)
versaframe.grid(column=0, row=10, columnspan=8, sticky=(N, W, E, S))

ttk.Label(versaframe, textvariable=versa1name, font=boldfont).grid(column=0, row=0, padx=(3,3), sticky=E)
ttk.Label(versaframe, textvariable = versa1_cstvar, font=normalfont).grid(column=0, row=3, padx=(3,3), sticky=E)
versa1_spin = ttk.Spinbox(versaframe, from_=0, to=10, width=2, font=normalfont, textvariable = versa1)
versa1_spin.grid(column=0, row=1, padx=(7,0), sticky=W)
versa1_spin.bind("<<Increment>>", versa1_up)
versa1_spin.bind("<<Decrement>>", versa1_down)
versa1_spin.state(['disabled'])

ttk.Label(versaframe, textvariable=versa2name, font=boldfont).grid(column=1, row=0, padx=(3,3), sticky=E)
ttk.Label(versaframe, textvariable = versa2_cstvar, font=normalfont).grid(column=1, row=3, padx=(3,3), sticky=E)
versa2_spin = ttk.Spinbox(versaframe, from_=0, to=10, width=2, font=normalfont, textvariable = versa2)
versa2_spin.grid(column=1, row=1, sticky=W)
versa2_spin.bind("<<Increment>>", versa2_up)
versa2_spin.bind("<<Decrement>>", versa2_down)
versa2_spin.state(['disabled'])

ttk.Label(versaframe, textvariable=versa3name, font=boldfont).grid(column=2, row=0, padx=(3,3), sticky=E)
ttk.Label(versaframe, textvariable = versa3_cstvar, font=normalfont).grid(column=2, row=3, padx=(3,3), sticky=E)
versa3_spin = ttk.Spinbox(versaframe, from_=0, to=10, width=2, font=normalfont, textvariable = versa3)
versa3_spin.grid(column=2, row=1, sticky=W)
versa3_spin.bind("<<Increment>>", versa3_up)
versa3_spin.bind("<<Decrement>>", versa3_down)
versa3_spin.state(['disabled'])

ttk.Label(versaframe, textvariable=versa4name, font=boldfont).grid(column=3, row=0, padx=(3,3), sticky=E)
ttk.Label(versaframe, textvariable = versa4_cstvar, font=normalfont).grid(column=3, row=3, padx=(3,3), sticky=E)
versa4_spin = ttk.Spinbox(versaframe, from_=0, to=10, width=2, font=normalfont, textvariable = versa4)
versa4_spin.grid(column=3, row=1, sticky=W)
versa4_spin.bind("<<Increment>>", versa4_up)
versa4_spin.bind("<<Decrement>>", versa4_down)
versa4_spin.state(['disabled'])

ttk.Label(versaframe, textvariable=versa5name, font=boldfont).grid(column=4, row=0, padx=(3,3), sticky=E)
ttk.Label(versaframe, textvariable = versa5_cstvar, font=normalfont).grid(column=4, row=3, padx=(3,3), sticky=E)
versa5_spin = ttk.Spinbox(versaframe, from_=0, to=10, width=2, font=normalfont, textvariable = versa5)
versa5_spin.grid(column=4, row=1, sticky=W)
versa5_spin.bind("<<Increment>>", versa5_up)
versa5_spin.bind("<<Decrement>>", versa5_down)
versa5_spin.state(['disabled'])

ttk.Label(versaframe, textvariable=versa6name, font=boldfont).grid(column=5, row=0, padx=(3,3), sticky=E)
ttk.Label(versaframe, textvariable = versa6_cstvar, font=normalfont).grid(column=5, row=3, padx=(3,3), sticky=E)
versa6_spin = ttk.Spinbox(versaframe, from_=0, to=10, width=2, font=normalfont, textvariable = versa6)
versa6_spin.grid(column=5, row=1, sticky=W)
versa6_spin.bind("<<Increment>>", versa6_up)
versa6_spin.bind("<<Decrement>>", versa6_down)
versa6_spin.state(['disabled'])

ttk.Label(versaframe, textvariable=versa7name, font=boldfont).grid(column=6, row=0, padx=(3,3), sticky=E)
ttk.Label(versaframe, textvariable = versa7_cstvar, font=normalfont).grid(column=6, row=3, padx=(3,3), sticky=E)
versa7_spin = ttk.Spinbox(versaframe, from_=0, to=10, width=2, font=normalfont, textvariable = versa7)
versa7_spin.grid(column=6, row=1, sticky=W)
versa7_spin.bind("<<Increment>>", versa7_up)
versa7_spin.bind("<<Decrement>>", versa7_down)
versa7_spin.state(['disabled'])

ttk.Label(versaframe, textvariable=versa8name, font=boldfont).grid(column=7, row=0, padx=(3,3), sticky=E)
ttk.Label(versaframe, textvariable = versa8_cstvar, font=normalfont).grid(column=7, row=3, padx=(3,3), sticky=E)
versa8_spin = ttk.Spinbox(versaframe, from_=0, to=10, width=2, font=normalfont, textvariable = versa8)
versa8_spin.grid(column=7, row=1, sticky=W)
versa8_spin.bind("<<Increment>>", versa8_up)
versa8_spin.bind("<<Decrement>>", versa8_down)
versa8_spin.state(['disabled'])

ttk.Label(versaframe, textvariable=versa9name, font=boldfont).grid(column=8, row=0, padx=(3,3), sticky=E)
ttk.Label(versaframe, textvariable = versa9_cstvar, font=normalfont).grid(column=8, row=3, padx=(3,3), sticky=E)
versa9_spin = ttk.Spinbox(versaframe, from_=0, to=10, width=2, font=normalfont, textvariable = versa9)
versa9_spin.grid(column=8, row=1, sticky=W)
versa9_spin.bind("<<Increment>>", versa9_up)
versa9_spin.bind("<<Decrement>>", versa9_down)
versa9_spin.state(['disabled'])

## Skill Labels (Warrior)

ttk.Label(skillsframe_warrior_rogue, text='Warrior', font=boldfont).grid(column=0, row=0, pady=(10,3), sticky=W)

ttk.Label(skillsframe_warrior_rogue, text='Ambidexterity', font=normalfont).grid(column=0, row=1, sticky=W)
ttk.Label(skillsframe_warrior_rogue, textvariable = ambidexterity_cstvar, font=normalfont).grid(column=1, row=1, padx=(3,3), sticky=E)
ambidexterity_spin = ttk.Spinbox(skillsframe_warrior_rogue, from_=0, to=1, width=3, font=normalfont, textvariable = ambidexterity)
ambidexterity_spin.grid(column=2, row=1, sticky=W)
ambidexterity_spin.bind("<<Increment>>", ambidexterity_up)
ambidexterity_spin.bind("<<Decrement>>", ambidexterity_down)

ttk.Label(skillsframe_warrior_rogue, text='Florentine', font=normalfont).grid(column=3, row=1, padx=(3,3), sticky=W)
ttk.Label(skillsframe_warrior_rogue, textvariable = florentine_cstvar, font=normalfont).grid(column=4, row=1, padx=(3,3), sticky=E)
florentine_spin = ttk.Spinbox(skillsframe_warrior_rogue, from_=0, to=1, width=3, font=normalfont, textvariable = florentine)
florentine_spin.grid(column=5, row=1, sticky=W)
florentine_spin.bind("<<Increment>>", florentine_up)
florentine_spin.bind("<<Decrement>>", florentine_down)
florentine_spin.state(['disabled'])

ttk.Label(skillsframe_warrior_rogue, text='Flurry of Blows', font=normalfont).grid(column=6, row=1, padx=(3,3), sticky=W)
ttk.Label(skillsframe_warrior_rogue, textvariable = flurry_cstvar, font=normalfont).grid(column=7, row=1, padx=(3,3), sticky=E)
flurry_spin = ttk.Spinbox(skillsframe_warrior_rogue, from_=0, to=10, width=3, font=normalfont, textvariable = flurry)
flurry_spin.grid(column=8, row=1, sticky=W)
flurry_spin.bind("<<Increment>>", flurry_up)
flurry_spin.bind("<<Decrement>>", flurry_down)
flurry_spin.bind('<Return>', calc_spent_cp)

ttk.Label(skillsframe_warrior_rogue, text='Heavy Armour', font=normalfont).grid(column=0, row=2, sticky=W)
ttk.Label(skillsframe_warrior_rogue, textvariable = heavy_armour_cstvar, font=normalfont).grid(column=1, row=2, padx=(3,3), sticky=E)
heavy_armour_spin = ttk.Spinbox(skillsframe_warrior_rogue, from_=0, to=1, width=3, font=normalfont, textvariable = heavy_armour)
heavy_armour_spin.grid(column=2, row=2, sticky=W)
heavy_armour_spin.bind("<<Increment>>", heavy_armour_up)
heavy_armour_spin.bind("<<Decrement>>", heavy_armour_down)

ttk.Label(skillsframe_warrior_rogue, text='Self Mutilate', font=normalfont).grid(column=3, row=2, padx=(3,3), sticky=W)
ttk.Label(skillsframe_warrior_rogue, textvariable = self_mutilate_cstvar, font=normalfont).grid(column=4, row=2, padx=(3,3), sticky=E)
self_mutilate_spin = ttk.Spinbox(skillsframe_warrior_rogue, from_=0, to=1, width=3, font=normalfont, textvariable = self_mutilate)
self_mutilate_spin.grid(column=5, row=2, sticky=W)
self_mutilate_spin.bind("<<Increment>>", self_mutilate_up)
self_mutilate_spin.bind("<<Decrement>>", self_mutilate_down)

ttk.Label(skillsframe_warrior_rogue, text='Shield', font=normalfont).grid(column=6, row=2, padx=(3,3), sticky=W)
ttk.Label(skillsframe_warrior_rogue, textvariable = shield_cstvar, font=normalfont).grid(column=7, row=2, padx=(3,3), sticky=E)
shield_spin = ttk.Spinbox(skillsframe_warrior_rogue, from_=0, to=1, width=3, font=normalfont, textvariable = shield)
shield_spin.grid(column=8, row=2, sticky=W)
shield_spin.bind("<<Increment>>", shield_up)
shield_spin.bind("<<Decrement>>", shield_down)

ttk.Label(skillsframe_warrior_rogue, text='Weapon Refocus', font=normalfont).grid(column=0, row=3, sticky=W)
ttk.Label(skillsframe_warrior_rogue, textvariable = refocus_cstvar, font=normalfont).grid(column=1, row=3, padx=(3,3), sticky=E)
refocus_spin = ttk.Spinbox(skillsframe_warrior_rogue, from_=0, to=10, width=3, font=normalfont, textvariable = refocus)
refocus_spin.grid(column=2, row=3, sticky=W)
refocus_spin.bind("<<Increment>>", refocus_up)
refocus_spin.bind("<<Decrement>>", refocus_down)

ttk.Label(skillsframe_warrior_rogue, text='Weapon Prof: Medium', font=normalfont).grid(column=0, row=4, sticky=W)
ttk.Label(skillsframe_warrior_rogue, textvariable = groupprof_med_cstvar, font=normalfont).grid(column=1, row=4, padx=(3,3), sticky=E)
groupprof_med_spin = ttk.Spinbox(skillsframe_warrior_rogue, from_=0, to=1, width=3, font=normalfont, textvariable = groupprof_med)
groupprof_med_spin.grid(column=2, row=4, sticky=W)
groupprof_med_spin.bind("<<Increment>>", groupprof_med_up)
groupprof_med_spin.bind("<<Decrement>>", groupprof_med_down)

ttk.Label(skillsframe_warrior_rogue, text='Weapon Prof: Large', font=normalfont).grid(column=3, row=4, padx=(3,3), sticky=W)
ttk.Label(skillsframe_warrior_rogue, textvariable = groupprof_large_cstvar, font=normalfont).grid(column=4, row=4, padx=(3,3), sticky=E)
groupprof_large_spin = ttk.Spinbox(skillsframe_warrior_rogue, from_=0, to=1, width=3, font=normalfont, textvariable = groupprof_large)
groupprof_large_spin.grid(column=5, row=4, sticky=W)
groupprof_large_spin.bind("<<Increment>>", groupprof_large_up)
groupprof_large_spin.bind("<<Decrement>>", groupprof_large_down)

ttk.Label(skillsframe_warrior_rogue, text='Weapon Prof: Exotic', font=normalfont).grid(column=6, row=4, padx=(3,3), sticky=W)
ttk.Label(skillsframe_warrior_rogue, textvariable = prof_exotic_cstvar, font=normalfont).grid(column=7, row=4, padx=(3,3), sticky=E)
prof_exotic_spin = ttk.Spinbox(skillsframe_warrior_rogue, from_=0, to=4, width=3, font=normalfont, textvariable = prof_exotic)
prof_exotic_spin.grid(column=8, row=4, sticky=W)
prof_exotic_spin.bind("<<Increment>>", groupprof_large_up)
prof_exotic_spin.bind("<<Decrement>>", groupprof_large_down)

ttk.Label(skillsframe_warrior_rogue, text='Spec +1: Specific', font=normalfont).grid(column=0, row=5, sticky=W)
ttk.Label(skillsframe_warrior_rogue, textvariable = spec_specific_cstvar, font=normalfont).grid(column=1, row=5, padx=(3,3), sticky=E)
spec_specific_spin = ttk.Spinbox(skillsframe_warrior_rogue, from_=0, to=10, width=3, font=normalfont, textvariable = spec_specific)
spec_specific_spin.grid(column=2, row=5, sticky=W)
spec_specific_spin.bind("<<Increment>>", spec_specific_up)
spec_specific_spin.bind("<<Decrement>>", spec_specific_down)
spec_specific_spin.bind('<Return>', calc_spent_cp)

ttk.Label(skillsframe_warrior_rogue, text='Spec +1: Group', font=normalfont).grid(column=3, row=5, padx=(3,3), sticky=W)
ttk.Label(skillsframe_warrior_rogue, textvariable = spec_group_cstvar, font=normalfont).grid(column=4, row=5, padx=(3,3), sticky=E)
spec_group_spin = ttk.Spinbox(skillsframe_warrior_rogue, from_=0, to=10, width=3, font=normalfont, textvariable = spec_group)
spec_group_spin.grid(column=5, row=5, sticky=W)
spec_group_spin.bind("<<Increment>>", spec_group_up)
spec_group_spin.bind("<<Decrement>>", spec_group_down)
spec_group_spin.bind('<Return>', calc_spent_cp)

ttk.Label(skillsframe_warrior_rogue, text='Slay/Parry', font=normalfont).grid(column=0, row=6, sticky=W)
ttk.Label(skillsframe_warrior_rogue, textvariable = slay_cstvar, font=normalfont).grid(column=1, row=6, padx=(3,3), sticky=E)
slay_spin = ttk.Spinbox(skillsframe_warrior_rogue, from_=0, to=10, width=3, font=normalfont, textvariable = slay)
slay_spin.grid(column=2, row=6, sticky=W)
slay_spin.bind("<<Increment>>", slay_up)
slay_spin.bind("<<Decrement>>", slay_down)
slay_spin.bind('<Return>', calc_spent_cp)
slay_spin.state(['disabled'])

ttk.Label(skillsframe_warrior_rogue, text='Slay/Parry: Master', font=normalfont).grid(column=3, row=6, padx=(3,3), sticky=W)
ttk.Label(skillsframe_warrior_rogue, textvariable = slay_master_cstvar, font=normalfont).grid(column=4, row=6, padx=(3,3), sticky=E)
slay_master_spin = ttk.Spinbox(skillsframe_warrior_rogue, from_=0, to=10, width=3, font=normalfont, textvariable = slay_master)
slay_master_spin.grid(column=5, row=6, sticky=W)
slay_master_spin.bind("<<Increment>>", slay_master_up)
slay_master_spin.bind("<<Decrement>>", slay_master_down)
slay_master_spin.bind('<Return>', calc_spent_cp)
slay_master_spin.state(['disabled'])

## Skill Labels (Rogue)

ttk.Label(skillsframe_warrior_rogue, text='Rogue', font=boldfont).grid(column=0, row=7, pady=(10,3), sticky=W)

ttk.Label(skillsframe_warrior_rogue, text='Dodge', font=normalfont).grid(column=0, row=8, sticky=W)
ttk.Label(skillsframe_warrior_rogue, textvariable = dodge_cstvar, font=normalfont).grid(column=1, row=8, padx=(3,3), sticky=E)
dodge_spin = ttk.Spinbox(skillsframe_warrior_rogue, from_=0, to=10, width=3, font=normalfont, textvariable = dodge)
dodge_spin.grid(column=2, row=8, sticky=W)
dodge_spin.bind("<<Increment>>", dodge_up)
dodge_spin.bind("<<Decrement>>", dodge_down)
dodge_spin.bind('<Return>', calc_spent_cp)
dodge_spin.state(['disabled'])

ttk.Label(skillsframe_warrior_rogue, text='Garrotte', font=normalfont).grid(column=3, row=8, padx=(3,3), sticky=W)
ttk.Label(skillsframe_warrior_rogue, textvariable = garrotte_cstvar, font=normalfont).grid(column=4, row=8, padx=(3,3), sticky=E)
garrotte_spin = ttk.Spinbox(skillsframe_warrior_rogue, from_=0, to=1, width=3, font=normalfont, textvariable = garrotte)
garrotte_spin.grid(column=5, row=8, sticky=W)
garrotte_spin.bind("<<Increment>>", garrotte_up)
garrotte_spin.bind("<<Decrement>>", garrotte_down)

ttk.Label(skillsframe_warrior_rogue, text='Sap', font=normalfont).grid(column=6, row=8, sticky=W, padx=(3,3))
ttk.Label(skillsframe_warrior_rogue, textvariable = sap_cstvar, font=normalfont).grid(column=7, row=8, padx=(3,3), sticky=E)
sap_spin = ttk.Spinbox(skillsframe_warrior_rogue, from_=0, to=10, width=3, font=normalfont, textvariable = sap)
sap_spin.grid(column=8, row=8, sticky=W)
sap_spin.bind("<<Increment>>", sap_up)
sap_spin.bind("<<Decrement>>", sap_down)
sap_spin.bind('<Return>', calc_spent_cp)

ttk.Label(skillsframe_warrior_rogue, text='Vital Blow', font=normalfont).grid(column=0, row=9, sticky=W)
ttk.Label(skillsframe_warrior_rogue, textvariable = vitalblow_cstvar, font=normalfont).grid(column=1, row=9, padx=(3,3), sticky=E)
vitalblow_spin = ttk.Spinbox(skillsframe_warrior_rogue, from_=0, to=10, width=3, font=normalfont, textvariable = vitalblow)
vitalblow_spin.grid(column=2, row=9, sticky=W)
vitalblow_spin.bind("<<Increment>>", vitalblow_up)
vitalblow_spin.bind("<<Decrement>>", vitalblow_down)
vitalblow_spin.bind('<Return>', calc_spent_cp)

ttk.Label(skillsframe_warrior_rogue, text='Critical +2: Specific', font=normalfont).grid(column=0, row=10, sticky=W)
ttk.Label(skillsframe_warrior_rogue, textvariable = crit_spec_cstvar, font=normalfont).grid(column=1, row=10, padx=(3,3), sticky=E)
crit_spec_spin = ttk.Spinbox(skillsframe_warrior_rogue, from_=0, to=10, width=3, font=normalfont, textvariable = crit_spec)
crit_spec_spin.grid(column=2, row=10, sticky=W)
crit_spec_spin.bind("<<Increment>>", crit_spec_up)
crit_spec_spin.bind("<<Decrement>>", crit_spec_down)
crit_spec_spin.bind('<Return>', calc_spent_cp)

ttk.Label(skillsframe_warrior_rogue, text='Critical +2: Group', font=normalfont).grid(column=3, row=10, padx=(3,3), sticky=W)
ttk.Label(skillsframe_warrior_rogue, textvariable = crit_group_cstvar, font=normalfont).grid(column=4, row=10, padx=(3,3), sticky=E)
crit_group_spin = ttk.Spinbox(skillsframe_warrior_rogue, from_=0, to=10, width=3, font=normalfont, textvariable = crit_group)
crit_group_spin.grid(column=5, row=10, sticky=W)
crit_group_spin.bind("<<Increment>>", crit_group_up)
crit_group_spin.bind("<<Decrement>>", crit_group_down)
crit_group_spin.bind('<Return>', calc_spent_cp)

ttk.Label(skillsframe_warrior_rogue, text='Execute', font=normalfont).grid(column=0, row=11, sticky=W)
ttk.Label(skillsframe_warrior_rogue, textvariable = execute_cstvar, font=normalfont).grid(column=1, row=11, padx=(3,3), sticky=E)
execute_spin = ttk.Spinbox(skillsframe_warrior_rogue, from_=0, to=10, width=3, font=normalfont, textvariable = execute)
execute_spin.grid(column=2, row=11, sticky=W)
execute_spin.bind("<<Increment>>", execute_up)
execute_spin.bind("<<Decrement>>", execute_down)
execute_spin.bind('<Return>', calc_spent_cp)
execute_spin.state(['disabled'])

ttk.Label(skillsframe_warrior_rogue, text='Execute: Master', font=normalfont).grid(column=3, row=11, padx=(3,3), sticky=W)
ttk.Label(skillsframe_warrior_rogue, textvariable = execute_master_cstvar, font=normalfont).grid(column=4, row=11, padx=(3,3), sticky=E)
execute_master_spin = ttk.Spinbox(skillsframe_warrior_rogue, from_=0, to=10, width=3, font=normalfont, textvariable = execute_master)
execute_master_spin.grid(column=5, row=11, sticky=W)
execute_master_spin.bind("<<Increment>>", execute_master_up)
execute_master_spin.bind("<<Decrement>>", execute_master_down)
execute_master_spin.bind('<Return>', calc_spent_cp)
execute_master_spin.state(['disabled'])

##### Initial setup

reset()

root.mainloop()
