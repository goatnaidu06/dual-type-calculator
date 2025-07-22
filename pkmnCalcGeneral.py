import pandas as pd

# Type effectiveness chart (Offense types as rows, Defense types as columns)
pokemon = {
    "Bug":     [1, 2, 1, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 2, 1, 1, 0.5, 2, 1, 0.5, 1],
    "Dark":    [1, 0.5, 1, 1, 0.5, 0.5, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1],
    "Dragon":  [1, 1, 2, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 1],
    "Electric":[1, 1, 0.5, 0.5, 1, 1, 1, 2, 1, 0, 0.5, 1, 1, 1, 1, 1, 1, 2],
    "Fairy":   [1, 2, 2, 1, 1, 2, 0.5, 1, 1, 1, 1, 1, 1, 0.5, 1, 1, 0.5, 1],
    "Fighting":[0.5, 2, 1, 1, 0.5, 1, 1, 0.5, 0, 1, 1, 2, 2, 0.5, 0.5, 2, 2, 1],
    "Fire":    [2, 1, 0.5, 1, 1, 1, 0.5, 1, 1, 1, 2, 2, 1, 1, 1, 0.5, 2, 0.5],
    "Flying":  [2, 1, 1, 0.5, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0.5, 0.5, 1],
    "Ghost":   [1, 0.5, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0, 1, 2, 1, 1, 1],
    "Ground":  [0.5, 1, 1, 2, 1, 1, 2, 0, 1, 1, 0.5, 1, 1, 2, 1, 2, 2, 1],
    "Grass":   [0.5, 1, 0.5, 1, 1, 1, 0.5, 0.5, 1, 2, 0.5, 1, 1, 0.5, 1, 2, 0.5, 2],
    "Ice":     [1, 1, 2, 1, 1, 1, 0.5, 2, 1, 2, 2, 0.5, 1, 1, 1, 1, 0.5, 0.5],
    "Normal":  [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0.5, 0.5, 1],
    "Poison":  [1, 1, 1, 1, 2, 1, 1, 1, 0.5, 0.5, 2, 1, 1, 0.5, 1, 0.5, 0, 1],
    "Psychic": [1, 0, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 0.5, 1, 0.5, 1],
    "Rock":    [2, 1, 1, 1, 1, 0.5, 2, 2, 1, 0.5, 1, 2, 1, 1, 1, 1, 0.5, 1],
    "Steel":   [1, 1, 1, 0.5, 2, 1, 0.5, 1, 1, 1, 1, 2, 1, 1, 1, 2, 0.5, 0.5],
    "Water":   [1, 1, 0.5, 1, 1, 1, 2, 1, 1, 2, 0.5, 1, 1, 1, 1, 2, 1, 0.5]
}

# Create DataFrame with offense types as rows and defense types as columns
df = pd.DataFrame(pokemon, index=pokemon.keys()).T

# User input handling
def clean_input(type_name):
    type_name = type_name.strip().capitalize()
    if type_name not in df.columns:
        print(f"Error: '{type_name}' is not a valid Pokémon type.")
        exit()
    return type_name

type1 = clean_input(input("Enter your first type: "))
type2 = clean_input(input("Enter your second type: "))

if type1 == type2:
    print("Invalid input: A Pokémon cannot have the same type twice.")
    exit()

# Compute combined effectiveness
combined_eff = df[type1] * df[type2]

# Get unique weaknesses, resistances, and immunities
weaknessesquad = sorted(set(combined_eff[combined_eff == 4].index.tolist()))  # Weaknesses (4×)
weaknesses = sorted(set(combined_eff[combined_eff == 2].index.tolist()))  # Weaknesses (2×)
resistances = sorted(set(combined_eff[combined_eff == 0.5].index.tolist()))  # Resistances (0.5×)
resistancesquad = sorted(set(combined_eff[combined_eff == 0.25].index.tolist()))  # Resistances (0.5×)
immunities = sorted(set(combined_eff[combined_eff == 0].index.tolist()))  # Immunities (0×)

defenses2 = len(resistances) + len(resistancesquad) + len(immunities)
totalbody2 = defenses2 + len(weaknesses) + len(weaknessesquad)

defensivescore2 = (defenses2 / totalbody2) * 100

defenses1 = len(resistances) + len(immunities)
totalbody1 = defenses1 + len(weaknesses)

defensivescore1 = (defenses1 / totalbody1) * 100

# Output results
print(f"A dual-type {type1}/{type2} Pokémon has:")
print(f"- {len(weaknessesquad)} quad-weaknesses (4x damage from): {', '.join(weaknessesquad) if weaknessesquad else 'None'}")
print(f"- {len(weaknesses)} weaknesses (2x damage from): {', '.join(weaknesses) if weaknesses else 'None'}")
print(f"- {len(resistances)} resistances (0.5x damage from): {', '.join(resistances) if resistances else 'None'}")
print(f"- {len(resistancesquad)} quad-resistances (0.25x damage from): {', '.join(resistancesquad) if resistancesquad else 'None'}")
print(f"- {len(immunities)} immunities (zero effect from): {', '.join(immunities) if immunities else 'None'}")
print(f"Defensive Score: {round(defensivescore2, 2)}%")
