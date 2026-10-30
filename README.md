# Stray Shores — macOS Survival Game 🏝️

**Stray Shores is a Mac game for Apple Silicon (arm64), with the game builder targeting macOS 26+.**

## Versions

| Component | Version | Packaging |
| --- | --- | --- |
| Game baseline | **v0.1.0** | Standalone source and Mac builder ZIP prepared |
| Game islands, markets & fantasy | **v0.1.1** | Separate source and Mac builder ZIP prepared |
| Graphical Mac launcher | **v0.1.4** | Mac app wrapper, GUI source and one-time standalone-app builder prepared |

The game and launcher have **independent versions**. Upgrading the launcher does not rename or replace a game version. Older games can remain installed.

## Features

Survival, four islands, markets, villagers, settlement organizers, food preservation, soil water and N/P/K nutrients, fruit trees, the rare Money Tree, five chest rarity classes, furniture, woodworking, pottery, glass and metal crafting. Game v0.1.1 adds regional markets and fantasy encounters.

## Installing the Mac launcher

The redesigned launcher v0.1.4 has improved contrast, clearer Play/Download buttons and a friendly missing-catalog state instead of a raw HTTP 404.

**The provided Launcher.app is a Python/Tk wrapper, not a self-contained signed binary.** To build a standalone Mac app:

1. Install Python 3 with Tk support from python.org.
2. Extract the launcher ZIP and run Build_and_Install_Launcher.command **once**.
3. The builder installs PyInstaller, creates the standalone launcher and puts it in **~/Applications/Stray Shores Launcher.app**.
4. In Finder choose **Go > Home > Applications**. Note: ~/Applications is not the system-wide /Applications folder. You can drag the built app into /Applications yourself.
5. Open the installed application normally; you no longer need to rerun a command for every launch.

### Apple security warnings

Locally built Stray Shores apps are **not Apple Developer ID signed or notarized**. macOS Gatekeeper may ask for approval. If you trust the app you compiled, use Finder > Open or System Settings > Privacy & Security > Open Anyway, when offered. Do not disable Gatekeeper globally.

## Game releases and launcher catalog

Separate source/builder ZIPs have been prepared for games **v0.1.0** and **v0.1.1**. These are **not compiled Mac applications**. A downloadable game version will only appear in the launcher once a compiled .app.zip archive and SHA-256 checksum are published in [GitHub Releases](https://github.com/CaptainCode48/Stray-Shores/releases).

The launcher supports checksum-verified game downloads, but the repository catalog has no published game assets yet. Missing catalog now results in a normal empty state.

Release tags: game-v0.1.0, game-v0.1.1, launcher-v0.1.4. Older game versions are kept for rollback.

**Publishing status:** README, release workflow and catalog generator are in this public repository. Game and launcher source archives still need uploading, and the native Mac build has not been tested.
