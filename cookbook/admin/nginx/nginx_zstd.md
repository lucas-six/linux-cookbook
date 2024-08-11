# NGINX: `zstd` Support

## Recipes

```bash
./configure --add-module=/path/to/zstd-nginx-module
```

```conf
http {
    zstd on;
    zstd_dict_file /path/to/dict;
    # zstd_types text/html;
    # zstd_comp_level 11;
    # zstd_min_length 256;  # in bytes
    # zstd_buffers 32 4k | 16 8k;
    # zstd_static off;
}
```

## More

- [Compression Algorithms: `ztd`](../../general_concepts/compression_algorithms)

## References

- [NGINX Documentation](https://nginx.org/en/docs/)
