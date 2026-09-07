"""Structural check for the iridex profile repo.

This repo is a public identity page. It has no application, so "works" means the page is
intact and the things it depends on are actually reachable.

The load-bearing check is the last one: the README embeds images from the brand-asset CDN.
If that host or a path breaks, the profile silently renders with broken images and nobody
finds out from the repo. So every asset URL the README references is fetched.

Standard library only, so it runs anywhere with no install step.
"""

import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

failures: list[str] = []

if not README.exists():
    print("FAIL README.md missing - this repo is the public identity page")
    sys.exit(1)

text = README.read_text(encoding="utf-8")

# --- the page must actually say who this is ------------------------------
if len(text.strip()) < 200:
    failures.append("README is under 200 characters - that is not an identity page")
if not re.search(r"(?m)^#\s+\S", text):
    failures.append("no top-level heading")

# --- every asset URL it depends on must resolve --------------------------
urls = sorted(set(re.findall(r"https://assets\.carpedieminnovationsinc\.com/[^\s\"')>]+", text)))
if not urls:
    print("note: no asset-CDN URLs referenced")
for url in urls:
    try:
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "cdi-verify/1.0"})
        with urllib.request.urlopen(req, timeout=20) as resp:
            if resp.status != 200:
                failures.append(f"{url} -> HTTP {resp.status}")
            else:
                print(f"ok  {url}")
    except urllib.error.HTTPError as e:
        failures.append(f"{url} -> HTTP {e.code}")
    except Exception as e:  # DNS, TLS, timeout
        failures.append(f"{url} -> {type(e).__name__}: {e}")

# --- and the identity claim must not have drifted off the org ------------
if "carpe-diem-innovations-inc" not in text:
    failures.append("README no longer references the parent organisation")

print(f"checked: {len(urls)} asset URL(s)")
for f in failures:
    print(f"  FAIL {f}")
sys.exit(1 if failures else 0)
