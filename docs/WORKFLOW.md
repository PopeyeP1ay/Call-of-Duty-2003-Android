# Call of Duty 1.5 (2003) to Android — personal development workflow

This page records the local process. The public repository contains **no commercial game data, APKs, signing keys, or private recompilation output**.

## 1. Prepare a compatible PC installation

Use a legally obtained Call of Duty 1.5 installation that contains `CoDSP.exe`, `gamex86.dll`, `cgamex86.dll`, `uix86.dll`, and `main/*.pk3`. United Offensive is a separate expansion and is not supported by the referenced CallofRecomp v0.2.4 build.

Windows CMD example (adjust the path to your own licensed installation):

```bat
cd /d "E:\COD2003Android\Game"
powershell -NoProfile -Command "Get-FileHash 'CoDSP.exe','gamex86.dll','cgamex86.dll','uix86.dll' -Algorithm SHA256 | Format-List"
```

Use the version-1.5 fingerprints documented in the [upstream baseline](https://github.com/Dr3amyBerry/callofrecomp/blob/main/analysis/baselines/cod1_sp_pc_1_5.json). Compatibility of all four PC binaries does **not** prove the Android campaign runs fully.

## 2. Obtain the experimental Android host

For private experimentation use the [upstream ARM64 releases](https://github.com/Dr3amyBerry/callofrecomp/releases). Review upstream documentation, the source provenance, and the version requirements. This documentation is **not** a claim that this public repository compiles an engine independently.

## 3. Prepare and import game data privately

Use the [upstream local-browser packager](https://dr3amyberry.github.io/callofrecomp/) to create a `.codpack` from your own compatible installation. The packager operates locally in the browser. For your own phone, import that package through the Android launcher.

Windows CMD transfer example:

```bat
"%LOCALAPPDATA%\Android\Sdk\platform-tools\adb.exe" -d push "E:\COD2003Android\callofrecomp.codpack" "/sdcard/Download/callofrecomp.codpack"
```

The `.codpack` is private copyrighted game data. **Never commit it to GitHub or upload it as an Actions artifact.**

## 4. English interface and touchscreen controls

The upstream v0.2.4 Android source contains hardcoded Spanish launcher and RetroTouch control labels. Local modifications can translate those UI strings to English while retaining the original controller behavior and layout. Game-localization files are separate from launcher text; English `.pk3` files are needed for English in-game content. Any patched APK is for private testing until the appropriate redistribution rights are established.

## 5. Optional local all-in-one APK experiment

A local experiment can embed the owner's `.codpack` in a private APK and extract it into app-specific storage on first launch. This requires a valid Android manifest, a correctly signed and ZIP-aligned APK, enough free device storage, and testing on physical ARM64 Android hardware. A successful build or installation does not alone prove that mission gameplay works. **Do not publish the bundled APK or the `.codpack`.**

## 6. GitHub Actions workflow

The workflow `source-only-checks.yml` performs documentation and asset-exclusion checks only. There is **no public APK build or downloadable game artifact**. Keep your actual game installation, patched binaries, local signing material, private generated modules, and personal builds in a separate working directory outside this Git repository.
