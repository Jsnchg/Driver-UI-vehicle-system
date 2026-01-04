# Force KiCad to Reload DS92LV16

## ✅ Confirmed: DS92LV16 IS in the Library File

The symbol is definitely in `lib/custom_components.kicad_sym` at line 1595. The issue is KiCad hasn't reloaded it.

## Method 1: Symbol Editor (Most Reliable - Do This First!)

1. **Open KiCad**
2. **Tools → Symbol Editor**
3. **File → Open Library**
4. **Navigate to**: `C:\Users\Jordan\Documents\GitHub\Driver-UI-vehicle-system\lib\custom_components.kicad_sym`
5. **Open it**
6. **You should see DS92LV16 in the symbol list on the left**

If you can see it here, the file is correct. Then:

7. **Close Symbol Editor**
8. **Open Schematic Editor**
9. **Press `A` to add symbol**
10. **In the symbol chooser, search for `DS92LV16`**
11. **If it still doesn't appear, continue to Method 2**

## Method 2: Remove and Re-add Library

1. **Open KiCad**
2. **Preferences → Manage Symbol Libraries**
3. **Click "Project Specific Libraries" tab**
4. **Find `custom_components` in the list**
5. **Select it and click "Remove" (trash icon)**
6. **Click "Add library" (folder icon)**
7. **Navigate to**: `C:\Users\Jordan\Documents\GitHub\Driver-UI-vehicle-system\lib\`
8. **Select**: `custom_components.kicad_sym`
9. **Click OK**
10. **Verify it appears in the list**
11. **Click OK to close preferences**
12. **Close KiCad completely**
13. **Reopen KiCad**
14. **Press `A` in schematic editor**
15. **Search for `DS92LV16`**

## Method 3: Clear KiCad Cache

1. **Close KiCad completely**
2. **Open PowerShell** and run:
   ```powershell
   Remove-Item "$env:APPDATA\kicad\9.0\cache\*" -Recurse -Force -ErrorAction SilentlyContinue
   ```
3. **Reopen KiCad**
4. **Open your project**
5. **Press `A` in schematic editor**
6. **Search for `DS92LV16`**

## Method 4: Verify Library Path

1. **Preferences → Manage Symbol Libraries**
2. **Click "Project Specific Libraries" tab**
3. **Find `custom_components`**
4. **Check the path** - it should be:
   - `C:\Users\Jordan\Documents\GitHub\Driver-UI-vehicle-system\lib\custom_components.kicad_sym`
   - OR relative: `lib/custom_components.kicad_sym`
5. **If path is wrong, fix it using Method 2**

## Method 5: Direct Library Access

1. **In Schematic Editor, press `A`**
2. **In symbol chooser, look for "Browse Libraries" or folder icon**
3. **Navigate directly to**: `lib/custom_components.kicad_sym`
4. **Open it**
5. **DS92LV16 should be in the list**

## Verification

After trying any method above:

1. **Press `A` in schematic editor**
2. **Type**: `DS92LV16` in search box
3. **OR type**: `custom_components:DS92LV16`
4. **It should appear!**

## If Still Not Working

The symbol file is correct. The issue is KiCad's library loading. Try:

1. **Check KiCad version** - Make sure you're using KiCad 9.0 or later
2. **Restart computer** - Sometimes Windows file handles prevent reload
3. **Check file permissions** - Make sure the file isn't read-only
4. **Try opening the library file in a text editor** - Verify it's not corrupted

