import random
import util

# These are the things that make up the final text you see in-game
ArtDescription_Sculpture = ["This {sculpture} {depicts} {image}. {desc_sentence_group}", 
       "This {sculpture} bears a {depiction} of {image}. {desc_sentence_group}", 
       "On this {sculpture} is a {depiction} of {image}. {desc_sentence_group}"]
ArtDescription_Weapon = ["This weapon is engraved with a {depiction} of {image}. {desc_sentence_group}",
    "This weapon bears a {depiction} of {image}. {desc_sentence_group}",
    "An engraving on this weapon {depicts} {image}. {desc_sentence_group}"]
ArtDescription_Furniture = ["This furniture is engraved with a {depiction} of {image}. {desc_sentence_group}",
    "This furniture bears a {depiction} of {image}. {desc_sentence_group}",
    "An engraving on this furniture {depicts} {image}. {desc_sentence_group}"]
# Main pulls this list
AllArt = [ArtDescription_Sculpture, ArtDescription_Furniture, ArtDescription_Weapon]

# These are lists of words that are used in the above text
sculpture = ["sculpture", "work", "piece", "carving"]
depicts = ["depicts", "shows", "portrays", "resembles", "illustrates", "represents", "is shaped like"]
depiction = ["depiction", "image", "portrayal", "representation", "illustration", "artwork"]
# Except image, image is... something else.
# Image has approximately 374 results time of writing
# IMPORTANT: When something starts capitalized, it likely refers to an actual file
image = [
    "a solitary {Character} {desc_pawn}",
    "a solitary {Character} {desc_pawn} near a {TerrainFeature}",
    "a solitary {Character} {desc_pawn} near a {Community}",
    "{Character}s playing {Game}",
    "a {Character} {desc_pawn} surrounded by {Character}s",
    "a {Character} {desc_pawn} playing {Game} with {Quantity_adjphrase} {Character}s",
    "a {Character} {desc_pawn} holding a {Weapon}",
    "a {Character} {desc_pawn} eating a {Vegetable}",
    "{Quantity_adjphrase} {PersonJob}s and {PersonJob}s eating {Vegetable}s together",
    "the minor celebrity {NamePerson} {desc_pawn}", # NamePerson pulls from all HumanStandard names :(
    "a {Character} wearing a {Apparel} {desc_pawn}",
    "a {Community}",
    "a {TerrainFeature}",
    "a {Weapon}",
    "a {TreeType} tree",
    "a {NaturalObject}",
    "{Quantity_adjphrase} {Weapon}s",
    "{Quantity_adjphrase} {Vegetable}s",
    "an empty {Apparel}",
    "a {Shape}",
    "a {Shape} surrounded by {Shape}s",
    "an abstracted rendering of {ConceptAny}",
    "a {AdjectiveAny} abstract shape"
]
desc_sentence = [
    "{Quantity_adjphrase} {ally}s watch the preparations.",
    "{Quantity_adjphrase} {ally}s help with the preparations.",
    "{Quantity_adjphrase} {Enemy}s shrink away from the scene.",
    "A {TerrainFeature} is visible in the distance.",
    "{Quantity_adjphrase} {PersonJob}s watch from a distance.",
    "{Quantity_adjphrase} {Animal}s wander peacefully.",
    "{PAWN_nameDef}'s pursuers are brandishing {Weapon}s.",
    "{PAWN_nameDef}'s pursuers are wreathed in {Color} smoke.",
    "{PAWN_nameDef}'s pursuers wear {AdjectiveAngsty} expressions.",
    "{PAWN_nameDef} is sweating.",
    "{PAWN_nameDef} is gasping for breath.",
    "{Quantity_adjphrase} {Enemy}s advance, brandishing {Weapon}s.",
    "A huge {Enemy} advances, brandishing a {Weapon}.",
    "{Quantity_adjphrase} {Enemy}s advance with a {AdjectiveBadass} look in their eyes.",
    "{Quantity_adjphrase} {Enemy}s advance with a {AdjectiveAngsty} look in their eyes.",
    "{Quantity_adjphrase} {Animal}s advance with glowing {Color} eyes.",
    "{Quantity_adjphrase} {Animal}s advance, covered in {Gore}.",
    "The ground is coated in {Gore}.",
    "{Quantity_adjphrase} {PersonJob}s flee the area.",
    "{Quantity_adjphrase} {Animal}s flee the area.",
    "{Quantity_adjphrase} {ally}s assist.",
    "{Quantity_adjphrase} {Animal}s wander the area.",
    "There is a makeshift shelter in the background.",
    "{Quantity_adjphrase} further veins are visible in the distance.",
    "{PAWN_nameDef} is sweaty and dirty from work.",
    "{Quantity_adjphrase} {Enemy}s cower from the assault.",
    "{Quantity_adjphrase} {Enemy}s flee the area.",
    "{Quantity_adjphrase} {Enemy}s are visibly wounded.",
    "A {Community} burns in the distance.",
    "A {Community} smokes in the distance.",
    "{ANIMAL_nameDef} is snuggling up against {HUMAN_nameDef}.",
    "{ANIMAL_nameDef} looks sleepy and drunk with love.",
    "{ANIMAL_nameDef} stands tall and looks noble.",
    "{ANIMAL_nameDef} is responding positively.",
    "{PURSUER_nameDef} is snuggling up against {ACCEPTER_nameDef}.",
    "{PURSUER_nameDef} is locking eyes with {ACCEPTER_nameDef}.",
    "{PURSUER_nameDef} is blowing air at {ACCEPTER_nameDef}.",
    "{PURSUER_nameDef} is stylistically bonded with {ACCEPTER_nameDef}.",
    "{PURSUER_nameDef} is a near-mirror image of {ACCEPTER_nameDef}.",
    "{PURSUER_nameDef} is touching {ACCEPTER_nameDef} aggressively.",
    "{REJECTED_nameDef} is sobbing uncontrollably.",
    "{REJECTED_nameDef} is sneering and crying at the same time.",
    "{REJECTED_nameDef} is stony-faced with shock.",
    "{DUMPER_nameDef} is stylistically separated from {REJECTED_nameDef}.",
    "{REJECTED_nameDef} has collapsed on the floor in a quivering heap.",
    "{REJECTED_nameDef} is gesticulating angrily at {DUMPER_nameDef}.",
    "{SPOUSE1_nameDef} is snuggling up against {SPOUSE2_nameDef}.",
    "{SPOUSE1_nameDef} is locking eyes with {SPOUSE2_nameDef}.",
    "{SPOUSE1_nameDef} is blowing air at {SPOUSE2_nameDef}.",
    "{SPOUSE1_nameDef} is stylistically bonded with {SPOUSE2_nameDef}.",
    "{SPOUSE1_nameDef} is a near-mirror image of {SPOUSE2_nameDef}.",
    "{SPOUSE1_nameDef} is touching {SPOUSE2_nameDef} aggressively.",
    "{CAPTURER_nameDef} is looking into {PRISONER_nameDef}'s eyes with a sense of dominance.",
    "{PRISONER_nameDef} is injured and seems to be in pain.",
    "{PRISONER_nameDef} looks resigned to {PRISONER_possessive} fate.",
    "{PRISONER_nameDef} is snarling with the fury of defeat.",
    "{CAPTURER_nameDef} is slapping {PRISONER_nameDef} to subdue {PRISONER_objective}.",
    "{CAPTURER_nameDef} is twisting {PRISONER_nameDef}'s ear.",
    "{CAPTURER_nameDef} is holding {PRISONER_nameDef} in a joint lock.",
    "{CAPTURER_nameDef} is spitting into {PRISONER_nameDef}'s face.",
    "{CAPTURER_nameDef} is laughing as tears well up in {PRISONER_nameDef}'s eyes.",
    "{CAPTURER_nameDef} is kicking {PRISONER_nameDef} for no obvious reason.",
    "{JOINER_nameDef} is nodding in understanding.",
    "{JOINER_nameDef} is smiling and making eye contact.",
    "{JOINER_nameDef} looks relieved.",
    "{JOINER_nameDef} looks hopeful.",
    "{PREY_nameDef} seems totally oblivious.",
    "{HUNTER_nameDef} is gripping {HUNTER_possessive} weapon tightly.",
    "{PREY_nameDef} is looking around as though {PREY_pronoun} senses that something is wrong.",
    "{SURGEON_nameDef} is sweating profusely.",
    "{SURGEON_nameDef} looks incredibly focused on the task.",
    "{SURGEON_nameDef} has blood smeared on {SURGEON_possessive} face.",
    "{PATIENT_nameDef} is shaking and writhing.",
    "{EXECUTIONER_nameDef} is sweating profusely.",
    "{EXECUTIONER_nameDef} is drooling a little bit.",
    "{EXECUTIONER_nameDef} has blood smeared on {EXECUTIONER_possessive} face.",
    "{PRISONER_nameDef} is shaking and writhing.",
    "{PRISONER_nameDef} seems to have given up entirely.",
    "{PRISONER_nameDef} has closed {PRISONER_possessive} eyes, seeming to pray to a higher power.",
    "{PRISONER_nameDef} looks defiant.",
    "{VICTIM_nameDef} seems to have given up entirely.",
    "{VICTIM_nameDef} has closed {VICTIM_possessive} eyes, seeming to pray to a higher power.",
    "{VICTIM_nameDef} looks defiant.",
    "{VICTIM_nameDef} is screaming with rage and terror.",
    "{VICTIM_nameDef} looks broken and exhausted.",
    "{VICTIM_nameDef} appears to be badly wounded.",
    "{ANIMAL_nameDef} is snarling aggressively.",
    "{ANIMAL_nameDef} appears to be in some sort of hypnotic state.",
    "{ANIMAL_nameDef} looks scared but interested.",
    "{ANIMAL_nameDef} appears fascinated.",
    "{TAMER_nameDef} is projecting a powerful sense of love towards {ANIMAL_nameDef}.",
    "The sun is setting behind them in a symbolic echo of the event.",
    "{Quantity_adjphrase} {Animal}s look on.",
    "A {PersonJob} watches silently {side_position}.",
    "Blood is pooling around {VICTIM_nameDef}'s body.",
    "{VICTIM_nameDef}'s eyes are rendered in a realistically lifeless fashion.",
    "{KILLER_nameDef} is baring {KILLER_possessive} teeth.",
    "{KILLER_nameDef} seems satisfied.",
    "{KILLER_nameDef} looks distressed at what {KILLER_pronoun} is doing.",
    "{KILLER_nameDef} looks pleased with the situation.",
    "{KILLER_nameDef} looks triumphant.",
    "{TRADER_nameDef} is smiling devilishly.",
    "{SELLER_nameDef} is laughing maniacally.",
    "{SELLER_nameDef} reluctantly hands {PRISONER_nameDef} over to the trader.",
    "{PRISONER_nameDef} stares defiantly at {PRISONER_possessive} new master.",
    "{TRADER_nameDef} drags {PRISONER_nameDef} away by {PRISONER_possessive} chains.",
    "{PRISONER_nameDef} stares at {SELLER_nameDef}, plotting {PRISONER_possessive} revenge.",
    "{PRISONER_nameDef} is crying.",
    "{PRISONER_nameDef} is spitting in {SELLER_nameDef}'s face.",
    "{PRISONER_nameDef} is melting into the ground.",
    "{SELLER_nameDef} is thrusting the chains of {PRISONER_nameDef} into {TRADER_nameDef}'s hands.",
    "An air of hopelessness pervades the situation.",
    "{TRAINER_nameDef} is showing pleasure.",
    "{TRAINER_nameDef} is smiling.",
    "{TRAINER_nameDef} looks bored.",
    "{TRAINER_nameDef} is threateningly brandishing {TRAINER_possessive} fist.",
    "{TRAINER_nameDef} is wrinkling {TRAINER_possessive} brow in concentration.",
    "{ANIMAL_nameDef} looks puzzled.",
    "{ANIMAL_nameDef} has a weapon in {ANIMAL_possessive} mouth.",
    "{ANIMAL_nameDef} is emitting effortful grunts.",
    "{TRAINER_nameDef} is shaking {TRAINER_possessive} head is frustration.",
    "{ANIMAL_nameDef} is trembling in fear.",
    "{ANIMAL_nameDef} appears to be morphing into a {Vegetable}.",
    "{ANIMAL_nameDef} is represented as a pile of power tools.",
    "{ANIMAL_nameDef} is half {Color} and half {Color}.",
    "{ANIMAL_nameDef} is covered in scales.",
    "{TRAINER_nameDef} is depicted with {Quantity_adjphrase} arms.",
    "{TRAINER_nameDef} is morphing into {ANIMAL_definite}.",
    "{BUYER_nameDef} is examining {SELLER_nameDef}'s wares.",
    "{SELLER_nameDef} considers an item.",
    "{SELLER_nameDef} starts haggling.",
    "{BUYER_nameDef} argues with {SELLER_nameDef}.",
    "{SELLER_nameDef} and {BUYER_nameDef} agree on a price.",
    "{BUYER_nameDef} pays for the item.",
    "{SELLER_nameDef} is counting {SELLER_possessive} money.",
    "{BUYER_nameDef} is taking {BUYER_possessive} goods.",
    "{PAWN_pronoun} is concentrating intently on the controls.",
    "{PAWN_pronoun} has {PAWN_possessive} eyes closed and looks confident.",
    "{PAWN_pronoun} is sleeping, {PAWN_possessive} eyes closed peacefully.",
    "{PAWN_pronoun} is smiling with grim joy.",
    "{PAWN_pronoun} seems to be fully in control of the situation.",
    "There is a flame trail licking off the back of the ship.",
    "A nearby {Animal} is looking up, startled.",
    "A {Animal} is fleeing the launch in fear.",
    "There is a {TerrainFeature} in the background.",
    "A {PersonJob} watches silently from afar.",
    "{target} appears without remorse.",
    "{target} is consumed with passionate rage.",
    "{target} has no emotion or expression.",
    "{target}'s body is covered in {Gore}.",
    "{target} is screaming furiously.",
    "{target} is visibly wounded.",
    "{target}'s eyes are glowing {Color}.",
    "{PAWN_pronoun} is sweating with exertion.",
    "{PAWN_pronoun} appears to be terrified.",
    "{PAWN_pronoun} is scratched and bleeding.",
    "{PAWN_pronoun} has lost {PAWN_possessive} balance.",
    "{VICTIM_nameDef} is covered in {Gore}.",
    "{VICTIM_nameDef} looks {AdjectiveAngsty}.",
    "{VICTIM_nameDef} is wincing in pain.",
    "{VICTIM_nameDef} is wincing in agony.",
    "{PAWN_nameDef}'s last project sits nearby, complete.",
    "A marvelous construction surrounds {PAWN_nameDef}.",
    "{Quantity_adjphrase} {PersonJob}s look grateful for {PAWN_nameDef}'s heroic effort.",
    "{Quantity_adjphrase} {PersonJob}s lie nearby in a similar state.",
    "The scene takes place inside a newly-built {Community}.",
    "{Quantity_adjphrase} fly-ridden {Animal} corpses surround the area.",
    "{Quantity_adjphrase} twisted {Color} {TerrainFeature}s surround the scene.",
    "{Quantity_adjphrase} {PersonJob}s are stricken with the same affliction.",
    "The scene takes place inside a {TreeType} forest.",
    "{Quantity_adjphrase} dying {Animal}s lay on the ground.",
    "{Quantity_adjphrase} {Animal}s sleep peacefully nearby.",
    "{Quantity_adjphrase} {PersonJob}s gaze upon the scene.",
    "A {PersonJob} watches from a distance.",
    "{Quantity_adjphrase} distant figures approaches from behind a {TerrainFeature}.",
    "{Quantity_adjphrase} {Enemy}s can be seen in the distance.",
    "{PAWN_nameDef} is practically surrounded by {Enemy}s.",
    "{PAWN_nameDef} is confronted by a {Enemy}.",
    "{Quantity_adjphrase} {Animal}s flee the scene of conflict in fear.",
    "In the distance, a {PersonJob} observes.",
    "{Quantity_adjphrase} {PersonJob}s are {event}.",
    "{Quantity_adjphrase} {Animal}s surround the group.",
    "The sun sets over a {TerrainFeature}.",
    "The sun rises over a {TerrainFeature}.",
    "{PAWN_nameDef} looks on in surprise.",
    "{PAWN_nameDef} looks on with excitement.",
    "{PAWN_nameDef} looks on in shock.",
    "{Quantity_adjphrase} figures approach from a nearby {TerrainFeature}.",
    "{Quantity_adjphrase} figures prepare tools and equipment.",
    "{Quantity_adjphrase} {Animal}s mill around uncertainly.",
    "The surroundings are muted and dull.",
    "{PAWN_nameDef} lies on the ground, {PAWN_possessive} body twisted at an unusual angle.",
    "{PAWN_nameDef} hides near a {TerrainFeature}, gazing out with a {AdjectiveAngsty} look.",
    "{PAWN_nameDef} rests quietly with a layer of sweat upon {PAWN_possessive} face.",
    "{Quantity_adjphrase} dead {Animal}s lay on the ground.",
    "Below, {PAWN_nameDef} plays {Game} with a {AdjectiveFriendly} look.",
    "{PAWN_nameDef} watches with awe on {PAWN_possessive} face.",
    "{Quantity_adjphrase} {PersonJob}s watch from below.",
    "{PAWN_nameDef} sits near a {TerrainFeature}, gazing at the sky.",
    "There is no {Enemy} in sight.",
    "{PAWN_nameDef} watches with visible fright.",
    "{PAWN_nameDef} is coordinating defensive measures.",
    "{Quantity_adjphrase} {PersonJob}s rush to prepare.",
    "All animal life has left the area.",
    "{PAWN_nameDef} organizes a resistance while {defender_circumstance}.",
    "{PAWN_nameDef} wields a {Weapon} defensively while {defender_circumstance}.",
    "{PAWN_nameDef} lies on the ground, wounded.",
    "{PAWN_nameDef} retaliates with {PAWN_possessive} {Weapon} while {defender_circumstance}.",
    "{PAWN_nameDef} stands as tall as a building, {defender_circumstance}.",
    "{PAWN_nameDef} wears a {AdjectiveBadass} expression.",
    "{PAWN_nameDef} wears a {AdjectiveAngsty} expression.",
    "{PAWN_nameDef} organizes a resistance.",
    "{PAWN_nameDef} wields a {Weapon} defensively.",
    "{PAWN_nameDef} retaliates with {PAWN_possessive} {Weapon}.",
    "The ground is coated in scrap metal.",
    "A {Community} of spectators watches the sky peacefully.",
    "{Quantity_adjphrase} {Animal}s wander nearby, unaware.",
    "As {PAWN_pronoun} reads, {PAWN_pronoun} starts {VerbFriendly}.",
    "A spectral {PersonJob} watches from the clouds.",
    "{PAWN_nameDef} sits near a {TerrainFeature}.",
    "A {Community} is visible in the far distance.",
    "A spaceship is visible in the far distance.",
    "{COLONIST_nameDef} is coordinating defensive measures.",
    "{ATTACKER_nameDef} cackles with glee.",
    "{COLONIST_nameDef} watches with visible fright.",
    "There is a {Community} in the background.",
    "The {OBJECT_label} appears to tower above {PAWN_nameDef}.",
    "The {OBJECT_label} glows a soft {Color}.",
    "The {OBJECT_label} is intricately detailed.",
    "{Quantity_adjphrase} {PersonJob}s marvel at the {OBJECT_label}.",
    "{Quantity_adjphrase} {PersonJob}s gaze in awe.",
    "{Quantity_adjphrase} {PersonJob}s are involved in the conversation.",
    "The area is decorated with {Color} and {Color}.",
    "{Quantity_adjphrase} {Animal}s play nearby.",
    "{Quantity_adjphrase} {PersonJob}s gaze upon {PAWN_objective}.",
    "{PAWN_pronoun} is surrounded by {Quantity_adjphrase} {Animal}s.",
    "{Quantity_adjphrase} {Animal}s rest peacefully.",
    "{Quantity_adjphrase} {Enemy}s are awestruck by the scene.",
    "A {Color} aurora shines in the background.",
    "In the distance, a {Community} is covered with snow.",
    "A field of {Vegetable}s is barely visible through the snow.",
    "A snow-covered {TerrainFeature} can be seen far away.",
    "A spectral image of {CORPSE_nameDef} looks over the scene with a {AdjectiveFriendly} expression.",
    "A spectral image of {CORPSE_nameDef} stands next to {VISITOR_nameDef}, wearing a {AdjectiveFriendly} expression.",
    "A spectral image of {CORPSE_nameDef} looks over the scene with a {AdjectiveAngsty} expression.",
    "A spectral image of {CORPSE_nameDef} stands next to {VISITOR_nameDef}, wearing a {AdjectiveAngsty} expression.",
    "{Quantity_adjphrase} {Animal}s rest near the scene.",
    "In the distance, a {Community} is visible.",
    "In the distance, a {TerrainFeature} is visible.",
    "{Quantity_adjphrase} {PersonJob}s are playing as well.",
    "{PAWN_nameDef} is glowing with a {Color} aura.",
    "{PAWN_nameDef}'s features are exaggerated.",
    "{PAWN_nameDef} towers above the scene.",
    "{Quantity_adjphrase} {PersonJob}s are slumped in defeat.",
    "A spectral image of {CORPSE_nameDef} stands next to {DIGGER_nameDef}, wearing a {AdjectiveFriendly} expression.",
    "A spectral image of {CORPSE_nameDef} stands next to {DIGGER_nameDef}, wearing a {AdjectiveAngsty} expression.",
    "{Quantity_adjphrase} {Enemy}s approach the area.",
    "{PAWN_nameDef} radiates determination.",
    "{PAWN_nameDef} is visibly wounded.",
    "{Quantity_adjphrase} filled cryptosleep caskets surround the scene.",
    "{CARRIER_nameDef} radiates determination.",
    "{SLEEPER_nameDef} is visibly wounded.",
    "{SLEEPER_nameDef} looks exhausted.",
    "{STRIPPED_nameDef} is visibly aroused.",
    "{STRIPPED_nameDef} is covered in unexplained moisture.",
    "{STRIPPED_nameDef} is breathing heavily for no obvious reason.",
    "{STRIPPED_nameDef} is fondling a shrub.",
    "{STRIPPED_nameDef} wears only a {AdjectiveAngsty} expression.",
    "The subject is surrounded by the results of {Quantity_adjphrase} failed experiments.",
    "The subject is surrounded by {Quantity_adjphrase} books.",
    "{PAWN_possessive} skill is visible in the work.",
    "{Quantity_adjphrase} {PersonJob}s watch with amazement.",
    "{Quantity_adjphrase} {Animal}s watch with amazement.",
    "{Quantity_adjphrase} ethereal spirits of ancient masters watch from above.",
    "{HUMAN_nameDef} is surrounded by uncountable {Animal}s.",
    "{ANIMAL_nameDef} is moving to join a {AnimalGroup} of its kin.",
    "The scene is packed with {Animal}s and {Animal}s.",
    "A line of uncountable {Animal}s waits to be tamed by {HUMAN_nameDef}.",
    "{PAWN_pronoun} has {PAWN_possessive} eyes closed and looks afraid.",
    "{PAWN_pronoun} is unconscious, {PAWN_possessive} tongue lolling out, drool dripping.",
    "{PAWN_pronoun} seems to have no idea what {PAWN_pronoun} is doing.",
    "{PAWN_pronoun} is strapped in with {PAWN_possessive} eyes closed, totally helpless.",
    "There is a flame trail licking off the back of the pod.",
    "A {Animal} is fleeing the impact in fear.",
    "{PAWN_pronoun} seems totally unaware of what is around {PAWN_objective}.",
    "{PAWN_possessive} face itself seems to be swelling.",
    "{PAWN_pronoun} is nearly unconscious, {PAWN_possessive} tongue lolling out, drool dripping.",
    "{PAWN_pronoun} is convulsing violently.",
    "{PAWN_pronoun} looks ashamed.",
    "{PAWN_pronoun} seems to be trying to laugh, despite the circumstances.",
    "{PAWN_pronoun} looks almost deflated, as though totally emptied by the intense vomiting.",
    "{PAWN_pronoun} is surrounded by an artistically rendered halo of filth.",
    "A {Animal} is eating from the trail of vomit in the background.",
    "{PAWN_pronoun} looks happy and sad at the same time.",
    "{PAWN_pronoun} has stains down {PAWN_possessive} front.",
    "There is a trail of discarded beverage containers behind {PAWN_objective}.",
    "There is a white substance on {PAWN_possessive} pants.",
    "{PAWN_pronoun} seems to have lost a shoe.",
    "{PAWN_possessive} hair is totally mussed up.",
    "{PAWN_possessive} flesh is visibly charring.",
    "{PAWN_possessive} eyes are wide with panic.",
    "{PAWN_pronoun} seems to be barely conscious; {PAWN_possessive} eyes are lifeless.",
    "{PAWN_possessive} mouth is open as {PAWN_pronoun} screams for help.",
    "The flames are about to envelop {PAWN_possessive} head.",
    "A symbolic halo of fire surrounds {PAWN_possessive} face.",
    "{PAWN_pronoun} is laughing maniacally.",
    "{PAWN_pronoun} seems to be losing {PAWN_objective}self.",
    "A plume of smoke is rising off {PAWN_objective}.",
    "{PAWN_pronoun} is rendered artistically in a corpse-like way.",
    "{PAWN_pronoun} is shaking with ungovernable rage.",
    "{PAWN_possessive} teeth are bared in a deadly snarl.",
    "{PAWN_possessive} eyes are dead pools of madness.",
    "Spittle is flying from {PAWN_possessive} mouth as {PAWN_possessive} screams with insane rage.",
    "{PAWN_pronoun} has lost part of {PAWN_possessive} clothing.",
    "{PAWN_pronoun} is grimacing in misery.",
    "{PAWN_pronoun} seems to be smiling maniacally.",
    "{PAWN_pronoun} is depicted with the snarling face of a {Animal}.",
    "{Animal}s symbolically surround {PAWN_possessive} head.",
    "{PAWN_pronoun} has a murderous glint in {PAWN_possessive} eye.",
    "{PAWN_possessive} entire body seems to be trembling with hatred.",
    "{PAWN_possessive} face is set in a look of twisted serenity.",
    "A single tear rolls down {PAWN_possessive} face.",
    "{PAWN_nameDef}'s face is covered with blood and fluid.",
    "{PAWN_nameDef} is licking {PAWN_possessive} fingers.",
    "{PAWN_nameDef} has blood and gore bits all down {PAWN_possessive} front.",
    "{PAWN_nameDef} is in the middle of a large pool of blood.",
    "{PAWN_nameDef} is eyeing someone else nearby with dark interest.",
    "The meat is glistening and appears very succulent.",
    "The meat is spilling all over {PAWN_nameDef}'s body.",
    "There are tools scattered all around.",
    "{PAWN_pronoun} is scratched and scarred from work injuries.",
    "{PAWN_pronoun} is covered in sweat.",
    "The work area is highly organized, with every tool in its proper place.",
    "{PAWN_pronoun} is rendered in an exaggerated way to appear more powerful.",
    "The size of {THING_definite} is exaggerated to emphasize its importance.",
    "{THING_definite} has an artistic glow added to it. It seems almost angelic.",
    "{PAWN_nameDef} is faded into the background to emphasize {PAWN_possessive} new creation.",
    "{Quantity_adjphrase} onlookers surround {PAWN_objective}.",
    "{PAWN_nameDef} is wiping {PAWN_possessive} brow.",
    "{PAWN_nameDef} is jumping for joy.",
    "{PAWN_nameDef} is high-fiving a friend.",
    "{PAWN_nameDef} is screaming with happiness.",
    "{PAWN_nameDef} is laughing uncontrollably.",
    "The work appears to be exceptionally complex.",
    "{PAWN_nameDef} is completely surrounded by an array of tools and apparatuses.",
    "{PAWN_nameDef} is staring at {PAWN_possessive} discovery with a sense of wonder.",
    "{PAWN_nameDef} is surrounded by {PAWN_possessive} notes on {THING_title}.",
    "{PAWN_nameDef}'s eyes sparkle with newfound wisdom.",
    "{PAWN_nameDef} is forever changed by the teachings of {THING_title}.",
    "There is a sense that some secrets are yet to be uncovered.",
]

style_clause = [
    "the work is infused with the idea of {ConceptAny} and is done in a {artstyle_adj} style",
    "the work is executed in a {artstyle_adj} style",
    "the {artstyle_adj} style of the central scene clashes with the {artstyle_adj} depiction of the background",
    "the work has a {artstyle_adj} feeling and a {composition} structure",
    "the overall composition is {composition}",
    "the style is {artstyle_adj} with {artstyle_adj} elements",
    "the image somehow expresses both {ConceptAny} and {ConceptAny}",
    "the image contrasts {ConceptAny} with {ConceptAny}",
    "the {composition} structure of the image almost conflicts with its {artstyle_adj} style",
    "the work is shaded in hues of {Color} and {Color}",
    "almost every shape in the image seems to be {composition}"
]
artextra_clause = [
    "the image is bordered by {subimageplural}",
    "at the edge of the image are {subimageplural}",
    "there is {subimagesingle} {side_position}",
    "the subjects are in front of {subimageany}",
    "the lower part of the image is dominated by {subimageany}",
    "the scene takes place in the middle of a {Community}",
    "the scene takes place on the outskirts of a {Community}",
    "the scene takes place inside a {Community} built near a {TerrainFeature}",
    "a {Character} {idles} {side_position}",
    "a {PAWN_adj} {Character} {idles} {side_position}",
    "{Quantity_adjphrase} {Character}s appear {side_position}",
    "{Quantity_adjphrase} {PAWN_adj} {Character}s appear {side_position}",
    "a {Animal} {idles} {side_position}",
    "if you squint your eyes, the {composition} composition of the image reveals the outline of {subimageany}",
    "the {emotional_expression} head of a {PAWN_adj} {PersonJob} watches over all",
    "a {PAWN_adj} {PersonJob} watches over all while {emotional_expression}",
    "the head of a {PAWN_adj} {PersonJob} watches over all",
    "the whole image is depicted by the careful arrangement of {subimageplural}"
]


# Other lists that are used for finalized strings
Quantity_adjphrase = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "several", "a group of", "a large group of", "dozens of", "hundreds of", "a thousand", "thousands of"]
Shape = ["triangle", "square", "rectangle", "cone", "line", "heart", "star", "circle", "ellipse"]
side_position = ["off to one side", "in the background", "in the distance", "in the lower part of the image", "in the upper part of the image", "to the left of the main scene", "to the right of the main scene", "near the edge of the image", "near the main subject", "far from the main subject", "beneath the main subject", "behind the focal point"]
event = ["throwing a party", "eating a communal meal", "discussing recent events", "rekindling old friendships", "talking hesitantly"]
AdjectiveAny = ["{AdjectiveBadass}", "{AdjectiveAngsty}", "{AdjectiveFriendly}", "{AdjectiveNatural}"]
ConceptAny = ["{ConceptPositive}", "{ConceptBadass}", "{ConceptAngsty}"]
style_group = ["{artextra_clause}. {style_clause}.", "{style_clause}. {artconjunction} {artextra_clause}.", "{style_clause}.", "{artextra_clause}.", ""]
defender_circumstance = ["shouting triumphantly", "glowing {Color}", "raising a fist in defiance", "flexing {PAWN_possessive} muscles"]
# DISCLAIMER: I pulled the labels from https://rimworldwiki.com/wiki/Stuff
labels = ["Animal bed", "Animal flap", "Animal sleeping box", "Armchair", "Art bench", "Autodoor", "Barricade", "Bed", "Bedroll", "Billiards table", "Bowler hat", "Breach axe", "Butcher table", "Button-down shirt", "Chess table", "Club", "Column", "Cowboy hat", "Dining chair", "Door", "Double bed", "Double bedroll", "Dresser", "Drug lab", "Duster", "Egg box", "Electric crematorium", "Electric tailor bench", "End table", "Fence", "Fence gate", "Flagstone", "Flak helmet", "Foam turret", "Game-of-Ur board", "Gladius", "Grand sculpture", "Grand stele", "Hand tailor bench", "Hi-tech research bench", "Hood", "Hoopstone ring", "Horseshoes pin", "Hospital bed", "Ikwa", "Jacket", "Knife", "Large sculpture", "Large stele", "Longsword", "Mace", "Mini-turret", "Mortar", "Pants", "Parka", "Patchleather", "Pen marker", "Plant pot", "Plate armor", "Poker table", "Royal bed", "Sandbags", "Sarcophagus", "Shelf", "Simple helmet", "Simple research bench", "Small sculpture", "Small shelf", "Spear", "Spike trap", "Stone tile", "Stonecutter's table", "Stool", "T-shirt", "Table (1x2)", "Table (2x2)", "Table (2x4)", "Table (3x3)", "Tribal headdress", "Tribalwear", "Tuque", "Urn", "Veil", "Wall", "War mask", "Baby decoration", "Blackboard", "Crib", "Face mask", "Heavy bandolier", "Kid helmet", "Kid pants", "Kid parka", "Kid romper", "Kid shirt", "Kid tribalwear", "Sash", "School desk", "Toy box", "Animalist slab (broad)", "Animalist slab (medium)", "Authority cap", "Autobong", "Blindfold", "Bonsai pot", "Broadwrap", "Burka", "Darklight brazier", "Drum", "Flophat", "Gibbet cage", "Grand altar", "Headwrap", "Kneel pillow", "Kneel sheet", "Large altar", "Lectern", "Medium altar", "Morbid slab (broad)", "Morbid slab (medium)", "Morbid stone tile", "Pew", "Reliquary", "Robe", "Shadecone", "Skullspike", "Slab bed", "Slab double bed", "Slave body strap", "Slave collar", "Slicecap", "Small altar", "Spikecore stone tile", "Styling station", "Tailcap", "Terror sculpture", "Torture crown", "Totemic slab (broad)", "Totemic slab (medium)", "Totemic stone tile", "Visage mask", "Axe", "Beret", "Brazier", "Cape", "Coronet", "Corset", "Crown", "Drape", "Fine stone tile", "Formal shirt", "Formal vest", "Grand meditation throne", "Ladies hat", "Large nature shrine", "Meditation throne", "Prestige robe", "Small nature shrine", "Stellic crown", "Top hat", "Warhammer"]
artstyle_adj = ["unoriginal", "simple", "complex and realistic", "surrealistic", "classical", "modern", "symbolic", "amateurish yet attractive", "detail-oriented", "blocky", "cubist", "impressionistic", "expressionistic", "photographic", "baroque", "dadaist", "glitch-art", "pixelated", "fauvist", "folksy", "figurative", "sinuous", "geometric", "abstract", "hyper-realistic", "pop art", "minimalistic", "neoclassical", "cel-shaded", "post-impressionistic", "purist", "rococo", "romanesque", "romantic", "graffiti-like", "erotic", "sensual", "heartfelt"]
composition = ["triangular", "rectangular", "square", "unbalanced", "well-balanced", "dynamic", "static", "vertical", "horizontal", "focused"]
idles = ["sits", "stands", "waits", "smiles", "lies", "poses", "appears", "is shown", "fades in", "floats"]
PAWN_adj = ["dead", "dying", "injured", "sleeping", "standing", "sitting", "crazy", "young", "old", "{Gore}-covered", "filthy", "{Apparel}-wearing", "{Weapon}-wielding", "{Vegetable}-eating"]
emotional_expression = ["smiling", "frowning", "scowling", "laughing", "staring", "crying", "screaming", "overjoyed"]

# Functions that act as chance lists in the process of file searching
def Character():
    if random.randint(1,10) <= 3:
        return "{Enemy}"
    elif random.randint(1,10) <= 4:
        return "{Animal}"
    elif random.randint(1,10) <= 6:
        return "{PersonJob}"
    else:
        return "{Mechanoid}"

# Functions that act as chance lists
def desc_pawn():
    if random.randint(1, 20) <= 12:
        return ""
    else:
        return random.choice(["flying through the air", "suspended in the air", "moving to the left", "moving to the right", "sitting on a table", "seen through a looking glass", "rendered in silhouette", "riding on a {Animal} wearing a {Apparel}", "looking {AdjectiveAny}", "covered in {Gore}"])

def artconjunction():
    if random.randint(1,10) <= 6:
        return ""
    else:
        return random.choice(["as an interesting contrast,", "rounding out the work,", "in addition to that,", "strikingly,", "provocatively,", "unusually for this kind of work,", "though few would expect it,", "besides that,"])

def subimageany():
    if random.randint(0,1) == 0:
        return "{subimagesingle}"
    else:
        return "{subimageplural}"

def subimageplural():
    if random.randint(1,10) <= 3:
        return "{Quantity_adjphrase} {Character}s"
    else:
        return random.choice(["{Quantity_adjphrase} {Vegetable}s", "{Quantity_adjphrase} {Shape}s"])
    
def subimagesingle():
    if random.randint(1,10) <= 4:
        return "a {Character}"
    else:
        return random.choice(["a {TerrainFeature}","a {Community}","a {TreeType} tree","a {Vegetable}","a {AnimalGroup} of {Animal}s"])

# Other other other other
def desc_sentence_group():
    if random.randint(0,1) == 0: # Mimickry of HasTale and Taleless generation
        return "{desc_sentence} {style_group}"
    else:
        return "{style_group}"

def special(string):
    if "name" in string.lower():
        # Use animal names
        if "animal" in string.lower() or "prey" in string.lower():
            return util.get_random_from_file("Words/Name_Animal.txt")
        # Use human names
        else:
            # DISCLAIMER: If the same pawn is supposed to be referenced twice, it will not do that :)
            # DISCLAIMER 2: The names come from https://github.com/dominictarr/random-name/blob/master/names.txt
            return util.get_random_from_file("Words/Name_Human.txt")
    elif "target" in string.lower():
        if random.randint(0,1) == 0:
            return util.get_random_from_file("Words/Name_Animal.txt")
        else:
            return util.get_random_from_file("Words/Name_Human.txt")
    elif "label" in string.lower():
        return random.choice(labels)
    elif "pronoun" in string.lower():
        return random.choice(["he", "she", "it"])
    elif "possessive" in string.lower():
        return random.choice(["his", "her", "its"])
    elif "objective" in string.lower():
        return random.choice(["him", "her", "it"])
    elif "definite" in string.lower():
        if "animal" in string.lower():
            return util.get_random_from_file("Words/Animal.txt")
        elif "thing" in string.lower():
            return random.choice(labels)
    else:
        return False