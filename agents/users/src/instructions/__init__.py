from pathlib import Path
from users.src.instructions.instructions_loader import load_instruction_sections

INSTRUCTIONS_FILE = Path(__file__).resolve().parent / "instructions.md"

_sections = load_instruction_sections(str(INSTRUCTIONS_FILE))

USERS_AGENT_INSTRUCTION = _sections["root_agent"]

FETCH_USERS_INSTRUCTION = _sections["fetch_users_agent"]
FORMAT_USERS_INSTRUCTION = _sections["format_users_agent"]
