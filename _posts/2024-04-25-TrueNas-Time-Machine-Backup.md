---
layout: post
title: "TrueNas Time Machine Backup"
date: 2024-04-25
tags: [backup, time machine]
categories: [howto]
---

## What is TrueNas?

TrueNas is an open-source storage operating system designed to provide reliable and efficient network attached storage (NAS). I will be running TrueNas as a virtual machine in Hyper-V for my time machine backup NAS.

# How Do I use TrueNas to backup my Macbook with Time Machine?

1. Install TrueNas: Instructions on how to install TrueNas can be found [with this link.](https://www.truenas.com/docs/core/gettingstarted/install/)
1. Login to the Web GUI: Instruction on how to login to the web GUI can be found [with this link.](https://www.truenas.com/docs/core/gettingstarted/loggingin/)
1. Create a Storage Pool: Instruction on how to create a storage pool can be found [with this link](https://www.truenas.com/docs/core/coretutorials/storage/pools/)
1. Now we must create a SMB share for the Time Machine backup.
    1. Click on the three dots next to Windows (SMB) Shares
    1. Click Advanced settings
    1. Click the checkbox for "Enable Apple SMB2/3 protocol Extensions"
    1. Save settings
    1. Go to Sharing
    1. Windows (SMB) Shares Add
    1. Select the path of the Storage Pool that was just made. In the Purpose* dropdown, select "Multiuser Time Machine share"
    1. Add a Description if you'd like
    1. Select Advanced Options
    1. Under Other Options select Time Machine
    1. Save
  1.  A dialog box Asking If you want to start the SMB Service will appear, select "Enable Service"
1. Create a user account to connect to the SMB share
    1. Go to Credentials in the side menu
    1. Local Users
    1. Select the Add button in the Users page
    1. Create a Username and Password
    1. Ensure "Samaba Authentication" is checked
    1. Save
    

