from pathlib import Path
from comments.src.instructions.instructions_loader import load_instruction_sections

INSTRUCTIONS_FILE = Path(__file__).resolve().parent / "instructions.md"

_sections = load_instruction_sections(str(INSTRUCTIONS_FILE))

COMMENTS_AGENT_INSTRUCTION = _sections["root_agent"]

FETCH_COMMENTS_INSTRUCTION = _sections["fetch_comments_agent"]
FORMAT_COMMENTS_INSTRUCTION = _sections["format_comments_agent"]
