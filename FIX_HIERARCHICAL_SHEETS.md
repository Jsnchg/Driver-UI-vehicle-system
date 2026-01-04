# Fix Hierarchical Sheet Errors

## Problem

KiCad cannot load hierarchical sheets because the file paths are broken or incorrect.

## Solution Steps

### Method 1: Fix Paths in Main Schematic (Recommended)

1. **Open your main KiCad project** (the one showing the error)

2. **In Schematic Editor:**
   - Right-click on each hierarchical sheet that's showing errors
   - Select **Properties** or **Edit Sheet**
   - Click the **File** field (or browse button)
   - Navigate to the correct file:
     - For `deserializer.kicad_sch`: Browse to `gmsl-deserializer\deserializer.kicad_sch`
     - For `connectors.kicad_sch`: Browse to `gmsl-deserializer\connectors.kicad_sch`
     - For `power.kicad_sch`: Browse to `gmsl-deserializer\power.kicad_sch`

3. **Use Relative Paths:**
   - Make sure paths are relative to your main project file
   - Example: `gmsl-deserializer\deserializer.kicad_sch` (not full path)

4. **Save the schematic**

### Method 2: Re-add Hierarchical Sheets

If fixing paths doesn't work:

1. **Delete the broken hierarchical sheets:**
   - Select each broken hierarchical sheet
   - Press Delete
   - Confirm deletion

2. **Re-add them correctly:**
   - Place → Hierarchical Sheet
   - Click where you want it
   - In the file browser, navigate to:
     ```
     C:\Users\Jordan\Documents\GitHub\Driver-UI-vehicle-system\gmsl-deserializer\
     ```
   - Select the correct `.kicad_sch` file
   - Click OK

### Method 3: Check File Permissions

If files exist but can't be read:

```powershell
# Check file permissions
Get-Acl ".\gmsl-deserializer\deserializer.kicad_sch" | Format-List

# Fix permissions if needed (run as Administrator)
icacls ".\gmsl-deserializer\*.kicad_sch" /grant "$env:USERNAME:(R)"
```

### Method 4: Verify File Locations

Run this to verify all files are in the correct location:

```powershell
cd C:\Users\Jordan\Documents\GitHub\Driver-UI-vehicle-system
Get-ChildItem .\gmsl-deserializer -Filter *.kicad_sch | Select-Object Name, FullName
```

Expected output:
- `deserializer.kicad_sch` should exist
- `connectors.kicad_sch` should exist  
- `power.kicad_sch` should exist

## Common Issues

### Issue 1: Path Too Long
If paths are truncated (ending with "..."), KiCad might have path length limits.

**Solution:** Use relative paths instead of absolute paths.

### Issue 2: Files Moved
If you moved the `gmsl-deserializer` folder, paths will break.

**Solution:** Update all hierarchical sheet references to new location.

### Issue 3: Case Sensitivity
Windows is case-insensitive, but KiCad might be sensitive.

**Solution:** Ensure exact case matches: `deserializer.kicad_sch` not `Deserializer.kicad_sch`

## Quick Fix Script

If you want to check all hierarchical sheet references in your project:

1. Open your main `.kicad_sch` file in a text editor
2. Search for `(sheet` to find all hierarchical sheets
3. Look for `(file` entries - these are the file paths
4. Verify each path is correct relative to your project

## Prevention

To avoid this in the future:

1. **Always use relative paths** in hierarchical sheets
2. **Keep the folder structure intact** - don't move `gmsl-deserializer` folder
3. **Use git submodules** if you want to track the GMSL project separately:
   ```bash
   git submodule add https://github.com/antmicro/gmsl-deserializer.git gmsl-deserializer
   ```

## Still Having Issues?

If none of these work:

1. Check if files are actually readable:
   ```powershell
   Get-Content ".\gmsl-deserializer\deserializer.kicad_sch" -TotalCount 5
   ```

2. Try opening the GMSL files directly in KiCad to verify they're not corrupted

3. Re-clone the GMSL deserializer if files seem corrupted:
   ```powershell
   Remove-Item -Recurse -Force .\gmsl-deserializer
   git clone --depth 1 https://github.com/antmicro/gmsl-deserializer.git gmsl-deserializer
   ```



