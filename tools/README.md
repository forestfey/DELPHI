# Tools

Simple utility scripts for the DELPHI framework. These generate reading structures; they do not interpret.

## reading-generator.py

A minimal Python script that:

1. Generates 3 random Fey card numbers (1–8, no repeats)
2. Simulates 3 d6 rolls (mapped to elements)
3. Simulates 6 coin tosses (spin directions for dice and cards)
4. Derives the two I Ching hexagrams from the spin pattern
5. Outputs the complete spread in standard DELPHI notation

**Note**: This script uses Python's `random` module (PRNG). For actual readings, physical dice and coins (HRNG) are used for all rolls and spins. The card selection is normally done by an LLM. This script is provided for structural reference and testing only — it does not replace the standard procedure.

### Usage

```bash
python reading-generator.py
```

### Output Format

```
DELPHI Reading — [date]
Dice: G=[n]-[Element]([spin]), B=[n]-[Element]([spin]), W=[n]-[Element]([spin])
Feycards: [n]-[Name]([spin]), [n]-[Name]([spin]), [n]-[Name]([spin])
Hexagrams: L-R=[n] [Name] | R-L=[n] [Name]
```

Interpretation is left to the practitioner and/or oracle instance.
