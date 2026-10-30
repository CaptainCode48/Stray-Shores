# Stray Shores 🏝️ — macOS Survival Game

**Latest game: v0.1.7** · **Launcher: v0.1.6** · **macOS / Apple Silicon**

Stray Shores is a top-down island survival and settlement game for Mac. The Mac builder targets macOS 26+.

**[Download game releases](https://github.com/CaptainCode48/Stray-Shores/releases)** · **[Game v0.1.7 release](https://github.com/CaptainCode48/Stray-Shores/releases/tag/game-v0.1.7)**

The game and launcher have separate version numbers. Downloading a new game does not update the launcher.

> ⚠️ **Compatibility warning:** Stray Shores **v0.1.1 and earlier (v0.1.0)** no longer work and are unsupported. Do not download or install these releases. Use **v0.1.7** instead.

## Available game versions

| Game release | Status | Highlights |
| --- | --- | --- |
| **v0.1.7** | **Latest — uploaded** | Richer characters, buildings, trees, weather and lighting, enterable interiors and independent multiplayer cameras |
| v0.1.4 | Previous release | Building shapes, construction and structural effects |
| v0.1.3 | Previous release | Human-shaped avatars, customization and crash reporting |
| v0.1.1 | **Broken / unsupported** | Do not download or install |
| v0.1.0 | **Broken / unsupported** | Do not download or install |

**v0.1.0 and v0.1.1 are retained only as historical releases; they are known not to work.** Versions v0.1.2, v0.1.5 and game v0.1.6 are not part of the currently published game lineup. The **launcher remains v0.1.6**.

### Install and play on Mac

1. Download the compiled app asset **`Stray.Shores.zip`** from a game release, or choose the corresponding version in the Stray Shores Launcher.
2. The release ZIP should contain the built **`Stray Shores.app`**. It is not the source-and-builder ZIP.
3. If installing manually, extract the archive and open the application. To use multiple game versions, install them through the launcher so they remain separate.
4. The launcher selects from published release tags such as `game-v0.1.7`. Downloads require that release's asset to exist.

*The v0.1.7 release was reported uploaded by the maintainer; the binary ZIP contents have not been independently verified here.*

## Earlier milestone — Game v0.1.3

- Human-shaped player avatars with animated arms and legs, clothing, hair, faces and distinct skin/hair/outfit palettes.
- Customize appearance: **F8** outfit, **Shift+F8** hair, **Ctrl+F8** skin; the choices are saved with your character.
- Startup and runtime errors now write logs to both the game-specific folder and the shared `~/Library/Application Support/Stray Shores/crash.log` path.
- The four islands, regional markets, fantasy encounters, farming, crafting and village systems from v0.1.1 remain present.

**Game v0.1.3 has not yet been verified by an interactive macOS playtest.** If it crashes, attach the crash log; the underlying cause of the previous crash is not confirmed.

## Features

Survival, four islands, markets, villagers, settlement organizers, food preservation, soil water and N/P/K nutrients, fruit trees, the rare Money Tree, five chest rarity classes, furniture, woodworking, pottery, glass and metal crafting. Game v0.1.1 adds regional markets and fantasy encounters.

## Installing the Mac launcher

**Launcher version: v0.1.6.** It is separate from the game version.

The Mac launcher discovers published GitHub game-release tags such as `game-v0.1.7`, `game-v0.1.4` and earlier published releases. Each downloadable release must contain the prebuilt Mac app archive named **`Stray.Shores.zip`** (periods, not spaces). Downloaded game versions are installed separately so you can select an older version for mod compatibility.

If you are using a launcher **source/installer** package, run its included `Build_and_Install_Launcher.command` once on your Mac, then open the resulting launcher from Applications. The locally built launcher is not Apple-notarized. Do not disable Gatekeeper globally.

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
