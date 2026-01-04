#!/usr/bin/env python3
"""
Validate KiCad symbol library for syntax errors
"""
import re
from pathlib import Path

def validate_library():
    """Validate the custom_components library file"""
    
    lib_file = Path("lib/custom_components.kicad_sym")
    
    if not lib_file.exists():
        print(f"[ERROR] Library not found: {lib_file}")
        return False
    
    print("=" * 60)
    print("LIBRARY VALIDATION")
    print("=" * 60)
    print(f"\nLibrary: {lib_file}")
    
    with open(lib_file, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')
    
    print(f"Size: {len(content):,} bytes")
    print(f"Lines: {len(lines):,}")
    
    # Check file structure
    print("\n" + "=" * 60)
    print("FILE STRUCTURE")
    print("=" * 60)
    
    has_opening = content.startswith('(kicad_symbol_lib')
    has_closing = content.strip().endswith(')')
    
    print(f"Opening tag: {'[OK]' if has_opening else '[ERROR]'}")
    print(f"Closing tag: {'[OK]' if has_closing else '[ERROR]'}")
    
    # Count parentheses
    open_parens = content.count('(')
    close_parens = content.count(')')
    balanced = open_parens == close_parens
    
    print(f"Opening parentheses: {open_parens}")
    print(f"Close parentheses: {close_parens}")
    print(f"Balanced: {'[OK]' if balanced else '[ERROR]'}")
    
    if not balanced:
        print(f"[ERROR] Unbalanced parentheses! Difference: {abs(open_parens - close_parens)}")
        return False
    
    # Check quotes (should be even)
    quotes = content.count('"')
    if quotes % 2 != 0:
        print(f"[ERROR] Odd number of quotes: {quotes}")
        return False
    else:
        print(f"Quotes: {quotes} [OK]")
    
    # Find all symbols
    print("\n" + "=" * 60)
    print("SYMBOL ANALYSIS")
    print("=" * 60)
    
    top_level_pattern = r'^\s*\(symbol\s+"([^"]+)"\s+\(pin_names'
    top_level_symbols = re.findall(top_level_pattern, content, re.MULTILINE)
    
    print(f"Top-level symbols found: {len(top_level_symbols)}")
    for i, sym in enumerate(top_level_symbols, 1):
        print(f"  {i:2d}. {sym}")
    
    # Check each symbol for issues
    print("\n" + "=" * 60)
    print("SYMBOL VALIDATION")
    print("=" * 60)
    
    issues_found = False
    
    for sym_name in top_level_symbols:
        # Find symbol definition
        sym_pattern = rf'^\s*\(symbol\s+"{re.escape(sym_name)}"\s+\(pin_names'
        match = re.search(sym_pattern, content, re.MULTILINE)
        
        if not match:
            print(f"[ERROR] {sym_name}: Could not find symbol definition")
            issues_found = True
            continue
        
        # Find the end of this symbol (next top-level symbol or end of file)
        start_pos = match.start()
        next_symbols = re.finditer(r'^\s*\(symbol\s+"[^"]+"\s+\(pin_names', content, re.MULTILINE)
        
        end_pos = len(content)
        for next_match in next_symbols:
            if next_match.start() > start_pos:
                end_pos = next_match.start()
                break
        
        sym_content = content[start_pos:end_pos]
        
        # Check for required elements
        has_properties = '(property' in sym_content
        has_unit = f'(symbol "{sym_name}_0_1"' in sym_content
        has_pins = '(pin' in sym_content
        
        if not has_properties:
            print(f"[WARNING] {sym_name}: Missing properties")
        if not has_unit:
            print(f"[ERROR] {sym_name}: Missing unit symbol")
            issues_found = True
        if not has_pins:
            print(f"[ERROR] {sym_name}: Missing pins")
            issues_found = True
        
        # Check for invalid characters in pin names
        pin_name_pattern = r'\(name\s+"([^"]+)"'
        pin_names = re.findall(pin_name_pattern, sym_content)
        
        for pin_name in pin_names:
            # Check for problematic characters
            if '[' in pin_name or ']' in pin_name:
                print(f"[WARNING] {sym_name}: Pin name has brackets: {pin_name}")
            if ':' in pin_name and '[' not in pin_name:
                # Colons might be OK, but check
                pass
    
    # Check for common syntax errors
    print("\n" + "=" * 60)
    print("SYNTAX CHECKS")
    print("=" * 60)
    
    # Check for malformed property definitions
    malformed_props = re.findall(r'\(property[^)]*$', content, re.MULTILINE)
    if malformed_props:
        print(f"[ERROR] Found {len(malformed_props)} potentially malformed property definitions")
        for i, prop in enumerate(malformed_props[:5], 1):
            print(f"  {i}. {prop[:80]}...")
        issues_found = True
    
    # Check for malformed pin definitions
    malformed_pins = re.findall(r'\(pin[^)]*$', content, re.MULTILINE)
    if malformed_pins:
        print(f"[ERROR] Found {len(malformed_pins)} potentially malformed pin definitions")
        for i, pin in enumerate(malformed_pins[:5], 1):
            print(f"  {i}. {pin[:80]}...")
        issues_found = True
    
    # Summary
    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)
    
    if issues_found:
        print("[ERROR] Issues found in library file!")
        print("\nRecommendation:")
        print("1. Open KiCad Symbol Editor")
        print("2. File -> Open Library")
        print("3. Try to open lib/custom_components.kicad_sym")
        print("4. KiCad will show the exact error and line number")
        return False
    else:
        print("[OK] No obvious syntax errors found")
        print("\nIf KiCad still can't load the library:")
        print("1. Try opening it in Symbol Editor to see exact error")
        print("2. Check KiCad version compatibility")
        print("3. Try removing the last added symbol (DS92LV16) temporarily")
        return True

if __name__ == "__main__":
    validate_library()

