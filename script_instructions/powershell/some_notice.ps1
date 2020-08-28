# commands like grep
# native PS
ipconfig.exe | Select-String "IPv4"
# like in cmd
ipconfig.exe | findstr "IPv4"

# If a command in PowerShell returns some objects, before parsing, they should be converted to strings using the Out-String -Stream command:
Get-Alias | Out-String -Stream | Select-String "curl"

# The following PowerShell code sample retrieves additional information about the logical local disks. Should be updated
Write-Host "Drive information for $env:ComputerName"
Get-WmiObject -Class Win32_LogicalDisk |
    Where-Object {$_.DriveType -ne 5} |
    Sort-Object -Property Name | 
    Select-Object Name, VolumeName, FileSystem, Description, VolumeDirty, `
        @{"Label"="DiskSize(GB)";"Expression"={"{0:N}" -f ($_.Size/1GB) -as [float]}}, `
        @{"Label"="FreeSpace(GB)";"Expression"={"{0:N}" -f ($_.FreeSpace/1GB) -as [float]}}, `
        @{"Label"="%Free";"Expression"={"{0:N}" -f ($_.FreeSpace/$_.Size*100) -as [float]}} |
    Format-Table -AutoSize

# somthing like du -hs; it seems need updated too
gci . | %{$f=$_; gci -r $_.FullName| measure-object -property length -sum | select  @{Name="Name"; Expression={$f}} , @{Name="Sum (MB)"; Expression={  "{0:N3}" -f ($_.sum / 1MB) }}, Sum } | sort Sum -desc | format-table -Property Name,"Sum (MB)", Sum -autosize
