"""
Role tests
"""

import os
import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('path,user,group,mode', [
    ('/opt/infopen', 'root', 'root', 0o755),
    ('/opt/infopen/monitoring-node', 'root', 'root', 0o755),
    ('/opt/infopen/monitoring-node/releases', 'root', 'root', 0o755),
    ('/opt/infopen/monitoring-node/repo', 'root', 'root', 0o755),
    ('/opt/infopen/monitoring-node/shared', 'root', 'root', 0o755),
    ('/var/opt/infopen', 'root', 'root', 0o755),
    ('/var/opt/infopen/monitoring-node', 'root', 'root', 0o755),
])
def test_service_folders(host, path, user, group, mode):
    """
    Ensure service root folders exists and have expected permissions
    """

    current_folder = host.file(path)

    assert current_folder.exists
    assert current_folder.is_directory
    assert current_folder.user == user
    assert current_folder.group == group
    assert current_folder.mode == mode


def test_service_ansistrano_current_link(host):
    """
    Ensure service has a "current" symlink
    """

    symlink_path = host.file('/opt/infopen/monitoring-node/current')
    expected_symlink_to = '/opt/infopen/monitoring-node/releases/19700101-1.0.0'

    assert symlink_path.exists
    assert symlink_path.is_symlink
    assert symlink_path.linked_to == expected_symlink_to
    assert symlink_path.user == 'root'
    assert symlink_path.group == 'root'


@pytest.mark.parametrize('process_name', [
    ('prometheus'),
    ('process-exporte'),  # process-exporter
    ('netdata'),
    ('cadvisor'),
    ('node_exporter'),
])
def test_processes(host, process_name):
    """
    Ensure expected processes running and available
    """

    processes = host.process.filter(comm=process_name)

    assert len(processes) == 1
