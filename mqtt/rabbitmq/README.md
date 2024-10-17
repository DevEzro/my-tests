# ⚙ SET UP
## 🟦 WINDOWS
- Instalar [Erlang](https://github.com/erlang/otp/releases/download/OTP-27.1.1/otp_win64_27.1.1.exe) (o acceder a la [página oficial](https://www.erlang.org/downloads))
- Instalar [RabbitMQ](https://github.com/rabbitmq/rabbitmq-server/releases/download/v4.0.2/rabbitmq-server-4.0.2.exe) (o acceder a la [página oficial](https://www.rabbitmq.com/docs/install-windows))
- Instalar en un entorno virtual pika: `pip install pika`

## 🐧 LINUX
- Instalar las dependencias junto con el paquete: 
```
# sync package metadata
sudo apt-get update
# install dependencies manually
sudo apt-get -y install socat logrotate init-system-helpers adduser

# download the package
sudo apt-get -y install wget
wget https://github.com/rabbitmq/rabbitmq-server/releases/download/v4.0.2/rabbitmq-server_4.0.2-1_all.deb

# install the package with dpkg
sudo dpkg -i rabbitmq-server_4.0.2-1_all.deb

rm rabbitmq-server_4.0.2-1_all.deb
```
- Para más info visitar la página de [RabbitMQ](https://www.rabbitmq.com/docs/install-debian)
- Arrancar el servicio: `systemctl start rabbitmq-server`

# ▶ EJECUCCIÓN
- `python recieve.py`
- `python send.py`


![Ejemplo de uso](https://github.com/user-attachments/assets/1139f5c1-543f-4647-9447-fff403da5677)
