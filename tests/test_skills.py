"""Runnable self-check for the Phase 9b skill loader.

    python -m tests.test_skills
"""

from agentic_ds.skills import load_skills, skill_menu


def test_all_five_skills_load_with_required_fields():
    skills = load_skills()
    names = {s["name"] for s in skills}
    assert names == {"ab_testing", "eda_report", "glm_diagnosis", "trend_check", "survival_comparison"}
    for s in skills:
        assert s["description"], f"{s['name']} has no description"
        assert s["instructions"], f"{s['name']} has no instructions"


def test_skill_menu_lists_every_skill():
    menu = skill_menu()
    for s in load_skills():
        assert s["name"] in menu
        assert s["description"] in menu


if __name__ == "__main__":
    test_all_five_skills_load_with_required_fields()
    test_skill_menu_lists_every_skill()
    print("OK — all skills self-checks passed.")
