---
layout: post
title: How To Set a High-Performance Power Profile on Windows
date: 2023-08-21 20:40:00 -0500
tags: [windows, power-management]
categories: [howto]
---

# How To Set a High-Performance Power Profile on Windows

Today, I found myself trying to RDP into a workstation in my HomeLab only to find that a connection could not be established. I looked over at the workstation that I had recently performed a clean install of Windows on to see that there was no HDD indicator LED winking at me like usual. I found this strange and immediately was worried that there was some sort of hardware error with this machine. I hit the power button expecting to see the BIOS show up and was surprised to see that the computer had been in a sleep or hibernation state.

## Setting a High-Performance Power Plan Using the GUI

To Change this in Windows Settings using the GUI, I found that ASUS had a great guide published in their support docs. [Change Power mode and plan](https://www.asus.com/support/FAQ/1044699/)

## Setting a High-Performance Power Plan Using PowerShell


In PowerShell, power plan settings can be set with the *powerconfg* command. To list all current power plans, use:

```powershell
powercfg /list
```

The output will show the <span title="Globally Unique IDentifier">GUID</span> of all available power plans. You can then set the profile with the following command:

```powershell
powercfg /setactive GUID_HERE
```
If you wanted to make sure that the computer always stayed on, like me for my backup server, you'd use these commands: 

```powershell
# Ensure the computer never goes to sleep
powercfg /change /standby-timeout-ac 0

# Ensure the display never turns off
powercfg /change /monitor-timeout-ac 0

# Ensure the hard disk never turns off
powercfg /change /disk-timeout-ac 0

# Explicitly disable hibernation (Optional)
powercfg /hibernate off
```
Now this is cool and all, but it seems like a lot of typing, how could we just run this as a PowerShell script?

```powershell
# Create a variable to store the GUID in, filter out the GUID to set with powercfg
$highPerformanceSchemeGuid = (powercfg /list | Where-Object { $_ -match "High performance" } | ForEach-Object { if ($_ -match "([a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12})") { $matches[1] } })

# Set the power scheme to High Performance
powercfg /setactive $highPerformanceSchemeGuid

# Ensure the computer never goes to sleep
powercfg /change /standby-timeout-ac 0

# Ensure the display never turns off
powercfg /change /monitor-timeout-ac 0

# Ensure the hard disk never turns off
powercfg /change /disk-timeout-ac 0

# Disable hibernation
powercfg /hibernate off
```

> You'll need to run this script in an Administrator PowerShell and will need to [allow scripts to be executed](../_posts/2023-08-26-running-ps-scripts.md) on the machine
{: .prompt-tip }
