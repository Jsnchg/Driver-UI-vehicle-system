#!/usr/bin/env python3
"""
Fix CAV25256 visibility in KiCad - Multiple methods
"""
import json
import os
import sys
from pathlib import Path

def fix_project_libraries(project_file):
    """Method 1: Fix project file library entries"""
    
    project_file = Path(project_file)
    if not project_file.exists():
        print(f"[ERROR] Project file not found: {project_file}")
        return False
    
    print(f"\n[Method 1] Fixing project file: {project_file}")
    
    with open(project_file, 'r', encoding='utf-8') as f:
        project = json.load(f)
    
    # Ensure libraries section
    if "libraries" not in project:
        project["libraries"] = {}
    if "pinned_symbol_libs" not in project["libraries"]:
        project["libraries"]["pinned_symbol_libs"] = []
    if "pinned_footprint_libs" not in project["libraries"]:
        project["libraries"]["pinned_footprint_libs"] = []
    
    # Get absolute paths
    project_dir = project_file.parent
    symbol_lib = project_dir.parent / "lib" / "custom_components.kicad_sym"
    footprint_lib = project_dir.parent / "lib" / "custom_components.pretty"
    
    # Convert to Windows path format
    symbol_lib_abs = str(symbol_lib.resolve()).replace('/', '\\')
    footprint_lib_abs = str(footprint_lib.resolve()).replace('/', '\\')
    
    # Remove old entries
    project["libraries"]["pinned_symbol_libs"] = [
        lib for lib in project["libraries"]["pinned_symbol_libs"]
        if not (isinstance(lib, str) and "custom_components" in lib.lower())
    ]
    project["libraries"]["pinned_footprint_libs"] = [
        lib for lib in project["libraries"]["pinned_footprint_libs"]
        if not (isinstance(lib, str) and "custom_components" in lib.lower())
    ]
    
    # Add with absolute path
    symbol_entry = f"{symbol_lib_abs};custom_components"
    footprint_entry = f"{footprint_lib_abs};custom_components"
    
    project["libraries"]["pinned_symbol_libs"].insert(0, symbol_entry)
    project["libraries"]["pinned_footprint_libs"].insert(0, footprint_entry)
    
    with open(project_file, 'w', encoding='utf-8') as f:
        json.dump(project, f, indent=2, ensure_ascii=False)
    
    print(f"[OK] Added absolute paths to project file")
    print(f"     Symbol: {symbol_entry}")
    print(f"     Footprint: {footprint_entry}")
    
    return True

def create_sym_lib_table(project_file):
    """Method 2: Create project-specific sym-lib-table"""
    
    project_file = Path(project_file)
    project_dir = project_file.parent
    sym_lib_table = project_dir / "sym-lib-table"
    
    print(f"\n[Method 2] Creating sym-lib-table: {sym_lib_table}")
    
    # Get absolute path
    symbol_lib = project_dir.parent / "lib" / "custom_components.kicad_sym"
    symbol_lib_abs = str(symbol_lib.resolve()).replace('\\', '/')
    
    # Create sym-lib-table content
    content = f"""(sym_lib_table
  (lib (name "custom_components")(type "KiCad")(uri "{symbol_lib_abs}")(options "")(descr "Custom Components including CAV25256"))
)
"""
    
    with open(sym_lib_table, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"[OK] Created sym-lib-table with custom_components library")
    return True

def verify_library_files():
    """Method 3: Verify library files exist and are valid"""
    
    print(f"\n[Method 3] Verifying library files...")
    
    base_dir = Path(".")
    symbol_lib = base_dir / "lib" / "custom_components.kicad_sym"
    footprint_lib = base_dir / "lib" / "custom_components.pretty" / "CAV25256.kicad_mod"
    
    if not symbol_lib.exists():
        print(f"[ERROR] Symbol library not found: {symbol_lib}")
        return False
    else:
        print(f"[OK] Symbol library exists: {symbol_lib}")
    
    if not footprint_lib.exists():
        print(f"[ERROR] Footprint not found: {footprint_lib}")
        return False
    else:
        print(f"[OK] Footprint exists: {footprint_lib}")
    
    # Check if CAV25256 is in the symbol file
    with open(symbol_lib, 'r', encoding='utf-8') as f:
        content = f.read()
        if "CAV25256" in content:
            print(f"[OK] CAV25256 found in symbol library")
        else:
            print(f"[WARNING] CAV25256 not found in symbol library content!")
            return False
    
    return True

def print_manual_steps():
    """Print manual steps for user"""
    
    print("\n" + "=" * 60)
    print("MANUAL STEPS TO MAKE CAV25256 VISIBLE")
    print("=" * 60)
    print("\n1. Close KiCad completely (if open)")
    print("\n2. Open KiCad")
    print("\n3. Open your project: gmsl-deserializer/gmsl-deserializer.kicad_pro")
    print("\n4. Go to: Preferences → Manage Symbol Libraries")
    print("\n5. Click 'Project Specific Libraries' tab")
    print("\n6. Click the folder icon (Add library)")
    print("\n7. Browse to: Driver-UI-vehicle-system/lib/")
    print("\n8. Select: custom_components.kicad_sym")
    print("\n9. Click OK")
    print("\n10. Verify 'custom_components' appears in the list")
    print("\n11. Click OK to close preferences")
    print("\n12. Close and reopen KiCad")
    print("\n13. Open schematic editor")
    print("\n14. Press 'A' to add symbol")
    print("\n15. Search for: 'CAV25256' or 'custom_components:CAV25256'")
    print("\n" + "=" * 60)

def main():
    """Main function"""
    
    print("=" * 60)
    print("Fixing CAV25256 Visibility in KiCad")
    print("=" * 60)
    
    # Find project file
    project_file = Path("gmsl-deserializer") / "gmsl-deserializer.kicad_pro"
    
    if not project_file.exists():
        print(f"[ERROR] Project file not found: {project_file}")
        print("Please run this script from Driver-UI-vehicle-system directory")
        return False
    
    # Verify files first
    if not verify_library_files():
        print("\n[ERROR] Library files are missing or invalid!")
        print("Run: python download_cav25256_library.py")
        return False
    
    # Fix project file
    fix_project_libraries(project_file)
    
    # Create sym-lib-table
    create_sym_lib_table(project_file)
    
    # Print manual steps
    print_manual_steps()
    
    print("\n[SUCCESS] Applied fixes!")
    print("\nNext: Follow the manual steps above, or restart KiCad and try again.")
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n[ERROR] {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

