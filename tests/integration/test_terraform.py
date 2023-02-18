from http.server import SimpleHTTPRequestHandler, HTTPServer
from subprocess import run
from threading import Thread

import pytest


@pytest.fixture()
def module_source_server(request):
    directory = request.path.parent / "data" / "terraform_module_source"

    class Server(HTTPServer):
        def finish_request(self, request, client_address):
            self.RequestHandlerClass(request, client_address, self, directory=directory)

    addr = ("127.0.0.1", 8000)
    with Server(addr, SimpleHTTPRequestHandler) as httpd:
        yield Thread(target=httpd.serve_forever, daemon=True).start()


class TestTerraformRegistryIntegration:
    def test_source_upstream_module(self, request, module_source_server):
        terraform_dir = request.path.parent / "data" / "terraform"
        terraform_init = f"terraform -chdir={terraform_dir} init -input=false".split()
        assert run(terraform_init).returncode == 0
