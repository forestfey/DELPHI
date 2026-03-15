#!/usr/bin/env python3
"""
DELPHI Reading Generator (Structural Reference)

Generates a complete DELPHI spread in standard notation.
Uses Python PRNG — for actual readings, use physical dice and coins.

License: CC-BY-NC-SA 4.0
"""

import random
from datetime import date

# Element mappings (d6)
ELEMENTS = {
    1: ("Fire", "red"),
    2: ("Air", "green"),
    3: ("Earth", "yellow"),
    4: ("Water", "blue"),
    5: ("Vortex", "purple"),
    6: ("Star", "gold"),
}

# Fey card archetypes
FEY_CARDS = {
    1: "Creation",
    2: "Anchor",
    3: "Pathfinder",
    4: "Synthesis",
    5: "Flow",
    6: "Abundance",
    7: "Decay",
    8: "Source",
}

# King Wen sequence (hexagram number by binary value 0-63)
# Binary: bottom line = bit 0, top line = bit 5
# up (yang) = 1, down (yin) = 0
KING_WEN = {
    0: (2, "Receptive"), 1: (23, "Splitting Apart"), 2: (8, "Holding Together"),
    3: (20, "Contemplation"), 4: (16, "Enthusiasm"), 5: (35, "Progress"),
    6: (45, "Gathering Together"), 7: (12, "Standstill"), 8: (15, "Modesty"),
    9: (52, "Keeping Still"), 10: (39, "Obstruction"), 11: (53, "Development"),
    12: (62, "Small Exceeding"), 13: (56, "Wanderer"), 14: (31, "Influence"),
    15: (33, "Retiring"), 16: (7, "Army"), 17: (4, "Youthful Folly"),
    18: (29, "Abysmal"), 19: (59, "Dispersion"), 20: (40, "Deliverance"),
    21: (64, "Before Completion"), 22: (47, "Oppression"), 23: (6, "Conflict"),
    24: (46, "Pushing Upward"), 25: (18, "Work on the Decayed"),
    26: (48, "Well"), 27: (57, "Gentle"), 28: (32, "Duration"),
    29: (50, "Cauldron"), 30: (28, "Great Exceeding"), 31: (44, "Coming to Meet"),
    32: (24, "Return"), 33: (27, "Nourishment"), 34: (3, "Difficulty at Beginning"),
    35: (42, "Increase"), 36: (51, "Arousing"), 37: (21, "Biting Through"),
    38: (17, "Following"), 39: (25, "Innocence"), 40: (36, "Darkening of Light"),
    41: (22, "Grace"), 42: (63, "After Completion"), 43: (37, "Family"),
    44: (55, "Abundance"), 45: (30, "Radiance"), 46: (49, "Revolution"),
    47: (13, "Fellowship"), 48: (19, "Approach"), 49: (41, "Decrease"),
    50: (60, "Limitation"), 51: (61, "Inner Truth"), 52: (54, "Marrying Maiden"),
    53: (38, "Opposition"), 54: (58, "Joyous"), 55: (10, "Treading"),
    56: (11, "Peace"), 57: (26, "Great Taming"), 58: (5, "Waiting"),
    59: (9, "Small Taming"), 60: (34, "Great Invigorating"),
    61: (14, "Great Possession"), 62: (43, "Breakthrough"),
    63: (1, "Creative"),
}


def spin_to_binary(spin):
    """Convert spin direction to binary: up=1 (yang), down=0 (yin)."""
    return 1 if spin == "up" else 0


def derive_hexagrams(dice_spins, card_spins):
    """
    Derive two hexagrams from the 6 spin values.

    Left-to-right (dice then cards), starting from top line:
    Line 6 (top) = dice[0] spin
    Line 5 = dice[1] spin
    Line 4 = dice[2] spin
    Line 3 = card[0] spin
    Line 2 = card[1] spin
    Line 1 (bottom) = card[2] spin

    Right-to-left reverses the order.
    """
    all_spins = dice_spins + card_spins
    all_reversed = list(reversed(all_spins))

    # Convert to binary values (top line = most significant bit)
    lr_binary = 0
    rl_binary = 0
    for i, s in enumerate(all_spins):
        lr_binary |= spin_to_binary(s) << (5 - i)
    for i, s in enumerate(all_reversed):
        rl_binary |= spin_to_binary(s) << (5 - i)

    lr_hex = KING_WEN.get(lr_binary, (0, "Unknown"))
    rl_hex = KING_WEN.get(rl_binary, (0, "Unknown"))

    return lr_hex, rl_hex


def generate_reading():
    """Generate a complete DELPHI spread."""
    # Card selection (3 from 8, no repeats)
    cards = random.sample(range(1, 9), 3)

    # Dice rolls (3 x d6)
    dice = [random.randint(1, 6) for _ in range(3)]

    # Spins (6 coin tosses)
    spins = [random.choice(["up", "down"]) for _ in range(6)]
    dice_spins = spins[:3]
    card_spins = spins[3:]

    # Derive hexagrams
    lr_hex, rl_hex = derive_hexagrams(dice_spins, card_spins)

    # Format output
    dice_labels = ["G", "B", "W"]
    card_positions = ["Past/Shadow", "Present/Ego", "Future/Environment"]

    print(f"DELPHI Reading — {date.today()}")
    print(f"{'=' * 50}")
    print()

    # Dice line
    dice_parts = []
    for i, (label, roll, spin) in enumerate(zip(dice_labels, dice, dice_spins)):
        elem_name = ELEMENTS[roll][0]
        dice_parts.append(f"{label}={roll}-{elem_name}({spin})")
    print(f"Dice: {', '.join(dice_parts)}")

    # Cards line
    card_parts = []
    for i, (num, spin) in enumerate(zip(cards, card_spins)):
        card_name = FEY_CARDS[num]
        card_parts.append(f"{num}-{card_name}({spin})")
    print(f"Feycards: {', '.join(card_parts)}")

    # Hexagrams
    print(f"Hexagrams: L-R={lr_hex[0]} ({lr_hex[1]}) | R-L={rl_hex[0]} ({rl_hex[1]})")

    print()
    print("--- Spread Detail ---")
    print()

    # Dice detail
    for label, roll, spin in zip(dice_labels, dice, dice_spins):
        elem_name, elem_color = ELEMENTS[roll]
        role = {"G": "Initial Impulse", "B": "Distortion", "W": "Liberation/Medicine"}[label]
        print(f"  {label} ({role}): {roll}-{elem_name} ({spin})")

    print()

    # Card detail
    for i, (num, spin) in enumerate(zip(cards, card_spins)):
        card_name = FEY_CARDS[num]
        print(f"  Card {i+1} ({card_positions[i]}): {num}-{card_name} ({spin})")

    print()
    print("--- Interpretation is left to the practitioner. ---")
    print()
    print("NOTE: This output was generated with Python PRNG.")
    print("For actual readings, use physical d6 and coins (HRNG).")


if __name__ == "__main__":
    generate_reading()
