import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_postfix_service_enabled(host):
    service = host.service('postfix')
    assert service.is_enabled


def test_postfix_service_running(host):
    service = host.service('postfix')
    assert service.is_running
