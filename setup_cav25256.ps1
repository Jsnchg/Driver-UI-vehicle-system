# PowerShell script to set up CAV25256 component in KiCad
# Run this script to download library and add to project

Write-Host "=== CAV25256 KiCad Setup Script ===" -ForegroundColor Green
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

Write-Host "[1/2] Downloading/Creating CAV25256 library..." -ForegroundColor Cyan
& $pythonCmd.Name download_cav25256_library.py

if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Failed to create library!" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "[2/2] Adding library to KiCad project..." -ForegroundColor Cyan
& $pythonCmd.Name add_cav25256_to_kicad.py

if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Failed to add library to project!" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "=== Setup Complete! ===" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Open KiCad" -ForegroundColor White
Write-Host "2. Open your project file" -ForegroundColor White
Write-Host "3. Press 'A' in schematic editor" -ForegroundColor White
Write-Host "4. Search for 'CAV25256'" -ForegroundColor White
Write-Host "5. Place component on schematic" -ForegroundColor White

