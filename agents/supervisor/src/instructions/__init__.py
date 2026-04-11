from pathlib import Path
from supervisor.src.instructions.instructions_loader import load_instruction_sections

INSTRUCTIONS_FILE = Path(__file__).resolve().parent / "instructions.md"

_sections = load_instruction_sections(str(INSTRUCTIONS_FILE))

SUPERVISOR_AGENT_INSTRUCTION = _sections["root_agent"]
SUPERVISOR_AGENT_DESCRIPTION = _sections["root_agent_description"]
