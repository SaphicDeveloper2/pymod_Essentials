import json
import os
from types import SimpleNamespace

# This class will act as a container for our mapping objects
_mappings = SimpleNamespace()

# Find the path to mappings.json relative to this file
_mappings_path = os.path.join(os.path.dirname(__file__), 'mappings.json')

try:
    with open(_mappings_path, 'r') as f:
        _data = json.load(f)

    # Dynamically create a SimpleNamespace for each top-level key in the JSON
    for key, value in _data.items():
        # The SimpleNamespace allows for dot notation access (e.g., creative_tabs.MISC)
        setattr(_mappings, key, SimpleNamespace(**value))

except FileNotFoundError:
    print("FATAL: Could not find mappings.json for pylib_essentials.")
except json.JSONDecodeError:
    print("FATAL: Could not parse mappings.json for pylib_essentials.")

# Expose the mapping objects directly for easy import
creative_tabs = getattr(_mappings, 'creative_tabs', SimpleNamespace())
enchantment_rarities = getattr(_mappings, 'enchantment_rarities', SimpleNamespace())
enchantment_categories = getattr(_mappings, 'enchantment_categories', SimpleNamespace())
vanilla_items = getattr(_mappings, 'vanilla_items', SimpleNamespace())
vanilla_effects = getattr(_mappings, 'vanilla_effects', SimpleNamespace())

