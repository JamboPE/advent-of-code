# Advent of Code 2024 Day 

# Part 1
#$fileInput = Get-Content -Path "2024/Day 2/dev_input" -Delimiter "`n"
$fileInput = Get-Content -Path "2024/Day 2/input" -Delimiter "`n"
$safe = 0
for ($i = 0; $i -lt $fileInput.Length; $i++) { # Each line
    $line = $fileInput[$i] -replace "`n", ""
    $line = $line -split " "
    $decending = $false
    $ascending = $false
    for ($j = 1; $j -lt $line.Length; $j++) { # Each number
        if ([Math]::Abs($line[$j-1] - $line[$j]) -gt 3) {
            break
        }
        if ($line[$j-1] - $line[$j] -lt 0) {
            if ($decending) {
                break
            } else {
                $ascending = $true
            }
        }
        if ($line[$j-1] - $line[$j] -gt 0) {
            if ($ascending) {
                break
            } else {
                $decending = $true
            }
        }
        if ($line[$j-1] - $line[$j] -eq 0) {
            break
        }
        if ($j -eq $line.Length - 1) {
            $safe += 1
        }
    }
}
Write-Host "[Part 1] Safe: $safe"


# Part 2
$fileInput = Get-Content -Path "2024/Day 2/dev_input" -Delimiter "`n"
#$fileInput = Get-Content -Path "2024/Day 2/input" -Delimiter "`n"

function Get-Subsets {
    param (
        $inputArray
    )
    $subsets = @($inputArray)
}

$safe = 0
for ($i = 0; $i -lt $fileInput.Length; $i++) { # Each line
    $line = $fileInput[$i] -replace "`n", ""
    $line = $line -split " "
    $decending = $false
    $ascending = $false
    for ($j = 1; $j -lt $line.Length; $j++) { # Each number
        if ([Math]::Abs($line[$j-1] - $line[$j]) -gt 3) {
            break
        }
        if ($line[$j-1] - $line[$j] -lt 0) {
            if ($decending) {
                break
            } else {
                $ascending = $true
            }
        }
        if ($line[$j-1] - $line[$j] -gt 0) {
            if ($ascending) {
                break
            } else {
                $decending = $true
            }
        }
        if ($line[$j-1] - $line[$j] -eq 0) {
            break
        }
        if ($j -eq $line.Length - 1) {
            $safe += 1
        }
    }
}
Write-Host "[Part 2] Safe: $safe"