# Process

A **process** represents a running program.
It’s the abstraction through which memory,
processor time, and I/O resources can be managed and monitored.

> "On a UNIX/Linux system, everything is a file; if not, it is a process."

A *“thread”* is an execution context within a process.
Every process has at least one thread, but some processes have many.
Each thread has its own stack and CPU context
but operates within the address space of its enclosing process.

## Components

- **virtual address space**
- status: RUNNABLE, STOP, SLEEP
- id: **pid**, **ppid**
- owner & permission: **uid**, **euid**, **gid**, **egid**
- execution priority: **niceness**
- **signal mask**
- **control terminal** (nondaemon)

## Life Cycle

`fork()` -> `exec()` -> `wait()`

## Signals

| signal | number | comment |
| :---: | :---: | :---: |
| `KILL` | `9` | terminate (destroy) process at *kernel* level. *unblocked*, *uncaught*, *unignored* |
| `STOP` | `17` | suspend process until *`CONT`*. *unblocked*, *uncaught*, *unignored* |
| `CONT` | `19` | continue (restore) process from *`STOP`* or *`TSTP`*, sent by *`bg`* and *`fg`*. *unblocked* |
| `INT` | `2` | `Ctrl+C` |
| `TERM` | `15` | default. normal termination |
| `TSTP` | `20` | `Ctrl+Z`. can be *ignored* |

## References

- Book: *UNIX and Linux System Administration Handbook, Fifth Edition* (2018)
