# NGINX Installation

## Ubuntu

See [Install on Ubuntu](https://nginx.org/en/linux_packages.html#Ubuntu).

```bash
# Install the prerequisites
apt install curl gnupg2 ca-certificates lsb-release openssl systemd

# stable nginx
echo "deb https://nginx.org/packages/ubuntu `lsb_release -cs` nginx" \
    | sudo tee /etc/apt/sources.list.d/nginx.list

# mainline nginx
echo "deb https://nginx.org/packages/mainline/ubuntu `lsb_release -cs` nginx" \
    | sudo tee /etc/apt/sources.list.d/nginx.list

# official nginx signing key
curl -fsSL https://nginx.org/keys/nginx_signing.key | sudo apt-key add -

# verify key
apt-key fingerprint ABF5BD827BD9BF62
# Output:
# pub   rsa2048 2011-08-19 [SC] [expires: 2024-06-14]
#       573B FD6B 3D8F BC64 1079  A6AB ABF5 BD82 7BD9 BF62
# uid   [ unknown] nginx signing key <signing-key@nginx.com>

apt update
apt install nginx
```

## References

- [Install NGINX on Ubuntu](https://nginx.org/en/linux_packages.html#Ubuntu)
- [NGINX Documentation](https://nginx.org/en/docs/)
- [NGINX Product Documentation](https://docs.nginx.com/)
