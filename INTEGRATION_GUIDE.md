# GMSL Deserializer Integration Guide

## Overview

This guide explains how the GMSL Deserializer project from [antmicro/gmsl-deserializer](https://github.com/antmicro/gmsl-deserializer) has been integrated into the Driver UI vehicle system KiCad project.

## Repository Structure

```
Driver-UI-vehicle-system/
├── gmsl-deserializer/          # Cloned GMSL deserializer project
│   ├── *.kicad_sch             # Schematic files
│   ├── *.kicad_pcb             # PCB layout files
│   ├── *.kicad_pro             # Project files
│   └── README.md               # Original project documentation
└── INTEGRATION_GUIDE.md        # This file
```

## GMSL Deserializer Project

The GMSL Deserializer is an open hardware design that:
- Translates up to 4 GMSL2 signals into 2x 4-lane MIPI CSI-2 interfaces
- Includes PoC (Power over Coax) circuit for up to 12W per GMSL line
- Uses 50-pin Antmicro Dual Camera connector
- Designed in KiCad 8

## Integration Methods

### Option 1: Reference as Submodule (Recommended)

Add the GMSL deserializer as a git submodule:

```bash
git submodule add https://github.com/antmicro/gmsl-deserializer.git gmsl-deserializer
```

### Option 2: Copy Specific Files

If you only need specific schematics or PCB layouts:

1. Copy the desired `.kicad_sch` or `.kicad_pcb` files
2. Add them to your main KiCad project
3. Update library paths if needed

### Option 3: Use as Library Reference

Reference the GMSL deserializer components in your main project:

1. Open your main KiCad project
2. Use "Append Schematic" to import sheets from gmsl-deserializer
3. Link components as needed

## Using in Your KiCad Project

### Importing Schematics

1. Open your main KiCad project
2. Go to **File → Append Schematic Sheet**
3. Navigate to `gmsl-deserializer/` directory
4. Select the desired schematic file (e.g., `deserializer.kicad_sch`)
5. The schematic will be added as a hierarchical sheet

### Importing PCB Layouts

1. In your main PCB editor
2. Go to **File → Append Board**
3. Select the GMSL deserializer PCB file
4. Components will be imported (you may need to update footprints)

### Key Files in GMSL Deserializer

- `gmsl-deserializer.kicad_sch` - Main schematic
- `deserializer.kicad_sch` - Deserializer circuit
- `connectors.kicad_sch` - Connector definitions
- `power.kicad_sch` - Power supply circuit
- `gmsl-deserializer.kicad_pcb` - Complete PCB layout

## Next Steps

1. **Review the schematics** to understand the circuit design
2. **Check component libraries** - ensure all symbols and footprints are available
3. **Integrate into your design** using one of the methods above
4. **Update connections** to match your vehicle system requirements
5. **Verify power requirements** - PoC circuit provides up to 12W per line

## GitHub Repository Connection

To connect your local repository to GitHub:

```bash
# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/Driver-UI-vehicle-system.git

# Or if remote already exists, update it
git remote set-url origin https://github.com/YOUR_USERNAME/Driver-UI-vehicle-system.git

# Push to GitHub
git add .
git commit -m "Initial commit with GMSL deserializer integration"
git push -u origin master
```

## References

- [GMSL Deserializer Repository](https://github.com/antmicro/gmsl-deserializer)
- [KiCad Documentation](https://docs.kicad.org/)
- [GMSL2 Specification](https://www.maximintegrated.com/en/design/technical-documents/tutorials/6/6197.html)

## License

The GMSL Deserializer project is licensed under Apache-2.0. Ensure compliance when using in your project.

