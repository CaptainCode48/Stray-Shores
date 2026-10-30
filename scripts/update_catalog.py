#!/usr/bin/env python3
"""Publish a game-only releases.json manifest for the Stray Shores launcher."""
import json, os, re, subprocess, tempfile
from pathlib import Path

def gh(*args):
    return subprocess.check_output(["gh", *args], text=True).strip()

repo = os.environ["GITHUB_REPOSITORY"]
releases = json.loads(gh("release","list","--limit","100","--json","tagName,isDraft,isPrerelease"))
entries = []
for release in releases:
    tag = release["tagName"]
    if release["isDraft"] or release["isPrerelease"] or not re.fullmatch(r"game-v\d+\.\d+\.\d+",tag):
        continue
    version = tag.removeprefix("game-v")
    details = json.loads(gh("release","view",tag,"--json","assets"))
    assets = {a["name"] for a in details.get("assets",[])}
    asset = f"Stray_Shores_{version}_macOS26_arm64.app.zip"
    if asset not in assets or asset+".sha256" not in assets: continue
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(["gh","release","download",tag,"--pattern",asset+".sha256","--dir",td],check=True)
        sha = (Path(td)/(asset+".sha256")).read_text().split()[0]
    if not re.fullmatch(r"[a-fA-F0-9]{64}",sha):
        raise ValueError("Invalid checksum for "+tag)
    entries.append(dict(version=version,sha256=sha.lower(),url=f"https://github.com/{repo}/releases/download/{tag}/{asset}",notes=f"Stray Shores Game {version} (macOS arm64)"))
entries.sort(key=lambda e:tuple(map(int,e["version"].split("."))),reverse=True)
if not entries:
    raise RuntimeError("No published game builds yet; catalog left unchanged")
with tempfile.TemporaryDirectory() as td:
    file=Path(td)/"releases.json"
    file.write_text(json.dumps({"releases":entries},indent=2)+"\n")
    if subprocess.run(["gh","release","view","launcher-catalog"],capture_output=True).returncode:
        gh("release","create","launcher-catalog","--title","Stray Shores update catalog","--notes","Machine-readable game build manifest.","--latest=false")
    subprocess.run(["gh","release","upload","launcher-catalog",str(file),"--clobber"],check=True)
