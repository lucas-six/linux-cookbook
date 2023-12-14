# RabbitMQ Setup on Ubuntu / Debian

## Basic Concepts

- MQ (消息队列)
- Use Case: Aysnc（异步处理）, Low-Coupling（解藕）

## Installation on Ubuntu / Debian

### Official Repo

```bash
sudo apt-get install curl gnupg apt-transport-https -y

## Team RabbitMQ's main signing key
curl -1sLf "https://keys.openpgp.org/vks/v1/by-fingerprint/0A9AF2115F4687BD29803A206B73A36E6026DFCA" | sudo gpg --dearmor | sudo tee /usr/share/keyrings/com.rabbitmq.team.gpg > /dev/null
## Community mirror of Cloudsmith: modern Erlang repository
curl -1sLf https://github.com/rabbitmq/signing-keys/releases/download/3.0/cloudsmith.rabbitmq-erlang.E495BB49CC4BBE5B.key | sudo gpg --dearmor | sudo tee /usr/share/keyrings/rabbitmq.E495BB49CC4BBE5B.gpg > /dev/null
## Community mirror of Cloudsmith: RabbitMQ repository
curl -1sLf https://github.com/rabbitmq/signing-keys/releases/download/3.0/cloudsmith.rabbitmq-server.9F4587F226208342.key | sudo gpg --dearmor | sudo tee /usr/share/keyrings/rabbitmq.9F4587F226208342.gpg > /dev/null

## Add apt repositories maintained by Team RabbitMQ
sudo tee /etc/apt/sources.list.d/rabbitmq.list <<EOF
## Provides modern Erlang/OTP releases
##
deb [signed-by=/usr/share/keyrings/rabbitmq.E495BB49CC4BBE5B.gpg] https://ppa1.novemberain.com/rabbitmq/rabbitmq-erlang/deb/ubuntu jammy main
deb-src [signed-by=/usr/share/keyrings/rabbitmq.E495BB49CC4BBE5B.gpg] https://ppa1.novemberain.com/rabbitmq/rabbitmq-erlang/deb/ubuntu jammy main

# another mirror for redundancy
deb [signed-by=/usr/share/keyrings/rabbitmq.E495BB49CC4BBE5B.gpg] https://ppa2.novemberain.com/rabbitmq/rabbitmq-erlang/deb/ubuntu jammy main
deb-src [signed-by=/usr/share/keyrings/rabbitmq.E495BB49CC4BBE5B.gpg] https://ppa2.novemberain.com/rabbitmq/rabbitmq-erlang/deb/ubuntu jammy main

## Provides RabbitMQ
##
deb [signed-by=/usr/share/keyrings/rabbitmq.9F4587F226208342.gpg] https://ppa1.novemberain.com/rabbitmq/rabbitmq-server/deb/ubuntu jammy main
deb-src [signed-by=/usr/share/keyrings/rabbitmq.9F4587F226208342.gpg] https://ppa1.novemberain.com/rabbitmq/rabbitmq-server/deb/ubuntu jammy main

# another mirror for redundancy
deb [signed-by=/usr/share/keyrings/rabbitmq.9F4587F226208342.gpg] https://ppa2.novemberain.com/rabbitmq/rabbitmq-server/deb/ubuntu jammy main
deb-src [signed-by=/usr/share/keyrings/rabbitmq.9F4587F226208342.gpg] https://ppa2.novemberain.com/rabbitmq/rabbitmq-server/deb/ubuntu jammy main
EOF

## Update package indices
sudo apt-get update -y

## Install Erlang packages
sudo apt-get install -y erlang-base \
                        erlang-asn1 erlang-crypto erlang-eldap erlang-ftp erlang-inets \
                        erlang-mnesia erlang-os-mon erlang-parsetools erlang-public-key \
                        erlang-runtime-tools erlang-snmp erlang-ssl \
                        erlang-syntax-tools erlang-tftp erlang-tools erlang-xmerl

## Install rabbitmq-server and its dependencies
sudo apt-get install rabbitmq-server -y --fix-missing
```

### System Repo

```bash
apt install rabbitmq
```

## Configuration

```conf
# /etc/security/limits.d/rabbitmq.conf

rabbitmq  soft  nofile  65535
rabbitmq  hard  nofile  65535
```

```conf
# /etc/rabbitmq/rabbitmq.conf

CONFIG_FILE=/etc/rabbitmq/rabbitmq.conf
NODE_IP_ADDRESS=
NODENAME=rabbit@localhost
RABBITMQ_LOG_BASE=/var/log/rabbitmq
; PLUGINS_DIR="/opt/homebrew/opt/rabbitmq/plugins:/opt/homebrew/share/rabbitmq/plugins"
```

```bash
systemctl start rabbitmq
rabbitmq-plugins enable rabbitmq_management

rabbitmqctl add_user <username> <password>
rabbitmqctl set_user_tags <username> administrator
rabbitmqctl set_permissions -p "<vhost=/>" <username> ".*" ".*" ".*"
rabbitmqctl list_users

systemctl enable|disable rabbitmq
systemctl start|stop|restart|status rabbitmq
```

### MQTT

```bash
rabbitmq-plugins enable rabbitmq_mqtt
```

```ini
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
