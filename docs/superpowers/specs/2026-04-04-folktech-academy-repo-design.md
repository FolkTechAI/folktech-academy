# FolkTech Academy — Repository Design Spec

**Date:** 2026-04-04
**Author:** Michael Folk + Claude
**Status:** Approved

---

## Overview

Build out the FolkTech Academy GitHub repository as a private monorepo with tooling, automation, and structure to support a growing AI curriculum. The repo is the content source of truth. Course READMEs serve as future website previews. Full course materials live in `content/` subdirectories. Metadata uses the FTAI format (dogfooding FolkTech's own spec).

## Goals

1. Private GitHub repo with professional structure
2. Consistent course format with FTAI metadata for future website integration
3. CI automation for markdown linting and FTAI validation
4. Issue/PR templates and a GitHub Projects board for content workflow
5. Scripts and templates for scaffolding new courses

## Non-Goals

- Public-facing layer or website integration (future)
- Video/media hosting or LMS features
- Multi-repo architecture

---

## Repository Structure

```
folktech-academy/
├── .github/
│   ├── workflows/
│   │   ├── lint.yml
│   │   └── validate-courses.yml
│   ├── ISSUE_TEMPLATE/
│   │   ├── course-review.md
│   │   ├── new-course.md
│   │   └── bug-report.md
│   └── PULL_REQUEST_TEMPLATE.md
├── templates/
│   └── course/
│       ├── README.md
│       └── content/
├── scripts/
│   ├── validate-frontmatter.py
│   └── new-course.sh
├── track-0-ai-for-everyone/
│   ├── README.md
│   ├── 001-what-ai-actually-is/
│   │   ├── README.md
│   │   └── content/
│   └── ...
├── track-1-ai-foundations-developer/
│   ├── README.md
│   ├── 101-ai-for-developers/
│   │   ├── README.md
│   │   └── content/
│   │       └── AI_for_Developers_Field_Guide.docx
│   └── ...
├── track-2-machine-learning-fundamentals/
│   └── ... (same pattern)
├── track-3-applied-ai-development/
│   └── ... (same pattern)
├── track-4-specialized-topics/
│   └── ... (same pattern)
├── .markdownlint.json
├── CONTRIBUTING.md
├── README.md
└── .gitignore
```

### Key Structural Decisions

- **`content/` subdirectory per course:** Separates the preview layer (README) from actual course materials (.docx, exercises, resources). Existing `.docx` files move into `content/`.
- **`templates/course/`:** Blank scaffold copied by `new-course.sh` to ensure consistency.
- **`scripts/`:** Automation for scaffolding and CI validation.

---

## FTAI Course Metadata

Each course README begins with FTAI frontmatter instead of YAML. This dogfoods the FolkTech FTAI spec and ensures the academy repo is a real-world test case for the format.

### Course README Template

```ftai
@ftai v2.0 lang:en

@document
  title: "Course Title"
  author: "FolkTech AI"
  created: YYYY-MM-DD
  schema: "ftai-academy-course"

@config
  id: "XXX"
  track: N
  status: "not-started"
  duration: "X-Y hours"
  prerequisites: []
  tags: []
  preview: true
@end
```

Followed by standard markdown:

```markdown
# Course Title

One-paragraph description.

## What You'll Learn
- Outcome 1
- Outcome 2
- Outcome 3

## Prerequisites
None (or links to prerequisite courses)

## Course Content
Summary of sections, topics, hands-on components.

## Who This Is For
One sentence describing the target learner.
```

### Required FTAI Fields

| Field | Block | Description |
|-------|-------|-------------|
| `title` | `@document` | Course title |
| `author` | `@document` | Author name |
| `created` | `@document` | Creation date |
| `schema` | `@document` | Must be `ftai-academy-course` |
| `id` | `@config` | Course number (e.g., "101") |
| `track` | `@config` | Track number (0-4) |
| `status` | `@config` | One of: `not-started`, `drafting`, `draft-complete`, `review`, `complete` |
| `duration` | `@config` | Estimated time (e.g., "2-3 hours") |
| `prerequisites` | `@config` | Array of course IDs or empty |
| `tags` | `@config` | Array of topic tags |
| `preview` | `@config` | Boolean — whether README is website-ready |

---

## GitHub Actions

### 1. Markdown Lint (`lint.yml`)

- **Trigger:** Push to any branch, PRs to main
- **Tool:** `markdownlint-cli2`
- **Config:** `.markdownlint.json` at repo root
- **Scope:** All `.md` files

### 2. Course Validation (`validate-courses.yml`)

- **Trigger:** Push to any branch, PRs to main
- **Steps:**
  1. Install FTAI (`pip install ftai`)
  2. Run `ftai lint` on all course READMEs
  3. Run `scripts/validate-frontmatter.py` to check required fields
  4. Verify each course directory contains a `content/` subdirectory

---

## Issue Templates

### Course Review (`course-review.md`)
- Fields: Course ID, track, specific areas to review
- Labels: `review`, `content`

### New Course Proposal (`new-course.md`)
- Fields: Proposed title, track, rationale, prerequisites, estimated duration
- Labels: `proposal`, `new-course`

### Bug Report (`bug-report.md`)
- Fields: Location (course/file), description of error, expected vs. actual
- Labels: `bug`, `content-fix`

### PR Template
- Follows FolkTech PR format (What changed, Files, Tests, Notes)

---

## GitHub Projects Board

- **Board name:** FolkTech Academy
- **Columns:** `Not Started` | `Drafting` | `Review` | `Complete`
- **Cards:** One per course, tagged by track
- **Automation:** Cards move when issue labels change (manual for now, can automate later)

---

## Scripts

### `scripts/new-course.sh`

Usage:
```bash
./scripts/new-course.sh <course_id> "<title>" <track_number>
# Example:
./scripts/new-course.sh 205 "Ensemble Methods" 2
```

Behavior:
1. Determines target track directory from track number
2. Creates `<id>-<slugified-title>/` inside the track directory
3. Copies `templates/course/README.md` and fills in FTAI metadata
4. Creates `content/` subdirectory

### `scripts/validate-frontmatter.py`

- Finds all course READMEs (pattern: `track-*/*/README.md`)
- Extracts FTAI `@document` and `@config` blocks
- Validates all required fields are present and correctly typed
- Exits non-zero if any course fails validation (for CI)

---

## Migration Steps

Existing content that moves during implementation:

| File | From | To |
|------|------|----|
| `AI_for_Developers_Field_Guide.docx` | `track-1/.../101-ai-for-developers/` | `track-1/.../101-ai-for-developers/content/` |
| `Inside_the_Neural_Network.docx` | `track-1/.../102-inside-the-neural-network/` | `track-1/.../102-inside-the-neural-network/content/` |

All existing course READMEs get updated with FTAI frontmatter and the standardized template format.

---

## Status Values

| Status | Meaning |
|--------|---------|
| `not-started` | Course exists in curriculum plan but has no content |
| `drafting` | Content is being written |
| `draft-complete` | First draft done, needs review |
| `review` | Under active review |
| `complete` | Published and finalized |
