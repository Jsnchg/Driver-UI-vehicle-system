# Script to fix hierarchical sheet paths in KiCad schematics
# This script updates broken file paths to use relative paths

param(
    [string]$SchematicFile = "",
    [string]$GmslPath = "gmsl-deserializer"
)

Write-Host "KiCad Hierarchical Sheet Path Fixer" -ForegroundColor Green
Write-Host "====================================" -ForegroundColor Green
Write-Host ""

# Find schematic files if not specified
if ([string]::IsNullOrEmpty($SchematicFile)) {
    $schematics = Get-ChildItem -Filter *.kicad_sch -Recurse | 
        Where-Object { $_.DirectoryName -notlike "*$GmslPath*" }
    
    if ($schematics.Count -eq 0) {
        Write-Host "No schematic files found. Please specify a file with -SchematicFile parameter." -ForegroundColor Yellow
        exit
    }
    
    Write-Host "Found $($schematics.Count) schematic file(s):" -ForegroundColor Cyan
    foreach ($sch in $schematics) {
        Write-Host "  - $($sch.FullName)" -ForegroundColor Gray
    }
    Write-Host ""
    
    $SchematicFile = $schematics[0].FullName
    Write-Host "Using: $SchematicFile" -ForegroundColor Yellow
    Write-Host ""
}

if (-not (Test-Path $SchematicFile)) {
    Write-Host "Error: Schematic file not found: $SchematicFile" -ForegroundColor Red
    exit 1
}

# Get the directory of the schematic file
$schematicDir = Split-Path -Parent $SchematicFile
$gmslFullPath = Join-Path $schematicDir $GmslPath

if (-not (Test-Path $gmslFullPath)) {
    Write-Host "Error: GMSL deserializer path not found: $gmslFullPath" -ForegroundColor Red
    Write-Host "Please ensure the gmsl-deserializer folder exists relative to your schematic." -ForegroundColor Yellow
    exit 1
}

Write-Host "Reading schematic file..." -ForegroundColor Cyan
$content = Get-Content $SchematicFile -Raw

# Find all hierarchical sheet references
$sheetPattern = '\(sheet\s+[^)]+\(file\s+"([^"]+)"'
$matches = [regex]::Matches($content, $sheetPattern)

if ($matches.Count -eq 0) {
    Write-Host "No hierarchical sheets found in schematic." -ForegroundColor Yellow
    exit 0
}

Write-Host "Found $($matches.Count) hierarchical sheet(s)" -ForegroundColor Cyan
Write-Host ""

$modified = $false
$backupFile = "$SchematicFile.backup"

# Create backup
Copy-Item $SchematicFile $backupFile -Force
Write-Host "Backup created: $backupFile" -ForegroundColor Gray
Write-Host ""

foreach ($match in $matches) {
    $fullMatch = $match.Groups[0].Value
    $filePath = $match.Groups[1].Value
    
    Write-Host "Found sheet reference: $filePath" -ForegroundColor Yellow
    
    # Check if it's a GMSL file
    if ($filePath -like "*gmsl-deserializer*" -or 
        $filePath -like "*deserializer*" -or 
        $filePath -like "*connectors*" -or 
        $filePath -like "*power*") {
        
        # Extract just the filename
        $fileName = Split-Path -Leaf $filePath
        
        # Build relative path
        $relativePath = Join-Path $GmslPath $fileName
        
        # Verify file exists
        $fullRelativePath = Join-Path $schematicDir $relativePath
        if (Test-Path $fullRelativePath) {
            Write-Host "  -> Fixing to: $relativePath" -ForegroundColor Green
            
            # Replace in content
            $newMatch = $fullMatch -replace [regex]::Escape($filePath), $relativePath
            $content = $content -replace [regex]::Escape($fullMatch), $newMatch
            $modified = $true
        } else {
            Write-Host "  -> WARNING: File not found at $fullRelativePath" -ForegroundColor Red
        }
    } else {
        Write-Host "  -> Skipping (not a GMSL file)" -ForegroundColor Gray
    }
    Write-Host ""
}

if ($modified) {
    # Write updated content
    Set-Content -Path $SchematicFile -Value $content -NoNewline
    Write-Host "Schematic file updated successfully!" -ForegroundColor Green
    Write-Host "Backup saved at: $backupFile" -ForegroundColor Gray
    Write-Host ""
    Write-Host "Next steps:" -ForegroundColor Cyan
    Write-Host "1. Open the schematic in KiCad" -ForegroundColor White
    Write-Host "2. Verify hierarchical sheets load correctly" -ForegroundColor White
    Write-Host "3. If everything works, you can delete the backup file" -ForegroundColor White
} else {
    Write-Host "No changes needed." -ForegroundColor Yellow
    Remove-Item $backupFile -ErrorAction SilentlyContinue
}



