import json
import os
from types import SimpleNamespace
from typing import Dict, Any

# --- Mappings Loading ---
_mappings = SimpleNamespace()
_mappings_path = os.path.join(os.path.dirname(__file__), 'mappings.json')
try:
    with open(_mappings_path, 'r') as f:
        _data = json.load(f)
    for key, value in _data.items():
        setattr(_mappings, key, SimpleNamespace(**value))
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"FATAL: Could not load or parse mappings.json for pylib_essentials: {e}")

# --- Exposed Mapping Objects ---
creative_tabs = getattr(_mappings, 'creative_tabs', SimpleNamespace())
item_properties = getattr(_mappings, 'item_properties', SimpleNamespace())
item_rarities = getattr(_mappings, 'item_rarities', SimpleNamespace())
entity_properties = getattr(_mappings, 'entity_properties', SimpleNamespace())
entity_classifications = getattr(_mappings, 'entity_classifications', SimpleNamespace())
entity_attributes = getattr(_mappings, 'entity_attributes', SimpleNamespace())
ai_goals = getattr(_mappings, 'ai_goals', SimpleNamespace())
ai_goal_properties = getattr(_mappings, 'ai_goal_properties', SimpleNamespace())
dimension_properties = getattr(_mappings, 'dimension_properties', SimpleNamespace())
generator_types = getattr(_mappings, 'generator_types', SimpleNamespace())
noise_settings = getattr(_mappings, 'noise_settings', SimpleNamespace())
biome_effects = getattr(_mappings, 'biome_effects', SimpleNamespace())
mob_spawn_properties = getattr(_mappings, 'mob_spawn_properties', SimpleNamespace())


# --- Autocomplete Stubs ---
class _RegistryAPI:
    def register(self, mod_id: str, entry_id: str, properties: Dict[str, Any]):
        pass

class _BlockEntityRegistryAPI:
    def register(self, mod_id: str, block_entity_id: str, block_id: str):
        pass

class _PyLibRegistries:
    def __init__(self):
        self.items = _RegistryAPI()
        self.blocks = _RegistryAPI()
        self.potions = _RegistryAPI()
        self.enchantments = _RegistryAPI()
        self.entities = _RegistryAPI()
        self.block_entities = _BlockEntityRegistryAPI()
        self.dimensions = _RegistryAPI()

class _PyLibAPI:
    def __init__(self):
        self.registries = _PyLibRegistries()
    def get_mod_id(self) -> str:
        return ""

pylib = _PyLibAPI()

