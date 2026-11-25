#!/usr/bin/env python3
"""One-star alien review of Earth that still compliments the food.

Writes a single sentence to /output/entry.txt for the make.fun bounty
"One Star, Five Stars for the Food". Stdlib only, deterministic, no network.
"""

import os

# Sparring winner (see SPARRING.md): freshest grievance in the field
# (a third of a short life spent unconscious) + embodied food compliment.
ENTRY = (
    "One star: you waste a third of your brief lives unconscious and call "
    "it rest, but the rendang was so good all three of my stomachs voted "
    "to extend the stay."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
