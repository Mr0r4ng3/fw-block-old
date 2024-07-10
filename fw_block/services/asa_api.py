import json
from urllib import request
from requests import Session, adapters, Response, ConnectionError
from requests.auth import HTTPBasicAuth
from urllib3 import poolmanager, disable_warnings  # type: ignore
from ssl import create_default_context, Purpose, CERT_NONE


class CustomHttpAdapter(adapters.HTTPAdapter):
    def __init__(self, ssl_context=None, **kwargs):
        self.ssl_context = ssl_context
        super().__init__(**kwargs)

    def init_poolmanager(self, connections, maxsize, block=False):  # type: ignore
        self.poolmanager = poolmanager.PoolManager(
            num_pools=connections,
            maxsize=maxsize,
            block=block,
            ssl_context=self.ssl_context,
        )


class AsaAPI:

    def __init__(self, api_url: str, username: str, password: str) -> None:

        self.api_url = api_url
        self.username = username
        self.password = password

    def get_unsafe_client(self) -> Session:

        disable_warnings()

        ctx = create_default_context(Purpose.SERVER_AUTH)
        # to bypass verification after accepting Legacy connections
        ctx.check_hostname = False
        ctx.verify_mode = CERT_NONE
        # accepting legacy connections
        ctx.options |= 0x4
        session = Session()
        session.mount("https://", CustomHttpAdapter(ctx))
        return session

    def block_ip(self, ip_address: str) -> bool:

        commands = [
            f"shun {ip_address}",
        ]

        response = self.execute_command(commands)

        if response.status_code == 200:

            return True

        return False

    def unblock_ip(self, ip_address: str) -> bool:

        commands = [
            f"no shun {ip_address}",
        ]

        response = self.execute_command(commands)

        if response.status_code == 200:

            return True

        return False

    def get_shunned_ips(self) -> list[str]:

        commands = [
            "show shun",
        ]

        response = self.execute_command(commands)

        if response.status_code == 200:

            shunned_ips = response.json()["response"][0].split("\n")

            shunned_ips = shunned_ips[:-1] if shunned_ips[-1] == "" else shunned_ips

            cleaned_shunned_ips = [line.split()[2] for line in shunned_ips]

            return cleaned_shunned_ips

        return []

    def execute_command(self, commands: list[str]) -> Response:

        auth = HTTPBasicAuth(self.username, self.password)  # type: ignore
        headers = {"Content-Type": "application/json", "User-Agent": "REST API Agent"}

        body = json.dumps(
            {
                "commands": commands,
            }
        )

        response = self.get_unsafe_client().post(
            self.api_url,
            auth=auth,
            headers=headers,
            data=body,
            verify=False,
        )

        return response
