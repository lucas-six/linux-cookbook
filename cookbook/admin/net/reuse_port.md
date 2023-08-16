# Reuse Port

Since Linux *3.9*.

## TCP

Improved in Linux *4.6*.

The socket option **`SO_REUSEPORT`** allows *`accept()`* **load distribution** in a multi-threaded server
to be improved by using a distinct listener socket for each thread.
This provides improved load distribution as compared to traditional techniques
such using a single `accept()`ing thread that distributes connections,
or having multiple threads that compete to `accept()` from the same socket.

![socket SO_REUSEPORT](https://leven-cn.github.io/linux-cookbook/imgs/socket_SO_REUSEPORT.png)

In kernel, hash algorithms are used:

![socket SO_REUSEPORT using hash algorithms](https://leven-cn.github.io/linux-cookbook/imgs/socket_SO_REUSEPORT_hash.png)

## UDP

Improved in Linux *4.5*.

The socket option **`SO_REUSEPORT`** can provide better distribution of incoming datagrams
to multiple processes (or threads) as compared to the traditional technique of
having multiple processes compete to receive datagrams on the same socket.

## Python Recipes

- [Reuse Port - Python Cookbook](https://leven-cn.github.io/python-cookbook/cookbook/core/net/reuse_port)

## References

- [`bind`(2) - Debian Manpages](https://manpages.debian.org/bookworm/manpages-dev/bind.2.en.html)
- [`SO_REUSEPORT` - socket(7) - Debian Manpages](https://manpages.debian.org/bookworm/manpages/socket.7.en.html#SO_REUSEPORT)
