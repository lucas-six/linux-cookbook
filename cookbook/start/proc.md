# Process Control

## GNU `coreutils`

| Command | Comment |
| --- | --- |
| `kill` | Send a signal to processes |
| `sleep` | Delay for a specified time |
| `timeout` | Run a command with a time limit |
| `nohup` | Run a command immune to hangups |

## Process Information

### List Processes

```bash
ps aux
```

or

```bash
apt install procps  # Debian, Ubuntu
dnf install procps-ng  # RedHat

pgrep <pattern>
```

### PID

```bash
pidof <process-name>
```

### `top` / `htop` - View Processes Dynamically

```bash
top
```

or

```bash
apt install htop
dnf install htop

htop
```

### `pstree` - Display Process Tree

```bash
apt install psmisc
dnf install psmisc

pstree <pid>
```

### Process File System

`/proc/<pid>`

## Signal

```bash
kill -l

kill [-<signal=SIGTERM>] <pid>

killall [-u <user>] [-<signal=SIGTERM>] <proc-name>

apt install procps
dnf install procps-ng
pkill [-u <user>] [-<signal>] <process-name>
```

## Jobs

### Putting a Process in the Background

```bash
$ <cmd> &
[job-id] <pid>
```

### `jobs` - List jobs

```bash
$ jobs
[job-id]+ Running <cmd> &
```

### Returning a Process to the Foreground

```bash
$ fg %<job-id>
<cmd>
```

### Resume the program's execution in the background

Stopping (Pausing) a Process by *`Ctrl+Z`*.

```bash
$ jobs
[job-id]+ Stopped <cmd>
```

then

```bash
$ bg %<job-id>
[job-id]+ <cmd> &
```

## More

- [General Concept: **Process**](../general_concepts/proc)

## References

- [GNU Coreutils Manual](https://www.gnu.org/software/coreutils/manual/html_node/index.html)
- [Coreutils - Debian Wiki](https://wiki.debian.org/coreutils)
