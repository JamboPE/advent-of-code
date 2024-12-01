# Advent of Code 2024 Day 1 Part A
$firstList = @()
$secondList = @()
$fileInput = Get-Content -Path "2024/Day 1/input" -Delimiter "`n"
for ($i = 0; $i -lt $fileInput.Length; $i++) {
    $line = $fileInput[$i] -replace "`n", ""
    $line = $line -split "   "
    $firstList += $line[0]
    $secondList += $line[1]
}
$firstList = $firstList | Sort-Object
$secondList = $secondList | Sort-Object

# Part 1
$total = 0
for ($i = 0; $i -lt $firstList.Length; $i++) {
    $first = $firstList[$i]
    $second = $secondList[$i]
    $diff = [Math]::Abs($first - $second)
    $total += $diff
}
Write-Host "[Part 1] Total: $total"

# Part 2
$total = 0
$firstList | ForEach-Object {
    $simNum = 0
    $first = $_
    $secondList | ForEach-Object {
        $second = $_
        if ($first - $second -eq 0) {
            $simNum += 1
        }
    }
    $total += $simNum * $first
}
Write-Host "[Part 2] Total: $total"