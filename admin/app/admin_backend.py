import requests

class AdminBackend:
    host = 'admin-backend'
    port = 9901

    @staticmethod
    def __request_get(resource: str):
        backend_url = "{}:{}".format(AdminBackend.host, AdminBackend.port)
        ret = {}

        try:
            resp = requests.get("{}/{}".format(backend_url, resource))
        except requests.ConnectionError:
            ret["error"] = "Error connecting to admin backend"
            return ret

        try:
            data = resp.get_json()
        except:
            data = resp.text

        if resp.status_code != 200:
            ret["error"] = data["error"] if "error" in data else "Unspecified"
        else:
            ret["msg"] = data["msg"] if "msg" in data else "Success"

        return ret

    @staticmethod
    def __request_post_json(resource: str, json_to_send):
        backend_url = "{}:{}".format(AdminBackend.host, AdminBackend.port)
        ret = {}

        try:
            resp = requests.post("{}/{}".format(backend_url, resource), json=json_to_send)
        except requests.ConnectionError:
            ret["error"] = "Error connecting to admin backend"
            return ret

        try:
            data = resp.get_json()
        except:
            data = resp.text

        if resp.status_code != 200:
            ret["error"] = data["error"] if "error" in data else data
        else:
            ret["msg"] = data["msg"] if "msg" in data else data

        return ret

    @staticmethod
    def add_user(email: str, password: str):
        return AdminBackend.__request_post_json("user/add/{}".format(email), {"password": password})

    @staticmethod
    def view_user(email: str):
        return AdminBackend.__request_get("user/view/{}".format(email))

    @staticmethod
    def view_users():
        return AdminBackend.__request_get("user/viewall")

    @staticmethod
    def remove_user(email: str):
        return AdminBackend.__request_post_json("user/remove/{}".format(email), {})
