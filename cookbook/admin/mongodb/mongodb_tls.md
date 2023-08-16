# MongoDB TLS

```bash
# 合并公钥和私钥
cat <domain.tls.pem> <domain.tls.key> > </etc/ssl/mongodb.pem>
chown mongodb:mongodb </etc/ssl/mongodb.pem>
chmod 0400 </etc/ssl/mongodb.pem>
```

```yml
# /etc/mongod.conf

net:
  tls:
    mode: requireTLS
    certificateKeyFile: </etc/ssl/mongodb.pem>
```

```bash
# 客户端连接
chmod 0400 .ssh/<domain.ca.pem>
mongosh --tls --host <domain> [--port <=27017>] --tlsCAFile <~/.ssh/domain.ca.pem>
```
