# Call of Duty (2003) — Android ARM64 development notes (unofficial)

A source-only record of an **experimental personal Android ARM64 porting workflow** for the original *Call of Duty* (PC, 2003; compatible version 1.5). The local test project uses an English-language Android launcher and **RetroTouch** touchscreen controls.

**This repository contains documentation, public validation scripts, and GitHub Actions checks only. It does not include a ready-to-run game, the Call of Duty engine, a playable APK, generated recompilation modules, or original commercial game assets.** The GitHub workflow deliberately does **not** produce an APK.

## Development workflow

See [docs/WORKFLOW.md](docs/WORKFLOW.md) for the Windows CMD preparation, compatibility checks, local asset import, English launcher adaptation, and private testing process.

## Public GitHub Actions checks

The workflow at `.github/workflows/source-only-checks.yml` runs on pushes, pull requests, and manual dispatch. It checks that documented private file types are absent from the repository, compiles the small public Python verification tool, and confirms the documentation is present. It **cannot** reconstruct a playable native Android build from this public repository alone.

## Credits and notices

- Experimental CallofRecomp Android recompilation by [Dr3amyBerry / contributors](https://github.com/Dr3amyBerry/callofrecomp).
- RetroTouch controls from [Andiweli/RetroTouch](https://github.com/Andiweli/RetroTouch).
- Call of Duty and its game data are owned by their respective rights holders. This is an unofficial community/development project and is not affiliated with Activision.

No original Call of Duty PC data or third-party source is redistributed here. Before publishing modifications to third-party software, verify the applicable licenses and attribution requirements.

**Status:** Experimental and locally tested. Completing the full single-player campaign on all Android devices has not been established.
