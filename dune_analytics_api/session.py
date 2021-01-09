import requests


class Session:
    def __init__(self, cookie):
        self.cookie = cookie

    def __repr__(self):
        return self.cookie

    @classmethod
    def from_login(cls, username, password):
        csrf = cls._get_csrf()
        location = cls._request_login(username, password, csrf)
        cookie = cls._get_cookie(location)
        return cls(cookie)

    @classmethod
    def _get_csrf(cls):
        with requests.get("https://duneanalytics.com/api/auth/csrf") as response:
            return response.json()['csrf']

    @classmethod
    def _request_login(cls, username, password, csrf):
        data = f"csrf={csrf}&" \
               f"action=login&" \
               f"next=https%3A%2F%2Fduneanalytics.com&" \
               f"username={username}&password={password}"
        with requests.post(
                "https://duneanalytics.com/api/auth", data=data,
                headers={
                    'Cookie': f"csrf={csrf}",
                    'Content-Type': "application/x-www-form-urlencoded"
                }, allow_redirects=False) as response:
            return response.headers['location']

    @classmethod
    def _get_cookie(cls, location):
        with requests.get(location, allow_redirects=False) as response:
            return response.headers['Set-Cookie']
