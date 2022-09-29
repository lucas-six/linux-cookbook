# Virtualization (虚拟化)

## Types of Hypervisor

| Types | Hypervisors | Technologies |
| --- | --- | --- |
| Type-1 | native or bare-metal | KVM, [Xen](https://xenproject.org), Microsoft Hyper-V, VMware ESXi |
| Type-2 | hosted | VMware Workstation, [Oracle VirtualBox](https://www.virtualbox.org) |

![Hosted OS vs Bare-metal Hypervisors](https://leven-cn.github.io/linux-cookbook/imgs/virtualization-hypervisor-types.jpeg)

## Virtualization with Linux

| - | KVM | [Xen](https://xenproject.org) |
| --- | --- | --- |
| Start Year  | 2007, Linux 2.6.20+ | 2003 |
| Future Direction  | Server Virtualization | Desktop Virtualization |
| Cloud Service | AWS (2017+): C5+, Alibaba Cloud, Tencent Cloud | Oracle Cloud, IBM Softlayer |

## KVM (Kernel-based VM)

### Advantage

- Reuse hardware virtualization technologies (**hardware-assistant virtualization**),
such as *Intel VT* and *AMD-V*.
- Reuse software (kernel) virtualization technologies:
*vCPU*, *memory management*, *process schedule*, *I/O controller*, *device drivers*, *networking controllers*.

### vCPU Modes

| - | User Mode | Kernel Mode | Guest Mode |
| --- | --- | --- | --- |
| running | QEMU | KVM kernel module | Guest OS |
| virtualize | I/O: networking and disk storage | CPU and memory | - |

### Memory Virtualization

- Address Mapping
  - Intel EPT (Extend Page Table)
  - AMD NPT (Nested Page Table).
- TLB (Translation Lookaside Buffer)
- Intel VPID (Virtual-Processor Identifier)
- THP (Transparent Hugepage)
- Over-Commit (内存超分)
  1. Swapping (内存交换)
  2. Ballooning (气球): `virtio_balloon` driver
  3. Page Sharing (页共享): KSM (Kernel Samepage Merging)

## References

- [Xen Project](https://xenproject.org)
- [Oracle VM VirtualBox](https://www.virtualbox.org)
