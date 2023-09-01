import random

Pokemon_List = [
    {"name": "Bulbasaur", "Att": 49, "Vit": 45, "Def": 49, "SAt": 65, "SDf": 65, "Spe": 45, "Level": None, "Exp": None, "Type1": "Grass", "Type2": "Poison", "Mov1": "Tackle", "Mov2": "Growl", "Mov3": None, "Mov4": None},
    {"name": "Ivysaur", "Att": 62, "Vit": 60, "Def": 63, "SAt": 80, "SDf": 80, "Spe": 60, "Level": None, "Exp": None, "Type1": "Grass", "Type2": "Poison", "Mov1": "Tackle", "Mov2": "Growl", "Mov3": None, "Mov4": None},
    {"name": "Venusaur", "Att": 82, "Vit": 80, "Def": 83, "SAt": 100, "SDf": 100, "Spe": 80, "Level": None, "Exp": None, "Type1": "Grass", "Type2": "Poison", "Mov1": "Tackle", "Mov2": "Growl", "Mov3": None, "Mov4": None},
    {"name": "Charmander", "Att": 52, "Vit": 39, "Def": 43, "SAt": 60, "SDf": 50, "Spe": 65, "Level": None, "Exp": None, "Type1": "Fire", "Type2": "Fire", "Mov1": "Scratch", "Mov2": "Growl", "Mov3": None, "Mov4": None},
    {"name": "Charmeleon", "Att": 64, "Vit": 58, "Def": 58, "SAt": 80, "SDf": 65, "Spe": 80, "Level": None, "Exp": None, "Type1": "Fire", "Type2": None, "Mov1": "Ember", "Mov2": "Scratch", "Mov3": "Growl", "Mov4": None},
    {"name": "Charizard", "Att": 84, "Vit": 78, "Def": 78, "SAt": 109, "SDf": 85, "Spe": 100, "Level": None, "Exp": None, "Type1": "Fire", "Type2": "Flying", "Mov1": "Ember", "Mov2": "Scratch", "Mov3": "Growl", "Mov4": None},
    {"name": "Squirtle", "Att": 48, "Vit": 44, "Def": 65, "SAt": 50, "SDf": 64, "Spe": 43, "Level": None, "Exp": None, "Type1": "Water", "Type2": "Water", "Mov1": "Tackle", "Mov2": "Tackle", "Mov3": "Tackle", "Mov4": "Tackle"},
    {"name": "Wartortle", "Att": 63, "Vit": 59, "Def": 80, "SAt": 65, "SDf": 80, "Spe": 58, "Level": None, "Exp": None, "Type1": "Water", "Type2": None, "Mov1": "Tackle", "Mov2": "Tail Whip", "Mov3": "Water Gun", "Mov4": None},
    {"name": "Blastoise", "Att": 83, "Vit": 79, "Def": 100, "SAt": 85, "SDf": 105, "Spe": 78, "Level": None, "Exp": None, "Type1": "Water", "Type2": None, "Mov1": "Tackle", "Mov2": "Tail Whip", "Mov3": "Water Gun", "Mov4": "Withdraw"},
    {"name": "Caterpie", "Att": 30, "Vit": 35, "Def": 20, "SAt": 20, "SDf": 20, "Spe": 45, "Level": None, "Exp": None, "Type1": "Bug", "Type2": None, "Mov1": "Tackle", "Mov2": None, "Mov3": None, "Mov4": None},
    {"name": "Metapod", "Att": 20, "Vit": 55, "Def": 25, "SAt": 25, "SDf": 25, "Spe": 30, "Level": None, "Exp": None, "Type1": "Bug", "Type2": None, "Mov1": "Harden", "Mov2": None, "Mov3": None, "Mov4": None},
    {"name": "Butterfree", "Att": 45, "Vit": 50, "Def": 35, "SAt": 90, "SDf": 80, "Spe": 70, "Level": None, "Exp": None, "Type1": "Bug", "Type2": "Flying", "Mov1": "Confusion", "Mov2": "Harden", "Mov3": "Gust", "Mov4": None},
    {"name": "Weedle", "Att": 35, "Vit": 30, "Def": 20, "SAt": 20, "SDf": 20, "Spe": 50, "Level": None, "Exp": None, "Type1": "Bug", "Type2": "Poison", "Mov1": "Poison Sting", "Mov2": None, "Mov3": None, "Mov4": None},
    {"name": "Kakuna", "Att": 25, "Vit": 50, "Def": 25, "SAt": 25, "SDf": 25, "Spe": 35, "Level": None, "Exp": None, "Type1": "Bug", "Type2": "Poison", "Mov1": "Harden", "Mov2": None, "Mov3": None, "Mov4": None},
    {"name": "Beedrill", "Att": 90, "Vit": 40, "Def": 35, "SAt": 45, "SDf": 80, "Spe": 75, "Level": None, "Exp": None, "Type1": "Bug", "Type2": "Poison", "Mov1": "Fury Attack", "Mov2": "Harden", "Mov3": "Twineedle", "Mov4": None},
    {"name": "Pidgey", "Att": 45, "Vit": 40, "Def": 40, "SAt": 35, "SDf": 35, "Spe": 56, "Level": None, "Exp": None, "Type1": "Normal", "Type2": "Flying", "Mov1": "Gust", "Mov2": None, "Mov3": None, "Mov4": None},
    {"name": "Pidgeotto", "Att": 60, "Vit": 55, "Def": 55, "SAt": 50, "SDf": 50, "Spe": 71, "Level": None, "Exp": None, "Type1": "Normal", "Type2": "Flying", "Mov1": "Gust", "Mov2": "Sand Attack", "Mov3": None, "Mov4": None},
    {"name": "Pidgeot", "Att": 80, "Vit": 75, "Def": 80, "SAt": 70, "SDf": 70, "Spe": 101, "Level": None, "Exp": None, "Type1": "Normal", "Type2": "Flying", "Mov1": "Gust", "Mov2": "Quick Attack", "Mov3": "Wing Attack", "Mov4": None},
    {"name": "Rattata", "Att": 56, "Vit": 30, "Def": 35, "SAt": 25, "SDf": 35, "Spe": 72, "Level": None, "Exp": None, "Type1": "Normal", "Type2": None, "Mov1": "Tackle", "Mov2": "Tail Whip", "Mov3": None, "Mov4": None},
    {"name": "Raticate", "Att": 81, "Vit": 55, "Def": 60, "SAt": 50, "SDf": 70, "Spe": 97, "Level": None, "Exp": None, "Type1": "Normal", "Type2": None, "Mov1": "Tackle", "Mov2": "Tail Whip", "Mov3": "Quick Attack", "Mov4": None},
    {"name": "Spearow", "Att": 60, "Vit": 40, "Def": 30, "SAt": 31, "SDf": 31, "Spe": 70, "Level": None, "Exp": None, "Type1": "Normal", "Type2": "Flying", "Mov1": "Peck", "Mov2": None, "Mov3": None, "Mov4": None},
    {"name": "Fearow", "Att": 90, "Vit": 65, "Def": 65, "SAt": 61, "SDf": 61, "Spe": 100, "Level": None, "Exp": None, "Type1": "Normal", "Type2": "Flying", "Mov1": "Peck", "Mov2": "Growl", "Mov3": "Fury Attack", "Mov4": "Leer"},
    {"name": "Ekans", "Att": 60, "Vit": 35, "Def": 44, "SAt": 40, "SDf": 54, "Spe": 55, "Level": None, "Exp": None, "Type1": "Poison", "Type2": None, "Mov1": "Wrap", "Mov2": None, "Mov3": None, "Mov4": None},
    {"name": "Arbok", "Att": 85, "Vit": 60, "Def": 69, "SAt": 65, "SDf": 79, "Spe": 80, "Level": None, "Exp": None, "Type1": "Poison", "Type2": None, "Mov1": "Bite", "Mov2": "Glare", "Mov3": "Screech", "Mov4": "Leer"},
    {"name": "Pikachu", "Att": 55, "Vit": 35, "Def": 30, "SAt": 50, "SDf": 40, "Spe": 90, "Level": None, "Exp": None, "Type1": "Electric", "Type2": None, "Mov1": "Growl", "Mov2": "Thunder Shock", "Mov3": None, "Mov4": None},
    {"name": "Raichu", "Att": 90, "Vit": 60, "Def": 55, "SAt": 90, "SDf": 80, "Spe": 110, "Level": None, "Exp": None, "Type1": "Electric", "Type2": None, "Mov1": "Thunderbolt", "Mov2": "Quick Attack", "Mov3": None, "Mov4": None},
    {"name": "Sandshrew", "Att": 75, "Vit": 50, "Def": 85, "SAt": 20, "SDf": 30, "Spe": 40, "Level": None, "Exp": None, "Type1": "Ground", "Type2": None, "Mov1": "Scratch", "Mov2": "Defense Curl", "Mov3": None, "Mov4": None},
    {"name": "Sandslash", "Att": 100, "Vit": 75, "Def": 110, "SAt": 45, "SDf": 55, "Spe": 65, "Level": None, "Exp": None, "Type1": "Ground", "Type2": None, "Mov1": "Slash", "Mov2": "Swift", "Mov3": None, "Mov4": None},
    {"name": "Nidoran♀", "Att": 47, "Vit": 55, "Def": 52, "SAt": 40, "SDf": 40, "Spe": 41, "Level": None, "Exp": None, "Type1": "Poison", "Type2": None, "Mov1": "Growl", "Mov2": "Tackle", "Mov3": None, "Mov4": None},
    {"name": "Nidorina", "Att": 62, "Vit": 70, "Def": 67, "SAt": 55, "SDf": 55, "Spe": 56, "Level": None, "Exp": None, "Type1": "Poison", "Type2": None, "Mov1": "Double Kick", "Mov2": "Poison Sting", "Mov3": "Bite", "Mov4": None},
    {"name": "Nidoqueen", "Att": 92, "Vit": 90, "Def": 87, "SAt": 75, "SDf": 85, "Spe": 76, "Level": None, "Exp": None, "Type1": "Poison", "Type2": "Ground", "Mov1": "Body Slam", "Mov2": "Poison Sting", "Mov3": "Bite", "Mov4": "Double Kick"},
    {"name": "Nidoran♂", "Att": 57, "Vit": 40, "Def": 40, "SAt": 40, "SDf": 40, "Spe": 50, "Level": None, "Exp": None, "Type1": "Poison", "Type2": None, "Mov1": "Leer", "Mov2": "Peck", "Mov3": None, "Mov4": None},
    {"name": "Nidorino", "Att": 72, "Vit": 55, "Def": 55, "SAt": 55, "SDf": 55, "Spe": 65, "Level": None, "Exp": None, "Type1": "Poison", "Type2": None, "Mov1": "Horn Attack", "Mov2": "Poison Sting", "Mov3": "Leer", "Mov4": None},
    {"name": "Nidoking", "Att": 102, "Vit": 75, "Def": 85, "SAt": 85, "SDf": 75, "Spe": 85, "Level": None, "Exp": None, "Type1": "Poison", "Type2": "Ground", "Mov1": "Thrash", "Mov2": "Poison Sting", "Mov3": "Horn Attack", "Mov4": "Leer"},
    {"name": "Clefairy", "Att": 45, "Vit": 70, "Def": 48, "SAt": 60, "SDf": 65, "Spe": 35, "Level": None, "Exp": None, "Type1": "Fairy", "Type2": None, "Mov1": "Pound", "Mov2": "Growl", "Mov3": None, "Mov4": None},
    {"name": "Clefable", "Att": 70, "Vit": 95, "Def": 73, "SAt": 85, "SDf": 90, "Spe": 60, "Level": None, "Exp": None, "Type1": "Fairy", "Type2": None, "Mov1": "Sing", "Mov2": "Double Slap", "Mov3": "Minimize", "Mov4": None},
    {"name": "Vulpix", "Att": 41, "Vit": 38, "Def": 40, "SAt": 50, "SDf": 65, "Spe": 65, "Level": None, "Exp": None, "Type1": "Fire", "Type2": None, "Mov1": "Ember", "Mov2": "Tail Whip", "Mov3": None, "Mov4": None},
    {"name": "Ninetales", "Att": 76, "Vit": 73, "Def": 75, "SAt": 81, "SDf": 100, "Spe": 100, "Level": None, "Exp": None, "Type1": "Fire", "Type2": None, "Mov1": "Quick Attack", "Mov2": "Confuse Ray", "Mov3": "Flamethrower", "Mov4": "Fire Spin"},
    {"name": "Jigglypuff", "Att": 45, "Vit": 115, "Def": 20, "SAt": 45, "SDf": 25, "Spe": 20, "Level": None, "Exp": None, "Type1": "Normal", "Type2": "Fairy", "Mov1": "Sing", "Mov2": "Pound", "Mov3": "Disable", "Mov4": None},
    {"name": "Wigglytuff", "Att": 70, "Vit": 140, "Def": 45, "SAt": 85, "SDf": 50, "Spe": 45, "Level": None, "Exp": None, "Type1": "Normal", "Type2": "Fairy", "Mov1": "Double-Edge", "Mov2": "Sing", "Mov3": "Rest", "Mov4": None},
    {"name": "Zubat", "Att": 45, "Vit": 35, "Def": 30, "SAt": 40, "SDf": 40, "Spe": 55, "Level": None, "Exp": None, "Type1": "Poison", "Type2": "Flying", "Mov1": "Leech Life", "Mov2": "Supersonic", "Mov3": None, "Mov4": None},
    {"name": "Golbat", "Att": 80, "Vit": 70, "Def": 65, "SAt": 75, "SDf": 75, "Spe": 90, "Level": None, "Exp": None, "Type1": "Poison", "Type2": "Flying", "Mov1": "Wing Attack", "Mov2": "Confuse Ray", "Mov3": "Bite", "Mov4": None},
    {"name": "Oddish", "Att": 50, "Vit": 55, "Def": 45, "SAt": 75, "SDf": 65, "Spe": 30, "Level": None, "Exp": None, "Type1": "Grass", "Type2": "Poison", "Mov1": "Absorb", "Mov2": "Sweet Scent", "Mov3": None, "Mov4": None},
    {"name": "Gloom", "Att": 65, "Vit": 70, "Def": 65, "SAt": 85, "SDf": 75, "Spe": 40, "Level": None, "Exp": None, "Type1": "Grass", "Type2": "Poison", "Mov1": "Absorb", "Mov2": "Acid", "Mov3": "Sleep Powder", "Mov4": None},
    {"name": "Vileplume", "Att": 80, "Vit": 85, "Def": 80, "SAt": 110, "SDf": 90, "Spe": 50, "Level": None, "Exp": None, "Type1": "Grass", "Type2": "Poison", "Mov1": "Petal Dance", "Mov2": "Stun Spore", "Mov3": "Acid", "Mov4": None},
    {"name": "Paras", "Att": 70, "Vit": 35, "Def": 55, "SAt": 45, "SDf": 55, "Spe": 25, "Level": None, "Exp": None, "Type1": "Bug", "Type2": "Grass", "Mov1": "Scratch", "Mov2": "Stun Spore", "Mov3": None, "Mov4": None},
    {"name": "Parasect", "Att": 95, "Vit": 60, "Def": 80, "SAt": 60, "SDf": 80, "Spe": 30, "Level": None, "Exp": None, "Type1": "Bug", "Type2": "Grass", "Mov1": "Slash", "Mov2": "Spore", "Mov3": "Leech Life", "Mov4": None},
    {"name": "Venonat", "Att": 55, "Vit": 60, "Def": 50, "SAt": 40, "SDf": 55, "Spe": 45, "Level": None, "Exp": None, "Type1": "Bug", "Type2": "Poison", "Mov1": "Tackle", "Mov2": "Disable", "Mov3": None, "Mov4": None},
    {"name": "Venomoth", "Att": 65, "Vit": 70, "Def": 60, "SAt": 90, "SDf": 75, "Spe": 90, "Level": None, "Exp": None, "Type1": "Bug", "Type2": "Poison", "Mov1": "Psybeam", "Mov2": "Leech Life", "Mov3": "Sleep Powder", "Mov4": "Supersonic"},
    {"name": "Diglett", "Att": 55, "Vit": 25, "Def": 20, "SAt": 45, "SDf": 35, "Spe": 95, "Level": None, "Exp": None, "Type1": "Ground", "Type2": None, "Mov1": "Scratch", "Mov2": "Growl", "Mov3": None, "Mov4": None},
    {"name": "Dugtrio", "Att": 80, "Vit": 50, "Def": 50, "SAt": 70, "SDf": 70, "Spe": 120, "Level": None, "Exp": None, "Type1": "Ground", "Type2": None, "Mov1": "Slash", "Mov2": "Dig", "Mov3": None, "Mov4": None},
    {"name": "Meowth", "Att": 45, "Vit": 35, "Def": 35, "SAt": 40, "SDf": 40, "Spe": 90, "Level": None, "Exp": None, "Type1": "Normal", "Type2": None, "Mov1": "Scratch", "Mov2": "Growl", "Mov3": None, "Mov4": None},
    {"name": "Persian", "Att": 70, "Vit": 60, "Def": 60, "SAt": 65, "SDf": 65, "Spe": 115, "Level": None, "Exp": None, "Type1": "Normal", "Type2": None, "Mov1": "Slash", "Mov2": "Screech", "Mov3": "Bite", "Mov4": None},
    {"name": "Psyduck", "Att": 52, "Vit": 50, "Def": 48, "SAt": 65, "SDf": 50, "Spe": 55, "Level": None, "Exp": None, "Type1": "Water", "Type2": None, "Mov1": "Scratch", "Mov2": "Tail Whip", "Mov3": None, "Mov4": None},
    {"name": "Golduck", "Att": 82, "Vit": 80, "Def": 78, "SAt": 95, "SDf": 80, "Spe": 85, "Level": None, "Exp": None, "Type1": "Water", "Type2": None, "Mov1": "Screech", "Mov2": "Water Gun", "Mov3": "Fury Swipes", "Mov4": None},
    {"name": "Mankey", "Att": 80, "Vit": 40, "Def": 35, "SAt": 35, "SDf": 45, "Spe": 70, "Level": None, "Exp": None, "Type1": "Fighting", "Type2": None, "Mov1": "Scratch", "Mov2": "Leer", "Mov3": None, "Mov4": None},
    {"name": "Primeape", "Att": 105, "Vit": 65, "Def": 60, "SAt": 60, "SDf": 70, "Spe": 95, "Level": None, "Exp": None, "Type1": "Fighting", "Type2": None, "Mov1": "Karate Chop", "Mov2": "Fury Swipes", "Mov3": "Focus Energy", "Mov4": None},
    {"name": "Growlithe", "Att": 70, "Vit": 55, "Def": 45, "SAt": 70, "SDf": 50, "Spe": 60, "Level": None, "Exp": None, "Type1": "Fire", "Type2": None, "Mov1": "Bite", "Mov2": "Roar", "Mov3": None, "Mov4": None},
    {"name": "Arcanine", "Att": 110, "Vit": 90, "Def": 80, "SAt": 100, "SDf": 80, "Spe": 95, "Level": None, "Exp": None, "Type1": "Fire", "Type2": None, "Mov1": "Take Down", "Mov2": "Ember", "Mov3": "Flamethrower", "Mov4": None},
    {"name": "Poliwag", "Att": 50, "Vit": 40, "Def": 40, "SAt": 40, "SDf": 40, "Spe": 90, "Level": None, "Exp": None, "Type1": "Water", "Type2": None, "Mov1": "Bubble", "Mov2": "Hypnosis", "Mov3": None, "Mov4": None},
    {"name": "Poliwhirl", "Att": 65, "Vit": 65, "Def": 65, "SAt": 50, "SDf": 50, "Spe": 90, "Level": None, "Exp": None, "Type1": "Water", "Type2": None, "Mov1": "Water Gun", "Mov2": "Hypnosis", "Mov3": "Bubble Beam", "Mov4": None},
    {"name": "Poliwrath", "Att": 95, "Vit": 95, "Def": 95, "SAt": 70, "SDf": 90, "Spe": 70, "Level": None, "Exp": None, "Type1": "Water", "Type2": "Fighting", "Mov1": "Bubble Beam", "Mov2": "Hypnosis", "Mov3": "Submission", "Mov4": "Water Gun"},
    {"name": "Abra", "Att": 20, "Vit": 25, "Def": 15, "SAt": 105, "SDf": 55, "Spe": 90, "Level": None, "Exp": None, "Type1": "Psychic", "Type2": None, "Mov1": "Teleport", "Mov2": None, "Mov3": None, "Mov4": None},
    {"name": "Kadabra", "Att": 35, "Vit": 40, "Def": 30, "SAt": 120, "SDf": 70, "Spe": 105, "Level": None, "Exp": None, "Type1": "Psychic", "Type2": None, "Mov1": "Psybeam", "Mov2": "Kinesis", "Mov3": "Teleport", "Mov4": None},
    {"name": "Alakazam", "Att": 50, "Vit": 45, "Def": 40, "SAt": 135, "SDf": 85, "Spe": 120, "Level": None, "Exp": None, "Type1": "Psychic", "Type2": None, "Mov1": "Psychic", "Mov2": "Recover", "Mov3": "Reflect", "Mov4": "Teleport"},
    {"name": "Machop", "Att": 80, "Vit": 50, "Def": 35, "SAt": 35, "SDf": 35, "Spe": 35, "Level": None, "Exp": None, "Type1": "Fighting", "Type2": None, "Mov1": "Low Kick", "Mov2": "Leer", "Mov3": None, "Mov4": None},
    {"name": "Machoke", "Att": 100, "Vit": 70, "Def": 55, "SAt": 50, "SDf": 60, "Spe": 45, "Level": None, "Exp": None, "Type1": "Fighting", "Type2": None, "Mov1": "Karate Chop", "Mov2": "Seismic Toss", "Mov3": "Submission", "Mov4": None},
    {"name": "Machamp", "Att": 130, "Vit": 80, "Def": 65, "SAt": 65, "SDf": 85, "Spe": 55, "Level": None, "Exp": None, "Type1": "Fighting", "Type2": None, "Mov1": "Cross Chop", "Mov2": "Rock Slide", "Mov3": "Dynamic Punch", "Mov4": None},
    {"name": "Bellsprout", "Att": 75, "Vit": 35, "Def": 35, "SAt": 70, "SDf": 30, "Spe": 40, "Level": None, "Exp": None, "Type1": "Grass", "Type2": "Poison", "Mov1": "Vine Whip", "Mov2": "Growth", "Mov3": None, "Mov4": None},
    {"name": "Weepinbell", "Att": 90, "Vit": 50, "Def": 50, "SAt": 85, "SDf": 45, "Spe": 55, "Level": None, "Exp": None, "Type1": "Grass", "Type2": "Poison", "Mov1": "Razor Leaf", "Mov2": "Sweet Scent", "Mov3": "Sleep Powder", "Mov4": None},
    {"name": "Victreebel", "Att": 105, "Vit": 65, "Def": 65, "SAt": 100, "SDf": 70, "Spe": 70, "Level": None, "Exp": None, "Type1": "Grass", "Type2": "Poison", "Mov1": "Leaf Blade", "Mov2": "Sleep Powder", "Mov3": "Acid", "Mov4": None},
    {"name": "Tentacool", "Att": 40, "Vit": 40, "Def": 35, "SAt": 50, "SDf": 100, "Spe": 70, "Level": None, "Exp": None, "Type1": "Water", "Type2": "Poison", "Mov1": "Poison Sting", "Mov2": "Supersonic", "Mov3": None, "Mov4": None},
    {"name": "Tentacruel", "Att": 70, "Vit": 65, "Def": 65, "SAt": 80, "SDf": 120, "Spe": 100, "Level": None, "Exp": None, "Type1": "Water", "Type2": "Poison", "Mov1": "Hydro Pump", "Mov2": "Barrier", "Mov3": "Toxic Spikes", "Mov4": None},
    {"name": "Geodude", "Att": 80, "Vit": 40, "Def": 100, "SAt": 30, "SDf": 30, "Spe": 20, "Level": None, "Exp": None, "Type1": "Rock", "Type2": "Ground", "Mov1": "Tackle", "Mov2": "Defense Curl", "Mov3": None, "Mov4": None},
    {"name": "Graveler", "Att": 95, "Vit": 55, "Def": 115, "SAt": 45, "SDf": 45, "Spe": 35, "Level": None, "Exp": None, "Type1": "Rock", "Type2": "Ground", "Mov1": "Rock Throw", "Mov2": "Magnitude", "Mov3": "Self-Destruct", "Mov4": None},
    {"name": "Golem", "Att": 120, "Vit": 80, "Def": 130, "SAt": 55, "SDf": 65, "Spe": 45, "Level": None, "Exp": None, "Type1": "Rock", "Type2": "Ground", "Mov1": "Earthquake", "Mov2": "Explosion", "Mov3": "Rock Slide", "Mov4": None},
    {"name": "Ponyta", "Att": 85, "Vit": 55, "Def": 40, "SAt": 65, "SDf": 65, "Spe": 90, "Level": None, "Exp": None, "Type1": "Fire", "Type2": None, "Mov1": "Ember", "Mov2": "Stomp", "Mov3": None, "Mov4": None},
    {"name": "Rapidash", "Att": 100, "Vit": 70, "Def": 65, "SAt": 80, "SDf": 80, "Spe": 105, "Level": None, "Exp": None, "Type1": "Fire", "Type2": None, "Mov1": "Fire Spin", "Mov2": "Take Down", "Mov3": "Agility", "Mov4": None},
    {"name": "Slowpoke", "Att": 65, "Vit": 65, "Def": 65, "SAt": 40, "SDf": 40, "Spe": 15, "Level": None, "Exp": None, "Type1": "Water", "Type2": "Psychic", "Mov1": "Tackle", "Mov2": "Growl", "Mov3": None, "Mov4": None},
    {"name": "Slowbro", "Att": 75, "Vit": 110, "Def": 80, "SAt": 100, "SDf": 80, "Spe": 30, "Level": None, "Exp": None, "Type1": "Water", "Type2": "Psychic", "Mov1": "Water Gun", "Mov2": "Withdraw", "Mov3": "Amnesia", "Mov4": None},
    {"name": "Magnemite", "Att": 35, "Vit": 70, "Def": 55, "SAt": 95, "SDf": 55, "Spe": 45, "Level": None, "Exp": None, "Type1": "Electric", "Type2": "Steel", "Mov1": "Tackle", "Mov2": "Thunder Shock", "Mov3": "Supersonic", "Mov4": None},
    {"name": "Magneton", "Att": 60, "Vit": 95, "Def": 90, "SAt": 120, "SDf": 70, "Spe": 70, "Level": None, "Exp": None, "Type1": "Electric", "Type2": "Steel", "Mov1": "Spark", "Mov2": "Sonic Boom", "Mov3": "Thunder Wave", "Mov4": "Magnet Bomb"},
    {"name": "Farfetch'd", "Att": 65, "Vit": 55, "Def": 65, "SAt": 58, "SDf": 62, "Spe": 60, "Level": None, "Exp": None, "Type1": "Normal", "Type2": "Flying", "Mov1": "Peck", "Mov2": "Sand Attack", "Mov3": "Leer", "Mov4": "Fury Cutter"},
    {"name": "Doduo", "Att": 85, "Vit": 45, "Def": 55, "SAt": 35, "SDf": 35, "Spe": 75, "Level": None, "Exp": None, "Type1": "Normal", "Type2": "Flying", "Mov1": "Peck", "Mov2": "Growl", "Mov3": None, "Mov4": None},
    {"name": "Dodrio", "Att": 110, "Vit": 70, "Def": 80, "SAt": 60, "SDf": 60, "Spe": 100, "Level": None, "Exp": None, "Type1": "Normal", "Type2": "Flying", "Mov1": "Drill Peck", "Mov2": "Agility", "Mov3": "Tri Attack", "Mov4": None},
    {"name": "Seel", "Att": 45, "Vit": 55, "Def": 45, "SAt": 45, "SDf": 70, "Spe": 45, "Level": None, "Exp": None, "Type1": "Water", "Type2": None, "Mov1": "Headbutt", "Mov2": "Growl", "Mov3": None, "Mov4": None},
    {"name": "Dewgong", "Att": 70, "Vit": 80, "Def": 70, "SAt": 70, "SDf": 95, "Spe": 70, "Level": None, "Exp": None, "Type1": "Water", "Type2": "Ice", "Mov1": "Aurora Beam", "Mov2": "Rest", "Mov3": "Take Down", "Mov4": None},
    {"name": "Grimer", "Att": 80, "Vit": 50, "Def": 50, "SAt": 40, "SDf": 50, "Spe": 25, "Level": None, "Exp": None, "Type1": "Poison", "Type2": None, "Mov1": "Pound", "Mov2": "Disable", "Mov3": None, "Mov4": None},
    {"name": "Muk", "Att": 105, "Vit": 75, "Def": 105, "SAt": 65, "SDf": 100, "Spe": 50, "Level": None, "Exp": None, "Type1": "Poison", "Type2": None, "Mov1": "Sludge", "Mov2": "Minimize", "Mov3": "Acid Armor", "Mov4": None},
    {"name": "Shellder", "Att": 65, "Vit": 100, "Def": 180, "SAt": 45, "SDf": 25, "Spe": 40, "Level": None, "Exp": None, "Type1": "Water", "Type2": None, "Mov1": "Tackle", "Mov2": "Withdraw", "Mov3": None, "Mov4": None},
    {"name": "Cloyster", "Att": 95, "Vit": 180, "Def": 180, "SAt": 85, "SDf": 45, "Spe": 70, "Level": None, "Exp": None, "Type1": "Water", "Type2": "Ice", "Mov1": "Spike Cannon", "Mov2": "Aurora Beam", "Mov3": "Withdraw", "Mov4": "Ice Beam"},
    {"name": "Gastly", "Att": 35, "Vit": 30, "Def": 30, "SAt": 100, "SDf": 35, "Spe": 80, "Level": None, "Exp": None, "Type1": "Ghost", "Type2": "Poison", "Mov1": "Lick", "Mov2": "Hypnosis", "Mov3": None, "Mov4": None},
    {"name": "Haunter", "Att": 50, "Vit": 45, "Def": 45, "SAt": 115, "SDf": 55, "Spe": 95, "Level": None, "Exp": None, "Type1": "Ghost", "Type2": "Poison", "Mov1": "Shadow Punch", "Mov2": "Confuse Ray", "Mov3": "Dream Eater", "Mov4": None},
    {"name": "Gengar", "Att": 65, "Vit": 60, "Def": 60, "SAt": 130, "SDf": 75, "Spe": 110, "Level": None, "Exp": None, "Type1": "Ghost", "Type2": "Poison", "Mov1": "Shadow Ball", "Mov2": "Hypnosis", "Mov3": "Nightmare", "Mov4": "Dream Eater"},
    {"name": "Onix", "Att": 45, "Vit": 160, "Def": 180, "SAt": 30, "SDf": 45, "Spe": 70, "Level": None, "Exp": None, "Type1": "Rock", "Type2": "Ground", "Mov1": "Rock Throw", "Mov2": "Harden", "Mov3": None, "Mov4": None},
    {"name": "Drowzee", "Att": 48, "Vit": 45, "Def": 40, "SAt": 43, "SDf": 90, "Spe": 42, "Level": None, "Exp": None, "Type1": "Psychic", "Type2": None, "Mov1": "Pound", "Mov2": "Hypnosis", "Mov3": "Disable", "Mov4": None},
    {"name": "Hypno", "Att": 73, "Vit": 70, "Def": 70, "SAt": 73, "SDf": 115, "Spe": 67, "Level": None, "Exp": None, "Type1": "Psychic", "Type2": None, "Mov1": "Psychic", "Mov2": "Hypnosis", "Mov3": "Headbutt", "Mov4": None},
    {"name": "Krabby", "Att": 105, "Vit": 90, "Def": 70, "SAt": 25, "SDf": 25, "Spe": 50, "Level": None, "Exp": None, "Type1": "Water", "Type2": None, "Mov1": "Bubble", "Mov2": "Vice Grip", "Mov3": None, "Mov4": None},
    {"name": "Kingler", "Att": 130, "Vit": 115, "Def": 90, "SAt": 50, "SDf": 50, "Spe": 75, "Level": None, "Exp": None, "Type1": "Water", "Type2": None, "Mov1": "Crabhammer", "Mov2": "Leer", "Mov3": "Stomp", "Mov4": None},
    {"name": "Voltorb", "Att": 30, "Vit": 50, "Def": 55, "SAt": 55, "SDf": 55, "Spe": 100, "Level": None, "Exp": None, "Type1": "Electric", "Type2": None, "Mov1": "Tackle", "Mov2": "Sonic Boom", "Mov3": None, "Mov4": None},
    {"name": "Electrode", "Att": 50, "Vit": 70, "Def": 80, "SAt": 80, "SDf": 80, "Spe": 150, "Level": None, "Exp": None, "Type1": "Electric", "Type2": None, "Mov1": "Spark", "Mov2": "Self-Destruct", "Mov3": "Swift", "Mov4": None},
    {"name": "Exeggcute", "Att": 40, "Vit": 80, "Def": 60, "SAt": 60, "SDf": 45, "Spe": 40, "Level": None, "Exp": None, "Type1": "Grass", "Type2": "Psychic", "Mov1": "Barrage", "Mov2": "Hypnosis", "Mov3": "Reflect", "Mov4": None},
    {"name": "Exeggutor", "Att": 95, "Vit": 125, "Def": 75, "SAt": 125, "SDf": 95, "Spe": 55, "Level": None, "Exp": None, "Type1": "Grass", "Type2": "Psychic", "Mov1": "Egg Bomb", "Mov2": "Stomp", "Mov3": "Sleep Powder", "Mov4": None},
    {"name": "Cubone", "Att": 50, "Vit": 50, "Def": 95, "SAt": 40, "SDf": 50, "Spe": 35, "Level": None, "Exp": None, "Type1": "Ground", "Type2": None, "Mov1": "Bone Club", "Mov2": "Growl", "Mov3": None, "Mov4": None},
    {"name": "Marowak", "Att": 80, "Vit": 80, "Def": 110, "SAt": 50, "SDf": 80, "Spe": 45, "Level": None, "Exp": None, "Type1": "Ground", "Type2": None, "Mov1": "Bonemerang", "Mov2": "Rage", "Mov3": "Focus Energy", "Mov4": None},
    {"name": "Hitmonlee", "Att": 120, "Vit": 53, "Def": 53, "SAt": 35, "SDf": 110, "Spe": 87, "Level": None, "Exp": None, "Type1": "Fighting", "Type2": None, "Mov1": "Rolling Kick", "Mov2": "Jump Kick", "Mov3": "Focus Energy", "Mov4": None},
    {"name": "Hitmonchan", "Att": 105, "Vit": 79, "Def": 105, "SAt": 35, "SDf": 110, "Spe": 76, "Level": None, "Exp": None, "Type1": "Fighting", "Type2": None, "Mov1": "Mega Punch", "Mov2": "Fire Punch", "Mov3": "Ice Punch", "Mov4": "Thunder Punch"},
    {"name": "Lickitung", "Att": 55, "Vit": 75, "Def": 50, "SAt": 60, "SDf": 75, "Spe": 30, "Level": None, "Exp": None, "Type1": "Normal", "Type2": None, "Mov1": "Lick", "Mov2": "Supersonic", "Mov3": None, "Mov4": None},
    {"name": "Koffing", "Att": 65, "Vit": 95, "Def": 85, "SAt": 60, "SDf": 85, "Spe": 35, "Level": None, "Exp": None, "Type1": "Poison", "Type2": None, "Mov1": "Tackle", "Mov2": "Smog", "Mov3": None, "Mov4": None},
    {"name": "Weezing", "Att": 90, "Vit": 120, "Def": 95, "SAt": 85, "SDf": 70, "Spe": 60, "Level": None, "Exp": None, "Type1": "Poison", "Type2": None, "Mov1": "Sludge", "Mov2": "Smokescreen", "Mov3": "Self-Destruct", "Mov4": None},
    {"name": "Rhyhorn", "Att": 85, "Vit": 80, "Def": 95, "SAt": 30, "SDf": 30, "Spe": 25, "Level": None, "Exp": None, "Type1": "Ground", "Type2": "Rock", "Mov1": "Horn Attack", "Mov2": "Stomp", "Mov3": None, "Mov4": None},
    {"name": "Rhydon", "Att": 130, "Vit": 105, "Def": 120, "SAt": 45, "SDf": 45, "Spe": 40, "Level": None, "Exp": None, "Type1": "Ground", "Type2": "Rock", "Mov1": "Rock Slide", "Mov2": "Fury Attack", "Mov3": "Horn Drill", "Mov4": None},
    {"name": "Chansey", "Att": 5, "Vit": 250, "Def": 5, "SAt": 35, "SDf": 105, "Spe": 50, "Level": None, "Exp": None, "Type1": "Normal", "Type2": None, "Mov1": "Pound", "Mov2": "Sing", "Mov3": "Heal Bell", "Mov4": None},
    {"name": "Tangela", "Att": 55, "Vit": 115, "Def": 85, "SAt": 100, "SDf": 40, "Spe": 60, "Level": None, "Exp": None, "Type1": "Grass", "Type2": None, "Mov1": "Constrict", "Mov2": "Sleep Powder", "Mov3": None, "Mov4": None},
    {"name": "Kangaskhan", "Att": 95, "Vit": 105, "Def": 80, "SAt": 40, "SDf": 80, "Spe": 90, "Level": None, "Exp": None, "Type1": "Normal", "Type2": None, "Mov1": "Comet Punch", "Mov2": "Leer", "Mov3": "Bite", "Mov4": "Dizzy Punch"},
    {"name": "Horsea", "Att": 40, "Vit": 70, "Def": 70, "SAt": 70, "SDf": 25, "Spe": 60, "Level": None, "Exp": None, "Type1": "Water", "Type2": None, "Mov1": "Bubble", "Mov2": "Smokescreen", "Mov3": None, "Mov4": None},
    {"name": "Seadra", "Att": 65, "Vit": 95, "Def": 95, "SAt": 95, "SDf": 45, "Spe": 85, "Level": None, "Exp": None, "Type1": "Water", "Type2": None, "Mov1": "Bubble Beam", "Mov2": "Smokescreen", "Mov3": "Agility", "Mov4": None},
    {"name": "Goldeen", "Att": 67, "Vit": 60, "Def": 60, "SAt": 35, "SDf": 50, "Spe": 63, "Level": None, "Exp": None, "Type1": "Water", "Type2": None, "Mov1": "Peck", "Mov2": "Tail Whip", "Mov3": None, "Mov4": None},
    {"name": "Seaking", "Att": 92, "Vit": 65, "Def": 65, "SAt": 65, "SDf": 80, "Spe": 68, "Level": None, "Exp": None, "Type1": "Water", "Type2": None, "Mov1": "Waterfall", "Mov2": "Horn Attack", "Mov3": "Fury Attack", "Mov4": None},
    {"name": "Staryu", "Att": 45, "Vit": 55, "Def": 55, "SAt": 70, "SDf": 55, "Spe": 85, "Level": None, "Exp": None, "Type1": "Water", "Type2": None, "Mov1": "Water Gun", "Mov2": "Harden", "Mov3": None, "Mov4": None},
    {"name": "Starmie", "Att": 75, "Vit": 85, "Def": 85, "SAt": 100, "SDf": 85, "Spe": 115, "Level": None, "Exp": None, "Type1": "Water", "Type2": "Psychic", "Mov1": "Swift", "Mov2": "Recover", "Mov3": "Minimize", "Mov4": None},
    {"name": "Mr. Mime", "Att": 45, "Vit": 65, "Def": 65, "SAt": 100, "SDf": 120, "Spe": 90, "Level": None, "Exp": None, "Type1": "Psychic", "Type2": "Fairy", "Mov1": "Confusion", "Mov2": "Barrier", "Mov3": "Light Screen", "Mov4": None},
    {"name": "Scyther", "Att": 110, "Vit": 80, "Def": 80, "SAt": 55, "SDf": 80, "Spe": 105, "Level": None, "Exp": None, "Type1": "Bug", "Type2": "Flying", "Mov1": "Slash", "Mov2": "Swords Dance", "Mov3": "Agility", "Mov4": None},
    {"name": "Jynx", "Att": 50, "Vit": 35, "Def": 35, "SAt": 115, "SDf": 95, "Spe": 95, "Level": None, "Exp": None, "Type1": "Ice", "Type2": "Psychic", "Mov1": "Ice Punch", "Mov2": "Lovely Kiss", "Mov3": "Powder Snow", "Mov4": None},
    {"name": "Electabuzz", "Att": 83, "Vit": 57, "Def": 57, "SAt": 95, "SDf": 85, "Spe": 105, "Level": None, "Exp": None, "Type1": "Electric", "Type2": None, "Mov1": "Thunder Punch", "Mov2": "Thunderbolt", "Mov3": "Swift", "Mov4": None},
    {"name": "Magmar", "Att": 95, "Vit": 57, "Def": 57, "SAt": 100, "SDf": 85, "Spe": 93, "Level": None, "Exp": None, "Type1": "Fire", "Type2": None, "Mov1": "Ember", "Mov2": "Leer", "Mov3": "Fire Punch", "Mov4": "Smokescreen"},
    {"name": "Pinsir", "Att": 125, "Vit": 100, "Def": 100, "SAt": 55, "SDf": 70, "Spe": 85, "Level": None, "Exp": None, "Type1": "Bug", "Type2": None, "Mov1": "Vice Grip", "Mov2": "Seismic Toss", "Mov3": None, "Mov4": None},
    {"name": "Tauros", "Att": 100, "Vit": 75, "Def": 95, "SAt": 40, "SDf": 70, "Spe": 110, "Level": None, "Exp": None, "Type1": "Normal", "Type2": None, "Mov1": "Tackle", "Mov2": "Stomp", "Mov3": "Tail Whip", "Mov4": None},
    {"name": "Magikarp", "Att": 10, "Vit": 20, "Def": 55, "SAt": 15, "SDf": 20, "Spe": 80, "Level": None, "Exp": None, "Type1": "Water", "Type2": None, "Mov1": "Splash", "Mov2": None, "Mov3": None, "Mov4": None},
    {"name": "Gyarados", "Att": 125, "Vit": 79, "Def": 70, "SAt": 60, "SDf": 100, "Spe": 81, "Level": None, "Exp": None, "Type1": "Water", "Type2": "Flying", "Mov1": "Dragon Rage", "Mov2": "Bite", "Mov3": "Leer", "Mov4": None},
    {"name": "Lapras", "Att": 85, "Vit": 80, "Def": 80, "SAt": 85, "SDf": 95, "Spe": 60, "Level": None, "Exp": None, "Type1": "Water", "Type2": "Ice", "Mov1": "Water Gun", "Mov2": "Sing", "Mov3": "Mist", "Mov4": "Confuse Ray"},
    {"name": "Ditto", "Att": 48, "Vit": 48, "Def": 48, "SAt": 48, "SDf": 48, "Spe": 48, "Level": None, "Exp": None, "Type1": "Normal", "Type2": None, "Mov1": "Transform", "Mov2": None, "Mov3": None, "Mov4": None},
    {"name": "Eevee", "Att": 55, "Vit": 50, "Def": 50, "SAt": 45, "SDf": 65, "Spe": 55, "Level": None, "Exp": None, "Type1": "Normal", "Type2": None, "Mov1": "Tackle", "Mov2": "Tail Whip", "Mov3": None, "Mov4": None},
    {"name": "Vaporeon", "Att": 65, "Vit": 60, "Def": 60, "SAt": 110, "SDf": 95, "Spe": 65, "Level": None, "Exp": None, "Type1": "Water", "Type2": None, "Mov1": "Water Gun", "Mov2": "Quick Attack", "Mov3": "Haze", "Mov4": None},
    {"name": "Jolteon", "Att": 65, "Vit": 60, "Def": 60, "SAt": 110, "SDf": 95, "Spe": 130, "Level": None, "Exp": None, "Type1": "Electric", "Type2": None, "Mov1": "Thunder Shock", "Mov2": "Quick Attack", "Mov3": "Double Kick", "Mov4": None},
    {"name": "Flareon", "Att": 130, "Vit": 60, "Def": 60, "SAt": 95, "SDf": 110, "Spe": 65, "Level": None, "Exp": None, "Type1": "Fire", "Type2": None, "Mov1": "Ember", "Mov2": "Quick Attack", "Mov3": "Fire Spin", "Mov4": None},
    {"name": "Porygon", "Att": 60, "Vit": 70, "Def": 70, "SAt": 85, "SDf": 75, "Spe": 40, "Level": None, "Exp": None, "Type1": "Normal", "Type2": None, "Mov1": "Tackle", "Mov2": "Sharpen", "Mov3": "Psybeam", "Mov4": "Agility"},
    {"name": "Omanyte", "Att": 40, "Vit": 35, "Def": 100, "SAt": 90, "SDf": 55, "Spe": 35, "Level": None, "Exp": None, "Type1": "Rock", "Type2": "Water", "Mov1": "Water Gun", "Mov2": "Horn Attack", "Mov3": "Withdraw", "Mov4": None},
    {"name": "Omastar", "Att": 60, "Vit": 70, "Def": 125, "SAt": 115, "SDf": 70, "Spe": 55, "Level": None, "Exp": None, "Type1": "Rock", "Type2": "Water", "Mov1": "Hydro Pump", "Mov2": "Horn Attack", "Mov3": "Withdraw", "Mov4": None},
    {"name": "Kabuto", "Att": 80, "Vit": 90, "Def": 105, "SAt": 55, "SDf": 45, "Spe": 55, "Level": None, "Exp": None, "Type1": "Rock", "Type2": "Water", "Mov1": "Scratch", "Mov2": "Harden", "Mov3": None, "Mov4": None},
    {"name": "Kabutops", "Att": 115, "Vit": 105, "Def": 125, "SAt": 65, "SDf": 70, "Spe": 80, "Level": None, "Exp": None, "Type1": "Rock", "Type2": "Water", "Mov1": "Slash", "Mov2": "Swords Dance", "Mov3": "Leer", "Mov4": None},
    {"name": "Aerodactyl", "Att": 105, "Vit": 65, "Def": 60, "SAt": 60, "SDf": 75, "Spe": 130, "Level": None, "Exp": None, "Type1": "Rock", "Type2": "Flying", "Mov1": "Wing Attack", "Mov2": "Agility", "Mov3": "Supersonic", "Mov4": None},
    {"name": "Snorlax", "Att": 110, "Vit": 160, "Def": 65, "SAt": 65, "SDf": 110, "Spe": 30, "Level": None, "Exp": None, "Type1": "Normal", "Type2": None, "Mov1": "Body Slam", "Mov2": "Rest", "Mov3": "Snore", "Mov4": None},
    {"name": "Articuno", "Att": 85, "Vit": 100, "Def": 85, "SAt": 125, "SDf": 95, "Spe": 85, "Level": None, "Exp": None, "Type1": "Ice", "Type2": "Flying", "Mov1": "Ice Beam", "Mov2": "Agility", "Mov3": "Mist", "Mov4": None},
    {"name": "Zapdos", "Att": 90, "Vit": 85, "Def": 90, "SAt": 125, "SDf": 90, "Spe": 100, "Level": None, "Exp": None, "Type1": "Electric", "Type2": "Flying", "Mov1": "Thunder Shock", "Mov2": "Drill Peck", "Mov3": "Thunder Wave", "Mov4": None},
    {"name": "Moltres", "Att": 100, "Vit": 90, "Def": 90, "SAt": 125, "SDf": 85, "Spe": 90, "Level": None, "Exp": None, "Type1": "Fire", "Type2": "Flying", "Mov1": "Ember", "Mov2": "Fire Spin", "Mov3": "Agility", "Mov4": None},
    {"name": "Dratini", "Att": 64, "Vit": 45, "Def": 45, "SAt": 50, "SDf": 50, "Spe": 50, "Level": None, "Exp": None, "Type1": "Dragon", "Type2": None, "Mov1": "Wrap", "Mov2": "Leer", "Mov3": "Thunder Wave", "Mov4": None},
    {"name": "Dragonair", "Att": 84, "Vit": 65, "Def": 65, "SAt": 70, "SDf": 70, "Spe": 70, "Level": None, "Exp": None, "Type1": "Dragon", "Type2": None, "Mov1": "Slam", "Mov2": "Agility", "Mov3": "Dragon Rage", "Mov4": "Safeguard"},
    {"name": "Dragonite", "Att": 134, "Vit": 95, "Def": 95, "SAt": 100, "SDf": 100, "Spe": 80, "Level": None, "Exp": None, "Type1": "Dragon", "Type2": "Flying", "Mov1": "Wing Attack", "Mov2": "Slam", "Mov3": "Agility", "Mov4": "Hyper Beam"},
    {"name": "Mewtwo", "Att": 110, "Vit": 90, "Def": 90, "SAt": 154, "SDf": 90, "Spe": 130, "Level": None, "Exp": None, "Type1": "Psychic", "Type2": None, "Mov1": "Confusion", "Mov2": "Disable", "Mov3": "Barrier", "Mov4": "Recover"},
    {"name": "Mew", "Att": 100, "Vit": 100, "Def": 100, "SAt": 100, "SDf": 100, "Spe": 100, "Level": None, "Exp": None, "Type1": "Psychic", "Type2": None, "Mov1": "Pound", "Mov2": "Transform", "Mov3": None, "Mov4": None}
]


My_PC= []

Moves_List=[
    {"name": "Acid", "Type": "Poison", "Category": "Special", "Power": 40, "Acc": 100, "PP": 30, "Effect": "May lower the target's Special Defense stat", "CritRatio": 1},
    {"name": "Amnesia", "Type": "Psychic", "Category": "Status", "Power": None, "Acc": None, "PP": 20, "Effect": "Raises the user's Special Defense stat", "CritRatio": 1},
    {"name": "Aurora Beam", "Type": "Ice", "Category": "Special", "Power": 65, "Acc": 100, "PP": 20, "Effect": "May lower the target's Attack stat", "CritRatio": 1},
    {"name": "Barrage", "Type": "Normal", "Category": "Physical", "Power": 15, "Acc": 85, "PP": 20, "Effect": "Hits 2-5 times in one turn", "CritRatio": 1},
    {"name": "Barrier", "Type": "Psychic", "Category": "Status", "Power": None, "Acc": None, "PP": 20, "Effect": "Raises the user's Defense stat", "CritRatio": 1},
    {"name": "Bide", "Type": "Normal", "Category": "Physical", "Power": None, "Acc": None, "PP": 10, "Effect": "User takes damage for two to three turns, then strikes back", "CritRatio": 1},
    {"name": "Bind", "Type": "Normal", "Category": "Physical", "Power": 15, "Acc": 85, "PP": 20, "Effect": "Traps and damages the target for 4-5 turns", "CritRatio": 1},
    {"name": "Blizzard", "Type": "Ice", "Category": "Special", "Power": 110, "Acc": 70, "PP": 5, "Effect": "May freeze the target", "CritRatio": 1},
    {"name": "Body Slam", "Type": "Normal", "Category": "Physical", "Power": 85, "Acc": 100, "PP": 15, "Effect": "May paralyze the target", "CritRatio": 1},
    {"name": "Bone Club", "Type": "Ground", "Category": "Physical", "Power": 65, "Acc": 85, "PP": 20, "Effect": "May cause flinching", "CritRatio": 1},
    {"name": "Bonemerang", "Type": "Ground", "Category": "Physical", "Power": 50, "Acc": 90, "PP": 10, "Effect": "Hits twice in one turn", "CritRatio": 1},
    {"name": "Bubble", "Type": "Water", "Category": "Special", "Power": 40, "Acc": 100, "PP": 30, "Effect": "May lower the target's Speed stat", "CritRatio": 1},
    {"name": "BubbleBeam", "Type": "Water", "Category": "Special", "Power": 65, "Acc": 100, "PP": 20, "Effect": "May lower the target's Speed stat", "CritRatio": 1},
    {"name": "Clamp", "Type": "Water", "Category": "Physical", "Power": 35, "Acc": 85, "PP": 10, "Effect": "Traps and damages the target for 4-5 turns", "CritRatio": 1},
    {"name": "Comet Punch", "Type": "Normal", "Category": "Physical", "Power": 18, "Acc": 85, "PP": 15, "Effect": "Hits 2-5 times in one turn", "CritRatio": 1},
    {"name": "Confuse Ray", "Type": "Ghost", "Category": "Status", "Power": None, "Acc": 100, "PP": 10, "Effect": "Confuses the target", "CritRatio": 1},
    {"name": "Confusion", "Type": "Psychic", "Category": "Special", "Power": 50, "Acc": 100, "PP": 25, "Effect": "May confuse the target", "CritRatio": 1},
    {"name": "Constrict", "Type": "Normal", "Category": "Physical", "Power": 10, "Acc": 100, "PP": 35, "Effect": "May lower the target's Speed stat", "CritRatio": 1},
    {"name": "Conversion", "Type": "Normal", "Category": "Status", "Power": None, "Acc": None, "PP": 30, "Effect": "Changes the user's type to that of a selected move", "CritRatio": 1},
    {"name": "Counter", "Type": "Fighting", "Category": "Physical", "Power": None, "Acc": 100, "PP": 20, "Effect": "Deals double the damage received from a physical attack back to the attacker", "CritRatio": 1},
    {"name": "Crabhammer", "Type": "Water", "Category": "Physical", "Power": 100, "Acc": 90, "PP": 10, "Effect": "High critical hit ratio", "CritRatio": 1.5},
    {"name": "Cut", "Type": "Normal", "Category": "Physical", "Power": 50, "Acc": 95, "PP": 30, "Effect": "None", "CritRatio": 1},
    {"name": "Defense Curl", "Type": "Normal", "Category": "Status", "Power": None, "Acc": None, "PP": 40, "Effect": "Raises the user's Defense stat", "CritRatio": 1},
    {"name": "Dig", "Type": "Ground", "Category": "Physical", "Power": 80, "Acc": 100, "PP": 10, "Effect": "Digs underground on first turn, attacks on second turn", "CritRatio": 1},
    {"name": "Disable", "Type": "Normal", "Category": "Status", "Power": None, "Acc": 100, "PP": 20, "Effect": "Disables the target's last used move", "CritRatio": 1},
    {"name": "Dizzy Punch", "Type": "Normal", "Category": "Physical", "Power": 70, "Acc": 100, "PP": 10, "Effect": "May confuse the target", "CritRatio": 1},
    {"name": "Double Kick", "Type": "Fighting", "Category": "Physical", "Power": 30, "Acc": 100, "PP": 30, "Effect": "Hits twice in one turn", "CritRatio": 1},
    {"name": "Double-Edge", "Type": "Normal", "Category": "Physical", "Power": 120, "Acc": 100, "PP": 15, "Effect": "User takes recoil damage", "CritRatio": 1},
    {"name": "Double Team", "Type": "Normal", "Category": "Status", "Power": None, "Acc": None, "PP": 15, "Effect": "Raises the user's evasion", "CritRatio": 1},
    {"name": "Double Slap", "Type": "Normal", "Category": "Physical", "Power": 15, "Acc": 85, "PP": 10, "Effect": "Hits 2-5 times in one turn", "CritRatio": 1},
    {"name": "Dragon Rage", "Type": "Dragon", "Category": "Special", "Power": None, "Acc": 100, "PP": 10, "Effect": "Always deals 40 HP of damage", "CritRatio": 1},
    {"name": "Dream Eater", "Type": "Psychic", "Category": "Special", "Power": 100, "Acc": 100, "PP": 15, "Effect": "User recovers half the HP inflicted on the target", "CritRatio": 1},
    {"name": "Drill Peck", "Type": "Flying", "Category": "Physical", "Power": 80, "Acc": 100, "PP": 20, "Effect": "None", "CritRatio": 1},
    {"name": "Earthquake", "Type": "Ground", "Category": "Physical", "Power": 100, "Acc": 100, "PP": 10, "Effect": "None", "CritRatio": 1},
    {"name": "Egg Bomb", "Type": "Normal", "Category": "Physical", "Power": 100, "Acc": 75, "PP": 10, "Effect": "None", "CritRatio": 1},
    {"name": "Ember", "Type": "Fire", "Category": "Special", "Power": 40, "Acc": 100, "PP": 25, "Effect": "May burn the target", "CritRatio": 1},
    {"name": "Explosion", "Type": "Normal", "Category": "Physical", "Power": 250, "Acc": 100, "PP": 5, "Effect": "User faints", "CritRatio": 1},
    {"name": "Fire Blast", "Type": "Fire", "Category": "Special", "Power": 110, "Acc": 85, "PP": 5, "Effect": "May burn the target", "CritRatio": 1},
    {"name": "Fire Punch", "Type": "Fire", "Category": "Physical", "Power": 75, "Acc": 100, "PP": 15, "Effect": "May burn the target", "CritRatio": 1},
    {"name": "Fire Spin", "Type": "Fire", "Category": "Special", "Power": 35, "Acc": 85, "PP": 15, "Effect": "Traps and damages the target for 4-5 turns", "CritRatio": 1},
    {"name": "Fissure", "Type": "Ground", "Category": "Physical", "Power": None, "Acc": 30, "PP": 5, "Effect": "One-Hit-KO, if it hits", "CritRatio": 1},
    {"name": "Flamethrower", "Type": "Fire", "Category": "Special", "Power": 90, "Acc": 100, "PP": 15, "Effect": "May burn the target", "CritRatio": 1},
    {"name": "Flash", "Type": "Normal", "Category": "Status", "Power": None, "Acc": 100, "PP": 20, "Effect": "Lowers the target's accuracy", "CritRatio": 1},
    {"name": "Fly", "Type": "Flying", "Category": "Physical", "Power": 90, "Acc": 95, "PP": 15, "Effect": "Flies up on first turn, then strikes the next turn", "CritRatio": 1},
    {"name": "Focus Energy", "Type": "Normal", "Category": "Status", "Power": None, "Acc": None, "PP": 30, "Effect": "Increases the user's critical hit ratio", "CritRatio": 1},
    {"name": "Fury Attack", "Type": "Normal", "Category": "Physical", "Power": 15, "Acc": 85, "PP": 20, "Effect": "Hits 2-5 times in one turn", "CritRatio": 1},
    {"name": "Fury Swipes", "Type": "Normal", "Category": "Physical", "Power": 18, "Acc": 80, "PP": 15, "Effect": "Hits 2-5 times in one turn", "CritRatio": 1},
    {"name": "Glare", "Type": "Normal", "Category": "Status", "Power": None, "Acc": 100, "PP": 30, "Effect": "Paralyzes the target", "CritRatio": 1},
    {"name": "Growl", "Type": "Normal", "Category": "Status", "Power": None, "Acc": 100, "PP": 40, "Effect": "Lowers the target's Attack stat", "CritRatio": 1},
    {"name": "Growth", "Type": "Normal", "Category": "Status", "Power": None, "Acc": None, "PP": 40, "Effect": "Raises the user's Attack and Special Attack stats", "CritRatio": 1},
    {"name": "Guillotine", "Type": "Normal", "Category": "Physical", "Power": None, "Acc": 30, "PP": 5, "Effect": "One-Hit-KO, if it hits", "CritRatio": 1},
    {"name": "Gust", "Type": "Flying", "Category": "Special", "Power": 40, "Acc": 100, "PP": 35, "Effect": "None", "CritRatio": 1},
    {"name": "Harden", "Type": "Normal", "Category": "Status", "Power": None, "Acc": None, "PP": 30, "Effect": "Raises the user's Defense stat", "CritRatio": 1},
    {"name": "Headbutt", "Type": "Normal", "Category": "Physical", "Power": 70, "Acc": 100, "PP": 15, "Effect": "May cause flinching", "CritRatio": 1},
    {"name": "High Jump Kick", "Type": "Fighting", "Category": "Physical", "Power": 130, "Acc": 90, "PP": 10, "Effect": "If it misses, the user loses half their maximum HP", "CritRatio": 1},
    {"name": "Horn Attack", "Type": "Normal", "Category": "Physical", "Power": 65, "Acc": 100, "PP": 25, "Effect": "None", "CritRatio": 1},
    {"name": "Horn Drill", "Type": "Normal", "Category": "Physical", "Power": None, "Acc": 30, "PP": 5, "Effect": "One-Hit-KO, if it hits", "CritRatio": 1},
    {"name": "Hydro Pump", "Type": "Water", "Category": "Special", "Power": 110, "Acc": 80, "PP": 5, "Effect": "None", "CritRatio": 1},
    {"name": "Hyper Beam", "Type": "Normal", "Category": "Special", "Power": 150, "Acc": 90, "PP": 5, "Effect": "User must recharge next turn", "CritRatio": 1},
    {"name": "Hyper Fang", "Type": "Normal", "Category": "Physical", "Power": 80, "Acc": 90, "PP": 15, "Effect": "May cause flinching", "CritRatio": 1},
    {"name": "Hyper Voice", "Type": "Normal", "Category": "Special", "Power": 90, "Acc": 100, "PP": 10, "Effect": "None", "CritRatio": 1},
    {"name": "Hypnosis", "Type": "Psychic", "Category": "Status", "Power": None, "Acc": 60, "PP": 20, "Effect": "Puts the target to sleep", "CritRatio": 1},
    {"name": "Ice Beam", "Type": "Ice", "Category": "Special", "Power": 90, "Acc": 100, "PP": 10, "Effect": "May freeze the target", "CritRatio": 1},
    {"name": "Ice Punch", "Type": "Ice", "Category": "Physical", "Power": 75, "Acc": 100, "PP": 15, "Effect": "May freeze the target", "CritRatio": 1},
    {"name": "Jump Kick", "Type": "Fighting", "Category": "Physical", "Power": 70, "Acc": 95, "PP": 25, "Effect": "If it misses, the user loses half their maximum HP", "CritRatio": 1},
    {"name": "Karate Chop", "Type": "Fighting", "Category": "Physical", "Power": 50, "Acc": 100, "PP": 25, "Effect": "High critical hit ratio", "CritRatio": 0},
    {"name": "Kinesis", "Type": "Psychic", "Category": "Status", "Power": None, "Acc": 80, "PP": 15, "Effect": "Lowers the target's Accuracy", "CritRatio": 1},
    {"name": "Leech Life", "Type": "Bug", "Category": "Physical", "Power": 80, "Acc": 100, "PP": 10, "Effect": "User recovers half the HP inflicted on the target", "CritRatio": 1},
    {"name": "Leech Seed", "Type": "Grass", "Category": "Status", "Power": None, "Acc": 90, "PP": 10, "Effect": "Drains the target's HP over time", "CritRatio": 1},
    {"name": "Leer", "Type": "Normal", "Category": "Status", "Power": None, "Acc": 100, "PP": 30, "Effect": "Lowers the target's Defense stat", "CritRatio": 1},
    {"name": "Lick", "Type": "Ghost", "Category": "Physical", "Power": 30, "Acc": 100, "PP": 30, "Effect": "May paralyze the target", "CritRatio": 1},
    {"name": "Light Screen", "Type": "Psychic", "Category": "Status", "Power": None, "Acc": None, "PP": 30, "Effect": "Halves damage from special attacks for 5 turns", "CritRatio": 1},
    {"name": "Lovely Kiss", "Type": "Normal", "Category": "Status", "Power": None, "Acc": 75, "PP": 10, "Effect": "Puts the target to sleep", "CritRatio": 1},
    {"name": "Low Kick", "Type": "Fighting", "Category": "Physical", "Power": None, "Acc": 100, "PP": 20, "Effect": "The heavier the target, the stronger the attack", "CritRatio": 1},
    {"name": "Mega Drain", "Type": "Grass", "Category": "Special", "Power": 40, "Acc": 100, "PP": 15, "Effect": "User recovers half the HP inflicted on the target", "CritRatio": 1},
    {"name": "Mega Kick", "Type": "Normal", "Category": "Physical", "Power": 120, "Acc": 75, "PP": 5, "Effect": "None", "CritRatio": 1},
    {"name": "Mega Punch", "Type": "Normal", "Category": "Physical", "Power": 80, "Acc": 85, "PP": 20, "Effect": "None", "CritRatio": 1},
    {"name": "Metronome", "Type": "Normal", "Category": "Status", "Power": None, "Acc": None, "PP": 10, "Effect": "Randomly selects and uses any move in the game", "CritRatio": 1},
    {"name": "Mimic", "Type": "Normal", "Category": "Status", "Power": None, "Acc": None, "PP": 10, "Effect": "Permanently copies the opponent's last used move", "CritRatio": 1},
    {"name": "Minimize", "Type": "Normal", "Category": "Status", "Power": None, "Acc": None, "PP": 20, "Effect": "Sharply raises the user's evasion", "CritRatio": 1},
    {"name": "Mirror Move", "Type": "Flying", "Category": "Status", "Power": None, "Acc": None, "PP": 20, "Effect": "Copies the opponent's last used move and uses it", "CritRatio": 1},
    {"name": "Mist", "Type": "Ice", "Category": "Status", "Power": None, "Acc": None, "PP": 30, "Effect": "Prevents stat reductions in the user's party", "CritRatio": 1},
    {"name": "Night Shade", "Type": "Ghost", "Category": "Special", "Power": None, "Acc": 100, "PP": 15, "Effect": "Inflicts damage equal to the user's level", "CritRatio": 1},
    {"name": "Pay Day", "Type": "Normal", "Category": "Physical", "Power": 40, "Acc": 100, "PP": 20, "Effect": "User receives money after battle", "CritRatio": 1},
    {"name": "Peck", "Type": "Flying", "Category": "Physical", "Power": 35, "Acc": 100, "PP": 35, "Effect": "None", "CritRatio": 1},
    {"name": "Petal Dance", "Type": "Grass", "Category": "Special", "Power": 120, "Acc": 100, "PP": 10, "Effect": "User becomes uncontrollable for 2-3 turns", "CritRatio": 1},
    {"name": "Pin Missile", "Type": "Bug", "Category": "Physical", "Power": 25, "Acc": 95, "PP": 20, "Effect": "Hits 2-5 times in one turn", "CritRatio": 1},
    {"name": "Poison Gas", "Type": "Poison", "Category": "Status", "Power": None, "Acc": 90, "PP": 40, "Effect": "Poisons the target", "CritRatio": 1},
    {"name": "Poison Sting", "Type": "Poison", "Category": "Physical", "Power": 15, "Acc": 100, "PP": 35, "Effect": "May poison the target", "CritRatio": 1},
    {"name": "Poisonpowder", "Type": "Poison", "Category": "Status", "Power": None, "Acc": 75, "PP": 35, "Effect": "Poisons the target", "CritRatio": 1},
    {"name": "Pound", "Type": "Normal", "Category": "Physical", "Power": 40, "Acc": 100, "PP": 35, "Effect": "None", "CritRatio": 1},
    {"name": "Psybeam", "Type": "Psychic", "Category": "Special", "Power": 65, "Acc": 100, "PP": 20, "Effect": "May confuse the target", "CritRatio": 1},
    {"name": "Psychic", "Type": "Psychic", "Category": "Special", "Power": 90, "Acc": 100, "PP": 10, "Effect": "May lower the target's Special Defense stat", "CritRatio": 1},
    {"name": "Psywave", "Type": "Psychic", "Category": "Special", "Power": None, "Acc": 100, "PP": 15, "Effect": "Inflicts random damage between 0.5x and 1.5x the user's level", "CritRatio": 1},
    {"name": "Quick Attack", "Type": "Normal", "Category": "Physical", "Power": 40, "Acc": 100, "PP": 30, "Effect": "User attacks first", "CritRatio": 1},
    {"name": "Rage", "Type": "Normal", "Category": "Physical", "Power": 20, "Acc": 100, "PP": 20, "Effect": "Raises the user's Attack stat when hit", "CritRatio": 1},
    {"name": "Razor Leaf", "Type": "Grass", "Category": "Physical", "Power": 55, "Acc": 95, "PP": 25, "Effect": "High critical hit ratio", "CritRatio": 0},
    {"name": "Razor Wind", "Type": "Normal", "Category": "Special", "Power": 80, "Acc": 100, "PP": 10, "Effect": "Charges on first turn, then strikes on the next", "CritRatio": 0},
    {"name": "Reflect", "Type": "Psychic", "Category": "Status", "Power": None, "Acc": None, "PP": 20, "Effect": "Halves damage from physical attacks for 5 turns", "CritRatio": 1},
    {"name": "Rest", "Type": "Psychic", "Category": "Status", "Power": None, "Acc": None, "PP": 10, "Effect": "User sleeps for 2 turns and restores HP and status", "CritRatio": 1},
    {"name": "Roar", "Type": "Normal", "Category": "Status", "Power": None, "Acc": None, "PP": 20, "Effect": "In battles, the opponent switches. In the wild, the Pokemon runs", "CritRatio": 1},
    {"name": "Rock Slide", "Type": "Rock", "Category": "Physical", "Power": 75, "Acc": 90, "PP": 10, "Effect": "May cause flinching", "CritRatio": 1},
    {"name": "Rock Throw", "Type": "Rock", "Category": "Physical", "Power": 50, "Acc": 90, "PP": 15, "Effect": "None", "CritRatio": 1},
    {"name": "Rolling Kick", "Type": "Fighting", "Category": "Physical", "Power": 60, "Acc": 85, "PP": 15, "Effect": "May cause flinching", "CritRatio": 1},
    {"name": "Sand-Attack", "Type": "Ground", "Category": "Status", "Power": None, "Acc": 100, "PP": 15, "Effect": "Lowers the target's Accuracy", "CritRatio": 1},
    {"name": "Scratch", "Type": "Normal", "Category": "Physical", "Power": 40, "Acc": 100, "PP": 35, "Effect": "None", "CritRatio": 1},
    {"name": "Screech", "Type": "Normal", "Category": "Status", "Power": None, "Acc": 85, "PP": 40, "Effect": "Sharply lowers the target's Defense stat", "CritRatio": 1},
    {"name": "Seismic Toss", "Type": "Fighting", "Category": "Physical", "Power": None, "Acc": 100, "PP": 20, "Effect": "Inflicts damage equal to the user's level", "CritRatio": 1},
    {"name": "Self-Destruct", "Type": "Normal", "Category": "Physical", "Power": 200, "Acc": 100, "PP": 5, "Effect": "User faints and deals damage to the target", "CritRatio": 1},
    {"name": "Shadow Ball", "Type": "Ghost", "Category": "Special", "Power": 80, "Acc": 100, "PP": 15, "Effect": "May lower the target's Special Defense stat", "CritRatio": 1},
    {"name": "Sharpen", "Type": "Normal", "Category": "Status", "Power": None, "Acc": None, "PP": 30, "Effect": "Raises the user's Attack stat", "CritRatio": 1},
    {"name": "Sing", "Type": "Normal", "Category": "Status", "Power": None, "Acc": 55, "PP": 15, "Effect": "Puts the target to sleep", "CritRatio": 1},
    {"name": "Sketch", "Type": "Normal", "Category": "Status", "Power": None, "Acc": None, "PP": 1, "Effect": "Permanently copies the opponent's last used move", "CritRatio": 1},
    {"name": "Skull Bash", "Type": "Normal", "Category": "Physical", "Power": 130, "Acc": 100, "PP": 10, "Effect": "Charges on first turn, then strikes on the next. May cause flinching", "CritRatio": 1},
    {"name": "Sky Attack", "Type": "Flying", "Category": "Physical", "Power": 140, "Acc": 90, "PP": 5, "Effect": "Charges on first turn, then strikes on the next. May cause flinching", "CritRatio": 0},
    {"name": "Slam", "Type": "Normal", "Category": "Physical", "Power": 80, "Acc": 75, "PP": 20, "Effect": "None", "CritRatio": 1},
    {"name": "Slash", "Type": "Normal", "Category": "Physical", "Power": 70, "Acc": 100, "PP": 20, "Effect": "High critical hit ratio", "CritRatio": 0},
    {"name": "Sleep Powder", "Type": "Grass", "Category": "Status", "Power": None, "Acc": 75, "PP": 15, "Effect": "Puts the target to sleep", "CritRatio": 1},
    {"name": "Sludge", "Type": "Poison", "Category": "Special", "Power": 65, "Acc": 100, "PP": 20, "Effect": "May poison the target", "CritRatio": 1},
    {"name": "Smog", "Type": "Poison", "Category": "Special", "Power": 30, "Acc": 70, "PP": 20, "Effect": "May poison the target", "CritRatio": 1},
    {"name": "Smokescreen", "Type": "Normal", "Category": "Status", "Power": None, "Acc": 100, "PP": 20, "Effect": "Lowers the target's Accuracy", "CritRatio": 1},
    {"name": "Soft-Boiled", "Type": "Normal", "Category": "Status", "Power": None, "Acc": None, "PP": 10, "Effect": "Restores the user's HP", "CritRatio": 1},
    {"name": "Solar Beam", "Type": "Grass", "Category": "Special", "Power": 120, "Acc": 100, "PP": 10, "Effect": "Charges on first turn, then strikes on the next", "CritRatio": 1},
    {"name": "Sonic Boom", "Type": "Normal", "Category": "Special", "Power": None, "Acc": 90, "PP": 20, "Effect": "Always inflicts 20 HP", "CritRatio": 1},
    {"name": "Spike Cannon", "Type": "Normal", "Category": "Physical", "Power": 20, "Acc": 100, "PP": 15, "Effect": "Hits 2-5 times in one turn", "CritRatio": 1},
    {"name": "Spore", "Type": "Grass", "Category": "Status", "Power": None, "Acc": 100, "PP": 15, "Effect": "Puts the target to sleep", "CritRatio": 1},
    {"name": "Stomp", "Type": "Normal", "Category": "Physical", "Power": 65, "Acc": 100, "PP": 20, "Effect": "May cause flinching", "CritRatio": 1},
    {"name": "Strength", "Type": "Normal", "Category": "Physical", "Power": 80, "Acc": 100, "PP": 15, "Effect": "None", "CritRatio": 1},
    {"name": "String Shot", "Type": "Bug", "Category": "Status", "Power": None, "Acc": 95, "PP": 40, "Effect": "Lowers the target's Speed stat", "CritRatio": 1},
    {"name": "Struggle", "Type": "Normal", "Category": "Physical", "Power": 50, "Acc": None, "PP": None, "Effect": "Only usable when all PP are gone. Hurts the user", "CritRatio": 1},
    {"name": "Stun Spore", "Type": "Grass", "Category": "Status", "Power": None, "Acc": 75, "PP": 30, "Effect": "Paralyzes the target", "CritRatio": 1},
    {"name": "Submission", "Type": "Fighting", "Category": "Physical", "Power": 80, "Acc": 80, "PP": 25, "Effect": "User receives recoil damage", "CritRatio": 1},
    {"name": "Substitute", "Type": "Normal", "Category": "Status", "Power": None, "Acc": None, "PP": 10, "Effect": "Uses HP to creates a decoy that takes hits", "CritRatio": 1},
    {"name": "Super Fang", "Type": "Normal", "Category": "Physical", "Power": None, "Acc": 90, "PP": 10, "Effect": "Inflicts damage equal to half the target's HP", "CritRatio": 1},
    {"name": "Supersonic", "Type": "Normal", "Category": "Status", "Power": None, "Acc": 55, "PP": 20, "Effect": "Confuses the target", "CritRatio": 1},
    {"name": "Surf", "Type": "Water", "Category": "Special", "Power": 90, "Acc": 100, "PP": 15, "Effect": "May hit multiple targets", "CritRatio": 1},
    {"name": "Swift", "Type": "Normal", "Category": "Special", "Power": 60, "Acc": None, "PP": 20, "Effect": "Bypasses Accuracy and Evasion modifiers", "CritRatio": 1},
    {"name": "Swords Dance", "Type": "Normal", "Category": "Status", "Power": None, "Acc": None, "PP": 20, "Effect": "Sharply raises the user's Attack stat", "CritRatio": 1},
    {"name": "Tackle", "Type": "Normal", "Category": "Physical", "Power": 40, "Acc": 100, "PP": 35, "Effect": "None", "CritRatio": 1},
    {"name": "Tail Whip", "Type": "Normal", "Category": "Status", "Power": None, "Acc": 100, "PP": 30, "Effect": "Lowers the target's Defense stat", "CritRatio": 1},
    {"name": "Take Down", "Type": "Normal", "Category": "Physical", "Power": 90, "Acc": 85, "PP": 20, "Effect": "User receives recoil damage", "CritRatio": 1},
    {"name": "Teleport", "Type": "Psychic", "Category": "Status", "Power": None, "Acc": None, "PP": 20, "Effect": "Allows the user to flee wild battles; also warps the user to the last Pokemon Center", "CritRatio": 1},
    {"name": "Thrash", "Type": "Normal", "Category": "Physical", "Power": 120, "Acc": 100, "PP": 10, "Effect": "User becomes uncontrollable for 2-3 turns", "CritRatio": 1},
    {"name": "Thunder", "Type": "Electric", "Category": "Special", "Power": 110, "Acc": 70, "PP": 10, "Effect": "May paralyze the target", "CritRatio": 1},
    {"name": "Thunder Punch", "Type": "Electric", "Category": "Physical", "Power": 75, "Acc": 100, "PP": 15, "Effect": "May paralyze the target", "CritRatio": 1},
    {"name": "Thunder Shock", "Type": "Electric", "Category": "Special", "Power": 40, "Acc": 100, "PP": 30, "Effect": "May paralyze the target", "CritRatio": 1},
    {"name": "Thunder Wave", "Type": "Electric", "Category": "Status", "Power": None, "Acc": 90, "PP": 20, "Effect": "Paralyzes the target", "CritRatio": 1},
    {"name": "Thunderbolt", "Type": "Electric", "Category": "Special", "Power": 90, "Acc": 100, "PP": 15, "Effect": "May paralyze the target", "CritRatio": 1},
    {"name": "Toxic", "Type": "Poison", "Category": "Status", "Power": None, "Acc": 90, "PP": 10, "Effect": "Badly poisons the target", "CritRatio": 1},
    {"name": "Transform", "Type": "Normal", "Category": "Status", "Power": None, "Acc": None, "PP": 10, "Effect": "User becomes a copy of the target until it leaves battle", "CritRatio": 1},
    {"name": "Tri Attack", "Type": "Normal", "Category": "Special", "Power": 80, "Acc": 100, "PP": 10, "Effect": "May paralyze, burn, or freeze the target", "CritRatio": 1},
    {"name": "Twineedle", "Type": "Bug", "Category": "Physical", "Power": 25, "Acc": 100, "PP": 20, "Effect": "Hits twice and may poison the target", "CritRatio": 1},
    {"name": "Twister", "Type": "Dragon", "Category": "Special", "Power": 40, "Acc": 100, "PP": 20, "Effect": "May cause flinching", "CritRatio": 1},
    {"name": "Vice Grip", "Type": "Normal", "Category": "Physical", "Power": 55, "Acc": 100, "PP": 30, "Effect": "None", "CritRatio": 1},
    {"name": "Vine Whip", "Type": "Grass", "Category": "Physical", "Power": 45, "Acc": 100, "PP": 25, "Effect": "None", "CritRatio": 1},
    {"name": "Water Gun", "Type": "Water", "Category": "Special", "Power": 40, "Acc": 100, "PP": 25, "Effect": "None", "CritRatio": 1},
    {"name": "Waterfall", "Type": "Water", "Category": "Physical", "Power": 80, "Acc": 100, "PP": 15, "Effect": "May cause flinching", "CritRatio": 1},
    {"name": "Whirlwind", "Type": "Normal", "Category": "Status", "Power": None, "Acc": None, "PP": 20, "Effect": "In battles, the opponent switches. In the wild, the Pokemon runs", "CritRatio": 1},
    {"name": "Wing Attack", "Type": "Flying", "Category": "Physical", "Power": 60, "Acc": 100, "PP": 35, "Effect": "None", "CritRatio": 1},
    {"name": "Withdraw", "Type": "Water", "Category": "Status", "Power": None, "Acc": None, "PP": 40, "Effect": "Raises the user's Defense stat", "CritRatio": 1},
    {"name": "Wrap", "Type": "Normal", "Category": "Physical", "Power": 15, "Acc": 90, "PP": 20, "Effect": "Traps the target for 2-5 turns", "CritRatio": 1},
    {"name": "Zap Cannon", "Type": "Electric", "Category": "Special", "Power": 120, "Acc": 50, "PP": 5, "Effect": "Paralyzes the target", "CritRatio": 1}
]

Type_Effectiveness = [
    {"Type": "Normal", "Normal": "Normal", "Fighting": "Normal", "Flying": "Normal", "Poison": "Normal", "Ground": "Normal", "Rock": "Normal", "Bug": "Normal", "Ghost": "Ineffective", "Steel": "Not Effective", "Fire": "Normal", "Water": "Normal", "Grass": "Normal", "Electric": "Normal", "Psychic": "Normal", "Ice": "Normal", "Dragon": "Normal", "Dark": "Not Effective", "Fairy": "Normal"},
    {"Type": "Fighting", "Normal": "Super Effective", "Fighting": "Normal", "Flying": "Not Effective", "Poison": "Not Effective", "Ground": "Normal", "Rock": "Super Effective", "Bug": "Not Effective", "Ghost": "Ineffective", "Steel": "Super Effective", "Fire": "Normal", "Water": "Normal", "Grass": "Normal", "Electric": "Normal", "Psychic": "Not Effective", "Ice": "Super Effective", "Dragon": "Normal", "Dark": "Super Effective", "Fairy": "Not Effective"},
    {"Type": "Flying", "Normal": "Normal", "Fighting": "Super Effective", "Flying": "Normal", "Poison": "Normal", "Ground": "Ineffective", "Rock": "Not Effective", "Bug": "Super Effective", "Ghost": "Normal", "Steel": "Not Effective", "Fire": "Normal", "Water": "Normal", "Grass": "Super Effective", "Electric": "Not Effective", "Psychic": "Normal", "Ice": "Normal", "Dragon": "Normal", "Dark": "Normal", "Fairy": "Normal"},
    {"Type": "Poison", "Normal": "Normal", "Fighting": "Normal", "Flying": "Normal", "Poison": "Not Effective", "Ground": "Super Effective", "Rock": "Normal", "Bug": "Normal", "Ghost": "Normal", "Steel": "Ineffective", "Fire": "Normal", "Water": "Normal", "Grass": "Super Effective", "Electric": "Normal", "Psychic": "Normal", "Ice": "Normal", "Dragon": "Normal", "Dark": "Normal", "Fairy": "Super Effective"},
    {"Type": "Ground", "Normal": "Normal", "Fighting": "Normal", "Flying": "Normal", "Poison": "Normal", "Ground": "Normal", "Rock": "Super Effective", "Bug": "Normal", "Ghost": "Normal", "Steel": "Super Effective", "Fire": "Super Effective", "Water": "Super Effective", "Grass": "Not Effective", "Electric": "Super Effective", "Psychic": "Normal", "Ice": "Normal", "Dragon": "Normal", "Dark": "Normal", "Fairy": "Normal"},
    {"Type": "Rock", "Normal": "Normal", "Fighting": "Not Effective", "Flying": "Super Effective", "Poison": "Normal", "Ground": "Not Effective", "Rock": "Normal", "Bug": "Super Effective", "Ghost": "Normal", "Steel": "Super Effective", "Fire": "Super Effective", "Water": "Normal", "Grass": "Normal", "Electric": "Normal", "Psychic": "Normal", "Ice": "Super Effective", "Dragon": "Normal", "Dark": "Normal", "Fairy": "Normal"},
    {"Type": "Bug", "Normal": "Normal", "Fighting": "Not Effective", "Flying": "Not Effective", "Poison": "Not Effective", "Ground": "Normal", "Rock": "Normal", "Bug": "Normal", "Ghost": "Normal", "Steel": "Not Effective", "Fire": "Normal", "Water": "Normal", "Grass": "Super Effective", "Electric": "Normal", "Psychic": "Super Effective", "Ice": "Normal", "Dragon": "Normal", "Dark": "Super Effective", "Fairy": "Normal"},
    {"Type": "Ghost", "Normal": "Ineffective", "Fighting": "Normal", "Flying": "Normal", "Poison": "Normal", "Ground": "Normal", "Rock": "Normal", "Bug": "Normal", "Ghost": "Super Effective", "Steel": "Normal", "Fire": "Normal", "Water": "Normal", "Grass": "Normal", "Electric": "Normal", "Psychic": "Super Effective", "Ice": "Normal", "Dragon": "Normal", "Dark": "Ineffective", "Fairy": "Normal"},
    {"Type": "Steel", "Normal": "Normal", "Fighting": "Super Effective", "Flying": "Normal", "Poison": "Ineffective", "Ground": "Super Effective", "Rock": "Super Effective", "Bug": "Normal", "Ghost": "Normal", "Steel": "Not Effective", "Fire": "Not Effective", "Water": "Normal", "Grass": "Normal", "Electric": "Normal", "Psychic": "Normal", "Ice": "Super Effective", "Dragon": "Normal", "Dark": "Normal", "Fairy": "Super Effective"},
    {"Type": "Fire", "Normal": "Normal", "Fighting": "Normal", "Flying": "Normal", "Poison": "Normal", "Ground": "Normal", "Rock": "Super Effective", "Bug": "Normal", "Ghost": "Normal", "Steel": "Super Effective", "Fire": "Not Effective", "Water": "Not Effective", "Grass": "Super Effective", "Electric": "Normal", "Psychic": "Normal", "Ice": "Normal", "Dragon": "Normal", "Dark": "Normal", "Fairy": "Normal"},
    {"Type": "Water", "Normal": "Normal", "Fighting": "Normal", "Flying": "Normal", "Poison": "Normal", "Ground": "Super Effective", "Rock": "Super Effective", "Bug": "Normal", "Ghost": "Normal", "Steel": "Not Effective", "Fire": "Super Effective", "Water": "Not Effective", "Grass": "Not Effective", "Electric": "Normal", "Psychic": "Normal", "Ice": "Normal", "Dragon": "Normal", "Dark": "Normal", "Fairy": "Normal"},
    {"Type": "Grass", "Normal": "Normal", "Fighting": "Normal", "Flying": "Not Effective", "Poison": "Super Effective", "Ground": "Not Effective", "Rock": "Normal", "Bug": "Super Effective", "Ghost": "Normal", "Steel": "Not Effective", "Fire": "Not Effective", "Water": "Super Effective", "Grass": "Not Effective", "Electric": "Normal", "Psychic": "Normal", "Ice": "Normal", "Dragon": "Normal", "Dark": "Normal", "Fairy": "Normal"},
    {"Type": "Electric", "Normal": "Normal", "Fighting": "Normal", "Flying": "Super Effective", "Poison": "Normal", "Ground": "Ineffective", "Rock": "Normal", "Bug": "Normal", "Ghost": "Normal", "Steel": "Normal", "Fire": "Normal", "Water": "Super Effective", "Grass": "Not Effective", "Electric": "Not Effective", "Psychic": "Normal", "Ice": "Normal", "Dragon": "Normal", "Dark": "Normal", "Fairy": "Normal"},
    {"Type": "Psychic", "Normal": "Normal", "Fighting": "Super Effective", "Flying": "Normal", "Poison": "Normal", "Ground": "Normal", "Rock": "Normal", "Bug": "Normal", "Ghost": "Normal", "Steel": "Ineffective", "Fire": "Normal", "Water": "Normal", "Grass": "Normal", "Electric": "Normal", "Psychic": "Not Effective", "Ice": "Normal", "Dragon": "Normal", "Dark": "Super Effective", "Fairy": "Normal"},
    {"Type": "Ice", "Normal": "Normal", "Fighting": "Normal", "Flying": "Super Effective", "Poison": "Normal", "Ground": "Super Effective", "Rock": "Normal", "Bug": "Normal", "Ghost": "Normal", "Steel": "Super Effective", "Fire": "Super Effective", "Water": "Super Effective", "Grass": "Normal", "Electric": "Normal", "Psychic": "Normal", "Ice": "Not Effective", "Dragon": "Super Effective", "Dark": "Normal", "Fairy": "Normal"},
    {"Type": "Dragon", "Normal": "Normal", "Fighting": "Normal", "Flying": "Normal", "Poison": "Normal", "Ground": "Normal", "Rock": "Normal", "Bug": "Normal", "Ghost": "Normal", "Steel": "Normal", "Fire": "Normal", "Water": "Normal", "Grass": "Normal", "Electric": "Normal", "Psychic": "Normal", "Ice": "Super Effective", "Dragon": "Super Effective", "Dark": "Normal", "Fairy": "Not Effective"},
    {"Type": "Dark", "Normal": "Normal", "Fighting": "Normal", "Flying": "Normal", "Poison": "Normal", "Ground": "Normal", "Rock": "Normal", "Bug": "Normal", "Ghost": "Super Effective", "Steel": "Normal", "Fire": "Normal", "Water": "Normal", "Grass": "Normal", "Electric": "Normal", "Psychic": "Super Effective", "Ice": "Normal", "Dragon": "Normal", "Dark": "Not Effective", "Fairy": "Normal"},
    {"Type": "Fairy", "Normal": "Normal", "Fighting": "Super Effective", "Flying": "Normal", "Poison": "Not Effective", "Ground": "Normal", "Rock": "Normal", "Bug": "Normal", "Ghost": "Normal", "Steel": "Not Effective", "Fire": "Normal", "Water": "Normal", "Grass": "Normal", "Electric": "Normal", "Psychic": "Normal", "Ice": "Normal", "Dragon": "Super Effective", "Dark": "Super Effective", "Fairy": "Normal"}
]

Nemesis_PC=[]
Status_Chart_Oponent=[{"name": "Squirtle","HP": None, "Status": None, "Def": 0, "SDf": 0, "Att": 0, "SAt": 0, "Spe": 0, "Acc": 0}]
Status_Chart=[{"name": "Charmander", "HP": None, "Status": None, "Def": 0, "SDf": 0, "Att": 0, "SAt": 0, "Spe": 0, "Acc": 0}]


def Pokemon_Stats(Pokemon_List, Pokemon_Name):
    for pokemon in Pokemon_List:
        if pokemon["name"] == Pokemon_Name:
            return pokemon
    raise ValueError("Wrong name, please try again.")


def Fight_Trainer_Calc(User, Oponent, Level_O):
    #Pokemon fighting music
    #Get stats from Pokemon A
    for Pokemons in My_PC:
        if Pokemons["name"]== User:
            Level_U=Pokemons["Level"]
            Vit_U=Pokemons["Vit"]
            Spe_U=Pokemons["Spe"]
            Mov1_U=Pokemons["Mov1"]
            Mov2_U=Pokemons["Mov2"]
            Mov3_U=Pokemons["Mov3"]
            Mov4_U=Pokemons["Mov4"]
    #Get stats from pokemon B
    for Pokemons in Pokemon_List:
        if Pokemons["name"]== Oponent:
            Vit_O=Pokemons["Vit"]
            Spe_O=Pokemons["Spe"]
            Mov1_O=Pokemons["Mov1"]
            Mov2_O=Pokemons["Mov2"]
            Mov3_O=Pokemons["Mov3"]
            Mov4_O=Pokemons["Mov4"]
    #Set Total HP values
    HP_U=(((2*Vit_U+0+0)*Level_U)/100)+Level_U+10
    print(f"Your {User} has {HP_U} HP")
    HP_O=(((2*Vit_O+0+0)*Level_U)/100)+Level_U+10
    print(f"The Oponent´s {Oponent} has {HP_O} HP")
    #Asumo EV e IV 0 por ahora y base sus stats de Vit


    while HP_O > 0 or HP_U >0:
        #What action does the trainer take
        for Status in Status_Chart_Oponent:
            if Status["name"] == Oponent:
                O_Mon_Spe=Status["Spe"]
                S_O_Stat=Status_Change(O_Mon_Spe)
        for Status in Status_Chart:
            if Status["name"] == User:
                U_Mon_Spe=Status["Spe"]
                S_U_Stat=Status_Change(U_Mon_Spe)

        print("What will you do? ")
        Opt=input("Fight        Bag ")
        if Opt == "Fight":
            while True:
                Att=input(f"{Mov1_U}        {Mov2_U}            {Mov3_U}            {Mov4_U}    ")
                if Att != Mov4_U and Att != Mov1_U and Att != Mov2_U and Att != Mov3_U:
                    print("Please select one of the vailable moves")
                else:
                    break
            Actual_Speed_U=Spe_U * S_U_Stat
            Actual_Speed_O=Spe_O * S_O_Stat
            #check speeds, considering changes in speed stat
            if Actual_Speed_U > Actual_Speed_O:
                #User hits first
                Damage=Damage_Calc(Att, User, Oponent, Level_U, Status_Chart_Oponent, Status_Chart)
                HP_O=HP_O - Damage
                print((f"The Oponent´s {Oponent} has {HP_O} HP"))
                if HP_O <= 0:
                    return print("You win")
                MovRand = [Mov1_O, Mov2_O, Mov3_O, Mov4_O]
                RandAtt = random.choice(MovRand)
                print(RandAtt)
                Damage=Damage_Calc(RandAtt, Oponent, User, Level_O, Status_Chart, Status_Chart_Oponent)
                HP_U=HP_U - Damage
                print((f"Your {User} has {HP_U} HP"))
                if HP_U <= 0:
                    return print("You lose")
            else:
                #PC Hits first
                MovRand = [Mov1_O, Mov2_O, Mov3_O, Mov4_O]
                RandAtt = random.choice(MovRand)
                Damage=Damage_Calc(RandAtt, Oponent, User, Level_O)
                HP_U=HP_U - Damage
                print((f"Your {User} has {HP_U} HP"))
                if HP_U <= 0:
                    return print("You lose")
                Damage=Damage_Calc(Att, User, Oponent, Level_U)
                HP_O=HP_O - Damage
                print((f"The Oponent´s {Oponent} has {HP_O} HP"))
                if HP_O <= 0:
                    return print("You win")
        #first att, calc dmg, take hp, if >0, print hp, then 
        #Second att, calc dmg, take hp, if >0, print hp, then
        
def Get_Stat(Stat_To_Get, List_To_Use, Name):
    for Pokemons in List_To_Use:
        if Pokemons["name"]== Name:
            Stat=Pokemons[Stat_To_Get]
            return Stat

def Damage_Calc(Move, AtackingMon, DefensiveMon, Level, St_CH_Def_Mon, St_Ch_Att_Mon):
    #Dejare para desp el miss chance en respuesta
    #Get stats for calc
    for Pokemons in My_PC:
        if Pokemons["name"]== AtackingMon:
            AType1=Pokemons["Type1"]
            AType2=Pokemons["Type2"]
    for Pokemons in Pokemon_List:
        if Pokemons["name"]== DefensiveMon:
            DType1=Pokemons["Type1"]
            DType2=Pokemons["Type2"]
    for Moves in Moves_List:
        if Moves["name"]== Move:
            Power=Moves["Power"]
            MType=Moves["Type"]
            Critical_Chance=Moves["CritRatio"]
            Cat=Moves["Category"]
    for Status in St_Ch_Att_Mon:
        if Status["name"] == AtackingMon:
            AMon_Att=Status["Att"]
            AMon_SAt=Status["SAt"]

    for Status in St_CH_Def_Mon:
        if Status["name"] == DefensiveMon:
            DMon_Def=Status["Def"]
            DMon_SDf=Status["SDf"]     

    #Correct stats of att and def
    if Cat == "Status":
        Status_Move(St_CH_Def_Mon)
        #ApplyStatusChange
        return
    elif Cat== "Physical":
        A=Get_Stat("Att", My_PC, AtackingMon)
        D=Get_Stat("Def", Pokemon_List, DefensiveMon)
        AStat=Status_Change(AMon_Att)
        DStat=Status_Change(DMon_Def)
    else:
        A=Get_Stat("SAt", My_PC, AtackingMon)
        D=Get_Stat("SDf", Pokemon_List, DefensiveMon)
        AStat=Status_Change(AMon_SAt)
        DStat=Status_Change(DMon_SDf)
        
    #Crit
    if Critical_Chance== 1:
        rand=random.randrange(0, 100)
        if rand < 25:
            Critical=2
            print("Its a critical hit! ")
        else:
            Critical=1
    else:
        rand=random.randrange(0, 100)
        if rand < 50:
            Critical=2
            print("Its a critical hit! ")
        else:
            Critical=1

    #STAB Get_stats
    if MType == AType1 or MType == AType2:
        STAB= 1.5
    else:
        STAB=1
    #Pokemons Type effectiveness   
    for Effectiveness in Type_Effectiveness:
        if Effectiveness["Type"]== AType1 and Effectiveness["Type"] != None:
            if Effectiveness[DType1]=="Not Effective":
                TypeDif1=0.5
            elif Effectiveness[DType1]=="Ineffective":
                TypeDif1=0
            elif Effectiveness[DType1]=="Super Effective":
                TypeDif1=2
            else:
                TypeDif1=1
            if Effectiveness[DType2]=="Not Effective":
                TypeDif1=0.5
            elif Effectiveness[DType2]=="Ineffective":
                TypeDif1=0
            elif Effectiveness[DType2]=="Super Effective":
                TypeDif1=2
            else:
                TypeDif1=1  
        else:
            TypeDif1=1
    #Second Type
    for Effectiveness in Type_Effectiveness:
        if Effectiveness["Type"]== AType2 and Effectiveness["Type"] != None:
            if Effectiveness[DType1]=="Not Effective":
                TypeDif2=0.5
            elif Effectiveness[DType1]=="Ineffective":
                TypeDif2=0
            elif Effectiveness[DType1]=="Super Effective":
                TypeDif2=2
            else:
                TypeDif2=1
            if Effectiveness[DType2]=="Not Effective":
                TypeDif2=0.5
            elif Effectiveness[DType2]=="Ineffective":
                TypeDif2=0
            elif Effectiveness[DType2]=="Super Effective":
                TypeDif2=2
            else:
                TypeDif2=1 
        else:
            TypeDif2=1
    #Rand
    rand=random.randrange(85, 100, 1)
    Rand=rand/100
    
    Dmg=(((((2*Level*Critical)/5)*Power*((A*AStat)/(D*DStat)))/50)+2)*STAB*TypeDif1*TypeDif2*Rand    
    return Dmg

def Status_Move(Status_Chart_DefensiveMon):
    #needs sharply reducing stats or increasing stats, plus status
    for moves in Moves_List:
        if moves["Effect"]=="Lowers the target's Defense stat":
            A=Status_Chart_DefensiveMon[0]["Def"]
            Status_Chart_DefensiveMon.update({"Def": (A-1)})
        elif moves["Effect"]=="Lowers the target's Speed stat":
            A=Status_Chart_DefensiveMon[0]["Spe"]
            Status_Chart_DefensiveMon.update({"Spe": (A-1)})
        elif moves["Effect"]=="Lowers the target's Attack stat":
            A=Status_Chart_DefensiveMon[0]["Att"]
            Status_Chart_DefensiveMon.update({"Att": (A-1)})
        elif moves["Effect"]=="Lowers the target's Accurracy stat":
            A=Status_Chart_DefensiveMon[0]["Acc"]
            Status_Chart_DefensiveMon.update({"Acc": (A-1)})
        elif moves["Effect"]=="May lower the target's Special Defense stat":
            A=Status_Chart_DefensiveMon[0]["SDf"]
            Status_Chart_DefensiveMon.update({"SDf": (A-1)})
        else:
            print("Dude what whas that?!") #Change the [0] por actual pokemon in chart
    
def Status_Change(Stat):

    if Stat == -1:
        AStat=0.67
    elif Stat == -2:
        AStat=0.5
    elif Stat == -3:
        AStat=0.4
    elif Stat == -4:
        AStat=0.33
    elif Stat == -5:
        AStat=0.29
    elif Stat < -6:
        AStat=0.25
    elif Stat == 0:
        AStat=1
    elif Stat == 1:
        AStat=1.5
    elif Stat == 2:
        AStat=2
    elif Stat == 3:
        AStat=2.5
    elif Stat == 4:
        AStat=3
    elif Stat == 5:
        AStat=3.5
    else:
        AStat=4
    return AStat


def main():

#pedir nombre
    #name = input("What´s your name? ")
    #print(f"Welcome to the Pokémon world {name}, choose one of these Pokémon as a partner in your new journey.")
    
#elegir pokemon random
    Pokemones= [ "Charmander", "Bulbasaur", "Squirtle"]
    print("The options are ", end="")
    for poke in Pokemones:
        print(poke, end=" ")
    print("")
    while True:
        Starter = input("Which one do you choose? ")
        if Starter == "Charmander":
            print("You chose Charmander")
            Nemesis="Squirtle"
            break
        elif Starter == "Bulbasaur":
            print("You chose Bulbasaur.")
            Nemesis="Charmander"
            break
        elif Starter =="Squirtle":
            print("You chose Squirtle.")
            Nemesis="Bulbasaur"
            break
        else:
            print("Please choose one of the available Pokemon.")
    First_Pokemon=Pokemon_Stats(Pokemon_List, Starter)
    First_Pokemon.update({"Level": 5})
    My_PC.append(First_Pokemon)
    First_Nemesis_Pokemon=Pokemon_Stats(Pokemon_List, Nemesis)
    First_Nemesis_Pokemon.update({"Level": 5})
    Nemesis_PC.append(First_Nemesis_Pokemon)
    print("You have a ", My_PC[0]["name"], "and it´s level ", My_PC[0]["Level"] )
    
    
    
    
#primer encuentro
    #Who vs Who
    print("Larry: Now that we´ve got our first pokemon, lets duel and see who is best")
    Level_O=5
    Fight_Trainer_Calc(Starter, Nemesis, Level_O)
    #Enemy = Rand_Encounter(Pokemon_List)
    #Fight(Starter, Enemy, Pokemon_List)


#Rand Encounter
def Rand_Encounter(Pokemon_List):
    x=random.choice([10, 13, 16, 19, 21, 25])
    Encounter=(Pokemon_List[x]["name"])
    print("You have encountered a ", Encounter)
    return Pokemon_List[x]["name"]


if __name__ == "__main__":
    main()