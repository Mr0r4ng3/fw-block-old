
# FW-BLOCK

This project is created to carry out the shun command on cisco ASA firewall devices.

# Table of Contents

This is a table of contents for your project. It helps the reader navigate through the README quickly.
- [Project Title](#project-title)
- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [License](#license)


# Installation

To deploy we will use **docker compose** with the following steps

Clone the repo
```shell
git clone https://github.com/Mr0r4ng3/fw-block.git
```

Move to the app directory
```shell
cd fw-block
```

Set the **SERVER_NAME** enviroment variable
```shell
export SERVER_NAME="<server_domain_or_ip>"
```

Create a **.env** file for django enviroment variables
```shell
touch .env
```

Edit the **.env** file and set the following variables:
- **SECRET_KEY**
- **DEBUG**
- **CSRF_TRUSTED_ORIGINS**
- **FW_USER**
- **FW_PASSWORD**

```shell
nano .env
```

Put the **ssl certificate** and key in **./docker/nginx/ssl** or generate a **self signed** with the following steps
```shell
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ./docker/nginx/ssl/fwblock.key -out ./docker/nginx/ssl/fwblock.crt
```

Create a strong **Diffie-Hellman** group, which is used in negotiating Perfect Forward Secrecy with clients
```shell
sudo openssl dhparam -out ./docker/nginx/ssl/dhparam.pem 4096
```

Finally we run our application with docker compose
```shell
docker compose up
```


# Development

To start the server in development mode we must first install [poetry](https://python-poetry.org/docs/#installation) and [nodejs](https://nodejs.org/en/download/package-manager). Once installed we follow these steps

Clone the repository
```shell
git clone https://github.com/Mr0r4ng3/fw-block.git
```
Install dependencies
```shell
poetry install --no-root
```
Create a **.env** file for django enviroment variables
```shell
touch .env
```

Edit the **.env** file and set the following variables:
- **SECRET_KEY**
- **DEBUG**
- **CSRF_TRUSTED_ORIGINS**
- **FW_USER**
- **FW_PASSWORD**

```shell
nano .env
```

Get a shell with the **virtual enviroment** activated
```shell
poetry shell
```

Create and migrate the **database**
```shell
python manage.py migrate
```

Run the tailwind server
```shell
python manage.py tailwind start
```

Run the development server
```shell
python manage.py runserver
```

# License

[GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/)

