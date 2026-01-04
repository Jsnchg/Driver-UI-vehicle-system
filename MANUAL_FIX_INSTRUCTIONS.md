# Manual Fix for Hierarchical Sheet Errors

## Quick Fix in KiCad (Easiest Method)

Since the script can't find your project file, here's how to fix it manually in KiCad:

### Step 1: Open Your KiCad Project

1. Open KiCad
2. Open your project (File → Open Project)
3. Open the schematic that's showing the error

### Step 2: Fix Each Hierarchical Sheet

For each broken hierarchical sheet:

1. **Right-click on the hierarchical sheet** that's showing an error
2. **Select "Properties"** (or press `E`)
3. **In the Properties dialog:**
   - Look for the **"File"** field
   - Click the **folder/browse button** next to it
4. **Navigate to the correct file:**
   - Go to: `C:\Users\Jordan\Documents\GitHub\Driver-UI-vehicle-system\gmsl-deserializer\`
   - Select the correct file:
     - For `deserializer.kicad_sch` error → select `deserializer.kicad_sch`
     - For `connectors.kicad_sch` error → select `connectors.kicad_sch`
     - For `power.kicad_sch` error → select `power.kicad_sch`
5. **Click OK**
6. **Save the schematic** (Ctrl+S)

### Step 3: Repeat for All Broken Sheets

Do this for each hierarchical sheet that's showing an error.

### Step 4: Verify

1. Close and reopen the schematic
2. The errors should be gone
3. The hierarchical sheets should load correctly

## Alternative: Re-add Hierarchical Sheets

If fixing paths doesn't work:

1. **Delete the broken hierarchical sheets:**
   - Select each broken sheet
   - Press `Delete`
   - Confirm deletion

2. **Re-add them correctly:**
   - **Place → Hierarchical Sheet**
   - Click where you want it on the schematic
   - In the file browser, navigate to:
     ```
     C:\Users\Jordan\Documents\GitHub\Driver-UI-vehicle-system\gmsl-deserializer\
     ```
   - Select the file you need (`deserializer.kicad_sch`, `connectors.kicad_sch`, or `power.kicad_sch`)
   - Click **OK**
   - Place the sheet on your schematic

3. **Save** (Ctrl+S)

## Why This Happens

The hierarchical sheet paths get stored as:
- **Absolute paths** that break when files move
- **Paths that are too long** (Windows 260-character limit)
- **Incorrect relative paths**

## Prevention

After fixing:
1. ✅ Make sure paths are **relative** (like `gmsl-deserializer\file.kicad_sch`)
2. ✅ Keep the `gmsl-deserializer` folder in the same location relative to your project
3. ✅ Don't move project folders after adding hierarchical sheets

## If You Can't Find the Files

Verify the files exist:
```powershell
cd C:\Users\Jordan\Documents\GitHub\Driver-UI-vehicle-system
Get-ChildItem .\gmsl-deserializer -Filter *.kicad_sch | Select-Object Name
```

You should see:
- `deserializer.kicad_sch` ✅
- `connectors.kicad_sch` ✅
- `power.kicad_sch` ✅

## Still Having Issues?

1. **Check file permissions** - Make sure you can read the files
2. **Try opening files directly** - Open `gmsl-deserializer\deserializer.kicad_sch` directly in KiCad to verify it's not corrupted
3. **Re-clone if needed:**
   ```powershell
   cd C:\Users\Jordan\Documents\GitHub\Driver-UI-vehicle-system
   Remove-Item -Recurse -Force .\gmsl-deserializer
   git clone --depth 1 https://github.com/antmicro/gmsl-deserializer.git gmsl-deserializer
   ```

