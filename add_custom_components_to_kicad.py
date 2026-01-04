#!/usr/bin/env python3
"""
Add custom component libraries (CAV25256, NCV97200, etc.) to KiCad project
"""
import json
import os
import sys
from pathlib import Path

def add_custom_components_to_project(project_file=None):
    """Add custom component libraries to KiCad project"""
    
    # Find project file if not specified
    if project_file is None:
        # Look for .kicad_pro files in current directory
        project_files = list(Path(".").glob("*.kicad_pro"))
        if project_files:
            project_file = project_files[0]
        else:
            # Check in gmsl-deserializer subdirectory
            gmsl_proj = Path("gmsl-deserializer") / "gmsl-deserializer.kicad_pro"
            if gmsl_proj.exists():
                project_file = gmsl_proj
            else:
                print("[ERROR] No KiCad project file found!")
                print("Please specify project file or run from project directory.")
                return False
    
    project_file = Path(project_file)
    
    if not project_file.exists():
        print(f"[ERROR] Project file not found: {project_file}")
        return False
    
    print("=" * 60)
    print("Adding Custom Component Libraries to KiCad Project")
    print("=" * 60)
    print(f"\nProject file: {project_file}")
    
    # Library paths (relative to project)
    lib_dir = Path("lib")
    symbol_lib = lib_dir / "custom_components.kicad_sym"
    footprint_lib = lib_dir / "custom_components.pretty"
    
    # Check if libraries exist
    if not symbol_lib.exists():
        print(f"\n[WARNING] Symbol library not found: {symbol_lib}")
        print("[INFO] Run download_custom_libraries.py first!")
        return False
    
    if not footprint_lib.exists():
        print(f"\n[WARNING] Footprint library not found: {footprint_lib}")
        print("[INFO] Run download_custom_libraries.py first!")
        return False
    
    # Verify components
    with open(symbol_lib, 'r', encoding='utf-8') as f:
        content = f.read()
        components = []
        if "CAV25256" in content:
            components.append("CAV25256")
        if "NCV97200" in content:
            components.append("NCV97200")
        
        print(f"\n[INFO] Components found: {', '.join(components) if components else 'None'}")
    
    # Read project file
    try:
        with open(project_file, 'r', encoding='utf-8') as f:
            project = json.load(f)
    except Exception as e:
        print(f"[ERROR] Failed to read project file: {e}")
        return False
    
    # Ensure libraries section exists
    if "libraries" not in project:
        project["libraries"] = {}
    
    # Add symbol library
    if "pinned_symbol_libs" not in project["libraries"]:
        project["libraries"]["pinned_symbol_libs"] = []
    
    # Use ${KIPRJMOD} variable for relative paths
    symbol_entry = "${KIPRJMOD}/lib/custom_components.kicad_sym;custom_components"
    
    # Remove existing entry if present
    project["libraries"]["pinned_symbol_libs"] = [
        lib for lib in project["libraries"]["pinned_symbol_libs"]
        if not (isinstance(lib, str) and "custom_components" in lib)
    ]
    
    # Add symbol library
    project["libraries"]["pinned_symbol_libs"].insert(0, symbol_entry)
    print(f"\n[OK] Added symbol library: {symbol_entry}")
    
    # Add footprint library
    if "pinned_footprint_libs" not in project["libraries"]:
        project["libraries"]["pinned_footprint_libs"] = []
    
    footprint_entry = "${KIPRJMOD}/lib/custom_components.pretty;custom_components"
    
    # Remove existing entry if present
    project["libraries"]["pinned_footprint_libs"] = [
        lib for lib in project["libraries"]["pinned_footprint_libs"]
        if not (isinstance(lib, str) and "custom_components" in lib)
    ]
    
    # Add footprint library
    project["libraries"]["pinned_footprint_libs"].insert(0, footprint_entry)
    print(f"[OK] Added footprint library: {footprint_entry}")
    
    # Write project file
    try:
        with open(project_file, 'w', encoding='utf-8') as f:
            json.dump(project, f, indent=2, ensure_ascii=False)
        print(f"\n[OK] Project file updated: {project_file}")
    except Exception as e:
        print(f"[ERROR] Failed to write project file: {e}")
        return False
    
    print("\n" + "=" * 60)
    print("SUCCESS! Custom component libraries added to project")
    print("=" * 60)
    print("\nAvailable components:")
    for comp in components:
        print(f"  - {comp}")
    print("\nNext steps:")
    print("1. Open KiCad and load the project")
    print("2. Press 'A' in schematic editor to add symbol")
    print("3. Search for component name (e.g., 'CAV25256' or 'NCV97200')")
    print("4. Or use library prefix: 'custom_components:CAV25256'")
    print("5. Place the component on your schematic")
    print("\n[NOTE] Verify footprint dimensions match actual components!")
    print("[NOTE] Add library through Preferences -> Manage Symbol Libraries if not visible")
    
    return True

def add_to_all_projects():
    """Add library to all KiCad projects in directory"""
    
    project_files = list(Path(".").rglob("*.kicad_pro"))
    
    if not project_files:
        print("[INFO] No KiCad projects found in current directory")
        return False
    
    print(f"Found {len(project_files)} project file(s)")
    
    for proj_file in project_files:
        print(f"\nProcessing: {proj_file}")
        add_custom_components_to_project(proj_file)
    
    return True

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Add custom component libraries to KiCad project")
    parser.add_argument("--project", "-p", help="Specific project file (optional)")
    parser.add_argument("--all", "-a", action="store_true", help="Add to all projects in directory")
    
    args = parser.parse_args()
    
    try:
        if args.all:
            success = add_to_all_projects()
        else:
            success = add_custom_components_to_project(args.project)
        
        if success:
            sys.exit(0)
        else:
            sys.exit(1)
    except Exception as e:
        print(f"\n[ERROR] {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

