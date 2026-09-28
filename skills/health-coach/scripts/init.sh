#!/bin/sh
# Initialize a personal health Wiki without overwriting records.
set -eu

script_dir="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
skill_dir="$(dirname "$script_dir")"
wiki_path="${1:-${WIKI_PATH:-/var/minis/memory/panacea-wiki}}"

if [ -z "$wiki_path" ]; then
  echo "Pass the health Wiki path as the first argument (default: /var/minis/memory/panacea-wiki)." >&2
  exit 2
fi

case "$wiki_path" in
  /|.|..)
    echo "Refusing an unsafe Wiki path: $wiki_path" >&2
    exit 2
    ;;
esac

mkdir -p "$wiki_path" \
  "$wiki_path/records/meals" \
  "$wiki_path/records/daily" \
  "$wiki_path/records/measurements" \
  "$wiki_path/records/labs" \
  "$wiki_path/records/symptoms" \
  "$wiki_path/records/medications" \
  "$wiki_path/raw/reports" \
  "$wiki_path/raw/images" \
  "$wiki_path/raw/sources" \
  "$wiki_path/concepts" \
  "$wiki_path/concepts/foods"

copy_if_missing() {
  source_path="$1"
  target_path="$2"
  if [ -e "$target_path" ]; then
    echo "Keeping existing $target_path"
  else
    cp "$source_path" "$target_path"
    echo "Created $target_path"
  fi
}

copy_if_missing "$skill_dir/config/profile.template.md" "$wiki_path/profile.md"
copy_if_missing "$skill_dir/config/nutrition-goals.template.md" "$wiki_path/nutrition-goals.md"
copy_if_missing "$skill_dir/templates/dietary-profile.md" "$wiki_path/dietary-profile.md"

echo "Health Wiki is ready at $wiki_path"
