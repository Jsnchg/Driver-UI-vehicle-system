# Clear KiCad Cache to Force Library Reload
# This will force KiCad to reload all libraries on next startup

Write-Host "=== Clearing KiCad Cache ===" -ForegroundColor Cyan
Write-Host ""

$cachePath = "$env:APPDATA\kicad\9.0\cache"

if (Test-Path $cachePath) {
    Write-Host "Found cache directory: $cachePath" -ForegroundColor Yellow
    
    try {
        Remove-Item "$cachePath\*" -Recurse -Force -ErrorAction Stop
        Write-Host "[OK] Cache cleared successfully!" -ForegroundColor Green
        Write-Host ""
        Write-Host "Next steps:" -ForegroundColor Cyan
        Write-Host "1. Close KiCad completely (if open)" -ForegroundColor White
        Write-Host "2. Reopen KiCad" -ForegroundColor White
        Write-Host "3. Open your project" -ForegroundColor White
        Write-Host "4. Press A in schematic editor" -ForegroundColor White
        Write-Host "5. Search for DS92LV16" -ForegroundColor White
        Write-Host ""
        Write-Host "The library should reload and DS92LV16 should appear!" -ForegroundColor Green
    } catch {
        Write-Host "[ERROR] Could not clear cache: $_" -ForegroundColor Red
        Write-Host "Try closing KiCad first, then run this script again" -ForegroundColor Yellow
    }
} else {
    Write-Host "[INFO] Cache directory not found: $cachePath" -ForegroundColor Yellow
    Write-Host "This might be your first time using KiCad, or cache is already cleared" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Try:" -ForegroundColor Cyan
    Write-Host "1. Open KiCad" -ForegroundColor White
    Write-Host "2. Tools → Symbol Editor" -ForegroundColor White
    Write-Host "3. File → Open Library" -ForegroundColor White
    Write-Host "4. Navigate to: lib\custom_components.kicad_sym" -ForegroundColor White
    Write-Host "5. Verify DS92LV16 is in the list" -ForegroundColor White
}

Write-Host ""
Write-Host "Press any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

