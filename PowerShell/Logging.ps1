

$scriptName = $MyInvocation.MyCommand.Name # Gets the name of the script


$scriptName = $scriptName.Split('.')[0] # Takes the end of the script .ps1

$runtime = (get-date -Format 'hh-mm-dd-MM-yyyy') # Gets the date
$currentPath = (Get-Location).Path
$logfile = "$currentPath\" + "$scriptName" + "-" + "$runtime" + '.txt' # Creates the file
Write-Host ""
Write-Host "Logging..."
Write-Host ""
Write-Host ""
Start-Transcript -Path $logfile # Logs into the file
Write-Host ""
Write-Host ""