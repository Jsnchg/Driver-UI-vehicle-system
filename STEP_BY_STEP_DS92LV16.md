# Step-by-Step: Make DS92LV16 Appear in KiCad

## ✅ Confirmed: DS92LV16 IS in the file (line 1595)
## ✅ File is valid (no syntax errors)
## ✅ Library structure is correct

The issue is KiCad needs to be forced to reload the library.

## Method 1: Symbol Editor (Most Reliable)

1. **Open KiCad**
2. **Tools → Symbol Editor**
3. **File → Add Library** (NOT "New Library")
4. **Browse to**: `C:\Users\Jordan\Documents\GitHub\Driver-UI-vehicle-system\lib\custom_components.kicad_sym`
5. **Select it** and click **OK**
6. **Look at the library dropdown/list** (usually top-left or left sidebar)
7. **Click on `custom_components`** in that list
8. **Look at the symbol list below** (this shows all symbols in the selected library)
9. **Scroll through or search** - DS92LV16 should be there (it's #29, alphabetically it's after MAX96793)

**If you see DS92LV16 here**: The file is correct! Continue to Method 2.

**If you DON'T see DS92LV16 here**: KiCad will show an error message. Tell me what the error says.

## Method 2: Force Reload via Preferences

1. **Preferences → Manage Symbol Libraries**
2. **Click "Project Specific Libraries" tab**
3. **Find `custom_components` in the list**
4. **Select it** and click **Remove** (trash icon)
5. **Click "Add library"** (folder icon)
6. **Browse to**: `lib\custom_components.kicad_sym`
7. **Select it** and click **OK**
8. **Verify it appears in the list**
9. **Click OK** to close preferences
10. **Close KiCad COMPLETELY** (check Task Manager if needed)
11. **Reopen KiCad**
12. **Open your project**
13. **Press `A` in schematic editor**
14. **Type**: `DS92LV16` in search box
15. **OR type**: `custom_components:DS92LV16`

## Method 3: Clear Cache and Reload

1. **Close KiCad completely**
2. **Run PowerShell**:
   ```powershell
   Remove-Item "$env:APPDATA\kicad\9.0\cache\*" -Recurse -Force -ErrorAction SilentlyContinue
   ```
3. **Reopen KiCad**
4. **Follow Method 1 or Method 2**

## Verification

After trying any method:

- **In Symbol Editor**: DS92LV16 should appear in the symbol list when `custom_components` library is selected
- **In Schematic Editor**: Press `A`, search for `DS92LV16` or `custom_components:DS92LV16`

## If Still Not Working

Tell me:
1. Can you see DS92LV16 in Symbol Editor when you select the `custom_components` library?
2. What happens when you search for it in schematic editor?
3. Any error messages?

