import random

# Define main regions of Barovia
regions = [
    "Wolfrun", "Druidic Groves", "Mount Ghakis", 
    "Bogs of Berez", "Vallaki Valley", "Baratok Slopes", 
    "Ravenloft Moors", "Svalich Wood", "Barovian Basin"
]

# Predefined tables for each encounter type (NPC, Combat, Phenomena, Landmarks)
encounter_tables = {
    "NPC": {
        "Wolfrun": [
            "A wereraven monitoring the woods in raven form",
            "The green hag Jenny Greenteeth and her rattling wagon",
            "A group of patrolling werewolves in human form",
            "A Vallakian archer tracking an elk",
            "A deranged homunculus gathering ingredients for its master",
            "A werewolf-bitten commoner fearfully awaiting their first full moon",
            "A cursed commoner possessed by a shadow demon",
            "A team of Krezkian commoners searching for a missing person",
            "A travelling Vistani family of commoners in a barrel-top wagon heading toward the Vallaki encampment"
        ],
        "Druidic Groves": [
            "A deranged homunculus gathering ingredients for its master",
            "An outcast commoner cursed by a witch to bring pestilence upon their surroundings",
            "A werewolf forester building a life away from civilization",
            "A solitary herbalist druid picking mushrooms in the forest",
            "A group of berserkers hunting an elk",
            "A wereraven monitoring the woods in raven form",
            "The green hag Jenny Greenteeth and her rattling wagon of wares"
        ],
        "Mount Ghakis": [
            "A meditating revenant guarding the path",
            "A group of berserkers hunting a goat",
            "An injured berserker, wounded by Sangzor the giant goat"
        ],
        "Bogs of Berez": [
            "A wandering revenant hunting scarecrows",
            "An eccentric apprentice wizard communing with a lost soul",
            "A deranged homunculus gathering ingredients for its master",
            "An outcast commoner cursed by a witch to bring pestilence upon their surroundings",
            "A solitary herbalist druid picking mushrooms in the bog",
        ],
        "Vallaki Valley": [
            "A wandering revenant hunting wolves",
            "A team of Vallakian commoners searching for a missing person",
            "A pair of Vallakian scouts searching for a missing person",
            "A travelling Vistani family of commoners in a barrel-top wagon heading toward",
            "A trader’s caravan led by a watchful scout"
            "A Vallakian archer tracking an elk",
            "A Vallakian guard pursuing a murderer",
            "A deranged homunculus gathering ingredients for its master",
            "A demented herbalist druid picking mushrooms in the forest",
            "The green hag Jenny Greenteeth and her rattling wagon of wares",
            "A wereraven monitoring the woods in raven form",
            "A coven of Vallakian cultists preparing an animal sacrifice"
        ],
        "Baratok Slopes": [
            "A solitary herbalist druid picking mushrooms in the grasslands",
            "An outcast commoner cursed by a witch to bring pestilence upon their surroundings"
        ],
        "Ravenloft Moors": [
            "A wandering revenant hunting zombies",
            "A trader’s caravan led by a watchful scout travelling to The Village of Barovia",
            "An eccentric apprentice wizard communing with a lost soul",
            "A babbling ghost that asks travellers to lead it to its home",
            "A vampire spawn swordsman searching for a worthy opponent",
            "A faceless wraith that stalks travellers atop a dark horse",
            "A travelling Vistani family of commoners in a barrel-top wagon heading toward the Tser Pool encampment",
            "A wereraven monitoring the road in raven form",
            "The green hag Jenny Greenteeth and her rattling wagon of wares"
        ],
        "Svalich Wood": [
            "A team of Barovian commoners searching for a missing person abducted by a pack of werewolves",
            "A pair of Barovian scouts searching for a missing person abducted by a horde of hungry ghouls",
            "A travelling Vistani family of commoners in a barrel-top wagon heading toward the Vistani Camp",
            "A lonely werewolf hermit",
            "A cautious archer tracking an elk",
            "A babbling ghost that asks travellers to lead it to its home",
        ],
        "Barovian Basin": [
            "A team of Barovian commoners tending to their fields",
            "A travelling Vistani family of commoners in a barrel-top wagon heading toward the Tser Pool encampment",
            "A shepherd’s ghost watching over the spirit of a lamb",
        ],
    },
    "Combat": {
        "Wolfrun": [
            "A pack of 2d6+1 hungry wolves (Levels 1-4)",
            "A pack of 1d4+1 hungry direwolves (Levels 2-5)",
            "A pack of 1d4 werewolves hunting in wolf form (Level 2-9)",
        ],
        "Druidic Groves": [
            "A pack of 2d6 worgs (Levels 1-8)",
            "A cannibalistic druid accompanied by a swarm of 2d6 twig blights (Levels 3-5)",
            "A pack of 4d4 concealed needle blights (Levels 2-7)",
        ],
        "Mount Ghakis": [
            "A pack of 1d4 winter wolves prowling their territory (Level 2-9)",
            "A 1d2 hungry cave bears hunting for food (Levels 2-4)",
            "1d2 cannibalistic adventurers cursed to become bodaks by deals with a vestige (Levels 5-10)",
        ],
        "Bogs of Berez": [
            "A pack of 2d4 scavenging shadow mastiffs (Levels 3-10)",
            "1d2 maddened wraiths that attack any that enter their grove (Levels 4-9)",
            "A bubbling marsh filled by 4d4 ash zombies bloated with poison gas (Levels 2-7)",
            "1d4 undead giant constrictor snakes mindlessly searching for flesh (Levels 2-8)",
            "A pack of 2d4 ghouls picking through the remains of fallen travelers (Levels 2-7)", 
            "A will-o-wisp leading unwary travellers to a ruin infested by 2d6 zombies (Levels 3-7)",
            "1d2 maddened banshees wandering a mossy fen (Levels 3-7)",
            "A nest of 1d4 phase spiders awaiting a meal (Levels 2-9)",
            "A wandering corpse flower (Levels 5-8)",
        ],
        "Vallaki Valley": [
            "A pack of 1d4+1 hungry direwolves (Levels 2-5)",
            "A pack of 2d6+1 hungry wolves (Levels 1-4)",
            "A thirsty colony of 2d4+1 swarms of bats (Levels 1-4)",
        ],
        "Baratok Slopes": [
            "1d4 mutated brown bears with the features and temperaments of owlbears (Level 2-9)",
        ],
        "Ravenloft Moors": [
            "A group of 1d4 vampire spawn feeding on the corpse of an ill-fated traveller (Levels 4-10)",
            "A cloud of 1d4 blood-starved vampiric mists (Levels 3-9)",
            "A pack of 2d4 ghouls picking through the remains of fallen travelers (Levels 2-7)",
        ],
        "Svalich Wood": [
            "A pack of 2d6+1 hungry wolves (Levels 1-4)",
            "A thirsty colony of 2d4+1 swarms of bats (Levels 1-4)",
            "A giant boar fending off 4d4 twig blights (Levels 1-4)",
            "A pack of 1d4+1 hungry direwolves (Levels 2-5)",
            "A host of 1d4 ghosts haunting their unmarked graves (Levels 3-10)",
            "A nest of 1d8 giant spiders awaiting a meal (Levels 1-8)",
            "A hostile dryad defending her grove alongside 1d4 thornies (Levels 3-5)",
        ],
        "Barovian Basin": [
            "Nothing happens.",
        ],
    },
    "Phenomena": {
        "Wolfrun": [
            "A mutilated corpse",
            "A forgotten hunting trap",
            "A forgotten trinket lying in the tall grass",
            "Several swarms of ravens",
        ],
        "Druidic Groves": [
            "A mutilated corpse",
            "A ghostly fog that brings hallucinations of old regrets and hidden fears",
            "A forgotten trinket lying amidst a patch of yellowed grasses",
            "Several swarms of ravens",
            "A carved stone figurine of a maiden tucked into the hollow of an old tree",
        ],
        "Mount Ghakis": [
            "A ghostly fog that brings hallucinations of old regrets and hidden fears",
            "A herd of goats grazing on sparse grass",
            "A forgotten trinket buried beneath a snowdrift",
            "A frozen zombie buried beneath a snowdrift",
            "A skeletal rider",
            "A rockslide that threatens to knock the party down toward the banks of Luna Lake",
        ],
        "Bogs of Berez": [
            "A ghostly fog that brings hallucinations of old regrets and hidden fears",
            "A forgotten trinket lying in the mud",
            "A skeletal rider",
        ],
        "Vallaki Valley": [
            "A forgotten hunting trap",
            "A mutilated corpse",
            "A forgotten trinket lying in the mud",
            "A skeletal rider",
            "Several swarms of ravens",
            "A carved stone figurine of a maiden tucked into the hollow of an old tree",
        ],
        "Baratok Slopes": [
            "A ghostly fog that brings hallucinations of old regrets and hidden fears",
            "A watchful swarm of ravens perched atop a dead tree",
            "A mutated giant elk with multicolored horns",
            "A tree split by a lightning bolt", 
        ],
        "Ravenloft Moors": [
            "A mutilated corpse",
            "A ghostly fog that brings hallucinations of old regrets and hidden fears",
            "A skeletal rider",
            "A watchful swarm of ravens perched atop a dead tree",
        ],
        "Svalich Wood": [
            "A forgotten hunting trap",
            "A mutilated corpse",
            "A ghostly fog that brings hallucinations of old regrets and hidden fears",
            "A forgotten trinket lying in the mud",
            "Several watchful swarms of ravens",
            "A carved stone figurine of a maiden tucked into the hollow of an old tree",
            "A skeletal rider",
        ],
        "Barovian Basin": [
            "A skeletal rider",
            "A ghostly fog that brings hallucinations of old regrets and hidden fears",
            "A forgotten trinket lying in the mud",
            "A watchful swarm of ravens perched atop a dead tree",
        ],
    },
    "Landmarks": {
        "Wolfrun": [
            "A burnt ruin haunted by a fiery poltergeist: A pair of werewolves invaded this house years ago. Its owner fled the structure and set it aflame, burning the lycanthropes alive - but leaving her spouse and child to die in fire as she fled for Krezk. The poltergeist is the spirit of the owner’s spouse, and acts to protect its child’s unburied bones. The poltergeist is put to rest if the bones are buried.",
            "A crumbling sanctuary maintained by a kindly ghost: This old structure once held a shrine visited by travellers on the road. The ghost is the spirit of an old monk who once tended its chapel. The spirit is lonely, and has seen the building fall into disrepair as the woods grew up around its walls.",
            "A creaking water wheel connected to an abandoned miller’s cottage: The water wheel was once used to grind wheat into grain. The mechanism that drives the mill has long since rotted away, though a rusted lock keeps the wheel in its place. The cottage is bereft of any valuables, but contains an old bed and a rotted straw-stuffed mattress. The roof is intact, and can serve as shelter in the case of a storm.",
        ],
        "Druidic Groves": [
            "An overgrown field guarded by a single watchful scarecrow: A rotting wooden barn is the only remaining structure on this old, overgrown field. The barn contains a half-decayed loft and a set of stalls once used for oxen, but is otherwise empty. The scarecrow is a spy for Baba Lysaga and flees when not under direct observation, returning to Berez to deliver information to its master.",
            "The road splits in twain at this misted intersection. The eastern path winds through a blighted ridge that borders a rocky hill; the western path cuts through an autumnal grove. The western trail was created by druids, and leads to a spiked pit trap concealed by a thin tarp made of twigs and pine needles. Once the trap is set off, 2d6 twig blights emerge from the underbrush and attack any creatures surrounding the pit. The eastern path is safe. A DC 15 Wisdom (Survival) check can allow a creature to discern that the western trail has been travelled by far fewer creatures than the eastern one.",
            "A patch of mantraps awaiting unwary visitors: 1d4+1 mantraps border the road in a circular shape. As travellers cut through this area, each mantrap releases its attractive pollen, attempting to lure its prey toward its own plantlike maw.",
            "A pack of thorny guarding their den: A small field contains a number of ash-gray wildflowers with razor-sharp thorn-covered stalks. A tree containing a number of succulent-looking fruit sits at the center of the field. Its roots conceal the burrow of 1d6 thorny, who attack any creatures that approach. The wildflowers are difficult terrain; however, a creature may move through them at normal speed if that creature chooses to take 1 point of slashing damage for each five-foot square travelled in this way. The fruit tastes bitter, and its skin is as tough as leather.",
            "A creaking water wheel connected to an abandoned lumberjack’s cottage: This creaking water wheel once used the power of the Raven River to drive a saw that split trunks into lumber. The mechanism that drives the saw has long since rotted away, though a rusted lock keeps the wheel in its place. The abandoned lumberjack’s cottage connected to it is bereft of any valuables, but contains an old bed and a rotted straw-stuffed mattress. The roof is intact, and can serve as shelter in the case of a storm.",
            "A mossy slab of stone bearing a carving of a tree: This slab stands four feet in height, and rests on a stone surface bearing intricately carved curls and spirals. It was constructed as a monument to the Weaver of the Ladies Three by the druids of old Cerunnos long before Strahd arrived.",
        ],
        "Mount Ghakis": [
            "A crumbling tower atop a snow-covered peak: This old structure was once employed by the army of Delmor as a watchtower overlooking the southwestern corner of Barovia. The tower was stormed by Strahd’s forces long ago, and contains at its base a small, rotted wooden chest. The chest contains a broken pendant of a silver dragon that’s always cold to the touch.",
            "A swarm of tormented ghosts trapped within a darkened cavern: An old well at the center of this cavern holds the souls of twelve shrieking ghosts, whose remains have settled at the bottom of the cistern beneath. These wretched spirits were trapped here by a necromancer who sought to devour their life force and so grow powerful enough to defeat Strahd. Any creature that approaches the well finds themselves surrounded by the ghosts, who are bound to the shaft of the well by ethereal chains when manifested. The ghosts attack if the well is damaged. If the spirits are spoken to, one of them requests that their bones be recovered from the waters beneath. 1d4 shambling mounds lurk in the cistern, and attack if the bones are disturbed.",
        ],
        "Bogs of Berez": [
            "A sunken farm guarded by watchful scarecrows: The farm was abandoned years ago when a pack of rabid werewolves killed its inhabitants. A rotting wooden barn is the only remaining structure on this old field. Tall grasses and cattails border the several swampy streams that trickle through the loamy soil. The barn contains a half-decayed loft and a set of stalls once used for oxen, but is otherwise empty. The scarecrow are spies for Baba Lysaga, and attack any PCs that approach the barn while one scarecrow returns to Berez to inform its master.",
            "A mad alchemist’s lonely cottage: The alchemist and his homunculus can be found gathering ingredients elsewhere in Barovia. This cottage holds his living quarters, study, and laboratory. He is trying to create a potion of immortality.",
            "An overgrown fenced-in cemetery populated by wandering zombies: This cemetery once housed the dead of Berez. Its zombies are swollen with bog-water and do not pursue intruders beyond its rusted iron fences.",
            "A forgotten chapel ruined by age: This old shrine bears two altars: one to the Morninglord, and one to Mother Night. The Morninglord’s fine wooden altar has rotted away completely. Mother Night’s stone altar still bears the mark of her crescent moon, but moss and fungi have overgrown her side of the sanctum, cracking and crumbling the floor. It was swallowed up by the swamps when Berez was destroyed.",
            "A mossy standing stone slab bearing a carving of a single eye: This slab stands four feet in height, and rests on a stone surface bearing intricately carved curls and spirals. It was constructed as a monument to the Seeker of the Ladies Three by the druids of old Cerunnos long before Strahd arrived.",
        ],
        "Vallaki Valley": [
            "An old or excavated grave: This grave contains the remnants of a pair of Vallakian farmers.",
            "An overgrown fenced-in cemetery populated by wandering zombies: This overgrown, fenced-in cemetery once housed the dead of a small hamlet beyond Vallaki’s walls. Its twelve zombies are now overgrown with moss and mushrooms, and do not pursue intruders beyond its rusted fence. The three homes and well that once comprised the hamlet lie just over a hundred yards away.",
            "A maddened ghost that attacks any that enter its grove: This spirit is the final remnant of a hunter who was slain by a pack of wolves. It haunts the site of its death, and cannot be calmed so long as its bones remain unburied. Its bones can be found in a small hollow beneath the roots of a nearby tree, wound within the chain of an old pewter locket.",
            "A forgotten chapel defaced and desecrated by cultists: Lady Wachter’s most devout followers travel here on the night of each new moon, repeating profane rituals as they mark the walls and altar with diabolic symbols.",
            "A crumbling sanctuary maintained by a kindly ghost: This old structure once held a shrine visited by travellers on the road. The ghost is the spirit of an old monk who once tended its chapel. The spirit is lonely, and has seen the building fall into disrepair as the woods grew up around its walls.",
            "A trio of giant spiders lurking beneath a footbridge: This old stone bridge crosses a wide ditch fifteen feet across and twelve feet deep, with steep sides and few handholds. Each spider has constructed a web-woven lair beneath a separate side of the bridge. The spiders attack any creature that passes over the footbridge alone. Passers-by can see a well-worn trail that winds toward the south on the Barovian and Vallakian ends of the bridge. Any traveller that follows the trail through the trees eventually comes to a newer wooden bridge that provides safe passage across the ravine",
        ],
        "Baratok Slopes": [
            "A swarm of tormented ghosts trapped within a darkened cavern: An old well at the center of this cavern holds the souls of twelve shrieking ghosts, whose remains have settled at the bottom of the cistern beneath. These wretched spirits were trapped here by a necromancer who sought to devour their life force and so grow powerful enough to defeat Strahd. Any creature that approaches the well finds themselves surrounded by the ghosts, who are bound to the shaft of the well by ethereal chains when manifested. The ghosts attack if the well is damaged. If the spirits are spoken to, one of them requests that their bones be recovered from the waters beneath. 1d4 shambling mounds lurk in the cistern, and attack if the bones are disturbed",
        ],
        "Ravenloft Moors": [
            "A burnt ruin haunted by a fiery poltergeist: A pair of vampire spawn invaded this house years ago. Its owner fled the structure and set it aflame, burning the spawn alive - but leaving her spouse and child to die in fire as she fled for Vallaki. The poltergeist is the spirit of the owner’s spouse, and acts to protect its child’s unburied bones. The poltergeist is put to rest if the bones are buried."
            "A crumbling tower above a bone-strewn courtyard: This ancient watchtower is all that remains of a ruined fort used by the forces of Delmor during Strahd’s invasion. It stands above a flat, grassy yard scattered with rusted armor and old bones. The tower was stormed by Strahd’s forces long ago, and contains at its peak a brass spyglass. A person that looks through the spyglass sees the world suffering beneath a terrible storm, and sees only ghostly images when viewing characters non-native to Barovia. A character that dies and is resurrected in Barovia appears solid to the spyglass thereafter. A character that lingers in this tower can hear the whistling of wind and the far-away sound of marching troops, both of which soon fade.",
            "A forgotten chapel ruined by age: This old shrine bears two altars: one to the Morninglord, and one to Mother Night. The Morninglord’s fine wooden altar has decayed over time, leaving its carved sunburst barely visible. Mother Night’s stone altar still bears the mark of her crescent moon, but moss and fungi have overgrown her side of the sanctum, cracking and crumbling the floor.",
            "An underground crypt housing a colony of swarms of bats: The stone slab that covered the entrance to this crypt was pushed aside long ago, revealing crumbling stone steps leading down. The crypt contains three simple stone coffins of Delmorean nobility, the coffins’ carved text faded beyond legibility. The crypt has been looted of everything but the skeletons; however, a DC 15 Intelligence (Investigation) reveals a silver, crescent moon-shaped pendant forgotten behind a crypt. The chamber now serves as a home to a colony of bats, who rest here in the day and attack any creature that wakes them, fleeing once reduced to half hitpoints.",
            "A mossy standing stone slab bearing a carving of a wolf: This slab stands four feet in height, and rests on a stone surface bearing intricately carved curls and spirals. It was constructed as a monument to the Huntress of the Ladies Three by the druids of old Cerunnos long before Strahd arrived.",
        ],
        "Svalich Wood": [
            "A crumbling chapel maintained by a kindly ghost: This old structure once held a shrine visited by travellers on the road. The ghost is the spirit of an old monk who once tended its chapel. The spirit is lonely, and has seen the building fall into disrepair as the woods grew up around its walls.",
            "An old or excavated grave: This ancient headstone marks the remains of a Barovian soldier, who died of sickness during Strahd’s campaign to conquer the land."
        ],
        "Barovian Basin": [
            "A crumbling chapel maintained by a kindly spirit: This old structure once held a shrine visited by travellers on the road. The ghost is the spirit of an old monk who once tended its chapel. The spirit is lonely, and has seen the building fall into disrepair as the woods grew up around its walls.",
            "An old gravesite near an old ruin: This small collection of graves mark a Barovian farming family that died of a supernatural plague in the night. Their residence, thought cursed by the locals, lies crumbling nearby.",
        ],
    },
}
# Function to generate an encounter
def generate_encounter(region):
    # Step 1: Randomly select an encounter type (NPC, Combat, Phenomena, Landmarks)
    encounter_type = random.choice(["NPC", "Combat", "Phenomena", "Landmarks"])

    # Step 2: Pull the appropriate table based on region and encounter type
    encounter_list = encounter_tables[encounter_type][region]

    # Step 3: Randomly choose an encounter from the list
    encounter = random.choice(encounter_list)

    # Step 4: Return the generated encounter
    return encounter

# Example usage
def main():
    # Randomly select a region, or specify one based on your narrative needs
    region = "Wolfrun"
    
    # Generate the encounter for the chosen region
    encounter = generate_encounter(region)

    # Print the encounter details
    print(f"In the region of {region}, you encounter: {encounter}")

# Call the main function to run the generator
if __name__ == "__main__":
    main()
