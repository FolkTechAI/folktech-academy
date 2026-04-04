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
