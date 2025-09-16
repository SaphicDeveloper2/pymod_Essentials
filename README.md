PyLib EssentialsA compiler and utility library for creating Pymods for Minecraft Forge and later fabric, the idea is to keep the python code universal so pymods work on any loader.This package provides a development toolkit for modders using the PyLib Java mod. It includes:Mappings: A comprehensive set of Python objects that map to Minecraft's internal string IDs for things like creative tabs, item rarities, and vanilla items/effects. This provides full IDE autocompletion.Compiler: A command-line tool, pymod-compiler, that packages your Python source code and assets into a .pymod file, ready to be loaded by PyLib.InstallationYou can install the library using pip:pip install .
(Run this from the directory containing setup.py)Usage1. Project StructureOrganize your pymod project with the following structure:my_awesome_mod/
├── pymod.json             # Mod metadata (see below)
├── src/                   # Your Python source code
│   └── main.py            # The main entry point
└── assets/                # Your mod's textures, models, etc.
2. pymod.jsonThis file is required at the root of your project.{
   "id": "my_awesome_mod",
   "name": "My Awesome Mod",
   "version": "1.0.0",
   "author": "Your Name",
   "entry_script": "src/main.py"
   }
3. Writing Your ModIn your Python scripts, you can import the mappings to get full autocompletion.# src/main.py
   from pylib_essentials import creative_tabs, item_properties, item_rarities

print("Hello from My Awesome Mod!")

# pylib is a global object provided by the Java mod at runtime
pylib.registries.items.register(
pylib.get_mod_id(),
"ruby",
{
item_properties.CREATIVE_TAB: creative_tabs.MATERIALS,
item_properties.RARITY: item_rarities.RARE,
item_properties.TEXTURE: "assets/my_awesome_mod/textures/items/ruby.png"
}
)
4. CompilingNavigate to your project's root directory in your terminal and run the compiler:pymod-compiler
   This will create a .pymod file inside a new build/ directory. Drop this file into the Pymods folder in your Minecraft instance, and you're ready to go!