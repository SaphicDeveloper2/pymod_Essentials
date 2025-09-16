"""
The command-line compiler for packaging .pymod files.
"""
import json
import os
import zipfile
import shutil
import sys
import argparse

def package_mod(project_path):
    """
    Packages the pymod source and assets into a .pymod file.
    """
    print(f"Starting compilation for project: {project_path}")

    # 1. Read pymod.json
    config_path = os.path.join(project_path, 'pymod.json')
    if not os.path.exists(config_path):
        print(f"Error: 'pymod.json' not found in '{project_path}'")
        sys.exit(1)

    with open(config_path, 'r') as f:
        config = json.load(f)

    mod_id = config.get('id')
    entry_script = config.get('entry_script')

    if not mod_id or not entry_script:
        print("Error: 'id' and 'entry_script' are required in pymod.json")
        sys.exit(1)

    print(f"Compiling mod: {config.get('name')} (ID: {mod_id})")

    # 2. Define paths
    build_dir = os.path.join(project_path, 'build')
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    output_filename = f"{mod_id}-{config.get('version', '1.0.0')}.pymod"
    output_path = os.path.join(build_dir, output_filename)

    source_path = os.path.join(project_path, 'src')
    assets_path = os.path.join(project_path, 'assets')

    # 3. Create mod_info.json in memory
    mod_info = {
        "id": mod_id,
        "entry_script": entry_script.replace('\\', '/')
    }
    mod_info_str = json.dumps(mod_info, indent=4)

    # 4. Create the .pymod (ZIP) file
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.writestr('mod_info.json', mod_info_str)
        print("Added 'mod_info.json' to archive.")

        # Add source files relative to the project root
        if os.path.exists(source_path):
            for root, _, files in os.walk(source_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, project_path)
                    zipf.write(file_path, arcname)
            print(f"Packaged source files from: {source_path}")

        # Add asset files relative to the project root
        if os.path.exists(assets_path):
            for root, _, files in os.walk(assets_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, project_path)
                    zipf.write(file_path, arcname)
            print(f"Packaged asset files from: {assets_path}")

    print(f"\nSuccessfully created pymod: {output_path}")

def main():
    """
    Main entry point for the command-line interface.
    """
    parser = argparse.ArgumentParser(description="Compiler for PyLib mods.")
    parser.add_argument(
        'project_dir',
        nargs='?',
        default='.',
        help='The root directory of the pymod project (defaults to current directory).'
    )
    args = parser.parse_args()

    package_mod(os.path.abspath(args.project_dir))

if __name__ == '__main__':
    main()
