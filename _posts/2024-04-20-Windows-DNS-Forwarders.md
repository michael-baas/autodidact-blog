---
layout: post
title: "Windows Server DNS Forwarders"
date: 2024-04-20
tags: [Windows Server, DNS]
categories: [howto]
---

## Why are DNS Forwarders needed?

I recently created a VM of Windows Sever 2022 and setup a DNS server. I
was a little confused when clients weren't able to reach the internet.
The reason for this is there aren't any external IP address tables in
our DNS sever. To fix this we can set up forwarders. According to the
dialog box, "Forwarders are DNS servers that this server can use to
resolve DNS queries for records this server cannot resolve". In my case
this was anything outside of the local domain network.

## How to add DNS Forwarders in Windows Server

First you'll need to open DNS Manager. Next, right click on the server you'd like to set up DNS forwarders from and select properties, as shown below.

![DNS Manager properties](/assets/img/dns-manager.png)


Next you need to select the "Forwarders" tab in the properties dialog
box.

![DNS Manager select forwarders](/assets/img/dns-add-forwarders.png)

Add the IP address(es) of DNS servers to forward to. You will know the server has been taken successfully if you see the green check mark in the Validated column.

![DNS add IP](/assets/img/dns-forwarders-ip.png)

Finally, hit "Apply" to finalize the settings. 

![Apply Settings](/assets/img/dns-apply-settings.png)
