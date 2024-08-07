# Self-Signed TLS

## Recipes

### Self-Signed Certification

```bash
openssl req -new -x509 -newkey rsa:4096 -keyout client.key -out client.crt
```

## References

- [如何用 OpenSSL 创建自签名证书 - Azure](https://support.azure.cn/docs/azure-operations-guide/application-gateway/aog-application-gateway-howto-create-self-signed-cert-via-openssl.html)
