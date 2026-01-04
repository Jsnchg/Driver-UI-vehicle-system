# How to Integrate GMSL Deserializer into Your KiCad Project

## Current Setup

✅ **GMSL deserializer is cloned INTO your Driver-UI-vehicle-system project**
- Location: `C:\Users\Jordan\Documents\GitHub\Driver-UI-vehicle-system\gmsl-deserializer\`
- It's a **subdirectory** of your main project, not a separate project

## Integration Options

### Option 1: Reference Schematics (Recommended for Starting)

Use the GMSL deserializer schematics as reference or import specific sheets:

1. **Open your main KiCad project** (create one if you don't have it yet)
2. **In KiCad Schematic Editor:**
   - Go to **Place → Hierarchical Sheet**
   - Click on your schematic
   - In the file browser, navigate to:
     ```
     C:\Users\Jordan\Documents\GitHub\Driver-UI-vehicle-system\gmsl-deserializer\
     ```
   - Select `gmsl-deserializer.kicad_sch` or `deserializer.kicad_sch`
   - This adds it as a hierarchical sheet in your project

### Option 2: Copy Specific Components

If you only need specific parts:

1. Open `gmsl-deserializer\deserializer.kicad_sch` in KiCad
2. Select the components/circuits you need
3. Copy (Ctrl+C)
4. Open your main schematic
5. Paste (Ctrl+V)
6. Update connections as needed

### Option 3: Use as Complete Module

Import the entire GMSL deserializer board as a module:

1. **In your main KiCad project:**
   - File → Append Schematic Sheet
   - Navigate to `gmsl-deserializer\gmsl-deserializer.kicad_sch`
   - This imports the entire design as a hierarchical sheet

2. **For PCB integration:**
   - In PCB Editor: File → Append Board
   - Select `gmsl-deserializer\gmsl-deserializer.kicad_pcb`
   - Components will be imported (you may need to update footprints)

## Key Files Available

In `gmsl-deserializer\` directory:

- **`gmsl-deserializer.kicad_sch`** - Main complete schematic
- **`deserializer.kicad_sch`** - Deserializer circuit only
- **`connectors.kicad_sch`** - Connector definitions
- **`power.kicad_sch`** - Power supply/PoC circuit
- **`gmsl-deserializer.kicad_pcb`** - Complete PCB layout

## Step-by-Step: Add to Your Project

### If you DON'T have a KiCad project yet:

1. **Create new KiCad project:**
   ```
   File → New Project → Save as "Driver-UI-vehicle-system.kicad_pro"
   ```

2. **Add GMSL deserializer as hierarchical sheet:**
   - Place → Hierarchical Sheet
   - Browse to: `gmsl-deserializer\gmsl-deserializer.kicad_sch`
   - Place it on your schematic

3. **Connect to your vehicle system:**
   - Add your vehicle system components
   - Connect to GMSL deserializer inputs/outputs
   - Update power connections

### If you ALREADY have a KiCad project:

1. **Open your existing project**
2. **Add hierarchical sheet:**
   - Place → Hierarchical Sheet
   - Select `gmsl-deserializer\gmsl-deserializer.kicad_sch`
3. **Integrate connections:**
   - Connect your vehicle system to GMSL inputs
   - Connect MIPI CSI-2 outputs to your processing unit

## Important Notes

⚠️ **The GMSL deserializer is INSIDE your project folder:**
- Path: `Driver-UI-vehicle-system\gmsl-deserializer\`
- It's part of your repository
- You can reference it directly from your main KiCad project

⚠️ **Library Dependencies:**
- Make sure all symbol libraries are available
- Check footprint libraries are loaded
- The GMSL project uses standard KiCad libraries

## Verification

To verify files are there:

```powershell
cd C:\Users\Jordan\Documents\GitHub\Driver-UI-vehicle-system
Get-ChildItem .\gmsl-deserializer -Filter *.kicad* | Select-Object Name
```

You should see:
- `gmsl-deserializer.kicad_sch`
- `gmsl-deserializer.kicad_pcb`
- `deserializer.kicad_sch`
- `connectors.kicad_sch`
- `power.kicad_sch`
- `gmsl-deserializer.kicad_pro`

## Next Steps

1. ✅ Verify files exist (you just did this)
2. Open KiCad
3. Create or open your main project
4. Add GMSL deserializer as hierarchical sheet
5. Design your vehicle system around it




