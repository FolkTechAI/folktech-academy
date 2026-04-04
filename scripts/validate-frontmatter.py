#!/usr/bin/env python3
"""Validate FTAI frontmatter in all course READMEs."""

import glob
import os
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
