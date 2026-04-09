#!/usr/bin/env python3
"""Validate SKILL.md frontmatter for all skills in .claude/skills/."""

import glob
import sys
import yaml

REQUIRED_FIELDS = ["name", "description", "version", "author", "tags"]
SKILLS_GLOB = ".claude/skills/*/SKILL.md"
COOKIE_CUTTER_DIR = "cookie-cutter"


def parse_frontmatter(filepath):
    """Extract YAML frontmatter from a markdown file."""
    with open(filepath) as f:
        content = f.read()

    if not content.startswith("---"):
        return None, "Missing YAML frontmatter delimiter"

    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, "Malformed YAML frontmatter (missing closing ---)"

    try:
        data = yaml.safe_load(parts[1])
    except yaml.YAMLError as e:
        return None, f"Invalid YAML: {e}"

    return data, None


def validate_skill(filepath):
    """Validate a single SKILL.md file. Returns list of error strings."""
    # Skip cookie-cutter template
    if COOKIE_CUTTER_DIR in filepath:
        print(f"  SKIP {filepath} (cookie-cutter template)")
        return []

    errors = []
    data, parse_error = parse_frontmatter(filepath)

    if parse_error:
        return [f"{filepath}: {parse_error}"]

    if not isinstance(data, dict):
        return [f"{filepath}: Frontmatter is not a YAML mapping"]

    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"{filepath}: Missing required field '{field}'")
        elif not data[field]:
            errors.append(f"{filepath}: Field '{field}' is empty")

    if "tags" in data and not isinstance(data["tags"], list):
        errors.append(f"{filepath}: 'tags' must be a list")

    return errors


def main():
    files = sorted(glob.glob(SKILLS_GLOB))

    if not files:
        print("No SKILL.md files found.")
        return 0

    print(f"Validating {len(files)} skill(s)...\n")
    all_errors = []

    for filepath in files:
        errors = validate_skill(filepath)
        if errors:
            all_errors.extend(errors)
        elif COOKIE_CUTTER_DIR not in filepath:
            print(f"  OK   {filepath}")

    if all_errors:
        print(f"\n{len(all_errors)} error(s) found:\n")
        for err in all_errors:
            print(f"  ERROR {err}")
        return 1

    print("\nAll skills valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
