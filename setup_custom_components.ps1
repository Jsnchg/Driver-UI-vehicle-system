# PowerShell script to set up custom components (CAV25256, NCV97200, etc.) in KiCad
# Run this script to verify libraries and add to project

Write-Host "=== Custom Components KiCad Setup Script ===" -ForegroundColor Green
Write-Host ""

# Check if Python is available
$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCmd) {
    $pythonCmd = Get-Command python3 -ErrorAction SilentlyContinue
}

if (-not $pythonCmd) {
    Write-Host "[ERROR] Python not found!" -ForegroundColor Red
    Write-Host "Please install Python 3 to continue." -ForegroundColor Yellow
    exit 1
}

Write-Host "[1/2] Verifying custom component libraries..." -ForegroundColor Cyan
& $pythonCmd.Name download_custom_libraries.py

if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Failed to verify libraries!" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "[2/2] Adding libraries to KiCad project..." -ForegroundColor Cyan
& $pythonCmd.Name add_custom_components_to_kicad.py

if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Failed to add libraries to project!" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "=== Setup Complete! ===" -ForegroundColor Green
Write-Host ""
Write-Host "Available components:" -ForegroundColor Cyan
Write-Host "  - CAV25256 (Capacitor)" -ForegroundColor White
Write-Host "  - NCV97200 (IC)" -ForegroundColor White
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Open KiCad" -ForegroundColor White
Write-Host "2. Open your project file" -ForegroundColor White
Write-Host "3. Press 'A' in schematic editor" -ForegroundColor White
Write-Host "4. Search for 'CAV25256' or 'NCV97200'" -ForegroundColor White
Write-Host "5. Or use: 'custom_components:CAV25256'" -ForegroundColor White
Write-Host "6. Place component on schematic" -ForegroundColor White
Write-Host ""
Write-Host "[NOTE] If components don't appear, add library through:" -ForegroundColor Yellow
Write-Host "       Preferences -> Manage Symbol Libraries" -ForegroundColor Yellow

