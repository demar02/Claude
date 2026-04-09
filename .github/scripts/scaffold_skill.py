#!/usr/bin/env python3
"""Scaffold missing subdirectories for skills in .claude/skills/."""

import glob
import os
import sys

SKILLS_DIR = ".claude/skills"
SUBDIRS = ["scripts", "references", "assets"]
COOKIE_CUTTER_DIR = "cookie-cutter"


def scaffold_skill(skill_dir):
    """Ensure a skill directory has the expected subdirectories. Returns True if changes were made."""
    changed = False

    for subdir in SUBDIRS:
        path = os.path.join(skill_dir, subdir)
        if not os.path.isdir(path):
            os.makedirs(path, exist_ok=True)
            gitkeep = os.path.join(path, ".gitkeep")
            open(gitkeep, "a").close()
            print(f"  CREATED {path}/")
            changed = True

    return changed


def main():
    skill_dirs = sorted(glob.glob(os.path.join(SKILLS_DIR, "*")))
    skill_dirs = [d for d in skill_dirs if os.path.isdir(d)]

    if not skill_dirs:
        print("No skill directories found.")
        return 0

    print(f"Checking {len(skill_dirs)} skill(s) for missing structure...\n")
    any_changes = False

    for skill_dir in skill_dirs:
        name = os.path.basename(skill_dir)

        # Skip cookie-cutter template
        if name == COOKIE_CUTTER_DIR:
            print(f"  SKIP {name} (cookie-cutter template)")
            continue

        # Only scaffold if SKILL.md exists
        if not os.path.isfile(os.path.join(skill_dir, "SKILL.md")):
            print(f"  SKIP {name} (no SKILL.md)")
            continue

        changed = scaffold_skill(skill_dir)
        if changed:
            any_changes = True
        else:
            print(f"  OK   {name}")

    if any_changes:
        print("\nScaffolding complete. New directories were created.")
        return 2  # Signal to workflow that changes exist
    else:
        print("\nAll skills have complete structure.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
