# Compression Algorithms (压缩算法)

| Algorithms | Comments | Feature |
| --- | --- | --- |
| **Deflate** (**`zlib`**/**`zip`**) | *LZ77* + *Huffman Coding*, support for Windows/UNIX/Linux | Most Compatible |
| **Gzip** (**`gzip`**) | *LZ77* based, faster and more effective than *zip*, support for UNIX/Linux | - |
| **Bzip2** (**`bzip2`**) | similar with *Gzip* | - |
| **Brotli** | *LZ77* based, created by Google in 2015 | Web prefered |
| **Zstd** (**Zstandard**) | *Huff0* + *FSE*. RFC 8478 (2018). Open source by Facebook in 2016. MIME: `application/zstd` | dictionary based |
| **Pzstd** | Parallel *Zstd* | better than *Zstd* |

## Key Index (关键指标)

- 压缩率 或 压缩比
- 压缩速度

## References

- [Gzip on Wikipedia](https://en.wikipedia.org/wiki/Gzip)
- [Brotli.org](https://brotli.org/)
- [Brotli on GitHub](https://github.com/google/brotli)
- [Brotli on Google Research](https://research.google/pubs/pub47824/)
- [Zstd on GitHub](https://github.com/facebook/zstd)
- [RFC 8478 - Zstandard Compression and the application/zstd Media Type (2018)](https://datatracker.ietf.org/doc/html/rfc8478)
