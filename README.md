# FW-BLOCK

This project is created to carry out the shun command on cisco ASA firewall devices.


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY`
`DEBUG`
`IP_API_URL`
`FW_USER`
`FW_PASSWORD`

## Run Locally

Clone the project

```bash
  git clone https://github.com/Mr0r4ng3/fw-block.git
```

Go to the project directory

```bash
  cd fw-block
```

Create a .env file

```bash
  touch .env
```

Install dependencies

```bash
  poetry install --no-root
```

Run migrations
```bash
  python3 ./manage.py migrate
```
Start the server
```bash
  python3 ./manage.py runserver
```

## License

[GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/)

