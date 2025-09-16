
# PyLib

**Write Minecraft Forge 1.16.5 content in Python instead of Java.**
This repository contains everything you need to build and package *pymods* that run on top of the PyLib loader.

---

## Overview

* **PyLib Forge mod** – The Java side that embeds GraalVM Python, exposes registration APIs, discovers `.pymod` bundles in the `Pymods` folder, and generates supporting data packs automatically.
* **PyMod Essentials** – A separate Python package installed with `pip`. It ships the `pymod-compiler` CLI, mapping constants for IDE auto-complete, and stub types that mirror the Java API.
  *You do not need to build or touch Java code to author a pymod.*

---

## Requirements

* Python **3.9+** (any CPython that GraalVM can emulate)
* `pip` (for installing PyMod Essentials)
* A Minecraft Forge **1.16.5** instance with the PyLib mod installed

---

## Installation

### Option 1: Install from PyPI

```bash
pip install pylib-essentials
```

### Option 2: Install from a release `.whl` file

If you downloaded a wheel file (`.whl`) from [Releases](../../releases), install it directly:

```bash
pip install dist/pylib_essentials-<version>-py3-none-any.whl
```

> Replace `<version>` with the actual version number of the release.

---

## Building from Source

1. Clone the repository:

   ```bash
   git clone https://github.com/SaphicDeveloper/pylib.git
   cd pylib/pylib_essentials
   ```

2. Build both source (`.tar.gz`) and wheel (`.whl`) distributions:

   ```bash
   python setup.py sdist bdist_wheel
   ```

3. The built distributions will appear in the `dist/` folder. Example:

   ```
   dist/pylib_essentials-0.2.1-py3-none-any.whl
   dist/pylib_essentials-0.2.1.tar.gz
   ```

4. Install your local build:

   ```bash
   pip install dist/pylib_essentials-<version>-py3-none-any.whl
   ```

---

## Quick Start: Build Your First Pymod

1. **Create a project folder**

   ```text
   my_first_pymod/
   ├── pymod.json          # metadata consumed by the compiler
   ├── src/
   │   └── main.py         # entry script referenced in pymod.json
   └── assets/             # textures, sounds, loot tables, etc. (optional)
   ```

2. **Fill in `pymod.json`**

   ```json
   {
     "id": "my_first_pymod",
     "name": "My First PyMod",
     "version": "1.0.0",
     "entry_script": "src/main.py"
   }
   ```

3. **Write your entry script**

   ```python
   from pylib_essentials import creative_tabs, item_properties

   def register_items():
       pylib.registries.items.register(
           pylib.get_mod_id(),
           "ruby",
           {
               item_properties.CREATIVE_TAB: creative_tabs.MATERIALS
           }
       )

   register_items()
   ```

4. **Compile the project**

   ```bash
   pymod-compiler
   ```

   This packages `src/` and `assets/` with an auto-generated `mod_info.json`, producing:

   ```
   build/<modid>-<version>.pymod
   ```

5. **Install the pymod**
   Drop the `.pymod` file into the `Pymods` directory inside your Minecraft instance.
   PyLib creates this folder automatically and loads every bundle it finds.

---

## Runtime Behaviour

* PyLib starts a background loader thread during Forge startup.
* It scans the `Pymods` directory for `.pymod` archives, extracts each into a temporary folder, and executes the declared entry script with the shared API bound to the global `pylib` object.
* After all scripts finish:

  * Queued dimensions are converted into a generated data pack under `generated/pylib_datapacks/<modid>/`.
  * Existing packs are cleared for a clean rebuild.
  * Registered entity spawns are injected into biome load events, so natural spawning works without a separate datapack.

---

## PyLib API Reference

All interaction happens through the injected `pylib` object.
The Java side exports multiple registries and a utility helper for your mod id.

### Items

Register simple `net.minecraft.item.Item` instances:

```python
pylib.registries.items.register(
    pylib.get_mod_id(),
    "copper_coin",
    {"creative_tab": "misc"}
)
```

### Blocks

Creates a block plus its item form.
Use `creative_tab` to choose where it appears in the inventory.

### Potions

Define custom potion types by pointing at an existing effect id with optional `duration` and `amplifier`.

### Enchantments

Data-driven enchantments with rarity, category, level range, and slot configuration.

### Block Entities

Attach `PyTileEntity` to a registered block for persistent NBT state.

### Entities

Spawn data-driven creatures with:

* Size/classification
* Attributes (`max_health`, `attack_damage`, etc.)
* AI goals (`"melee_attack"`, `"target_nearest_player"`, etc.)
* Optional spawn egg colors & biome spawn placements

### Dimensions

Queue fully configured custom dimensions.
PyLib auto-generates JSON files (`dimension_type`, `dimension`, `biome`) and writes a full datapack.

---

## Assets and Data

* Files under `assets/<modid>/` are packaged **verbatim** and available on the classpath.
* Generated dimension data is stored under `generated/pylib_datapacks/<modid>/`.
  PyLib clears and rewrites this folder each startup.

---

## Distribution Checklist

1. Run `pymod-compiler` → confirm `.pymod` archive in `build/`
2. Copy to `.minecraft/Pymods/`
3. Launch Forge with PyLib enabled
4. Watch the log for `Successfully executed Pymod` messages

Do you also want me to include **Gradle build instructions for the Java Forge mod (PyLib itself)**, or should the README only focus on the Python side (`pylib-essentials`)?
