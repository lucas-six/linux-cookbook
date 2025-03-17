# mDNS: `avahi`

## Recipes

```bash
# Ubuntu
apt install avahi-daemon avahi-utils

systemctl restart avahi-daemon.service

avahi-browse -a -r
avahi-browse -r "_http._tcp"

avahi-publish -s [options] name service-type port [TXT data ...]
```

## References

- [Avahi Homepage](http://avahi.org/)
