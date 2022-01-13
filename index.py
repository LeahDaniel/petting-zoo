from slithering import Snake, Snail, Leech, LeglessLizard, Worm
from swimming import Fish, Shark, Seal, Manatee, Otter
from walking import Llama, Bear, Goat, Porcupine, Tiger
from attractions import Wetlands, PettingZoo, SnakePit

miss_fuzz = Llama("Miss Fuzz", "Happy Llama", "morning", "Llama Chow", 1234567)

fainter = Goat("Fainter", "Fainting Goat", "morning", "Goat Chow")

rawr = Bear("Rawr", "Grizzly Bear", "midday", "Bear Chow")

pokey = Porcupine("Pokey", "Very Sharp Porcupine", "midday", "Porcupine Chow")

stripey = Tiger("Stripey", "Bengal Tiger", "afternoon", "Tiger Chow")

fin_boy = Fish("Fin Boy", "Beta Fish", "Fish Chow")

biter = Shark("Biter", "Great White Shark", "Shark Chow")

cutie = Otter("Cutie", "Sea Otter", "Otter Chow")

flip_flop = Seal("Flip Flop", "Not a Sea Lion", "Seal Chow")

sea_cow = Manatee("Sea Cow", "Barbara Manatee", "Manatee Chow")

wriggly = Worm("Wriggly", "Earthworm", "Worm Chow")

slithery = Snake("Slithery", "Copperhead", "Snake Chow")

slimey = Snail("Slimey", "Tiny Lil Snail", "Snail Chow")

oh_its_real = LeglessLizard("Oh It's Real", "Basically a Snake", "Legless Lizard Chow")

sucky = Leech("Sucky", "Ew ew ew", "Leech Chow")

slither_inn = SnakePit("Slither Inn", "slithery and slimy critters")
critter_cove = Wetlands("Critter Cove", "slippery and swimmy critters")
varmint_village = PettingZoo("Varmint Village", "cute and fuzzy critters to cuddle")

critter_cove.add_animal(fin_boy)
critter_cove.add_animal(biter)
critter_cove.add_animal(cutie)
critter_cove.add_animal(flip_flop)
critter_cove.add_animal(sea_cow)

print(critter_cove)

varmint_village.add_animal(miss_fuzz)
varmint_village.add_animal(fainter)
varmint_village.add_animal(rawr)
varmint_village.add_animal(pokey)
varmint_village.add_animal(stripey)

print(varmint_village)

slither_inn.add_animal(slimey)
slither_inn.add_animal(sucky)
slither_inn.add_animal(oh_its_real)
slither_inn.add_animal(slithery)
slither_inn.add_animal(wriggly)

print(slither_inn)

miss_fuzz.chip_number = 9876543
print(miss_fuzz.chip_number)
print(sucky)

print(critter_cove.last_critter_added)
miss_fuzz.feedtest()
