#!/usr/bin/env python3
"""Export the report abstract as plain text for submission forms.

Adapted from abstract_text in extended-egglog-paper/scripts/produce-paper.py.
Keep paragraph breaks and reject unsupported LaTeX instead of silently
turning macro names into prose. Citations are omitted from this standalone
export; they remain in the PDF.
"""

import argparse
from pathlib import Path
import re


def abstract_text(source: str) -> str:
    text = re.sub(r"(?<!\\)%[^\n]*", "", source)
    text = re.sub(r"\\(?:begin|end)\{abstract\}", "", text)
    text = re.sub(r"~?\\cite(?:t|p)?(?:\[[^\]]*\])*\{[^{}]*\}", "", text)
    formatting = r"\\(?:textit|textbf|emph|texttt)\{([^{}]*)\}"
    while re.search(formatting, text):
        text = re.sub(formatting, r"\1", text)
    text = text.replace("~", " ").replace(r"\%", "%").replace(r"\&", "&")
    text = text.replace("``", '"').replace("''", '"')
    if re.search(r"[\\{}$]", text):
        raise ValueError("unsupported LaTeX; extend scripts/abstract-text.py before exporting")
    paragraphs = [" ".join(p.split()) for p in re.split(r"\n\s*\n", text) if p.strip()]
    return "\n\n".join(paragraphs) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    try:
        text = abstract_text(args.source.read_text(encoding="utf-8"))
    except ValueError as error:
        parser.error(f"{args.source}: {error}")
    args.output.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
