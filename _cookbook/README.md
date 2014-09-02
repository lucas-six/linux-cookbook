cookbook
==================

Cookbook

- [Linux User](#linux-user)
- [Bash Guide](#bash-guide)
- [Regular Expression](#regular-expression)
- [Doxygen Guide](#doxygen-guide)
- [Git Workflow](#git-workflow)

## Linux User

```bash
sudo shutdown -h|-r now

# Package Management on Debian/Ubuntu
sudo apt-get update
sudo apt-get install <pkg>
sudo apt-get remove/purge <pkg>

cd [~|-|..|<dir>]
pwd
ls [-l|-a|-r]
less <text-file>
ln -s <src> <sym-link>
cp|mv [-r|-u]
rm [-r|-f]
mkdir [-p]
wc [-l]
head|tail -n <num> <file>
tail -f <file>

which|man <cmd>

# gzip & bz2
tar xzvf <file>.[tar.gz|tgz]
tar xjvf <file>.tar.bz2
tar czvf <file>.[tar.gz|tgz] <file>...|<dir>
tar cjvf <file>.tar.bz2 <dir>...|<dir>

sudo <cmd>
sudo visudo

# New User/Group
#
# NOTE: `useradd` and `groupadd` are low-level utilities. On Debian, `adduser`
# and `addgroup` should be used instead.
#
# By default, each normal user in Debian is given a corresponding group with
# the same name, and the system users are placed in the `nogroup` group.
sudo [--system] adduser <user>
sudo passwd <user>
sudo [--system] addgroup <group>

# Add existing user to group (re-login required)
sudo adduser <user> <group>  # for Debian
sudo gpasswd -a <user> <group>  # for all Linux, as well as Debian

# Change file ownership
sudo chown <owner>[:<group>] <file> ...

# Search File
find <dir> <test-expr> <logic-operator...> <act>
    -name FILENAME-PATTERN
    -type [f|d|l|b|c]
    -size N[c|k|M|G]
    -empty
    -cmin [-|+]MINUTES
    -ctime [-|+]DAYS
    -inum INODE

    -and
    -or
    -not
    ()

    -print
    -delete
    -ls
    -exec CMD '{}' ';'|+
    
# Search File Contents
grep <expr> <file>

# Date & Time
date [+FORMAT]
	%% - '%'
	%H - hour (00-23)
	%I - hour (01-12)
	%M - minute (00-59)
	%S - second (00-59)
	%T - %H:%M:%S
	%R - %H:%M
	%y - year (00-99)
	%Y - year (0000-9999)
	%m - month (01-12)
	%d - day of month (01-31)
	%D - %m/%d/%y
	%u - day of week (1-7, 1=Monday)
	%w - day of week (0-6, 0=Sunday)
	%n - newline ('\n')
	%t - tab ('\t')

# Join Files
#
# Say we have downloaded a large file that has been split into multiple parts,
# and we want to join them back together. If the files were named:
#    movie.mp4.001, movie.mp4.002 ... movie.mp4.099
cat movie.mp4.0* > movie.mp4

# Mount ISO
mount -t iso9660 -o loop <img>.iso <mount-point>

# Mount CD-ROM
sudo mkdir /mnt/cdrom
sudo mount -t iso9660 -o loop /dev/cdrom /mnt/cdrom

# Umount before eject CD-ROM
sudo umount /dev/cdrom
sudo rmdir /mnt/cdrom

# Make ISO from CD-ROM
dd if=/dev/cdrom of=<dst-img>.iso

# Make ISO from local files
genisoimage -o <dst-img>.iso -R -J <dir>
    -R # Rock Ridge extensions, support long file names and POSIX-style file permissions
    -J # Joliet extensions, support long file names in Windows

# Blank/Write CD-ROM    
wodim dev=/dev/cdrom blank=fast
wodim dev=/dev/cdrom <dst-img>.iso

# Environment Variable
echo $PWD   # current directory
echo $USER  # current user name
echo $HOME  # home directory of current user

# Process Management
killall -9 <process-name>
kill -9 <pid>
ps aux
top

# Network Interface
#
# NOTE: `ifconfig` uses **obsolete** kernel interface `ioctl()` to get full
# address information, which limits hardware addresses to 8 bytes!
ip addr show [dev <if-dev>]                       # ifconfig
netstat -ie                                       # ifconfig
sudo ip addr add <ipv4>[/<prefix>] dev <if-dev>   # sudo ifconfig <if-dev> add <ipv4>
sudo ip addr del <ipv4>/<prefix=32> dev <if-dev>  # sudo ifconfig <if-dev> del <ipv4>
sudo ip link set <if-dev> up|down                 # sudo ifconfig <if-dev> up|down
sudo ip addr add 192.168.0.77/24 dev eth0         # sudo ifconfig eth0 192.168.0.77 netmask 255.255.255.0

# Network Routing
#
# NOTE: `route` is **obsolete**. use `ip route` instead.
ip route show [dev <if-dev>]                        # route
netstat -re                                         # route
sudo ip route add default via <ipv4> dev <if-dev>   # sudo route add default dev <if-dev>
sudo ip route add|del 192.168.0.77/24 dev eth0      # sudo route add|del -net 192.168.0.77/24 dev eth0
```

### Network Configuration

```
# Debian: /etc/network/interfaces
auto lo
iface lo inet loopback

auto eth0
iface eth0 inet static
	address 192.168.1.2
	netmask 255.255.255.0
	gateway 192.168.1.1
	dns-nameservers <DNS-IP-1> <DNS-IP-2> ...

auto eth1
iface eth1 inet dhcp
```

## Bash Guide

### Key Bindings

- `Tab` - Completion
- `Ctrl+D` - `exit` or EOF
- `Ctrl+C` - SIGTERM
- `Ctrl+A` / `Ctrl+E` - GoTo beginning/end of command line
- `Ctrl+U` / `Ctrl+K` - Cut from current position to beginning/end of commands
- `Ctrl+Y` - Paste
- `Ctrl+L` - `clear`
- `Ctrl+R` - History Search, `Ctrl+C` to quit
- `Ctrl+Z` - SIGSTP

### Expansion

```bash
$ echo text ~/*.txt {a,b} {A..C} $(echo a) $((1+1)) $USER
text /home/ly/a.txt a b A B C a 2 ly

$ echo "text ~/*.txt {a,b} {A..C} $(echo a) $((1+1)) $USER"
text ~/*.txt {a,b} {A..C} a 2 ly

$ echo 'text ~/*.txt {a,b} {A..C} $(echo a) $((1+1)) $USER'
text ~/*.txt {a,b} {A..C} $(echo a) $((1+1)) $USER
```

### I/O Redirection

```bash
# Redirect stderr
ls -l /bin/usr 2> ls-error.log

# Redirect stdout and stderr to one file
ls -l /bin/usr > ls.log 2>&1
```

In bash v4.0+, a more streamlined method for performing this combined
redirection:


```bash
ls -l /bin/usr &> ls.log
```

Sometimes "silence is golden", and we don't want output from a command.

```bash
ls -l /bin/usr > /dev/null 2>ls.log
```

### File Testing Operator

```
-e exist
-s NOT empty
-f regular file
-d directory
-S socket
-p named pipe
-h symbolic link
-r readable
-w writable
-nt newer than
-ot older than
-ef hard link
```

### Text Processing

```bash
# Substitute
str="a-b-c"
echo ${str/-/_}_d # a_b-c_d
echo ${str//-/_}_d # a_b_c_d

# Substring
str="abcdef"
echo ${str:1} # a
echo ${str:2:2} # bc

# Testing Operator
-z empty
-n NOT empty
```

## Regular Expression

 - `*` - Any numbers of characters
 - `?` - Any single of character
 - `[abc]` - Any character in set of `abc`
 - `[!abc]` - Any character NOT in set of `abc`
 - `[:alpha:]` - Any letter
 - `[:lower:]` - Any lower-case letter
 - `[:upper:]` - Any upper-case letter
 - `[:digit:]` - Any digit
 - `[:alnum:]` - Any letter or digit
 - `[:word:]` - `[:alnum:]` + `_`
 - `[:blank:]` - `Space` + `Tab`
 - `^abc` - Any line starting with `abc`
 - `abc$` - Any line ending with `abc`
 - `+` - More than once
 - `{n}`, `{n,m}` - from (n) to (m) times


## Doxygen Guide

More details on Doxygen, please refer to the on-line manual:

    http://www.stack.nl/~dimitri/doxygen/manual/

**STEP 1**: Doc code

```python
# Python code
## <function-or-method-description>.
#
# @param <param-name> <param-description>
# @return <return-name> <return-description>
# @exception <exception-name> <exception-description>
def func_or_method():
	'''<function-or-method-description>.
	'''
	# func or method definition
'''
@warning <warning-messages>
@todo <things to be done>
@deprecated
@see <reference to others>
@since <version>
'''
```

**STEP 2**: Generate Doxygen configuration file

```bash
doxygen -g Doxyfile
```

**STEP 3**: Update Doxygen configuration file

```
PROJECT_NAME =
PROJECT_NUMBER =
PROJECT_BRIEF =
PROJECT_LOGO =
OUTPUT_DIRECTORY = doc
CREATE_SUBDIRS = YES
OPTIMIZE_OUTPUT_FOR_C = YES                 # for C
OPTIMIZE_OUTPUT_JAVA = YES                  # for Python/Java
BUILTIN_STL_SUPPORT = YES                   # for C++
TYPEDEF_HIDES_STRUCT = YES                  # for C/C++
SKIP_FUNCTION_MACROS = NO                   # for C/C++
EXTRACT_ALL = YES
EXTRACT_PRIVATE = YES
EXTRACT_STATIC = YES
INPUT =
FILE_PATTERNS = *.py                        # for Python
FILE_PATTERNS = *.c *.h                     # for C
FILE_PATTERNS = *.cc *.cpp *.hh             # for C++
RECURSIVE = YES
SOURCE_BROWSER = YES
EXCLUDE_PATTERNS = */test/*
USE_MDFILE_AS_MAINPAGE = YES                # for GitHub
HTML_TIMESTAMP = YES
HTML_DYNAMIC_SECTIONS = YES
GENERATE_MAN = YES
MAN_LINKS = YES
```

**STEP 4**: Generate documentation

```bash
doxygen Doxyfile
```

## Git Workflow

### Start

```bash
git clone <git-url>
git init
```

### Mainstream

Branch `master` contains codes only for official releases with some version
tags.

```bash
git checkout master
git pull --rebase
git merge --no-ff dev
git tag -a <tag> -m '<tag-comment>' # e.g., git tag -a 'v0.1' -m 'v0.1 - Initial version'

git push
git push --tag
```

### Bugfix for Mainstream

```bash
git checkout -b <bugfix-A> master
# ... (git add/rm)
git diff [--cached] <path ...>
# ... (git commit -m)
git diff <bugfix-A>..master

git checkout master
git pull --rebase
git rebase <bugfix-A>
git branch -d <bugfix-A>
```

### Features/Topics

```bash
git checkout <feature-A> dev
git pull --rebase
# ... (git add/rm)
git diff [--cached] <path ...>
# ... (git commit)
git diff <feature-A>..dev

git checkout dev
git pull --rebase
git merge --no-ff <feature-A>
```

### Bugfix for Features/Topics

```bash
git checkout <feature-A>
git pull --rebase

git checkout -b <feature-A-bugfix>
# ... (git add/rm)
git diff [--cached] <path ...>
# ... (git commit)
git diff <feature-A>..<feature-A-bugfix>

git checkout <feature-A>
git pull --rebase
git rebase <feature-A-bugfix>
git branch -d <feature-A-bugfix>
```
