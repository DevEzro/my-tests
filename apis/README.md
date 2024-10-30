# API_MQTT
### Requisitos
-Kafka instalado

### Ejecutar Kafka, Zookeeper y topic
- En la ruta de Kafka (seguir el orden):
  - Zookeeper: `bin\windows\zookeeper-server-start.bat config\zookeeper.properties` 
  - Kafka: `bin\windows\kafka-server-start.bat config\server.properties` 
  - Topico: `bin\windows\kafka-topics.bat --create --topic topic --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1`

- En la ruta de la api: `uvicorn api_mqtt:app --reload` 
