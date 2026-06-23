#!/usr/bin/env bash
set -euo pipefail

REPO_URL="${1:-https://github.com/leandroer/KQL-Templates.git}"

git init
git branch -M main

if ! git remote | grep -q '^origin$'; then
  git remote add origin "$REPO_URL"
else
  git remote set-url origin "$REPO_URL"
fi

git add .
git commit -m "Modernize KQL Templates repository v1.0" || true
git push -u origin main
