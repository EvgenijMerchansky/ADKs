from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
AGENTS_DIR = PROJECT_ROOT / "agents"


def find_agent_dirs(agents_dir: Path) -> list[Path]:
    if not agents_dir.exists():
        raise FileNotFoundError(f"Agents directory not found: {agents_dir}")

    agent_dirs: list[Path] = []
    for item in agents_dir.iterdir():
        if not item.is_dir():
            continue
        if item.name.startswith("."):
            continue
        if (item / "requirements.txt").exists():
            agent_dirs.append(item)

    return sorted(agent_dirs, key=lambda p: p.name.lower())


def install_requirements(agent_dir: Path) -> None:
    requirements_file = agent_dir / "requirements.txt"

    print(f"\n=== Installing dependencies for: {agent_dir.name} ===")
    subprocess.run(
        [sys.executable, "-m", "pip", "install", "-r", str(requirements_file)],
        cwd=agent_dir,
        check=True,
    )


def build_pythonpath(project_root: Path, agents_dir: Path) -> str:
    existing = os.environ.get("PYTHONPATH", "")
    paths = [str(project_root), str(agents_dir)]

    if existing:
        paths.append(existing)

    return os.pathsep.join(paths)


def main() -> None:
    if not PROJECT_ROOT.exists():
        raise FileNotFoundError(f"Project root not found: {PROJECT_ROOT}")

    agent_dirs = find_agent_dirs(AGENTS_DIR)

    if not agent_dirs:
        raise RuntimeError(f"No agent directories with requirements.txt found in: {AGENTS_DIR}")

    print("Found agent directories:")
    for agent_dir in agent_dirs:
        print(f" - {agent_dir.name}")

    for agent_dir in agent_dirs:
        install_requirements(agent_dir)


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as exc:
        print(f"\nCommand failed with exit code: {exc.returncode}", file=sys.stderr)
        sys.exit(exc.returncode)
    except Exception as exc:
        print(f"\nError: {exc}", file=sys.stderr)
        sys.exit(1)
