# How to Add Library to KiCad Symbol Editor

## In Symbol Editor

KiCad Symbol Editor has these menu options:
- **New Library** - Creates a new empty library (don't use this)
- **Add Library** - Adds an existing library file (USE THIS!)

## Steps to See DS92LV16

1. **Open KiCad**
2. **Tools → Symbol Editor**
3. **File → Add Library** (or **Library → Add Library** depending on KiCad version)
4. **Browse to**: `C:\Users\Jordan\Documents\GitHub\Driver-UI-vehicle-system\lib\custom_components.kicad_sym`
5. **Select it** and click **OK**
6. **The library should appear** in the library list (usually on the left or top)
7. **Click on `custom_components`** in the library list
8. **Look for DS92LV16** in the symbol list below

## Alternative: Use Preferences

If "Add Library" doesn't work in Symbol Editor:

1. **Preferences → Manage Symbol Libraries**
2. **Click "Project Specific Libraries" tab** (or "Global Libraries")
3. **Click the folder icon** (Add library)
4. **Browse to**: `lib\custom_components.kicad_sym`
5. **Select it** and click **OK**
6. **Close KiCad completely**
7. **Reopen KiCad**
8. **Tools → Symbol Editor**
9. **The library should now be in the library dropdown/list**
10. **Select `custom_components`** and look for DS92LV16

## If You Still Don't See It

1. **Check the library list** - Make sure `custom_components` is selected
2. **Scroll through the symbol list** - DS92LV16 should be alphabetical
3. **Try searching** - Some versions have a search box in Symbol Editor
4. **Check for errors** - Look at the bottom status bar for error messages

## Verify the File

The library file is at:
- `C:\Users\Jordan\Documents\GitHub\Driver-UI-vehicle-system\lib\custom_components.kicad_sym`
- Also copied to: `C:\Users\Jordan\AppData\Roaming\kicad\9.0\symbols\custom_components.kicad_sym`

Both files should be identical and contain DS92LV16.

