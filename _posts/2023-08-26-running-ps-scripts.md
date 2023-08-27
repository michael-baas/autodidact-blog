---
layout: post
title: How To Enable PowerShell Scripts
date: 2023-08-26 09:40:00 -0000
tags: [windows, power-management]
categories: [howto]
---

# How to Enable PowerShell Scripts

Windows PowerShell has a safety feature called Execution Policies. Execution Policies are used to prevent malicious scripts and configurations from being executed on a machine by default. Execution Policies can be controlled in Windows for a local computer, current user or particular session. Group Policy can also be used to set execution policies for computers and users [^1]

There are several policy levels you can set:

1. Restricted (default): No scripts can be run, including those you write.
1. AllSigned: Only scripts that are signed by a trusted publisher can be run.
1. RemoteSigned: Scripts written on the local computer don't need to be signed. However, scripts downloaded from the internet (or received in email or via messaging) need to be signed by a trusted publisher before they can run.
1. Unrestricted: Any script can run, regardless of where it originates. If the script is downloaded from the internet, you'll still be prompted to confirm you want to run it.
1. Bypass: Nothing is blocked, and there are no warnings or prompts.
1. Undefined: Removes the currently assigned execution policy from the current scope. This means that the system will use the execution policy set at a wider scope.


[^1]: [Microsoft Learn](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.3)