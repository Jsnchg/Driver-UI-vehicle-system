# Quick fix for hierarchical sheet errors
# This script finds and fixes broken hierarchical sheet paths

Write-Host "=== KiCad Hierarchical Sheet Fixer ===" -ForegroundColor Green
Write-Host ""

# Find all KiCad schematic files (excluding gmsl-deserializer folder)
$schematics = Get-ChildItem -Filter *.kicad_sch -Recurse | 
    Where-Object { $_.DirectoryName -notlike "*gmsl-deserializer*" -and $_.Name -notlike "*gmsl*" }

if ($schematics.Count -eq 0) {
    Write-Host "No main schematic files found." -ForegroundColor Yellow
    Write-Host "Please make sure you have a KiCad project in this directory." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Current directory: $(Get-Location)" -ForegroundColor Gray
    Write-Host ""
    Write-Host "TIP: If you haven't created a KiCad project yet, you need to:" -ForegroundColor Cyan
    Write-Host "1. Open KiCad" -ForegroundColor White
    Write-Host "2. Create a new project or open existing one" -ForegroundColor White
    Write-Host "3. Add hierarchical sheets pointing to gmsl-deserializer files" -ForegroundColor White
    exit
}

Write-Host "Found $($schematics.Count) schematic file(s):" -ForegroundColor Cyan
foreach ($sch in $schematics) {
    Write-Host "  - $($sch.Name) in $($sch.DirectoryName)" -ForegroundColor Gray
}
Write-Host ""

# Process each schematic
foreach ($schematic in $schematics) {
    Write-Host "Processing: $($schematic.Name)" -ForegroundColor Yellow
    
    $content = Get-Content $schematic.FullName -Raw
    $schematicDir = $schematic.DirectoryName
    $modified = $false
    
    # Pattern to find hierarchical sheets with file paths
    $pattern = '\(sheet[^)]+\(file\s+"([^"]+)"'
    $matches = [regex]::Matches($content, $pattern)
    
    if ($matches.Count -eq 0) {
        Write-Host "  No hierarchical sheets found." -ForegroundColor Gray
        continue
    }
    
    Write-Host "  Found $($matches.Count) hierarchical sheet(s)" -ForegroundColor Cyan
    
    # Create backup
    $backupFile = "$($schematic.FullName).backup"
    Copy-Item $schematic.FullName $backupFile -Force
    Write-Host "  Backup created: $($schematic.Name).backup" -ForegroundColor Gray
    
    foreach ($match in $matches) {
        $fullMatch = $match.Groups[0].Value
        $filePath = $match.Groups[1].Value
        
        Write-Host "  Checking: $filePath" -ForegroundColor Gray
        
        # Check if it's a GMSL file
        $isGmslFile = $filePath -like "*gmsl*" -or 
                     $filePath -like "*deserializer*" -or 
                     $filePath -like "*connectors*" -or 
                     $filePath -like "*power*"
        
        if ($isGmslFile) {
            # Extract filename
            $fileName = Split-Path -Leaf $filePath
            
            # Build correct relative path
            $relativePath = "gmsl-deserializer\$fileName"
            
            # Check if file exists
            $fullPath = Join-Path $schematicDir $relativePath
            if (Test-Path $fullPath) {
                Write-Host "    -> Fixing to: $relativePath" -ForegroundColor Green
                
                # Replace the path in the content
                $newMatch = $fullMatch -replace [regex]::Escape($filePath), $relativePath
                $content = $content -replace [regex]::Escape($fullMatch), $newMatch
                $modified = $true
            } else {
                Write-Host "    -> WARNING: File not found at $fullPath" -ForegroundColor Red
            }
        } else {
            Write-Host "    -> Skipping (not a GMSL file)" -ForegroundColor Gray
        }
    }
    
    if ($modified) {
        # Write updated content
        Set-Content -Path $schematic.FullName -Value $content -NoNewline
        Write-Host "  Fixed!" -ForegroundColor Green
    } else {
        Write-Host "  No changes needed." -ForegroundColor Gray
        Remove-Item $backupFile -ErrorAction SilentlyContinue
    }
    Write-Host ""
}

Write-Host "=== Done ===" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Open your KiCad project" -ForegroundColor White
Write-Host "2. The hierarchical sheets should now load correctly" -ForegroundColor White
Write-Host "3. If everything works, you can delete the .backup files" -ForegroundColor White
