# Quick Fix for Hierarchical Sheet Errors

## The Problem

KiCad shows errors like:
```
Unable to open C:\Users\Jordan\Documents\Driver-UI-vehicle-system\gmsl-deserializer\deserializer.kicad_s... for reading.
```

The paths are being truncated or are incorrect.

## Quick Solution (Choose One)

### Option 1: Use the PowerShell Script (Easiest)

1. Open PowerShell in the project directory:
   ```powershell
   cd C:\Users\Jordan\Documents\GitHub\Driver-UI-vehicle-system
   ```

2. Run the fix script:
   ```powershell
   .\fix-sheet-paths.ps1
   ```

3. If you have a specific schematic file:
   ```powershell
   .\fix-sheet-paths.ps1 -SchematicFile "your-project.kicad_sch"
   ```

The script will:
- Find all hierarchical sheet references
- Fix broken paths to use relative paths
- Create a backup of your original file
- Update the schematic automatically

### Option 2: Manual Fix in KiCad

1. **Open your main KiCad project**

2. **For each broken hierarchical sheet:**
   - Right-click on the hierarchical sheet
   - Select **Properties** (or press `E`)
   - In the **File** field, click the browse button (folder icon)
   - Navigate to: `gmsl-deserializer\deserializer.kicad_sch` (or the correct file)
   - Click **OK**
   - Repeat for `connectors.kicad_sch` and `power.kicad_sch`

3. **Save the schematic** (Ctrl+S)

### Option 3: Re-add Hierarchical Sheets

1. **Delete the broken sheets:**
   - Select each broken hierarchical sheet
   - Press `Delete`
   - Confirm

2. **Re-add them:**
   - **Place → Hierarchical Sheet**
   - Click where you want it
   - Browse to: `gmsl-deserializer\deserializer.kicad_sch`
   - Click **OK**
   - Repeat for other sheets

## Why This Happened

The hierarchical sheet paths were likely stored as:
- **Absolute paths** that got broken when files moved
- **Paths that are too long** (Windows path limit)
- **Incorrect relative paths**

## Prevention

After fixing, make sure:
1. ✅ Use **relative paths** (like `gmsl-deserializer\file.kicad_sch`)
2. ✅ Keep the `gmsl-deserializer` folder in the same location
3. ✅ Don't move project folders after adding hierarchical sheets

## Verify Files Exist

Run this to check:
```powershell
cd C:\Users\Jordan\Documents\GitHub\Driver-UI-vehicle-system
Get-ChildItem .\gmsl-deserializer -Filter *.kicad_sch | Select-Object Name
```

You should see:
- `deserializer.kicad_sch` ✅
- `connectors.kicad_sch` ✅
- `power.kicad_sch` ✅
- `gmsl-deserializer.kicad_sch` ✅

## Still Not Working?

1. **Check file permissions:**
   ```powershell
   Get-Acl ".\gmsl-deserializer\deserializer.kicad_sch"
   ```

2. **Try opening files directly:**
   - Open KiCad
   - File → Open
   - Try opening `gmsl-deserializer\deserializer.kicad_sch` directly
   - If it opens, the file is fine - it's just the path reference

3. **Re-clone if corrupted:**
   ```powershell
   Remove-Item -Recurse -Force .\gmsl-deserializer
   git clone --depth 1 https://github.com/antmicro/gmsl-deserializer.git gmsl-deserializer
   ```



