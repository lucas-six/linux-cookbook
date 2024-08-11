# Cross-Site Request Forgery (CSRF) (跨站请求伪造)

**CSRF** (**Cross-Site Request Forgery**), also known as **one-click attack**, **XSRF**
or **session riding**,
is an attack that impersonates a trusted user and sends a website unwanted or unauthorized commands.

## Protection Solution

### 1. Cookie Hashing

```http
Set-Cookie: csrftoken=xxxxxx; Secure; HttpOnly; SameSite=Strict
```

### 2. One-Time CSRF Tokens

```html
<meta name="csrf-token" content="{{ csrf_token }}">
```

or

```html
<form method="POST" action="transfer.php">
  <input type="hidden" name="csrf-token" value="{{ csrf_token }}">
  <input type="text" name="toBankId">
  <input type="text" name="money">
  <input type="submit" name="submit" value="Submit">
</form>
```

### 3. NGINX `valid_referer`

See [NGINX: Valid Referer - Linux Cookbook](../admin/nginx/nginx_csrf).

### 4. XSS Prevention

Cross Site Scripting, XSS (跨站脚本攻击)

See [NGINX: Cross Site Scripting, XSS (跨站脚本攻击) - Linux Cookbook](../admin/nginx/nginx_xss).

## References

- [CSRF - MDN](https://developer.mozilla.org/en-US/docs/Glossary/CSRF)
- [Cross-site request forgery - Wikipedia](https://en.wikipedia.org/wiki/Cross-site_request_forgery)
