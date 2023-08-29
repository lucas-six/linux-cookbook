# NGINX Configuration: XSS (跨站脚本攻击)

## Recipes

```conf
server {
    # XSS Prevention
    add_header X-Frame-Options 'SAMEORIGIN';  # 只允许本网站的frame嵌套
    add_header X-XSS-Protection '1; mode=block';  # 开启XSS过滤器
    add_header X-Content-Type-Options 'nosniff';  # 禁止嗅探文件类型
}
```

## More

- [Cross Site Scripting, XSS (跨站脚本攻击)](../csrf)

## References

- [Nginx Documentation](https://nginx.org/en/docs/)
