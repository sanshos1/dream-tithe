# Dream Tithe

_A waking ledger for promises made after dark._

You wake with an image you cannot shake. Inside it is a promise: return the borrowed name, publish the forgotten letter, visit the place that kept appearing. By noon the dream has softened. By next week, the promise can be rewritten into anything.

Dream Tithe closes that escape hatch.

The dreamer binds the original witness, recurring motifs, and explicit waking terms into a GenLayer record. Later, proof is not narrated back to the contract. Public proof URLs are opened by independent validators and compared with the terms that were sealed on the first night.

## Three possible mornings

### RELEASED

Every waking term is evidenced. The dream has collected its tithe and the record can rest.

### LINGERING

The proof is real but incomplete. The contract names what remains unpaid instead of collapsing everything into a vague failure.

### FORFEITED

The witness or proof cannot be relied upon. Missing and unreachable evidence never becomes accidental success.

## A record from the night ledger

```json
{
  "dream_id": "DT-041",
  "motifs": ["red stair", "salt key"],
  "waking_terms": ["publish the letter", "return the key"],
  "state": "LINGERING",
  "unpaid_residue": ["return the key"]
}
```

The final two fields above are derived after consensus; they are not supplied by the dreamer.

## The ritual, in contract calls

`bind_dream` creates the immutable night record and authenticates its origin witness. `wake_dream` receives public proof locations, asks validators to read them, and writes the agreed consequence. `get_dream` opens one entry; `get_dreams_page` turns the ledger into an archive.

## What makes the machine honest

The witness and every proof are fetched independently. Validators agree on the terms satisfied, the residue still owed, and the evidence reliability. Only then does deterministic contract logic choose the morning state. A beautiful caller-written story has no authority over those fields.

## Entering the workshop

The illustrated experience lives in `frontend`; the night law is in `contracts/contract.py`; adversarial and ordinary mornings live in `tests`. A release is accepted only after the test suite, GenVM lint, and the frontend production build succeed.

Dream Tithe runs on GenLayer Bradbury. Its browser client receives the living contract address through `NEXT_PUBLIC_CONTRACT_ADDRESS`.

_Bound on Bradbury at_ `0x98Aa3F459B63BC96953fDf2cbCBA88dBB96d6eC9`.

_The chain does not interpret the dream for you. It remembers what you said it would cost._
