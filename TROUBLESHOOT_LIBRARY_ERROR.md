# Troubleshooting Library Loading Error

## Current Status

The library file `lib/custom_components.kicad_sym` appears to be syntactically correct:
- ✅ File structure is valid
- ✅ Parentheses are balanced (3854 open, 3854 close)
- ✅ Quotes are balanced (1544 quotes)
- ✅ All 29 symbols are properly defined
- ✅ No obvious syntax errors found

However, KiCad is reporting: **"Symbol library 'custom_components' failed to load"**

## Get the Exact Error Message

To find the exact problem:

1. **Open KiCad**
2. **Tools → Symbol Editor**
3. **File → Open Library**
4. **Navigate to**: `lib/custom_components.kicad_sym`
5. **Select it and click Open**
6. **KiCad will show the EXACT error message and line number**

This will tell us exactly what's wrong!

## Common Issues That Cause This Error

### 1. Invalid Characters in Pin Names
- **Fixed**: Removed brackets from pin names (D[15:0] → D15-0)
- **Status**: ✅ Fixed

### 2. Invalid Pin Numbers
- **Check**: All pin numbers should be numeric or "EP" for exposed pads
- **Status**: ✅ Verified

### 3. Malformed Property Values
- **Check**: Property values should be properly quoted
- **Status**: ✅ Verified

### 4. Missing Unit Symbols
- **Check**: Each symbol needs a unit symbol (e.g., SYMBOLNAME_0_1)
- **Status**: ✅ Verified

### 5. File Encoding Issues
- **Check**: File should be UTF-8 encoded
- **Status**: ✅ Verified

### 6. KiCad Version Compatibility
- **Check**: Library format version is 20220914 (KiCad 6.0+)
- **Status**: ✅ Compatible

## Testing Steps

### Step 1: Test Without DS92LV16

If DS92LV16 is causing the issue, we can temporarily remove it:

1. Backup the library file
2. Remove DS92LV16 symbol
3. Try loading in KiCad
4. If it loads, DS92LV16 has an issue
5. If it still fails, the issue is elsewhere

### Step 2: Test Individual Symbols

Try loading symbols one at a time to find which one causes the error.

### Step 3: Check KiCad Error Log

KiCad may have an error log file:
- Windows: `%APPDATA%\kicad\9.0\kicad.log`
- Check for detailed error messages

## Quick Fix: Recreate Library

If all else fails, we can:
1. Create a new library file
2. Add symbols one by one
3. Test after each addition
4. Find which symbol causes the error

## Next Steps

**Please provide:**
1. The EXACT error message from KiCad Symbol Editor
2. The line number (if shown)
3. Your KiCad version

This will help me fix the exact issue!

