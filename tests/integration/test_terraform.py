class TestTerraformRegistryIntegration:
    def test_source_upstream_module(self, terraform):
        terraform.exec_run()
