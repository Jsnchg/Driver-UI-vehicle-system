# Make CAV25256 Visible in KiCad

## Quick Fix (2 minutes)

The library is created and added to your project, but KiCad needs you to register it through Preferences to make it searchable.

### Step 1: Add Library to KiCad Preferences

1. **Open KiCad**
2. **Open** your project: `gmsl-deserializer/gmsl-deserializer.kicad_pro`
3. **Go to**: Preferences → Manage Symbol Libraries
4. **Click** "Project Specific Libraries" tab
5. **Check** if `custom_components` is listed:
   - **If YES**: Skip to Step 2
   - **If NO**: Continue below
6. **Click** the folder icon (Add library button)
7. **Browse to**: `C:\Users\Jordan\Documents\GitHub\Driver-UI-vehicle-system\lib\`
8. **Select**: `custom_components.kicad_sym`
9. **Click OK**
10. **Verify** `custom_components` appears in the list
11. **Click OK** to close preferences

### Step 2: Restart KiCad

1. **Close KiCad completely** (all windows)
2. **Reopen KiCad**
3. **Open Schematic Editor**
4. **Press `A`** to add symbol
5. **Search for**: `CAV25256` or `custom_components:CAV25256`
6. **It should now appear!** ✅

## Alternative: Use Library Browser

If search still doesn't work:

1. **Press `A`** in schematic editor
2. **Click** "Browse Libraries" button (usually at bottom)
3. **Navigate to**: `lib/custom_components.kicad_sym`
4. **Double-click** to open
5. **CAV25256** will be visible
6. **Select and place** directly

## Alternative: Search with Library Prefix

1. **Press `A`** to add symbol
2. **Type**: `custom_components:CAV25256` (with library prefix)
3. This forces search in the custom_components library
4. Works even if library doesn't show in list

## Verify It's Working

After adding through Preferences:

1. **Press `A`** in schematic
2. **Type**: `custom_components:` in search box
   - Should show CAV25256 symbol
3. **Or type**: `CAV25256`
   - Should appear in results

## Why This Happens

KiCad has two systems:
- **Schematic loading** - Uses library paths from project file (works ✅)
- **Search index** - Needs explicit registration through Preferences (needs fix ⚠️)

The library is configured correctly, but the search database needs manual registration.

## Files Created

✅ Symbol library: `lib/custom_components.kicad_sym`  
✅ Footprint: `lib/custom_components.pretty/CAV25256.kicad_mod`  
✅ Project file updated: `gmsl-deserializer/gmsl-deserializer.kicad_pro`  
✅ sym-lib-table created: `gmsl-deserializer/sym-lib-table`

## Troubleshooting

### Still not visible?

1. **Check library path** in Preferences → Manage Symbol Libraries
   - Should show: `custom_components` library
   - Path should be: `C:\Users\Jordan\Documents\GitHub\Driver-UI-vehicle-system\lib\custom_components.kicad_sym`

2. **Restart KiCad** completely (close all windows)

3. **Try Global Libraries** instead:
   - Preferences → Manage Symbol Libraries
   - Click "Global Libraries" tab
   - Add the same library file
   - Restart KiCad

4. **Verify file exists**:
   - Check: `lib/custom_components.kicad_sym` exists
   - Check: `lib/custom_components.pretty/CAV25256.kicad_mod` exists

5. **Use Symbol Editor to verify**:
   - Tools → Symbol Editor
   - File → Open Library
   - Browse to: `lib/custom_components.kicad_sym`
   - You should see CAV25256 - this confirms the library is valid

## Summary

✅ Library files created  
✅ Project file updated  
✅ sym-lib-table created  
⚠️ **Need to add through Preferences** to make it searchable

Once added through Preferences → Manage Symbol Libraries, CAV25256 will be searchable!

