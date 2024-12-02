# Advent of Code 2024 Day 2
$fileInput = Get-Content -Path "2024/Day 2/dev_input" -Delimiter "`n"
data = @()
for ($i = 0; $i -lt $fileInput.Length; $i++) {
    $line = $fileInput[$i] -replace "`n", ""
    $line = $line -split " "
    $data += $line
}
Write-Host $data