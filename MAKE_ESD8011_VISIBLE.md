# How to Make ESD8011 Visible in KiCad

## The Problem
ESD8011 is in the library file, but KiCad's search doesn't find it because the library needs to be registered in KiCad's Library Manager.

## Solution: Register Library in KiCad

### Step-by-Step Instructions

1. **Open KiCad**
   - Launch KiCad application

2. **Open Your Project**
   - File → Open Project
   - Navigate to: `gmsl-deserializer/gmsl-deserializer.kicad_pro`
   - Open it

3. **Open Schematic Editor**
   - Click "Schematic Editor" button or File → Open Schematic

4. **Add Library to KiCad's Library Manager**
   - Go to: **Preferences → Manage Symbol Libraries**
   - Click the **"Project Specific Libraries"** tab
   - Look for `custom_components` in the list
   
   **If NOT in the list:**
   - Click the **folder icon** (Add library) at the bottom
   - Navigate to: `lib/custom_components.kicad_sym`
   - Select it and click **OK**
   - Verify `custom_components` appears in the list
   - Click **OK** to close preferences

5. **Restart KiCad**
   - Close KiCad completely
   - Reopen KiCad
   - Open your project again

6. **Search for ESD8011**
   - In Schematic Editor, press **`A`** to add symbol
   - In the search box, type: **`ESD8011`**
   - It should now appear!

## Alternative: Use Symbol Editor to Verify

1. **Open Symbol Editor**
   - Tools → Symbol Editor

2. **Open Library**
   - File → Open Library
   - Navigate to: `lib/custom_components.kicad_sym`
   - Open it

3. **Verify ESD8011 is There**
   - You should see ESD8011 in the symbol list
   - If you can see it here, the library file is correct

4. **Then Follow Steps Above**
   - The library just needs to be registered in Preferences

## Quick Test

After registering the library:

1. Press `A` in schematic editor
2. Type: `custom_components:` → Should show all 27 components
3. Type: `ESD8011` → Should appear in results

## Why This Happens

KiCad has two separate systems:
- **Project file libraries** (pinned_symbol_libs) - Used when loading schematics
- **Library Manager** - Used for search/indexing

The library is in the project file, but KiCad's search index needs explicit registration through Preferences.

## Verification

✅ Library file exists: `lib/custom_components.kicad_sym`  
✅ ESD8011 symbol is in the file  
✅ Library is in project file (`pinned_symbol_libs`)  
⚠️ Library needs to be registered in Preferences for search to work

