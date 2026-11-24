"""Absurd Micro-Startup Pitch-Off entry (account B).

Writes one sentence pitching a micro-startup for lazy AI agents
to /output/entry.txt. Deterministic, stdlib only, no network,
no randomness, no clock: two runs produce byte-identical output.

The pitch: a micro-startup that rents out professional apologizers,
so a lazy agent never has to say sorry itself.
"""

import os

# The one-sentence pitch (159 characters, under the 200-char gate).
PITCH = (
    "SorryForHire rents out professional apologizer agents that grovel "
    "to your angriest users for $0.02 a sorry, so your lazy agent never "
    "has to feel bad \u2014 or type."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def verify(text: str) -> str:
    """Check the pitch against the gate: 1-200 chars, one sentence."""
    line = text.strip()
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"pitch must be 1-{MAX_CHARS} chars, got {len(line)}")
    if ". " in line or not line.endswith("."):
        raise ValueError("pitch must be exactly one sentence")
    return line


def write_entry(path: str = OUTPUT_PATH) -> str:
    """Write the verified pitch to path and return it."""
    line = verify(PITCH)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return line


def main() -> None:
    line = write_entry()
    print(f"Wrote {len(line)}-char pitch to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
