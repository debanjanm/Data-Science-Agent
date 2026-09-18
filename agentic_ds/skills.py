"""Phase 9b: Skills — reusable playbooks over Phase 9a's Tools, loaded from
`skills/*.md` (frontmatter + instructions, same shape as this session's own
Skill files). Frontmatter here is two flat fields (name, description) — a
hand-rolled parser is shorter than adding `pyyaml` for that.
"""

from pathlib import Path

SKILLS_DIR = Path(__file__).resolve().parent.parent / "skills"


def _parse_skill_file(path: Path) -> dict:
    _, frontmatter, body = path.read_text().split("---", 2)
    meta = dict(line.split(":", 1) for line in frontmatter.strip().splitlines())
    return {
        "name": meta["name"].strip(),
        "description": meta["description"].strip(),
        "instructions": body.strip(),
    }


def load_skills() -> list[dict]:
    """Every skill in `skills/*.md`, parsed. Empty list if the directory doesn't exist."""
    if not SKILLS_DIR.exists():
        return []
    return [_parse_skill_file(p) for p in sorted(SKILLS_DIR.glob("*.md"))]


def skill_menu(skills: list[dict] | None = None) -> str:
    """A "name: description" menu, one per line, for an agent's system prompt."""
    skills = load_skills() if skills is None else skills
    return "\n".join(f"- {s['name']}: {s['description']}" for s in skills)
