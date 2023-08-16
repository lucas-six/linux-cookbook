# MongoDB Usage

## Connect

```bash
mongosh [--host <=localhost>] [--port <=27017>]

mongosh [<mongodb-url>]

# <Ctrl+D> to disconnect
```

### Standalone URL

```url
mongodb://<user>:<pwd>@<ip>:<port=27017>/<db_name>?authMechanism=SCRAM-SHA-256&connectTimeoutMS=3500&appName=<app_name>
```

### Replica Set URL

```url
mongodb://<user>:<pwd>@<ip1>:<port=27017>,<ip2>:<port=27017>,<ip3>:<port=27017>/<db_name>?replicaSet=<rs-name>&authMechanism=SCRAM-SHA-256&maxPoolSize=4096&connectTimeoutMS=3500&serverSelectionTimeoutMS=3500&appName=<app_name>
```

## Basic

```bash
> show users

> show dbs

# switch database
> use <dbname>
```

## Users

### `role`

- All DBs
  - **`root`** root user
  - `dbAdminAnyDatabase` db admin for all databases
  - `userAdminAnyDatabase` user admin for all databases
  - `readWriteAnyDatabase` read and write permissions for all databases
  - `readAnyDatabase` read-only permissions for all databases
  - `backup`, `restore` backup permission
  - `restore` restore permission
- Single DB
  - **`dbOwner`** all permissions for one database
  - `dbAdmin` ab admin for one database
  - `userAdmin` user admin for one database
  - `readWrite` read and write permissions for one database
  - `read` read-only permission for one database
- Cluster
  - `clusterAdmin`, `clusterManager`, `clusterMonitor`, `hostManager`

### Create Root

```bash
> use admin
> db.createUser( { user: '<root_name>', pwd: passwordPrompt(), roles: ['root'] } )
```

### Create Admin for All Databases

```bash
# Admin (Standalone)
> db.createUser({
    user: "<super_admin_name>",
    pwd: passwordPrompt(),
    roles:
        [
            { role: "userAdminAnyDatabase", db: "admin" },
            { role: "readWriteAnyDatabase", db: "admin" }
        ]
})

# Admin (Replica Set)
> db.createUser({
    user: "<super_admin_name>",
    pwd: passwordPrompt(),
    roles:
        [
            { role: "userAdminAnyDatabase", db: "admin" },
            { role: "readWriteAnyDatabase", db: "admin" },
            { role: "clusterAdmin", db: "admin" }
        ]
})
```

### Create Database Admin

```bash
> use <dbname>
> db.createUser( { user: '<username>', pwd: passwordPrompt(), roles: ['dbOwner'] } )

# OR:

> db.createUser({
    user: "<db_owner_name>",
    pwd: passwordPrompt(),
    roles:
        [
            { role: "dbOwner", db: "<db_name>" }
        ]
})
```

### Delete Users

```bash
> db.dropUser('<username>')
```

### Auth

```bash
> db.auth('<username>', '<password>')
```

### Change Password

```bash
> db.changeUserPassword('<username>', passwordPrompt())
```

### Grant or Revoke Roles

```bash
# Grank
> db.grantRolesToUser( '<username>', [ '<role-name>' or { 'role': '<role-name>', db: '<dbname>' } ] )

# Revoke
> db.revokeRolesFromUser( '<username>', [ '<role-name>' or { 'role': '<role-name>', db: '<dbname>' } ] )
```

## Collections

### Delete

```bash
> db.<collectionName>.drop()
```

### Documetation

```bash
# 创建文档
> db.<collectionName>.insertOne( {
  myString: 'string',
  myDate: new Date(),
  myISODate: ISODate(), // ISO-8601
} )
myDate.toString()
myDate.getMonth()

# 查询单个文档
> db.<collectionName>.findOne(
  {
    <filed>: <value>,
    <field>: {
      $gt: <N>              // greater than
      $lt: <N>              // less than
      $gte: <N>             // greater than or equal to
      $lte: <N>             // less than or equal to
      $ne: <N>              // not equal to
      $in: [...]
      $regex: /<pattern>/, $options: '<options>'
    },
  })
> db.<collectionName>.findOne(
  {
    <query filter>
  },
  {
    <filed>: 1, ...  // Specify the Fields to Return
    <filed>: 0, ...  // Return All but the Excluded Fields
  })

# 查询多个文档
> db.<collectionName>.find(
  {
    <query filter>
  })
> db.<collectionName>.find(
  {
    <query filter>
  }).limit(<N>)

# 创建索引
> db.<collectionName>.createIndex(
  {
    <fieldName>: 1 / -1 / "text",
    ...
  },
  {
    background: true,
    unique: true,
    name: "<IndexName>",
    weights: {
      <fieldName>: <N>,
      ...
    }
  }
)
```

## Dump and Restore

### Dump Data

```bash
mongodump [-h|--host <=localhost>[:<=27017>]|[--port <=27017>]] [-u <user> -p <password> [--authenticationDatabase <=admin>]] [-d|--db <database>] [-c|--collection <collection>] [-o|--out <out-dir=bin/dump>]
```

### Restore Data

```bash
mongorestore [-h|--host <=localhost>[:<=27017>]] [--port <=27017>] [--nsInclude <database.collection>] [<data-dir=bin/dump>]
```

## Export and Import Data

### Export Data

```bash
mongoexport [-h|--host <=localhost>] [--port <=27017>] [-u <user>] [-p <password>] [--authenticationDatabase <=admin>] -d <database> -c <collection> -o <data.json>
```

### Import Data

```bash
mongoimport [-h|--host <host=localhost>] [--port <port=27017>] [-u <user>] [-p <password>] -d <database> -c <collection> --file <data.json>
```

## Version Compatibility

```bash
use admin

db.adminCommand( { getParameter: 1, featureCompatibilityVersion: 1 } )
db.adminCommand( { setFeatureCompatibilityVersion: <version=5.0, 4.4> } )
```
