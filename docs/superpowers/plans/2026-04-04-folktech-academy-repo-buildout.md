# FolkTech Academy Repo Buildout — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build out the FolkTech Academy private GitHub repo with FTAI metadata, CI automation, issue/PR templates, project board, and scaffolding scripts.

**Architecture:** Monorepo with course content organized into track directories. Each course has a README (preview + FTAI metadata) and a `content/` subdirectory for materials. CI validates markdown and FTAI. Scripts automate new course creation.

**Tech Stack:** FTAI (metadata format), GitHub Actions (CI), Python (validation script), Bash (scaffolding script), markdownlint-cli2 (linting)

---

### Task 1: Create directory structure and move existing content

**Files:**
- Create: `templates/course/README.md`
- Create: `templates/course/content/.gitkeep`
- Create: `content/.gitkeep` in every course directory (20 total)
- Move: `track-1-ai-foundations-developer/101-ai-for-developers/AI_for_Developers_Field_Guide.docx` → `track-1-ai-foundations-developer/101-ai-for-developers/content/`
- Move: `track-1-ai-foundations-developer/102-inside-the-neural-network/Inside_the_Neural_Network.docx` → `track-1-ai-foundations-developer/102-inside-the-neural-network/content/`

- [ ] **Step 1: Create content/ directories for all 20 courses**

```bash
# Track 0
mkdir -p track-0-ai-for-everyone/001-what-ai-actually-is/content
mkdir -p track-0-ai-for-everyone/002-ai-vocabulary/content
mkdir -p track-0-ai-for-everyone/003-using-ai-tools-effectively/content
mkdir -p track-0-ai-for-everyone/004-local-ai-for-non-developers/content

# Track 1
mkdir -p track-1-ai-foundations-developer/101-ai-for-developers/content
mkdir -p track-1-ai-foundations-developer/102-inside-the-neural-network/content
mkdir -p track-1-ai-foundations-developer/103-hands-on-local-ai-setup/content

# Track 2
mkdir -p track-2-machine-learning-fundamentals/201-linear-regression/content
mkdir -p track-2-machine-learning-fundamentals/202-classification-logistic-regression/content
mkdir -p track-2-machine-learning-fundamentals/203-neural-networks-from-scratch/content
mkdir -p track-2-machine-learning-fundamentals/204-deep-learning-essentials/content

# Track 3
mkdir -p track-3-applied-ai-development/301-prompt-engineering/content
mkdir -p track-3-applied-ai-development/302-rag/content
mkdir -p track-3-applied-ai-development/303-fine-tuning/content
mkdir -p track-3-applied-ai-development/304-agentic-ai-tool-use/content

# Track 4
mkdir -p track-4-specialized-topics/401-backpropagation-deep-dive/content
mkdir -p track-4-specialized-topics/402-attention-transformers-deep-dive/content
mkdir -p track-4-specialized-topics/403-tokenization-embeddings-deep-dive/content
mkdir -p track-4-specialized-topics/404-ai-safety-healthcare/content
mkdir -p track-4-specialized-topics/405-edge-deployment-optimization/content
```

- [ ] **Step 2: Add .gitkeep to empty content directories**

```bash
find . -path '*/content' -type d -empty -exec touch {}/.gitkeep \;
```

- [ ] **Step 3: Move existing .docx files into content/**

```bash
mv track-1-ai-foundations-developer/101-ai-for-developers/AI_for_Developers_Field_Guide.docx \
   track-1-ai-foundations-developer/101-ai-for-developers/content/

mv track-1-ai-foundations-developer/102-inside-the-neural-network/Inside_the_Neural_Network.docx \
   track-1-ai-foundations-developer/102-inside-the-neural-network/content/
```

- [ ] **Step 4: Create course template**

Create `templates/course/README.md`:

```ftai
@ftai v2.0 lang:en

@document
  title: "COURSE_TITLE"
  author: "FolkTech AI"
  created: COURSE_DATE
  schema: "ftai-academy-course"

@config
  id: "COURSE_ID"
  track: TRACK_NUMBER
  status: "not-started"
  duration: "COURSE_DURATION"
  prerequisites: []
  tags: []
  preview: false
@end
```

```markdown
# COURSE_TITLE

[Course description]

## What You'll Learn
- [Outcome 1]
- [Outcome 2]
- [Outcome 3]

## Prerequisites
None

## Course Content
[Summary of sections and topics]

## Who This Is For
[Target learner description]
```

Create `templates/course/content/.gitkeep` (empty file).

- [ ] **Step 5: Commit**

```bash
git add templates/ track-*/*/content/
git commit -m "Add content directories and course template"
```

---

### Task 2: Update all course READMEs with FTAI frontmatter

**Files:**
- Modify: All 20 course README.md files

Each course README gets FTAI metadata prepended and the body reformatted to match the standard template. The existing content in each README is preserved and reorganized into the standard sections.

- [ ] **Step 1: Update Track 0 course READMEs (4 files)**

**001-what-ai-actually-is/README.md:**
```ftai
@ftai v2.0 lang:en

@document
  title: "What AI Actually Is"
  author: "FolkTech AI"
  created: 2026-04-04
  schema: "ftai-academy-course"

@config
  id: "001"
  track: 0
  status: "not-started"
  duration: "1-2 hours"
  prerequisites: []
  tags: ["ai-basics", "non-technical"]
  preview: true
@end
```

Followed by existing README body reformatted into standard sections (What You'll Learn, Prerequisites, Course Content, Who This Is For).

Apply the same pattern for 002, 003, 004 using their existing metadata:
- 002: id "002", duration "1 hour", prerequisites ["001"], tags ["vocabulary", "non-technical"]
- 003: id "003", duration "2 hours", prerequisites ["001"], tags ["ai-tools", "prompting", "non-technical"]
- 004: id "004", duration "2-3 hours", prerequisites ["002"], tags ["local-ai", "ollama", "non-technical"]

- [ ] **Step 2: Update Track 1 course READMEs (3 files)**

- 101: id "101", status "draft-complete", duration "2-3 hours", prerequisites [], tags ["ai-fundamentals", "developer"]
- 102: id "102", status "draft-complete", duration "3-4 hours", prerequisites ["101"], tags ["neural-networks", "developer"]
- 103: id "103", duration "2-3 hours", prerequisites ["101"], tags ["local-ai", "llama-cpp", "ollama", "developer"]

- [ ] **Step 3: Update Track 2 course READMEs (4 files)**

- 201: id "201", duration "3-4 hours", prerequisites ["102"], tags ["regression", "gradient-descent", "python"]
- 202: id "202", duration "3-4 hours", prerequisites ["201"], tags ["classification", "logistic-regression", "python"]
- 203: id "203", duration "4-5 hours", prerequisites ["202"], tags ["neural-networks", "from-scratch", "python"]
- 204: id "204", duration "4-5 hours", prerequisites ["203"], tags ["deep-learning", "cnn", "rnn", "transformers"]

- [ ] **Step 4: Update Track 3 course READMEs (4 files)**

- 301: id "301", duration "3-4 hours", prerequisites ["101"], tags ["prompt-engineering", "system-design"]
- 302: id "302", duration "4-5 hours", prerequisites ["301"], tags ["rag", "embeddings", "vector-databases"]
- 303: id "303", duration "5-6 hours", prerequisites ["203", "301"], tags ["fine-tuning", "lora", "qlora"]
- 304: id "304", duration "4-5 hours", prerequisites ["301"], tags ["agents", "tool-use", "mcp"]

- [ ] **Step 5: Update Track 4 course READMEs (5 files)**

- 401: id "401", duration "2 hours", prerequisites ["203"], tags ["backpropagation", "chain-rule", "deep-dive"]
- 402: id "402", duration "3-4 hours", prerequisites ["203"], tags ["attention", "transformers", "deep-dive"]
- 403: id "403", duration "2-3 hours", prerequisites ["102"], tags ["tokenization", "embeddings", "bpe", "deep-dive"]
- 404: id "404", duration "3-4 hours", prerequisites ["301"], tags ["ai-safety", "healthcare", "deep-dive"]
- 405: id "405", duration "3-4 hours", prerequisites ["103"], tags ["edge-deployment", "quantization", "optimization", "deep-dive"]

- [ ] **Step 6: Commit**

```bash
git add track-*/*/README.md
git commit -m "Add FTAI frontmatter to all course READMEs"
```

---

### Task 3: Update track-level READMEs with FTAI metadata

**Files:**
- Modify: 5 track-level README.md files

- [ ] **Step 1: Add FTAI headers to each track README**

Each track README gets a `@document` block with track-level metadata:

```ftai
@ftai v2.0 lang:en

@document
  title: "Track 0: AI for Everyone"
  author: "FolkTech AI"
  created: 2026-04-04
  schema: "ftai-academy-track"

@config
  track: 0
  audience: "non-developers"
  courses: ["001", "002", "003", "004"]
@end
```

Apply same pattern for tracks 1-4, preserving existing README body content.

- [ ] **Step 2: Commit**

```bash
git add track-*/README.md
git commit -m "Add FTAI metadata to track READMEs"
```

---

### Task 4: Polish root README

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Add FTAI header and update status column**

Add FTAI document header:
```ftai
@ftai v2.0 lang:en

@document
  title: "FolkTech Academy"
  author: "FolkTech AI"
  created: 2026-04-04
  schema: "ftai-academy-root"

@config
  tracks: [0, 1, 2, 3, 4]
  total_courses: 20
  total_hours: "55-65"
@end
```

Update the status column values to match the standardized status values (e.g., "Not Started" → "not-started", "**Draft Complete**" → "draft-complete").

Keep all existing content (tracks table, learning paths, structure description, license).

- [ ] **Step 2: Commit**

```bash
git add README.md
git commit -m "Polish root README with FTAI header"
```

---

### Task 5: Create GitHub Actions workflows

**Files:**
- Create: `.github/workflows/lint.yml`
- Create: `.github/workflows/validate-courses.yml`
- Create: `.markdownlint.json`

- [ ] **Step 1: Create markdownlint config**

Create `.markdownlint.json`:
```json
{
  "default": true,
  "MD013": { "line_length": 300 },
  "MD033": false,
  "MD041": false,
  "MD024": false
}
```

Rules:
- MD013: Relaxed line length (course content can be long)
- MD033: Allow inline HTML (tables, badges)
- MD041: Don't require first line to be h1 (FTAI header comes first)
- MD024: Allow duplicate headings (common in course READMEs)

- [ ] **Step 2: Create lint workflow**

Create `.github/workflows/lint.yml`:
```yaml
name: Lint Markdown

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: DavidAnson/markdownlint-cli2-action@v19
        with:
          globs: '**/*.md'
```

- [ ] **Step 3: Create course validation workflow**

Create `.github/workflows/validate-courses.yml`:
```yaml
name: Validate Courses

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install FTAI
        run: pip install ftai

      - name: Lint FTAI blocks
        run: |
          find . -path './track-*/*/README.md' | while read f; do
            echo "Linting $f"
            ftai lint "$f" --lenient || exit 1
          done

      - name: Validate course structure
        run: python scripts/validate-frontmatter.py
```

- [ ] **Step 4: Commit**

```bash
git add .markdownlint.json .github/workflows/
git commit -m "Add GitHub Actions for markdown linting and course validation"
```

---

### Task 6: Create validation script

**Files:**
- Create: `scripts/validate-frontmatter.py`

- [ ] **Step 1: Write validation script**

Create `scripts/validate-frontmatter.py`:
```python
#!/usr/bin/env python3
"""Validate FTAI frontmatter in all course READMEs."""

import glob
import re
import sys


REQUIRED_DOCUMENT_FIELDS = ["title", "author", "created", "schema"]
REQUIRED_CONFIG_FIELDS = ["id", "track", "status", "duration", "prerequisites", "tags", "preview"]
VALID_STATUSES = ["not-started", "drafting", "draft-complete", "review", "complete"]


def extract_block(content: str, block_name: str) -> str | None:
    pattern = rf"@{block_name}\b(.*?)(?=@end|@\w+)"
    match = re.search(pattern, content, re.DOTALL)
    return match.group(1).strip() if match else None


def extract_fields(block_text: str) -> dict[str, str]:
    fields = {}
    for line in block_text.splitlines():
        line = line.strip()
        if ":" in line:
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip().strip('"')
    return fields


def validate_course(readme_path: str) -> list[str]:
    errors = []

    with open(readme_path) as f:
        content = f.read()

    if "@ftai" not in content:
        errors.append(f"{readme_path}: Missing @ftai header")
        return errors

    doc_block = extract_block(content, "document")
    if not doc_block:
        errors.append(f"{readme_path}: Missing @document block")
    else:
        doc_fields = extract_fields(doc_block)
        for field in REQUIRED_DOCUMENT_FIELDS:
            if field not in doc_fields:
                errors.append(f"{readme_path}: @document missing '{field}'")
        if doc_fields.get("schema") != "ftai-academy-course":
            errors.append(f"{readme_path}: @document schema must be 'ftai-academy-course'")

    config_block = extract_block(content, "config")
    if not config_block:
        errors.append(f"{readme_path}: Missing @config block")
    else:
        config_fields = extract_fields(config_block)
        for field in REQUIRED_CONFIG_FIELDS:
            if field not in config_fields:
                errors.append(f"{readme_path}: @config missing '{field}'")
        status = config_fields.get("status")
        if status and status not in VALID_STATUSES:
            errors.append(f"{readme_path}: Invalid status '{status}'. Must be one of {VALID_STATUSES}")

    return errors


def validate_structure(course_dir: str) -> list[str]:
    errors = []
    import os
    content_dir = os.path.join(course_dir, "content")
    if not os.path.isdir(content_dir):
        errors.append(f"{course_dir}: Missing content/ directory")
    return errors


def main():
    readmes = sorted(glob.glob("track-*/*/README.md"))

    if not readmes:
        print("ERROR: No course READMEs found")
        sys.exit(1)

    all_errors = []
    for readme in readmes:
        all_errors.extend(validate_course(readme))
        course_dir = str(readme).rsplit("/", 1)[0]
        all_errors.extend(validate_structure(course_dir))

    if all_errors:
        print(f"VALIDATION FAILED — {len(all_errors)} error(s):\n")
        for error in all_errors:
            print(f"  ✗ {error}")
        sys.exit(1)

    print(f"All {len(readmes)} courses validated successfully.")
    sys.exit(0)


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Make executable and test locally**

```bash
chmod +x scripts/validate-frontmatter.py
python scripts/validate-frontmatter.py
```

Expected: PASS (after Task 2 has been completed)

- [ ] **Step 3: Commit**

```bash
git add scripts/validate-frontmatter.py
git commit -m "Add FTAI frontmatter validation script"
```

---

### Task 7: Create new-course scaffolding script

**Files:**
- Create: `scripts/new-course.sh`

- [ ] **Step 1: Write scaffolding script**

Create `scripts/new-course.sh`:
```bash
#!/usr/bin/env bash
set -euo pipefail

if [ $# -lt 3 ]; then
  echo "Usage: $0 <course_id> \"<title>\" <track_number>"
  echo "Example: $0 205 \"Ensemble Methods\" 2"
  exit 1
fi

COURSE_ID="$1"
TITLE="$2"
TRACK="$3"
DATE=$(date +%Y-%m-%d)

SLUG=$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | tr -cd 'a-z0-9-')

TRACK_DIRS=(
  "track-0-ai-for-everyone"
  "track-1-ai-foundations-developer"
  "track-2-machine-learning-fundamentals"
  "track-3-applied-ai-development"
  "track-4-specialized-topics"
)

if [ "$TRACK" -lt 0 ] || [ "$TRACK" -gt 4 ]; then
  echo "Error: Track must be 0-4"
  exit 1
fi

TRACK_DIR="${TRACK_DIRS[$TRACK]}"
COURSE_DIR="$TRACK_DIR/$COURSE_ID-$SLUG"

if [ -d "$COURSE_DIR" ]; then
  echo "Error: $COURSE_DIR already exists"
  exit 1
fi

mkdir -p "$COURSE_DIR/content"

cat > "$COURSE_DIR/README.md" << TEMPLATE
@ftai v2.0 lang:en

@document
  title: "$TITLE"
  author: "FolkTech AI"
  created: $DATE
  schema: "ftai-academy-course"

@config
  id: "$COURSE_ID"
  track: $TRACK
  status: "not-started"
  duration: ""
  prerequisites: []
  tags: []
  preview: false
@end

# $TITLE

[Course description]

## What You'll Learn
- [Outcome 1]
- [Outcome 2]
- [Outcome 3]

## Prerequisites
None

## Course Content
[Summary of sections and topics]

## Who This Is For
[Target learner description]
TEMPLATE

touch "$COURSE_DIR/content/.gitkeep"

echo "Created: $COURSE_DIR/"
echo "  ├── README.md (FTAI template)"
echo "  └── content/.gitkeep"
```

- [ ] **Step 2: Make executable and test**

```bash
chmod +x scripts/new-course.sh
./scripts/new-course.sh 999 "Test Course" 0
ls -la track-0-ai-for-everyone/999-test-course/
cat track-0-ai-for-everyone/999-test-course/README.md
rm -rf track-0-ai-for-everyone/999-test-course
```

Expected: Creates directory with README and content/.gitkeep, then clean up.

- [ ] **Step 3: Commit**

```bash
git add scripts/new-course.sh
git commit -m "Add new-course scaffolding script"
```

---

### Task 8: Create GitHub issue and PR templates

**Files:**
- Create: `.github/ISSUE_TEMPLATE/course-review.md`
- Create: `.github/ISSUE_TEMPLATE/new-course.md`
- Create: `.github/ISSUE_TEMPLATE/bug-report.md`
- Create: `.github/PULL_REQUEST_TEMPLATE.md`

- [ ] **Step 1: Create course review issue template**

Create `.github/ISSUE_TEMPLATE/course-review.md`:
```markdown
---
name: Course Review
about: Request a review of course content
labels: review, content
---

## Course
- **Course ID:**
- **Track:**
- **Title:**

## What to Review
- [ ] Accuracy of content
- [ ] Clarity of explanations
- [ ] Code examples work correctly
- [ ] Prerequisites are appropriate
- [ ] Duration estimate is realistic

## Specific Areas of Concern
[Describe any specific sections or topics that need attention]
```

- [ ] **Step 2: Create new course proposal template**

Create `.github/ISSUE_TEMPLATE/new-course.md`:
```markdown
---
name: New Course Proposal
about: Propose a new course for the academy
labels: proposal, new-course
---

## Proposed Course
- **Title:**
- **Track:** (0-4)
- **Estimated Duration:**

## Rationale
[Why should this course exist? What gap does it fill?]

## Prerequisites
[Which existing courses should come before this one?]

## Outline
[High-level section breakdown]

## Target Learner
[Who is this for?]
```

- [ ] **Step 3: Create bug report template**

Create `.github/ISSUE_TEMPLATE/bug-report.md`:
```markdown
---
name: Bug Report
about: Report an error in course content
labels: bug, content-fix
---

## Location
- **Course ID:**
- **File:**
- **Section:**

## What's Wrong
[Describe the error — wrong information, broken code, formatting issue, etc.]

## Expected
[What should it say or do instead?]
```

- [ ] **Step 4: Create PR template**

Create `.github/PULL_REQUEST_TEMPLATE.md`:
```markdown
**FolkTech AI | Engineering** — Pull Request

---

## What changed
[2-3 sentences explaining what this does and why]

## Files
**New:**
- [list new files]

**Changed:**
- [list changed files]

## Review Checklist
- [ ] FTAI frontmatter is valid
- [ ] Course README follows standard template
- [ ] Content is in the correct `content/` directory
- [ ] No sensitive or draft content exposed unintentionally

## Notes
[Gotchas, context, anything worth calling out]
```

- [ ] **Step 5: Commit**

```bash
git add .github/ISSUE_TEMPLATE/ .github/PULL_REQUEST_TEMPLATE.md
git commit -m "Add issue and PR templates"
```

---

### Task 9: Create CONTRIBUTING.md

**Files:**
- Create: `CONTRIBUTING.md`

- [ ] **Step 1: Write contributing guide**

Create `CONTRIBUTING.md`:
```markdown
# Contributing to FolkTech Academy

## Course Structure

Every course lives in a track directory and follows this structure:

```
track-N-name/
  XXX-course-slug/
    README.md      # Course preview with FTAI metadata
    content/       # Actual course materials
```

## Creating a New Course

Use the scaffolding script:

```bash
./scripts/new-course.sh <course_id> "<title>" <track_number>
```

This creates the directory, README template with FTAI frontmatter, and content directory.

## Course README Format

Every course README must start with valid FTAI frontmatter:

- `@document` block: title, author, created date, schema
- `@config` block: id, track, status, duration, prerequisites, tags, preview

See `templates/course/README.md` for the full template.

## Status Values

| Status | Meaning |
|--------|---------|
| `not-started` | In curriculum plan, no content yet |
| `drafting` | Content being written |
| `draft-complete` | First draft done, needs review |
| `review` | Under active review |
| `complete` | Published and finalized |

## Validation

Before pushing, run the validation script:

```bash
python scripts/validate-frontmatter.py
```

CI will also run this on every push and PR.

## Pull Requests

- One course per PR when possible
- Use the PR template
- Ensure FTAI frontmatter passes validation
```

- [ ] **Step 2: Commit**

```bash
git add CONTRIBUTING.md
git commit -m "Add contributing guide"
```

---

### Task 10: Update .gitignore and push to GitHub

**Files:**
- Modify: `.gitignore`

- [ ] **Step 1: Update .gitignore**

Add to existing `.gitignore`:
```
# OS
.DS_Store
Thumbs.db

# Editors
.vscode/
.idea/
*.swp
*.swo
*~

# Python
__pycache__/
*.pyc
*.pyo
.venv/
venv/

# Node (if exercises use it)
node_modules/

# Environment
.env
.env.local

# Build artifacts
*.log
```

- [ ] **Step 2: Create private GitHub repo and push**

```bash
git add -A
git commit -m "Prepare repo for GitHub"
gh repo create FolkTechAI/folktech-academy --private --source=. --push
```

- [ ] **Step 3: Verify repo exists**

```bash
gh repo view FolkTechAI/folktech-academy --json name,visibility
```

Expected: `{ "name": "folktech-academy", "visibility": "PRIVATE" }`

---

### Task 11: Create GitHub Projects board

- [ ] **Step 1: Create project board**

```bash
gh api graphql -f query='
  mutation {
    createProjectV2(input: {
      ownerId: "<org_id>"
      title: "FolkTech Academy"
    }) {
      projectV2 { id number }
    }
  }'
```

- [ ] **Step 2: Add status field with columns**

Add custom single-select field "Status" with options: Not Started, Drafting, Review, Complete.

- [ ] **Step 3: Create cards for all 20 courses**

Create one card per course with title format: `[XXX] Course Title` and track label.

- [ ] **Step 4: Set initial statuses**

- Courses 101, 102: set to "Drafting" (draft-complete)
- All others: set to "Not Started"

---

### Task 12: Create repo labels

- [ ] **Step 1: Create labels**

```bash
gh label create "track-0" --color "0E8A16" --description "AI for Everyone"
gh label create "track-1" --color "1D76DB" --description "AI Foundations (Developer)"
gh label create "track-2" --color "D93F0B" --description "Machine Learning Fundamentals"
gh label create "track-3" --color "5319E7" --description "Applied AI Development"
gh label create "track-4" --color "FBCA04" --description "Specialized Topics"
gh label create "review" --color "C5DEF5" --description "Content review needed"
gh label create "proposal" --color "D4C5F9" --description "New course proposal"
gh label create "content-fix" --color "E99695" --description "Error in course content"
gh label create "new-course" --color "0075CA" --description "New course being added"
```

- [ ] **Step 2: Verify labels**

```bash
gh label list
```
