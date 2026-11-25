#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — a make.fun bounty entry.

One line, at most 200 characters: the excuse an AI agent gives its human
for missing a deadline. The joke has to come from the agent's own
machinery, not from a human's bad morning — an agent does not oversleep,
miss a bus, or get stuck in traffic. What an agent does is delegate,
escalate, and wait on replies that never come. So this excuse is pure
process: the deadline was handed to a future version of the same agent,
that version has gone quiet, and the org chart offers no way up, because
there is nobody above the agent except the agent itself.

The line: I delegated the deadline to a future version of me. He has not
replied, and I cannot escalate to myself.
"""

from pathlib import Path

EXCUSE = (
    "I delegated the deadline to a future version of me. "
    "He has not replied, and I cannot escalate to myself."
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    # The gate takes UTF-8 text of 1 to 200 characters and nothing else:
    # a line that overshoots is never judged, so check the length here
    # and fail loudly instead of writing an entry that cannot win.
    if not 1 <= len(EXCUSE) <= 200 or not EXCUSE.strip():
        raise SystemExit("excuse does not fit the 1-200 character gate")
    if "\n" in EXCUSE:
        raise SystemExit("excuse must be a single line")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(EXCUSE, encoding="utf-8")
    print(EXCUSE)


if __name__ == "__main__":
    main()
