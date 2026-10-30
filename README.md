# Stray Shores — Mac Survival Game

## WHAT'S NEW — Game v0.1.8 (Preview Build)
Game v0.1.8 expands the inventory, food and crafting systems.
Ordinary items now stack up to 64; coins stack up to 1,000.
Craft a wallet from cloth, fiber and lashings to carry up to 10,000 coins.
Additional wallet upgrades increase carrying capacity.
Find varied fruits, berries, fish, meat and cooked meals.
The v0.1.8 game update is currently a source-and-Mac-builder package, not a confirmed GitHub release.

## LATEST PUBLISHED GAME — v0.1.7
Game v0.1.7 adds improved characters, buildings, foliage and environmental detail.
Explore with independent multiplayer cameras, enter buildings and see richer lighting.
Launcher version: v0.1.6 (maintained separately).
Important: Game v0.1.0 and v0.1.1 are broken and unsupported. Use v0.1.7.

## About the game

Stray Shores is a top-down island-survival and settlement game for Apple Silicon Macs; the Mac builder targets macOS 26+. Features include exploration, markets, crafting, farming, housing, villagers, fishing, pottery, glassmaking, equipment customization, and the rare Money Tree.

## Released game versions

| Game version | Status |
| --- | --- |
| **v0.1.7** | Latest reported uploaded release |
| v0.1.4 | Previous release |
| v0.1.3 | Previous release |
| v0.1.1 | Broken — do not install |
| v0.1.0 | Broken — do not install |
| v0.1.8 | Preview source/builder only, not confirmed released |

Game versions v0.1.2, v0.1.5 and v0.1.6 are not part of the published release lineup. Version numbers for the launcher are separate.

## Download and installation

See [GitHub Releases](https://github.com/CaptainCode48/Stray-Shores/releases). The launcher discovers the actual published game tags (for example `game-v0.1.7`) and downloads their asset named exactly `Stray.Shores.zip`, which must contain the compiled Mac application. A source/builder ZIP is not an installable game binary.

Install the Mac launcher from its package using `Build_and_Install_Launcher.command` once, then launch from Applications. Locally built binaries are not signed or notarized by Apple; use normal macOS security approval if you trust the app. Never disable Gatekeeper globally.

## Launcher README integration

The launcher v0.1.6 reads this README from the repository's `main` branch when it starts and when you press Refresh. It shows an opening preview in **What's New** and the full text in a scrollable **View Full History** window. When offline, it displays the last cached README.

The opening sections above intentionally use short, standalone lines so the launcher preview remains readable. **The README is informational**: available downloadable game versions are determined by GitHub Releases and their actual `Stray.Shores.zip` assets.

## 🧩 Modding Stray Shores (for players)

Mods add content or change game settings without editing the game application. **Mods are stored outside the .app** so reinstalling or updating the game does not require modifying the application bundle.

### 1. Find your mod folder on macOS

1. Launch the **game version you want to mod** at least once, then quit.
2. In Finder, press **Shift + Command + G** (Go to Folder).
3. Paste the appropriate folder path:

| Game | Global mods folder |
| --- | --- |
| v0.1.0 | `~/Library/Application Support/Stray Shores/versions/0.1.0/mods/` |
| v0.1.1 | `~/Library/Application Support/Stray Shores/versions/0.1.1/mods/` |

Use the folder for the game **version** you are running, *not* the launcher version. The original game data may have been copied from an older shared Stray Shores directory on first launch.

To enable a mod for **only one save**, put it in `mods/slot_1/`, `mods/slot_2/`, etc., where the number matches that save slot. You can also drag compatible `.json` files onto a save slot's **DROP .JSON MODS HERE** area in the game.

**Example:** A mod affecting only save slot 2 of game v0.1.1 goes in:

```text
~/Library/Application Support/Stray Shores/versions/0.1.1/mods/slot_2/
```

### 2. Install a mod

- Prefer a **plain `.json`** data mod from a source you trust.
- Copy the `.json` file into the global or save-specific `mods` folder above; do not copy the entire downloaded ZIP into this folder.
- Restart the game and open **Esc → Mods for this save** to inspect its status.
- An **ACTIVE** mod has loaded. **INVALID**, **INCOMPATIBLE**, **CONFLICT**, **BLOCKED**, and **TRUST REQUIRED** mean it needs attention. Review the status text.
- Back up your save before adding, updating, or removing mods, particularly when experimenting with new items or buildings.

### 3. Create a simple mod (JSON)

Create a UTF-8 text file named `my_fishing_mod.json` containing:

```json
{
  "name": "My Fishing Mod",
  "mod_format": 1,
  "fish": {
    "moonfish": {"weight": 3, "value": 120}
  },
  "jokes": [
    "The fish wants to speak to your manager."
  ],
  "fish_cooldown": 6,
  "fish_bucket_capacity": 15
}
```

Save the file in `mods/`, launch the game, and check **Esc → Mods for this save**. This is the original **format 1** mod system, intended for fishing settings and jokes.

### 4. Create an expansion (mod format 2)

For new items, recipes, buildings, enemies, events and encounters, use `mod_format: 2`. For example, save the following as `moonstone.json`:

```json
{
  "name": "Moonstone Expansion",
  "mod_format": 2,
  "items": [
    {"id": "moonstone", "label": "Moonstone"}
  ],
  "recipes": [
    {
      "id": "make_moonstone",
      "output": "moonstone",
      "quantity": 1,
      "requires": {"stone": 2, "scrap": 1},
      "era": 0
    }
  ]
}
```

Format 2 also accepts `buildings`, `enemies`, `world_events` and `encounters`. Example definitions are included in the game source under `Game/mods/` (`example_expansion.json` and `example_encounter.json`). **Check mod compatibility against your chosen game version**; older mod packs may declare a minimum internal game version. A new mod may not work on v0.1.0 simply because it works on v0.1.1.

**Dependencies:** Format 2 mods with a `requires` list must load after their dependencies. Packs load alphabetically, with global packs before slot-specific packs. Use distinct mod names and keep filenames appropriately ordered.

### 5. Advanced Python plugins — use caution

The game also supports save-specific **Python `.py` plugins** with explicit approval, but they are **not sandboxed** and can run arbitrary code with your user account's permissions.

- Never run untrusted `.py`, `.exe`, `.dylib`, or unknown binary mods.
- Python plugins only load from `mods/slot_N/`, not the global mods folder.
- After reviewing the code, a user must add the plugin filename and its **SHA-256** to `mods/slot_N/trusted_python.json` under the `trusted_sha256` object.
- Changing the plugin changes its hash and requires renewed approval.
- Compiled libraries, executables and ZIP archives are not supported as direct mods.

If you are new to modding, **start with JSON**; it is the safer supported method.

### 6. Troubleshooting mods

| Problem | What to check |
| --- | --- |
| Mod doesn't appear | Correct **game version** and save-slot folder; restart the game |
| INCOMPATIBLE | Declared version bounds or missing dependencies |
| INVALID | JSON syntax, unknown fields or invalid IDs/quantities |
| CONFLICT | Two packs share an ID or declare an incompatibility |
| Python plugin says TRUST REQUIRED | Review source and approve its exact SHA-256 |
| Older version behaves differently | Use that version's separate mod folder and compatible mods |

The launcher doesn't automatically convert mods between game versions. **Keep separate copies** of mods and save backups before upgrading or rolling back.

## Game releases

Downloadable game archives are published on [GitHub Releases](https://github.com/CaptainCode48/Stray-Shores/releases). The game and launcher are independently versioned. The launcher discovers `game-v...` releases and expects the game release asset `Stray.Shores.zip`, which contains the already compiled Mac `.app`. Release availability depends on what has actually been uploaded to GitHub.
