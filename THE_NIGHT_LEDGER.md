# The night ledger

_Entry copied before the image thins._

There was a red elevator. There was salt rain. Someone named a station and someone else promised to return a brass token.

DreamTithe begins from a strange but useful premise: memory changes, while a promise should not quietly change with it. A dreamer therefore binds four things together before morning:

1. the image they remember;
2. the motifs that make the memory recognizable;
3. concrete waking terms;
4. one public witness that validators can authenticate independently.

The contract is intentionally literal. It does not diagnose the dream, infer hidden symbolism, or ask validators to invent a moral. When `wake` is called, settlement depends on the frozen terms that were actually fulfilled. All terms paid produces `RELEASED`; some remaining produces `LINGERING`; reopening the debt without payment produces `FORFEITED`.

This makes DreamTithe less like a game oracle and more like a receipt written in impossible ink. GenLayer is used only where interpretation of an external witness is needed. The final arithmetic remains deterministic and inspectable.

The live Bradbury sigil and original binding transaction are written in `night-receipt.json`. Its field names belong to this world because the repository itself is part of the fiction.
