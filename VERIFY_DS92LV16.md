# DS92LV16 Verification

## Confirmed: DS92LV16 IS in the Library

I've verified that DS92LV16 is definitely in the `lib/custom_components.kicad_sym` file:

- **Location**: Line 1593
- **Symbol Number**: 29 of 29 total symbols
- **File Structure**: Valid KiCad symbol library format
- **Symbol Definition**: Complete and properly formatted

## Why It Might Not Be Visible

KiCad caches library information. Even though the symbol is in the file, KiCad may not have reloaded it.

## Solution: Force KiCad to Reload Library

### Method 1: Reload Library in Preferences

1. **Open KiCad**
2. **Preferences → Manage Symbol Libraries**
3. **Click "Project Specific Libraries" tab**
4. **Find `custom_components` in the list**
5. **Click "Reload" button** (if available)
   - OR remove it and re-add it:
   - Click the library entry
   - Click "Remove" (trash icon)
   - Click "Add library" (folder icon)
   - Navigate to: `lib/custom_components.kicad_sym`
   - Select it and click OK
6. **Click OK** to close preferences
7. **Close KiCad completely**
8. **Reopen KiCad**
9. **Press `A` in schematic editor**
10. **Search for `DS92LV16`**

### Method 2: Verify in Symbol Editor

1. **Tools → Symbol Editor**
2. **File → Open Library**
3. **Navigate to**: `lib/custom_components.kicad_sym`
4. **Open it**
5. **You should see DS92LV16 in the symbol list**

If you can see it in Symbol Editor, the file is correct and you just need to reload it in Preferences.

### Method 3: Clear KiCad Cache

1. **Close KiCad completely**
2. **Delete cache folder** (if it exists):
   - `%APPDATA%\kicad\9.0\cache\*`
   - Or: `C:\Users\Jordan\AppData\Roaming\kicad\9.0\cache\*`
3. **Reopen KiCad**
4. **Open your project**
5. **Search for DS92LV16**

## Verification Commands

Run these in PowerShell to verify:

```powershell
cd C:\Users\Jordan\Documents\GitHub\Driver-UI-vehicle-system
Select-String -Path "lib\custom_components.kicad_sym" -Pattern "DS92LV16"
```

Should show:
- Line 1593: `(symbol "DS92LV16"`
- Line 1597: `(property "Value" "DS92LV16"`
- Line 1606: `(symbol "DS92LV16_0_1"`

## All 29 Components in Library

1. CAV25256
2. NCV97200
3. NCV8445
4. RSL200
5. KW12-3
6. NCV7450
7. ESDONCAN1LT
8. NCV890100
9. NCV891330
10. NSVF4015SG4
11. NBA3N012C
12. AD3531R
13. TDC7200
14. MC14049B
15. TUSB9261
16. NUP1105L
17. NV25128
18. NSDP301MX2W
19. ESD7551
20. NSVF4009SG4
21. AWRL6432
22. NRVHPM220
23. NCV75215DB001R2G
24. NV24C128MUW
25. AS0149AT
26. NCV92310
27. ESD8011
28. MAX96793
29. **DS92LV16** ← This one!

## If Still Not Visible

If DS92LV16 still doesn't appear after reloading:

1. Check if other components from the library are visible (e.g., CAV25256, NCV97200)
2. If other components work but DS92LV16 doesn't, there may be a syntax issue
3. Try opening the library file in Symbol Editor directly
4. Check KiCad error messages in the message panel

The symbol is definitely in the file - it's just a matter of getting KiCad to recognize it!

