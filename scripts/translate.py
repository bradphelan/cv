#!/usr/bin/env python3
"""
Translate README.md → README.de.md using the Anthropic API.
Instructions are read from CLAUDE.md.
Requires: ANTHROPIC_API_KEY env var, pip install anthropic
"""

import os
import sys
import anthropic

def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    with open("CLAUDE.md", encoding="utf-8") as f:
        instructions = f.read()

    with open("README.md", encoding="utf-8") as f:
        source = f.read()

    client = anthropic.Anthropic(api_key=api_key)

    print("Calling Anthropic API for translation...", file=sys.stderr)

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=4096,
        system=instructions,
        messages=[
            {
                "role": "user",
                "content": f"Translate the following CV to German according to your instructions:\n\n{source}"
            }
        ]
    )

    translation = message.content[0].text

    with open("README.de.md", "w", encoding="utf-8") as f:
        f.write(translation)

    print("Written README.de.md", file=sys.stderr)

if __name__ == "__main__":
    main()
