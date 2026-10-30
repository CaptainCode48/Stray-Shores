# Stray Shores — macOS Game 🏝️

**Stray Shores is a game for Mac computers running macOS 26 or later on Apple Silicon (arm64).**

| Component | Current version |
|---|---|
| **Game** | **v0.1.1** |
| **Launcher** | **v0.1.2** |

## Game v0.1.1 — Islands, Markets & Fantasy

- Four ocean-separated islands: Starter Island, Amber Wilds, Frostwood Reach and Sunken Keys.
- Amber Bazaar, Frost Exchange and Tide Market, with local commodity trading and port investments.
- The Grove Spirit, Frost Warden and Tide Oracle, offering fantasy interactions and rewards.
- Persistent island-market standings and fantasy quest progress.
- All existing farming, village, crafting, preservation and survival systems, including the five reward chest classes and rare Money Tree.

## Mac installation and source

Download the game source/builder ZIP and run `Build_Standalone_ARM64_on_Mac.command` on an Apple Silicon Mac with macOS 26+; then use `Install_App_in_Applications.command`. The separate launcher uses `Launch_Version_Manager.command`.

**The Mac binary and automatic-update catalog will appear under [Releases](https://github.com/CaptainCode48/Stray-Shores/releases) once the source and release workflow have been published and the macOS build succeeds.** No Mac binary is being claimed as available yet.

Game releases use tags `game-v0.1.1`; launcher releases use tags `launcher-v0.1.2`. Publishing a new game version does not change the launcher's version number. Older game builds remain available through the launcher only if their release assets have been published.

The local v0.1.1 builder includes game source, release workflow, update-catalog generator, and launcher source.
