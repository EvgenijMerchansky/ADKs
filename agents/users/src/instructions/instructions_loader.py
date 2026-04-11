import re
from pathlib import Path


def load_instruction_sections(file_path: str) -> dict[str, str]:
    """
    Loads Markdown sections from a single instructions.md file.

    Expected format:
    # section_name
    content...

    # another_section
    content...
    """
    text = Path(file_path).read_text(encoding="utf-8")

    pattern = re.compile(
        r"^#\s+(?P<name>[^\n]+)\n(?P<body>.*?)(?=^#\s+|\Z)",
        re.MULTILINE | re.DOTALL,
    )

    sections: dict[str, str] = {}

    for match in pattern.finditer(text):
        name = match.group("name").strip()
        body = match.group("body").strip()
        sections[name] = body

    return sections
