# Pokémon Dual-Type Weakness & Resistance Calculator

A Python-based terminal utility that calculates **weaknesses, resistances, quad-weaknesses, immunities**, and overall **defensive score** for any theoretical or real **dual-type Pokémon** combination — even if no Pokémon with that combination exists (e.g., Fairy/Ground or Bug/Dragon).

This tool is ideal for competitive theorycrafting, fakemon design, or exploring rare type synergies.

## 🔍 Features

- Accepts any combination of two Pokémon types  
- Supports existing and non-existent dual-type combos  
- Calculates:
  - Weaknesses (2×)
  - Quad-weaknesses (4×)
  - Resistances (0.5×)
  - Quad-resistances (0.25×)
  - Immunities (0×)
  - Defensive score (overall type durability)
- Clean terminal output

## 🧠 How It Works

- A type-effectiveness dictionary is used as a matrix.
- User inputs two types (in any order).
- The script computes how each of the 18 attack types interact with the chosen dual typing.
- Types are normalized (e.g., "ICE" → "Ice").

Effectiveness multipliers follow official game mechanics:
- **4.0×** = Quad Weakness  
- **2.0×** = Weakness  
- **1.0×** = Neutral  
- **0.5×** = Resistance  
- **0.25×** = Quad Resistance  
- **0.0×** = Immunity  

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/goatnaidu06/dual-type-calculator.git  
cd dual-type-calculator  
```

### 2. Install Dependencies

```bash
pip install pandas  
```

### 3. Run the Program

```bash
python3 pkmnCalcGeneral.py  
```

### 4. Enter Your Type Combination

```
Enter your first type: Fairy
Enter your second type: Ground
A dual-type Fairy/Ground Pokémon has:
- 0 quad-weaknesses (4x damage from): None
- 4 weaknesses (2x damage from): Grass, Ice, Steel, Water
- 4 resistances (0.5x damage from): Bug, Dark, Fighting, Rock
- 0 quad-resistances (0.25x damage from): None
- 2 immunities (zero effect from): Dragon, Electric
Defensive Score: 60.0%
```

## 📁 File Structure

```
pkmnCalcGeneral.py    # Main script for general dual-type calculation  
README.md             # Project documentation
LICENSE.txt           # Project license
```

## 🎯 Ideal Use Cases

- Design and balance your own Pokémon or fan region  
- Explore underused or unique dual types for team building  
- Analyze defensive potential of custom types in ROM hacks or fan games  

## 📜 License

MIT License. See [LICENSE](LICENSE.txt) for details.

## 👨‍💻 Author

**Neil Naidu**  
[GitHub Profile](https://github.com/goatnaidu06)
