---
layout: post
title: How To Install and Remove Default Apps from Windows Using PowerShell
date: 2023-08-26 8:40:00 -000
tags: [windows, powershell]
categories: [howto]
---

# How To Install and Remove Default Apps from Windows Using PowerShell

## How To Install Apps with PowerShell

1. Open PowerShell as Administrator
1. Get a list of all default Windows apps
```powershell
Get-AppxPackage -AllUsers | Select Name
```
You'll notice there's quite a long list of apps returned
1. Search for an App
Let's filter our search for a specific app. For example, if we wanted to reinstall the Windows Store app, we could find the name of the Windows Store with the following command:
```powershell
Get-AppxPackage -AllUsers | Where-Object { $_.Name -like '*store*' } | Select Name
```
```terminal
Name
----
Microsoft.Services.Store.Engagement
Microsoft.Services.Store.Engagement
Microsoft.StorePurchaseApp
Microsoft.WindowsStore
```
As you can see, the results are much more manageable
1. Reinstall the app using the name we just found
```powershell
Get-AppxPackage -AllUsers Microsoft.WindowsStore | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}
```


## How To Remove Default Apps with Powershell

1. Get a list of installed apps and the package's full name
```powershell
Get-AppxPackage | select Name, PackageFullName | Format-List
```
1. Search through the results 

![Powershell how to use find instruction screenshot](/assets/img/find-powershell.png)
Alternatively, you can hit alt + space then hit "e" and "f" to open the search dialog instead of right-clicking the title bar.
1. Remove the app with the package's full name
```powershell
# Remove the Camera App
Remove-AppxPackage Microsoft.WindowsCamera_2023.2305.4.0_x64__8wekyb3d8bbwe
```
1. Remove multiple apps 
```powershell
# Removes BingWeather, GetHelp and People
"Microsoft.BingWeather", "Microsoft.GetHelp", "Microsoft.People" | ForEach { Get-AppxPackage -Name $_ | Remove-AppxPackage }
```