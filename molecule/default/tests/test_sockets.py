import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_socket_rabbitmq_server(host):
    assert host.socket("tcp://127.0.0.1:5672").is_listening
