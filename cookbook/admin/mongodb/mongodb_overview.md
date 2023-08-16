# MongoDB Overview

Distributed Document Database (分布式文档数据库)

- NoSQL
- Rich JSON (BSON)
- schema-less (弱模式)
- Scale-Out (横向扩展)

## Scenario (应用场景)

- 小文件(Rich JSON和二进制文件)存储 (相比于*HDFS*)
- 弱事务性业务数据
- 物联网
- 日志
- 爬虫数据

## Fundamental Concepts (基础概念)

### Schema

- `database` (数据库)
- `collection` (集合)
  - `index` (索引)
    - Unique Indexes
    - [TTL Indexes](https://www.mongodb.com/docs/v6.0/core/index-ttl/)
  - [Capped Collections](https://www.mongodb.com/docs/v6.0/core/capped-collections/): fixed size, FIFO
- `document` (文档): **BSON**
- `field` (字段)

### Deployment (部署)

- `standalone` (单节点)
- `replica set` (副本集)
- `sharded cluster` (分片集群)

### Storage Engines (存储引擎)

- `WiredTiger`
- In-Memory
- pluggable storage engine API (自定义)

### Document Field Types (文档字段类型)

- `ObjectId`: `_id`
- `int` (32-bit)
- `long` (64-bit)
- `string`
- `date` (UTC datetime in milliseconds, 64-bit signed integer)
- `boolean`
- `null`
- `double`
- `decimal`
- `BinData`
- `object`
- `array`
- `Regular Expression`
- ~~`timestamp`~~ (for internal MongoDB use, use `date` instead)
- ~~`undefined`~~
- ~~`symbol`~~

## References

- [MongoDB Documentation](https://www.mongodb.com/docs/)
