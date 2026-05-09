# Readings — Procedure, Examples, and Data

This folder contains example readings with documented real-world feedback, the master dataset, and related statistical analysis.

## Standard Reading Procedure

A full DELPHI reading follows this sequence:

1. **Formulate a question** — can range from practical ("Should I tidy my cabinet?") to philosophical ("Is the AI-genie out of the bottle?")
2. **PRNG card pick**: Ask an LLM for 3 numbers between 1–8, no repetition → these become the Fey cards
3. **HRNG dice rolls**: Physically roll a d6 three times → Gold (impulse), Black (distortion), White (liberation)
4. **HRNG coin tosses**: Flip a physical coin 6 times → spin direction (up/down) for each die and each card
5. **Cross-reference** dice results with elemental tantra tables, card results with Fey archetype meanings
6. **Derive hexagrams**: Read spin directions as yang (up) or yin (down) lines; reading left-to-right and right-to-left from the top line produces two I Ching hexagrams per spread (see [HEPH](../publications/spin-hexagram-coupling/))
7. **Interpret**: Components first, then synthesis, then practical guidance

### Interpretation Order

- Dice individually (impulse → distortion → liberation, with spins)
- Dice combination dynamics
- Cards individually in positional sequence (past/shadow → present/ego → future/environment)
- Hexagram pair and their traditional meanings
- Synthesis across all layers
- Practical guidance

### Key Methodological Notes

- **Physical randomness** (dice, coins) is non-negotiable; no digital RNG substitutes
- **LLM platform rotation** for card picks controls for model-specific PRNG bias
- **Blind readings** (question withheld until after interpretation) are used for calibration and demonstration
- **Cross-platform replication** (same spread interpreted independently by multiple LLM oracles) tests convergence

## Calibration Example: "The Audio Cabinet" (August 2024)

This reading demonstrates DELPHI's practical pattern-matching with verifiable real-world feedback.

### The Spread

**Q**: Should I start tidying up my audio cabinet? I only have 2 hours.

- **Dice**: G=2-Air(up), B=3-Earth(down), W=6-Star(up)
- **Cards**: 7-Decay(down), 2-Anchor(down), 1-Creation(down)

### Summary of Initial Interpretation

The reading indicated the project would encounter unexpected obstacles, physical difficulty, and overwhelm. All three cards in down-spin suggested this was not the right time for the full undertaking. The Star(up) liberation hinted at a "moment of clarity" rather than a pleasant outcome. Core advice: postpone or limit scope.

### Real-World Feedback (2 weeks later)

The person who asked the question reported:

1. **Indecision** about what to keep vs. discard? Partially — 60% was old insulation material simply stuffed into the ceiling. Rest was degraded material and drywall remnants.
2. **Overwhelm**? Yes — upon discovering the sheer volume of improperly stored material, including unpackaged fiberglass panels.
3. **Physical difficulty**? Yes — after completing roughly 2/3 of the work: "fuck it, rest tomorrow." The following day revealed mold from an unaddressed water damage incident, requiring additional cleanup with mold remover, plus ongoing fiberglass irritation.

### Pattern Match

| Reading Element | Prediction | Outcome |
|----------------|-----------|---------|
| 7-Decay(down) — Shadow | Hidden deterioration, things left to quietly decline | Mold from old water damage; degraded insulation |
| 2-Anchor(down) — Present | No solid ground, no clear strategy for scope | Overwhelm at discovering scale of problem |
| 1-Creation(down) — Future | Forced start won't hold; more chaos than before | Work abandoned partway, worse mess next day |
| 6-Star(up) — Liberation | Moment of harsh clarity | Realization of how badly the space had been neglected |
| 3-Earth(down) — Distortion | Physical heaviness, rigid patterns | Literal physical difficulty (fiberglass, mold, drywall) |

This example is included as a calibration anchor because the question is mundane, the predictions are specific, and the feedback is concrete and independently verifiable.

## Dataset

The master spreadsheet tracking all readings (approaching N=120 as of March 2026) will be added to [`data/`](data/) once the formal statistical analysis milestone is reached.

Key tracked variables per reading include: date, question, platform (card picker), dice results, card results, all spin directions, derived hexagrams, interpretation notes, and any available real-world feedback.

## Example Readings

Additional documented readings are stored in [`examples/`](examples/), including:

- Blind/reveal calibration readings across multiple LLM platforms
- Readings with precognitive pattern-matches confirmed over time
- Personal readings demonstrating the framework's therapeutic utility
- Cross-platform replication studies (same spread, independent interpretations)

```
   readings/
  └── data/
      └── reading-results-analysis-_clean.xlsx
  └── examples/
	  ├── 03-04-2026_Artemis2-chart.png
	  ├── 03-04-2026_Artemis2-reading.md
	  ├── 03-04-2026_Artemis2-reading.pdf
	  ├── 10-03-2026_OAI-demo.png
	  ├── 10-03-2026_OAI-demo_kofi.md
	  ├── 10-03-2026_OAI-demo_kofi.pdf
	  ├── 22-11-2024_AI-agency.md
	  ├── 22-11-2024_AI-agency.pdf
	  ├── 22-11-2024_AI-agency-chart.png
      ├── DELPHI-Testreading_comparisons.md
	  ├── DELPHI-Testreading_comparisons.pdf	  
	  ├── US_no_metric_system_why.md
	  ├── US_no_metric_system_why.pdf
	  ├── US_no_metric_system_why.png	  
      └── README.md
