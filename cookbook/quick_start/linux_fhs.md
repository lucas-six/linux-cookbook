# Filesystem Hierarchy Standard (FHS)

![Linux FHS](https://leven-cn.github.io/linux-cookbook/imgs/Linux-FHS.png)

- `/root`: root directory.
- `/home`: user home directory.
- `/etc`: contains all of the system-wide configuration files.
- `/bin`: contains binaries (programs).
- `/lib`: contains shared library files used by the core system programs.
- `/sbin`: contains “system” binaries.
- `/usr`: contains all the programs and support files used by regular users.
- `/boot`: contains the Linux kernel, initial RAM disk image (for drivers needed at boot time),
and the boot loader.
- `/dev`: contains device nodes.
- `/var`: variable files, such as logs.
- `/var/log`: contains log files.
- `/tmp`: temporary files, emptied each time when the system is rebooted.
- `/var/tmp`: same with `/tmp`.
- `/media`: mount points.
- `/mnt`: use `/media` instead.
- `/run`: runtime data, such as pid files.
- `/var/run`: use `/run` instead (FHS 3.0).
- `/proc`: contains process and kernel information. `procfs` mounted.

![Linux Common Filesystem Hierarchy](https://leven-cn.github.io/linux-cookbook/imgs/Linux-filesystem-hierarchy.jpg)
