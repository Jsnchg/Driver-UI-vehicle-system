# GMSL Deserializer - Assembly Options

## What You Have

You have the **open hardware design files** (KiCad schematics and PCB layouts) for the GMSL Deserializer board. This is a **design**, not a finished product.

## Your Options

### Option 1: Use as Reference Design (Recommended for Integration)

**What it means:** Use the GMSL deserializer design as a reference or starting point for your own vehicle system design.

**What to do:**
- Study the schematics to understand the circuit
- Copy/modify the parts you need into your own design
- Integrate the GMSL functionality into your main Driver-UI vehicle system board
- Design your own PCB that includes GMSL deserializer functionality

**Best for:** Custom vehicle system design

### Option 2: Have PCB Manufactured

**What it means:** Send the PCB design files to a PCB manufacturer to get physical boards made.

**Steps:**
1. **Generate manufacturing files from KiCad:**
   - Open `gmsl-deserializer.kicad_pcb` in KiCad
   - File → Fabrication Outputs → Gerbers
   - Generate drill files
   - Generate BOM (Bill of Materials)

2. **Order PCBs from a fab house:**
   - JLCPCB (jlcpcb.com) - Popular, affordable
   - PCBWay (pcbway.com)
   - OSH Park (oshpark.com) - Good for prototypes
   - Eurocircuits, etc.

3. **Order components:**
   - Use the BOM (Bill of Materials) from the design
   - Order from Digikey, Mouser, LCSC, etc.

4. **Assemble yourself:**
   - Solder components (requires SMD soldering skills)
   - Or use assembly service from fab house

**Best for:** If you need the exact GMSL deserializer board as designed

### Option 3: Buy Pre-Assembled Board (If Available)

**What it means:** Check if Antmicro or distributors sell pre-assembled boards.

**Where to check:**
- Antmicro website/store
- Open Hardware Portal
- Electronics distributors
- Contact Antmicro directly

**Best for:** Quick prototyping, no assembly needed

### Option 4: Integrate into Your Design

**What it means:** Take the GMSL deserializer circuit and integrate it directly into your Driver-UI vehicle system board.

**Steps:**
1. Open your main vehicle system KiCad project
2. Add GMSL deserializer as hierarchical sheet (we did this)
3. Design your main board to include both:
   - Your vehicle system components
   - GMSL deserializer circuit
4. Have one unified PCB manufactured

**Best for:** Integrated vehicle system design

## What Most People Do

For a **Driver-UI vehicle system**, you typically want to:

1. **Integrate the GMSL functionality** into your main vehicle system board
2. **Not build a separate GMSL board** - combine everything into one design
3. **Use the GMSL schematics as reference** to understand:
   - How to connect GMSL cameras
   - What components are needed
   - How the PoC (Power over Coax) circuit works
   - How to interface with MIPI CSI-2

## Recommended Approach for Your Project

Since you're building a **Driver-UI vehicle system**, I recommend:

### Step 1: Study the Design
- Open the GMSL deserializer schematics in KiCad
- Understand the circuit topology
- Note key components and their values

### Step 2: Integrate into Your Design
- Add the GMSL deserializer circuit to your main vehicle system schematic
- Modify as needed for your specific requirements
- Design your unified PCB layout

### Step 3: Manufacture Your Combined Board
- Generate Gerbers from your integrated design
- Order PCBs
- Order components
- Assemble (or use assembly service)

## Cost Estimate

If you manufacture the GMSL deserializer board separately:
- **PCBs:** $20-100 (depending on quantity, typically 5-10 boards minimum)
- **Components:** $50-200 (depending on where you source)
- **Assembly:** $100-500 (if you use assembly service) or free if you DIY
- **Total:** ~$170-800 for first batch

If you integrate into your main board:
- Same PCB cost, but you get everything on one board
- More efficient, fewer interconnects

## Skills Needed

**To assemble yourself:**
- SMD soldering skills (0402, QFN packages)
- Reflow oven or hot air station
- Component sourcing and BOM management
- Testing and debugging

**If using assembly service:**
- Just need to provide Gerbers and BOM
- They handle everything
- More expensive but less work

## Next Steps

1. **Decide your approach:**
   - [ ] Use as reference only
   - [ ] Manufacture separate GMSL board
   - [ ] Integrate into main vehicle system board
   - [ ] Buy pre-assembled (if available)

2. **If manufacturing:**
   - Generate manufacturing files from KiCad
   - Choose PCB fab house
   - Order components
   - Plan assembly

3. **If integrating:**
   - Fix hierarchical sheet paths (use the fix script)
   - Design your integrated board
   - Manufacture combined design

## Questions to Ask Yourself

- Do I need a separate GMSL board, or can I integrate it?
- Do I have the skills to assemble SMD boards?
- What's my budget for prototyping?
- How many boards do I need?
- Do I want to modify the design or use it as-is?

## Resources

- [KiCad Manufacturing Tutorial](https://docs.kicad.org/)
- [JLCPCB Ordering Guide](https://jlcpcb.com/)
- [SMD Soldering Guide](https://www.sparkfun.com/tutorials/36)
- Contact Antmicro for commercial inquiries



