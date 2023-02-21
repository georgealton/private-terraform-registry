from http.server import SimpleHTTPRequestHandler, HTTPServer
from subprocess import run
from threading import Thread

import pytest


@pytest.fixture()
def module_server(request, shared_datadir):
    module_dir = shared_datadir / "terraform_module_source"

    class ModuleServer(HTTPServer):
        def finish_request(self, request, client_address):
            self.RequestHandlerClass(
                request,
                client_address,
                self,
                directory=module_dir,
            )

    addr = ("127.0.0.1", 8000)
    with ModuleServer(addr, SimpleHTTPRequestHandler) as httpd:
        yield Thread(target=httpd.serve_forever, daemon=True).start()


class TestTerraformRegistryIntegration:
    def test_source_upstream_module(self, shared_datadir, module_server):
        terraform_dir = shared_datadir / "terraform"
        terraform_init = f"terraform -chdir={terraform_dir} init -input=false".split()
        assert run(terraform_init).returncode == 0
