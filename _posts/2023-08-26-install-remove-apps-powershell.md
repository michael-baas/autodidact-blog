---
layout: post
title: How To Install and Remove Default Apps from Windows Using PowerShell
date: 2023-08-26 8:40:00 -0500
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
1. Search for an App
Let's filter our search for a specific app. For example, if we wanted to reinstall the Windows Store app, we could find the name of the Windows Store with the following command:
```powershell
Get-AppxPackage -AllUsers | Where-Object { $_.Name -like '*store*' } | Select Name
```

```terminal
Name
----
1527c705-839a-4832-9118-54d4Bd6a0c89
c5e2524a-ea46-4f67-841f-6a9465d9d515
E2A4F912-2574-4A75-9BB0-0D023378592B
F46D4000-FD22-4DB4-AC8E-4E1DDDE828FE
Microsoft.AAD.BrokerPlugin
Microsoft.AccountsControl
Microsoft.AsyncTextService
Microsoft.BioEnrollment
Microsoft.CredDialogHost
Microsoft.ECApp
Microsoft.LockApp
Microsoft.MicrosoftEdgeDevToolsClient
Microsoft.MicrosoftEdge
Microsoft.Win32WebViewHost
Microsoft.Windows.Apprep.ChxApp
Microsoft.Windows.AssignedAccessLockApp
Microsoft.Windows.CallingShellApp
Microsoft.Windows.CapturePicker
Microsoft.Windows.ContentDeliveryManager
Microsoft.Windows.NarratorQuickStart
Microsoft.Windows.OOBENetworkCaptivePortal
Microsoft.Windows.OOBENetworkConnectionFlow
Microsoft.Windows.ParentalControls
Microsoft.Windows.PeopleExperienceHost
Microsoft.Windows.PinningConfirmationDialog
Microsoft.Windows.SecHealthUI
Microsoft.Windows.SecureAssessmentBrowser
Microsoft.Windows.ShellExperienceHost
Microsoft.Windows.StartMenuExperienceHost
Microsoft.Windows.XGpuEjectDialog
Microsoft.XboxGameCallableUI
MicrosoftWindows.UndockedDevKit
NcsiUwpApp
Windows.CBSPreview
windows.immersivecontrolpanel
Windows.PrintDialog
Microsoft.Services.Store.Engagement
Microsoft.Services.Store.Engagement
Microsoft.UI.Xaml.2.0
Microsoft.NET.Native.Runtime.2.2
Microsoft.NET.Native.Framework.2.2
Microsoft.Advertising.Xaml
Microsoft.Wallet
Microsoft.MicrosoftEdge.Stable
Microsoft.VCLibs.140.00
Microsoft.VCLibs.140.00
Microsoft.NET.Native.Runtime.2.2
Microsoft.NET.Native.Runtime.2.2
Microsoft.XboxSpeechToTextOverlay
Microsoft.XboxGameOverlay
Microsoft.NET.Native.Framework.2.2
Microsoft.NET.Native.Framework.2.2
Microsoft.MixedReality.Portal
Microsoft.XboxIdentityProvider
Microsoft.WindowsCalculator
Microsoft.GetHelp
Microsoft.VCLibs.140.00.UWPDesktop
Microsoft.WindowsFeedbackHub
Microsoft.VCLibs.140.00.UWPDesktop
Microsoft.UI.Xaml.2.8
Microsoft.UI.Xaml.2.8
Microsoft.UI.Xaml.2.3
Microsoft.UI.Xaml.2.3
Microsoft.UI.Xaml.2.7
Microsoft.UI.Xaml.2.7
Microsoft.WindowsSoundRecorder
Microsoft.People
Microsoft.Windows.Search
Microsoft.Windows.CloudExperienceHost
MicrosoftWindows.Client.CBS
Microsoft.MicrosoftSolitaireCollection
Microsoft.MicrosoftOfficeHub
microsoft.windowscommunicationsapps
Microsoft.Windows.Photos
Microsoft.WindowsMaps
Microsoft.Getstarted
Microsoft.BingWeather
Microsoft.MicrosoftStickyNotes
Microsoft.Office.OneNote
Microsoft.UI.Xaml.2.0
Microsoft.MSPaint
Microsoft.NET.Native.Framework.1.7
Microsoft.NET.Native.Framework.1.7
Microsoft.NET.Native.Runtime.1.7
Microsoft.NET.Native.Runtime.1.7
Microsoft.HEIFImageExtension
Microsoft.XboxApp
Microsoft.WebpImageExtension
Microsoft.549981C3F5F10
Microsoft.DesktopAppInstaller
Microsoft.WindowsCamera
Microsoft.XboxGamingOverlay
Microsoft.Microsoft3DViewer
Microsoft.UI.Xaml.2.4
Microsoft.UI.Xaml.2.4
Microsoft.ScreenSketch
Microsoft.WindowsAlarms
Microsoft.StorePurchaseApp
Microsoft.WindowsStore
Microsoft.SkypeApp
Microsoft.Xbox.TCUI
Microsoft.ZuneMusic
Microsoft.VP9VideoExtensions
Microsoft.WindowsAppRuntime.1.3
Microsoft.WindowsAppRuntime.1.3
Microsoft.WebMediaExtensions
Microsoft.YourPhone
Microsoft.WindowsAppRuntime.1.2
Microsoft.WindowsAppRuntime.1.2
Microsoft.ZuneVideo
Microsoft.Winget.Source
```



1. Reinstall the app with the following command
```powershell
Get-AppxPackage -AllUsers *c
```