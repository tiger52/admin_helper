# Proxmox Ceph remove OSD – How to do it via Proxmox VE GUI and CLI?

by Keerthi PS | Jan 10, 2020

Are you looking for how to remove Proxmox Ceph OSD? We can help you with it.

Usually, we can do this via both Proxmox VE GUI and CLI. But before just removing the OSD, its status must be out and down.

At Bobcares, we often get requests to manage Proxmox Ceph storage, as a part of our Infrastructure Management Services.

Today, let’s see how our Support Engineers remove OSD from Proxmox Ceph.

 
## Integration of Proxmox with Ceph

Proxmox Virtual Environment is an open-source server virtualization environment.

Whereas Ceph is an open-source software-defined storage platform. This distributed object store and file system provide excellent performance, reliability, and scalability.

By integrating Ceph with Proxmox VE, we can run and manage Ceph storage directly on the hypervisor nodes.

The object storage daemon for the Ceph distributed file system is ceph-osd. In addition, it stores objects on a local file system and provides access to them over the network.

 
## How to remove Ceph OSD in Proxmox?

Before removing the OSD directly, one factor our Support Engineers consider is the status of OSD in the cluster. Usually, the OSD is ‘in’ and ‘up’ in the cluster.

So, let’s see how to remove it via the Proxmox VE GUI and from the command line.

 
### Remove Ceph OSD via Proxmox GUI

Now, let’s see how our Support Engineers remove the OSD via GUI.

1. Firstly, we select the Proxmox VE node in the tree.

2. Next, we go to **Ceph >> OSD panel**. Then we select the OSD to remove. And click the **OUT** button.

3. When the status is *OUT*, we click the **STOP** button. This changes the status from *up* to *down*.

4. Finally, we select the **More** drop-down and click **Destroy**.

Hence, this successfully removes the OSD.

 
### Remove Ceph OSD via CLI

Similarly, we can remove Ceph OSD via CLI. Here are the steps our Support Engineers follow to do remove OSD from the cluster.

1. Initially, we need to take it out of the cluster. We do this to copy data to other OSDs. For this, we use the command,

```
ceph osd out {osd-num}
```

2. Now the cluster starts to migrate the data to other OSDs. To observe it we use the command,

```
ceph -w
```

Here we carefully, observe the status showing up. When the migration completes we exit this window.

3. Then we stop the OSD before removing it. Here we ssh into the host and use the command,

```
sudo systemctl stop ceph-osd@{osd-num}
```

Now the OSD is down.

4. We cannot simply remove the OSD. First, we need to remove the OSD authentication key. Also, we remove the OSD from the OSD map, and from the ceph.conf file placed in */etc/ceph* path.

So to remove the OSD from the CRUSH map we use the command,

```
ceph osd crush remove {name}
```

And, to remove OSD auth key, we use the command,
```
ceph auth del osd.{osd-num}
```

Then to remove OSD, we run,
```
ceph osd rm {osd-num}
```

#for example
```
ceph osd rm 1
```

5. Finally, we remove the OSD entry from *ceph.conf*. For this, we ssh into the admin host and open the file */etc/ceph/ceph.conf*. And remove the entry which appears as,

Proxmox Ceph remove OSD.
```
[osd.1]
    host = {hostname}
```

Later, we update the same in all other hosts in the cluster.

 
## Conclusion

So far we saw steps to remove Proxmox Ceph OSD. Usually, we do this via both Proxmox VE GUI and command-line interface. Today, we saw how our Support Engineers remove it without any error.
