#!/usr/bin/env bash

rm dev/sphinx/source/changelog.md
rm dev/sphinx/source/code_of_conduct.md
rm dev/sphinx/source/contributing.md
rm dev/sphinx/source/license.rst
rm dev/sphinx/source/readme.md
rm dev/sphinx/source/security.md

cp CHANGELOG.md dev/sphinx/source/changelog.md
cp CODE_OF_CONDUCT.md dev/sphinx/source/code_of_conduct.md
cp CONTRIBUTING.md dev/sphinx/source/contributing.md
cp LICENSE dev/sphinx/source/license.rst
cp README.md dev/sphinx/source/readme.md
cp SECURITY.md dev/sphinx/source/security.md

# Keep the Why: context/ as its own section of the docs, "Why this project is
# built this way" — the topic files and their index, rendered by myst like the
# README. README, AGENTS and CLAUDE are for the folder on GitHub, not pages.
# Build-only copy, ignored by git (dev/sphinx/source/context/ in .gitignore).
rm -rf dev/sphinx/source/context
mkdir -p dev/sphinx/source/context
cp context/*.md dev/sphinx/source/context/
rm -f dev/sphinx/source/context/README.md dev/sphinx/source/context/AGENTS.md dev/sphinx/source/context/CLAUDE.md
# The index's 0-9/A-Z skeleton headings are for the file, not for the docs'
# table of contents: list the page by its title only.
printf -- '---\ntocdepth: 1\n---\n' | cat - dev/sphinx/source/context/index.md > dev/sphinx/source/context/index.md.tmp
mv dev/sphinx/source/context/index.md.tmp dev/sphinx/source/context/index.md

mkdir -vp dev/sphinx/build

cd dev/sphinx
rm build/html
ln -s ../../../docs build/html
make html -d
#echo "Creating CNAME file for GitHub."
#echo "unicorn-fy.docs.lucit.tech" >> build/html/CNAME

