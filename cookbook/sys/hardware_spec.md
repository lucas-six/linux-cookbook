# Hardware Specification

## CPU

### Use Cases

| Use Cases | Products |
| --- | -- |
| Desktop (桌面级) | Intel Core i3-i9, AMD |
| Server (服务器) | Intel Xeon |
| Embbed (嵌入式), also called `MCU` | ARM Ax |

### Performance

- **CPU Clock Speed** (CPU主频, GHz)
- **Memory-Bus Speed** (内存总线速度)
- **Cores** (核心数)
- **Threads** (线程数)
- **Chip Process** (芯片制程工艺, nm): *14*, *7*

### Command Line

```bash
cat /proc/cpuinfo
```

## Memory (SDRAM)

### Performance

- Architecture: *DDR4*, *DDR5*
- Maximum Capacity (容量)
- Channel (通道): 2 > 4 > 1
- Clock Frequency (频率)

### Command Line

```bash
dmidecode -t memory

cat /proc/meminfo
```

## References

- [CPU 性能天梯图](https://www.mydrivers.com/zhuanti/tianti/cpu/index.html)
