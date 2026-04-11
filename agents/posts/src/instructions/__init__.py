from pathlib import Path
from posts.src.instructions.instructions_loader import load_instruction_sections

INSTRUCTIONS_FILE = Path(__file__).resolve().parent / "instructions.md"

_sections = load_instruction_sections(str(INSTRUCTIONS_FILE))

POSTS_AGENT_INSTRUCTION = _sections["root_agent"]

FETCH_POSTS_INSTRUCTION = _sections["fetch_posts_agent"]
FORMAT_POSTS_INSTRUCTION = _sections["format_posts_agent"]
