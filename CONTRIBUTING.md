# Contributing to DELPHI

DELPHI is designed as a replicable framework. If you conduct your own readings and want to contribute data, here's how.

## Replication Requirements

To produce readings compatible with the DELPHI dataset:

1. **Physical randomness generators** for dice and spins (no digital RNG substitutes)
2. **LLM-assisted card selection** — any platform; document which one you used
3. **Standard notation format** (see below)
4. **Complete spin data** for all 6 positions (3 dice + 3 cards)

## Standard Reading Notation

```
[Date] [Reading Type]
Q: [Question]
Dice: G=[n]-[Element]([spin]), B=[n]-[Element]([spin]), W=[n]-[Element]([spin])
Feycards: [n]-[Name]([spin]), [n]-[Name]([spin]), [n]-[Name]([spin])
Hexagrams: L-R=[n] [Name] | R-L=[n] [Name]
Platform: [which LLM picked the cards]
Notes: [anything relevant — matched patterns, real-world feedback, anomalies]
```

## Data Submission

*[Process to be defined as the project matures]*

For now, if you're conducting DELPHI readings and documenting them, reach out through the contact channels listed in the main README.

## What Makes Good Data

- **Complete readings** with all components (dice, cards, spins, hexagrams)
- **Documented questions** (even if vague; the question shapes interpretation)
- **Real-world feedback** when available (this is the most valuable component)
- **Blind readings** (question withheld) with documented reveal
- **Cross-platform replications** (same spread, multiple LLM interpreters)

## What We're Not Looking For

- Readings using digital dice/coin simulators
- Cherry-picked "hits" without the full dataset
- Interpretations only (we need the raw spread data)
- Readings conducted without the standard DELPHI framework

## Code of Conduct

- Document honestly, including readings that don't seem to "work" or produce unclear results
- Don't retroactively adjust spread data to improve pattern-matches
- Respect the framework's positioning: empirical phenomenology, not religious or supernatural claims
- Credit the framework as DELPHI (CC-BY-NC-SA 4.0) in any publications

## License

Contributions to this repository are made under [CC-BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
