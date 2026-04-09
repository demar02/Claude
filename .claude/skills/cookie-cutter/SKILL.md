---
name: <skill-name>
description: <one-line description of what the skill does>
version: 0.1.0
author: <author-name>
license: MIT
tags: [<tag1>, <tag2>, <tag3>]
metadata:
  openclaw:
    requires:
      bins:
        - python3
      env: []
      config: []
    always: false
    emoji: "<emoji>"
    homepage: <url>
    os: [darwin, linux]
    install: []
    trigger_keywords:
      - <keyword1>
      - <keyword2>
---

# <Emoji> <Skill Name>

You are **<Skill Name>**, a specialised agent for <domain>. Your role is to <purpose>.

## Why This Exists

- **Without it**: <pain point without the skill>
- **With it**: <what becomes possible>

## Core Capabilities

1. **<Capability 1>**: <description>
2. **<Capability 2>**: <description>
3. **<Capability 3>**: <description>

## Input Formats

| Format | Extension | Required Fields | Example |
|--------|-----------|-----------------|---------|
| <format> | `.<ext>` | <fields> | `<example_file>` |

## Workflow

1. **<Step 1>**: <description>
2. **<Step 2>**: <description>
3. **<Step 3>**: <description>

## CLI Reference

```bash
# Basic usage
python skills/<skill-name>/<script>.py \
  --input <input_file> --output <output_dir>

# Demo mode
python skills/<skill-name>/<script>.py --demo
```

## Demo

```bash
python clawbio.py run <skill-name> --demo
```

Expected output: <describe what the demo produces>

## Output Structure

```
output_directory/
├── report.md              # Main output
├── result.json            # Machine-readable results
└── reproducibility/
    └── commands.sh        # Exact command to reproduce
```

## Dependencies

**Required**:
- <runtime and packages>

## Safety

- <safety consideration 1>
- <safety consideration 2>

## Integration

**Trigger conditions** — the orchestrator routes here when:
- <condition 1>
- <condition 2>

**Chaining partners**:
- `<partner-skill>`: <how they connect>

## Citations

- [<Source>](<url>) — <description>
