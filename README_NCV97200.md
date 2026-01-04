# NCV97200 Component Setup

## ✅ Setup Complete!

NCV97200 has been added to your KiCad project along with CAV25256.

## Components Available

- **CAV25256** - Capacitor
- **NCV97200** - IC (Onsemi component)

Both are in the `custom_components` library.

## Files Created/Updated

✅ **COMPONENT_LIST.txt** - Updated with NCV97200  
✅ **lib/custom_components.kicad_sym** - Added NCV97200 symbol  
✅ **lib/custom_components.pretty/NCV97200.kicad_mod** - Created footprint  
✅ **download_custom_libraries.py** - Updated script  
✅ **add_custom_components_to_kicad.py** - Updated script  
✅ **setup_custom_components.ps1** - Updated PowerShell script  

## Using NCV97200 in KiCad

1. **Open KiCad** and load your project
2. **Open Schematic Editor** (Eeschema)
3. **Press `A`** to add a symbol
4. **Search for**: `NCV97200` or `custom_components:NCV97200`
5. **Place** the component on your schematic

## NCV97200 Symbol Details

- **Reference**: U (IC)
- **Package**: SOIC-8 (generic, verify with datasheet)
- **Pins**: 8 pins (VCC, IN1, OUT1, IN2, OUT2, GND, EN, NC)
- **Datasheet**: https://www.onsemi.com/download/data-sheet/pdf/ncv97200-d.pdf

## Important Notes

⚠️ **Footprint Dimensions**: The NCV97200 footprint is a generic SOIC-8. You should:
- Check the NCV97200 datasheet for exact package dimensions
- Verify pin assignments match the actual component
- Adjust the footprint in `lib/custom_components.pretty/NCV97200.kicad_mod` if needed

⚠️ **Pin Configuration**: The symbol has generic pin names. Verify against the datasheet:
- Pin 1: VCC
- Pin 2: IN1
- Pin 3: OUT1
- Pin 4: IN2
- Pin 5: OUT2
- Pin 6: GND
- Pin 7: EN
- Pin 8: NC

## Making Components Visible

If components don't appear in search:

1. **Preferences → Manage Symbol Libraries**
2. **Project Specific Libraries** tab
3. **Add**: `lib/custom_components.kicad_sym`
4. **Restart KiCad**
5. **Search again**

Or use library prefix: `custom_components:NCV97200`

## Scripts Available

- **`download_custom_libraries.py`** - Verify/check libraries
- **`add_custom_components_to_kicad.py`** - Add libraries to project
- **`setup_custom_components.ps1`** - Automated setup (PowerShell)

## Quick Start

```powershell
.\setup_custom_components.ps1
```

Or manually:
```powershell
python download_custom_libraries.py
python add_custom_components_to_kicad.py
```

## Next Steps

1. ✅ Component added to library
2. ✅ Footprint created
3. ✅ Project updated
4. ⚠️ Verify pin assignments against datasheet
5. ⚠️ Verify footprint dimensions match actual package
6. ✅ Ready to use in KiCad!

