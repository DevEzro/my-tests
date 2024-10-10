# LINUX (UBUNTU)
## Update y upgrade
- `sudo apt update`
- `sudo apt upgrade`

## Instalar java y kafka
- `sudo apt install openjdk-11-jdk`
- `java --version`

- `wget https://downloads.apache.org/kafka/3.8.0/kafka_2.13-3.8.0.tgz`
- `tar -xvzf kafka_2.13-3.8.0.tgz`
- `cd kafka_2.13-3.8.0`

### Iniciar Zookeeper
- Linux: `bin/zookeeper-server-start.sh config/zookeeper.properties`
- Windows: `.\bin\windows\zookeeper-server-start.bat config/zookeeper.properties`

### Iniciar Kafka
- Linux: `bin/kafka-server-start.sh config/server.properties`
- Windows: `.\bin\windows\kafka-server-start.bat config/zookeeper.properties`
- 
### Crear tópico
- Linux: `bin/kafka-topics.sh --create --topic logs --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1`
- Wnidows: `.\bin\windows\kafka-topics.bat --create --topic logs --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1`

### Uso de confluent-kafka
- `source ruta/a/entorno/virtual`
- `pip install confluent kafka`

> [!NOTE]
Los códigos copiarlos y pegarlos

### EJECUCIÓN
- `python3 productor.py`
- `python3 consumidor.py`

>[!NOTE]
Si no funciona usar `python` en vez de `python3`
