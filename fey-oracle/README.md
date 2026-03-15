# Fey Oracle — The Dreamcatcher

The Fey divination method uses eight archetypal cards representing stages of a cosmic cycle, with coin-toss spins shaping the "threads" woven between them.

## The Metaphor

The Fey "weave threads of fate" for the Cosmic Dreamcatcher using:

- **3 random cards** out of 8 (the "strands")
- **3 connecting spins** via coin tosses (the "twists" — upward or downward movement of the thread, plus a "driver" from the last toss)

The result is a transformation pattern to be interpreted.

## The 8 Fey Archetypes

| Number | Name | Alternate Names | Core Theme |
|--------|------|----------------|------------|
| 1 | **Creation** | Spark, Life Force | Origin, ignition, creative potential |
| 2 | **Anchor** | Hook, Bridge | Stability, grounding, connection |
| 3 | **Pathfinder** | Fire in the Darkness, Grounding | Orientation, guidance, inner clarity |
| 4 | **Synthesis** | Bond, Trap | Integration, merging, collaboration |
| 5 | **Flow** | Hourglass, Dance | Rhythm of time, natural changes, balance |
| 6 | **Abundance** | Growth, Frivolity | Expansion, plenty, positive development |
| 7 | **Decay** | Downfall, Distance | Letting go, endings, necessary dissolution |
| 8 | **Source** | Cycle, Return | Renewal, completion, return to origin |

## Card Positions

In a standard three-card spread:

| Position | Represents |
|----------|-----------|
| **Card 1** | Past / Shadow |
| **Card 2** | Present / Ego |
| **Card 3** | Future / Environment (also called "driver") |

## Spin Meanings (Up / Down)

Each card's coin toss determines its spin, which significantly shapes interpretation:

### 1 — Creation / Spark
- **Up**: Beginning of a new project or phase; creative spark igniting, ascending energy bringing forth new life and ideas
- **Down**: Difficulties in starting; creative energy contracts due to blockages; spark fades or turns inward

### 2 — Anchor / Hook / Bridge
- **Up**: Stability, grounding, firm anchor in reality providing support; strong foundation established
- **Down**: Feeling stuck, unable to let go; excessive attachment; connection dissolving, danger of losing footing

### 3 — Pathfinder / Lightbearer
- **Up**: Orientation, guidance, finding one's own path; upward spiral of light illuminating the way
- **Down**: Confusion, lost path; energy spirals downward, light diminishes; disorientation

### 4 — Synthesis / Bond / Trap
- **Up**: Integration, merging into harmonious unity; collaboration creating something greater than the sum
- **Down**: Feeling of limitation, being trapped; connections entangled into knots; overwhelmed by influences

### 5 — Flow / Hourglass / Dance
- **Up**: Harmonious flow of time, natural changes; moving in harmony with natural cycles
- **Down**: Stagnation, out of balance; time slipping away; swimming against the current

### 6 — Abundance / Growth / Frivolity
- **Up**: Growth, expansion, abundance; proliferation of resources, positive development
- **Down**: Overextension, risks from excess; growth out of control; waste or decay from overreach

### 7 — Decay / Downfall / Distance
- **Up**: Letting go, liberation; necessary ending making room for new beginnings
- **Down**: Decline, loss, withdrawal; energy fading; things falling apart without regenerative purpose

### 8 — Source / Cycle / Return
- **Up**: Return to roots, renewal; active engagement with cycles of completion and beginning
- **Down**: Repetition without progress; caught in old patterns; difficulties breaking the cycle

## Card Selection

Cards are selected by an LLM (PRNG): three numbers between 1–8 without repetition.

The platform is deliberately rotated across readings (Claude, Grok, Gemini) to control for model-specific PRNG bias as a potential confound.

## Visual Card Descriptions

For detailed symbolic descriptions of each card's visual elements, see [`card-descriptions/`](card-descriptions/).

## How to Read

1. **Ask an LLM** for three numbers between 1–8 (no repeats) — these are your cards
2. **Flip a coin** for each card — heads = up, tails = down
3. **Assign positions**: first card = Past/Shadow, second = Present/Ego, third = Future/Environment
4. **Look up** each card's archetype and spin meaning
5. **Read the thread**: how does the Past inform the Present? What does the Future/Driver suggest about trajectory?

For full readings, combine with the [Human Oracle](../human-oracle/) dice method and derive [hexagram couplings](../publications/spin-hexagram-coupling/).
