# RabbitMQ

## Basic Concepts

- MQ (消息队列)
- Use Case: Aysnc（异步处理）, Low-Coupling（解藕）

## Setup

- [Installation on Ubuntu / Debian](https://www.rabbitmq.com/docs/install-debian#apt-quick-start)
- [Configuration Example](https://www.rabbitmq.com/docs/configure#example-config)

### Core Configuration

```conf
# /etc/rabbitmq/rabbitmq.conf

## Relevant doc guide: https://www.rabbitmq.com/docs/networking.
##
## By default, RabbitMQ will listen on all interfaces, using
## the standard (reserved) AMQP 0-9-1 and 1.0 port.
##
# listeners.tcp.default = 5672

## TLS listeners are configured in the same fashion as TCP listeners,
## including the option to control the choice of interface.
##
# listeners.ssl.default = 5671

## It is possible to disable regular TCP (non-TLS) listeners. Clients
## not configured to use TLS and the correct TLS-enabled port won't be able
## to connect to this node.
# listeners.tcp = none

## Password hashing implementation. Will only affect newly
## created users. To recalculate hash for an existing user
## it's necessary to update her password.
##
## To use SHA-512, set to rabbit_password_hashing_sha512.
##
# password_hashing_module = rabbit_password_hashing_sha256
```

```bash
systemctl status rabbitmq-server
```

## Plugins

### Management Plugin

```bash
rabbitmq-plugins enable rabbitmq_management
```

```conf
# /etc/rabbitmq/rabbitmq.conf

## HTTP listener and embedded HTTP server (Cowboy) settings
#
# management.tcp.port = 15672
# management.tcp.ip   = 0.0.0.0

## HTTPS listener settings
##
## Relevant doc guides:
##
## * https://www.rabbitmq.com/docs/management
## * https://www.rabbitmq.com/docs/ssl
##
# management.ssl.port       = 15671
# management.ssl.cacertfile = /path/to/ca_certificate.pem
# management.ssl.certfile   = /path/to/server_certificate.pem
# management.ssl.keyfile    = /path/to/server_key.pem
```

```bash
rabbitmqctl add_user <username> <password>
rabbitmqctl set_user_tags <username> administrator
rabbitmqctl set_permissions -p "<vhost=/>" <username> ".*" ".*" ".*"
rabbitmqctl list_users
```

### Stream Plugin

```bash
rabbitmq-plugins enable rabbitmq_stream
```

```conf
# /etc/rabbitmq/rabbitmq.conf
# See https://github.com/rabbitmq/rabbitmq-server/blob/main/deps/rabbit/docs/rabbitmq.conf.example

## RabbitMQ Stream Protocol plain TCP listeners and their ports.
##
## Relevant doc guide: https://www.rabbitmq.com/docs/stream#tcp-listeners
##
# stream.listeners.tcp.default = 5552

## RabbitMQ Stream Protocol TLS listeners and their ports.
##
## Relevant doc guide: https://www.rabbitmq.com/docs/stream#tls
##
# stream.listeners.ssl.default = 5553
```

### MQTT Plugin

```bash
rabbitmq-plugins enable rabbitmq_mqtt
```

```conf
# /etc/rabbitmq/rabbitmq.conf
# See https://github.com/rabbitmq/rabbitmq-server/blob/main/deps/rabbit/docs/rabbitmq.conf.example

mqtt.listeners.tcp.default = 1883

# IPv4/IPv6
#mqtt.listeners.tcp.1 = 127.0.0.1:1883
#mqtt.listeners.tcp.2 = ::1:1883

#mqtt.tcp_listen_options.backlog = 4096
#mqtt.tcp_listen_options.recbuf  = 131072
#mqtt.tcp_listen_options.sndbuf  = 131072

#mqtt.tcp_listen_options.keepalive = true
#mqtt.tcp_listen_options.nodelay   = true

#mqtt.tcp_listen_options.exit_on_close = true
#mqtt.tcp_listen_options.send_timeout  = 120

## Default MQTT with TLS port is 8883
# mqtt.listeners.ssl.default = 8883
#ssl_options.cacertfile = /path/to/ca_certificate.pem
#ssl_options.certfile   = /path/to/server_certificate.pem
#ssl_options.keyfile    = /path/to/server_key.pem
#ssl_options.verify     = verify_peer
#ssl_options.fail_if_no_peer_cert  = true

# anonymous connections, if allowed, will use the default
# credentials specified here
mqtt.allow_anonymous  = true
mqtt.default_user     = guest
mqtt.default_pass     = guest

mqtt.vhost            = /
mqtt.exchange         = amq.topic
# 24 hours by default
mqtt.subscription_ttl = 86400000
mqtt.prefetch         = 10

## use DETS (disk-based) store for retained messages
# `rabbit_mqtt_retained_msg_store_ets` for RAM-based
mqtt.retained_message_store = rabbit_mqtt_retained_msg_store_dets
## only used by DETS store
mqtt.retained_message_store_dets_sync_interval = 2000
```

## References

- [RabbitMQ Home](https://www.rabbitmq.com/)
- [RabbitMQ Configuration Example (GitHub)](https://github.com/rabbitmq/rabbitmq-server/blob/main/deps/rabbit/docs/rabbitmq.conf.example)
