
# PyLib Essentials

*A compiler and utility library for creating Pymods for Minecraft Forge (and later Fabric).*

PyLib Essentials makes **Python modding for Minecraft** simple and universal. The goal is to keep Python code portable so that **Pymods work across multiple mod loaders** with minimal changes.

This package provides a **development toolkit** for modders using the [PyLib Java mod]().

---

## Features

* **Mappings** – Python objects that map to Minecraft’s internal string IDs for creative tabs, item rarities, vanilla items/effects, and more.
  → Includes full IDE autocompletion.
* **Compiler** – Command-line tool `pymod-compiler` that packages your Python source code and assets into a `.pymod` file, ready to be loaded by PyLib.
* **Cross-Loader Support** – Future compatibility with Fabric alongside Forge.

---

## Installation (Recommended)

Download the latest **`.whl` file** from the [Releases](https://github.com/SaphicDeveloper/pymod_Essentials/releases) page, then install with:

```bash
pip install path/to/pylib_essentials-x.y.z-py3-none-any.whl
```

*(Replace `x.y.z` with the actual version number.)*

---

## Building From Source (For Contributors)

If you want to modify or contribute to PyLib Essentials:

1. Clone the repository:

   ```bash
   git clone https://github.com/SaphicDeveloper/pylib.git
   cd pylib/pylib_essentials
   ```

2. Install in editable/development mode:

   ```bash
   pip install -e .
   ```

3. To build your own `.whl` and source distribution:

   ```bash
   python setup.py sdist bdist_wheel
   ```

4. Your files will be created in the `dist/` directory.
   You can test install them locally with:

   ```bash
   pip install dist/pylib_essentials-x.y.z-py3-none-any.whl
   ```

---

## Usage

### 1. Project Structure

```
my_awesome_mod/
├── pymod.json             # Mod metadata (see below)
├── src/                   # Your Python source code
│   └── main.py            # The main entry point
└── assets/                # Your mod's textures, models, etc.
```

### 2. `pymod.json`

```json
{
  "id": "my_awesome_mod",
  "name": "My Awesome Mod",
  "version": "1.0.0",
  "author": "Your Name",
  "entry_script": "src/main.py"
}
```

### 3. Writing Your Mod

```python
# src/main.py
from pylib_essentials import creative_tabs, item_properties, item_rarities

print("Hello from My Awesome Mod!")

# `pylib` is a global object provided by the Java mod at runtime
pylib.registries.items.register(
    pylib.get_mod_id(),
    "ruby",
    {
        item_properties.CREATIVE_TAB: creative_tabs.MATERIALS,
        item_properties.RARITY: item_rarities.RARE,
        item_properties.TEXTURE: "assets/my_awesome_mod/textures/items/ruby.png"
    }
)
```

### 4. Compiling

```bash
pymod-compiler
```

This creates a `.pymod` file inside a new `build/` directory.
Drop it into the `Pymods/` folder in your Minecraft instance to load it.

---

## Roadmap

* [x] Forge support
* [ ] Fabric support
* [ ] Advanced compiler options
* [ ] Example pymod templates

---

## License

PyLib Essentials is licensed under the **MIT License**.

