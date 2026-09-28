#!/bin/sh
# Panacea for Minis — skills installer.
# Run inside the Minis terminal (iSH / Alpine Linux).
set -eu

REPO="youzaiooo/panacea-minis"
BRANCH="main"
DEST="/var/minis/skills"
TMP="$(mktemp -d)"
URL="https://github.com/$REPO/archive/refs/heads/$BRANCH.tar.gz"

echo "==> Downloading skills package"
echo "    $URL"
if command -v wget >/dev/null 2>&1; then
  wget -q -O "$TMP/pm.tar.gz" "$URL"
else
  curl -fsSL -o "$TMP/pm.tar.gz" "$URL"
fi

echo "==> Extracting"
tar -xzf "$TMP/pm.tar.gz" -C "$TMP" || {
  echo "Extract failed. If this is an https/certificate issue, run: apk add ca-certificates && retry" >&2
  exit 1
}

echo "==> Installing to $DEST"
mkdir -p "$DEST"
cp -R "$TMP/panacea-minis-$BRANCH/skills/"* "$DEST/"
rm -rf "$TMP"

echo ""
echo "Installed skills in $DEST:"
ls "$DEST"
echo ""
echo "Done. Next step — initialize your health Wiki:"
echo "  sh $DEST/health-coach/scripts/init.sh"
echo ""
echo "Then tell your assistant: 带我填一下健康档案"
