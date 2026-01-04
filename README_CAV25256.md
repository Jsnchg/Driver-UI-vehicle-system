# CAV25256 KiCad Setup Guide

This guide will help you add the CAV25256 component to your KiCad project.

## Quick Start

### Option 1: Automated Setup (Recommended)

Run the PowerShell script:
```powershell
.\setup_cav25256.ps1
```

### Option 2: Manual Setup

1. **Create the library:**
   ```powershell
   python download_cav25256_library.py
   ```

2. **Add to project:**
   ```powershell
   python add_cav25256_to_kicad.py
   ```

3. **Or add to specific project:**
   ```powershell
   python add_cav25256_to_kicad.py --project "gmsl-deserializer/gmsl-deserializer.kicad_pro"
   ```

## What Gets Created

- **Symbol Library**: `lib/custom_components.kicad_sym`
  - Contains CAV25256 schematic symbol
  
- **Footprint Library**: `lib/custom_components.pretty/CAV25256.kicad_mod`
  - Contains CAV25256 PCB footprint

- **Component List**: `COMPONENT_LIST.txt`
  - Text list of components

## Using CAV25256 in KiCad

1. **Open KiCad** and load your project
2. **Open Schematic Editor** (Eeschema)
3. **Press `A`** to add a symbol
4. **Search for**: `CAV25256` or `custom_components:CAV25256`
5. **Place** the component on your schematic
6. **Assign footprint**: The footprint should auto-assign, but verify it matches your component

## Important Notes

⚠️ **Footprint Dimensions**: The default footprint is a generic SMD capacitor. You should:
- Check the CAV25256 datasheet for exact dimensions
- Adjust the footprint in `lib/custom_components.pretty/CAV25256.kicad_mod` if needed
- Common capacitor sizes: 0402, 0603, 0805, 1206, etc.

## Troubleshooting

### Library not showing in KiCad?

1. **Close KiCad completely**
2. **Reopen KiCad**
3. **Go to**: Preferences → Manage Symbol Libraries
4. **Check**: Project Specific Libraries tab
5. **Verify**: `custom_components` is listed

### Component not found?

1. **Press `A`** in schematic editor
2. **Type**: `custom_components:CAV25256` (with library prefix)
3. **Or**: Browse libraries and select `custom_components`

### Need to update footprint?

Edit: `lib/custom_components.pretty/CAV25256.kicad_mod`

Common adjustments:
- Pad size (currently 1.5mm x 1.5mm)
- Pad spacing (currently 2.5mm center-to-center)
- Component outline

## Files Created

```
Driver-UI-vehicle-system/
├── COMPONENT_LIST.txt                    # Component text list
├── download_cav25256_library.py          # Library creation script
├── add_cav25256_to_kicad.py             # Project integration script
├── setup_cav25256.ps1                   # Automated setup script
├── README_CAV25256.md                   # This file
└── lib/
    ├── custom_components.kicad_sym      # Symbol library
    └── custom_components.pretty/
        └── CAV25256.kicad_mod           # Footprint
```

## Adding More Components

To add more components to the same library:

1. Edit `lib/custom_components.kicad_sym` to add new symbols
2. Create new `.kicad_mod` files in `lib/custom_components.pretty/`
3. The library is already added to your project, so new components will be available immediately

## Support

If you encounter issues:
1. Check that Python 3 is installed
2. Verify project file exists and is valid JSON
3. Ensure `lib/` directory is created
4. Check KiCad version compatibility (tested with KiCad 9.0)

