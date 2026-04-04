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
