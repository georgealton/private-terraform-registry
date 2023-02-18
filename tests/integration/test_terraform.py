from subprocess import run
from os import environ

import pytest


# @pytest.mark.xfail(reason="Not Implemented")
class TestTerraformRegistryIntegration:
    def test_source_upstream_module(self, request):
        print(environ)
        cmd = f"terraform -chdir={request.path.parent/'data/terraform'} plan -input=false".split()
        plan = run(cmd, env=environ)
        assert plan.returncode == 0
