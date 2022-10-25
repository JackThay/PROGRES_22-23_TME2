from requests import *
from json import *
import unittest


class TestAPIMethods(unittest.TestCase):
        
    server_ip = 'localhost'
    server_port = 2100

    def test_add(self):
        r = get(f"http://{self.server_ip}:{self.server_port}/add/21/21")
        r = get(f"http://{self.server_ip}:{self.server_port}/add/-21/21")
        r = get(f"http://{self.server_ip}:{self.server_port}/add/21/-21")
        r = get(f"http://{self.server_ip}:{self.server_port}/add/-21/-21")

    def test_sub(self):
        r = get(f"http://{self.server_ip}:{self.server_port}/sub/21/21")
        r = get(f"http://{self.server_ip}:{self.server_port}/sub/-21/21")
        r = get(f"http://{self.server_ip}:{self.server_port}/sub/21/-21")
        r = get(f"http://{self.server_ip}:{self.server_port}/sub/-21/-21")

    def test_mul(self):
        r = get(f"http://{self.server_ip}:{self.server_port}/mul/21/21")
        r = get(f"http://{self.server_ip}:{self.server_port}/mul/-21/21")
        r = get(f"http://{self.server_ip}:{self.server_port}/mul/21/-21")
        r = get(f"http://{self.server_ip}:{self.server_port}/mul/-21/-21")

    def test_div(self):
        r = get(f"http://{self.server_ip}:{self.server_port}/div/21/21")
        r = get(f"http://{self.server_ip}:{self.server_port}/div/-21/21")
        r = get(f"http://{self.server_ip}:{self.server_port}/div/21/-21")
        r = get(f"http://{self.server_ip}:{self.server_port}/div/-21/-21")
        r = get(f"http://{self.server_ip}:{self.server_port}/div/0/21")
        # raise exception
        r = get(f"http://{self.server_ip}:{self.server_port}/div/21/0")

    def test_mod(self):
        r = get(f"http://{self.server_ip}:{self.server_port}/mod/21/21")
        r = get(f"http://{self.server_ip}:{self.server_port}/mod/-21/21")
        r = get(f"http://{self.server_ip}:{self.server_port}/mod/21/-21")
        r = get(f"http://{self.server_ip}:{self.server_port}/mod/-21/-21")
        r = get(f"http://{self.server_ip}:{self.server_port}/mod/0/21")
        # raise exception
        r = get(f"http://{self.server_ip}:{self.server_port}/mod/21/0")


if __name__ == '__main__':
    unittest.main()
