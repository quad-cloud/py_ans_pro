import os
import sys

from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.inventory import Inventory
from ansible.vars import VariableManager

variable_manager = VariableManager()
loader = DataLoader()

inventory = Inventory(loader=loader,
                      host_list='C:/Users/rohit/OneDrive/workspaces/quadyster/ansible-examples/lamp_haproxy/hosts',
                      variable_manager=variable_manager)
playbook_path = 'C:/Users/rohit/OneDrive/workspaces/quadyster/ansible-examples/lamp_haproxy/site.yml'

if not os.path.exists(playbook_path):
    print('[INFO] The playbook does not exist')
    sys.exit()

Options = namedtuple('Options', ['listtags', 'listtasks', 'listhosts', 'syntax', 'connection','module_path', 'forks', 'remote_user', 'private_key_file', 'ssh_common_args', 'ssh_extra_args', 'sftp_extra_args', 'scp_extra_args', 'become', 'become_method', 'become_user', 'verbosity', 'check'])
options = Options(listtags=False, listtasks=False, listhosts=False, syntax=False, connection='ssh', module_path=None, forks=100, remote_user='ec2-user', private_key_file='C:/Users/rohit/OneDrive/Pem', ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None, become=True, become_method=None, become_user='root', verbosity=None, check=False)

variable_manager.extra_vars = {'hosts': 'webservers'} # This can accomodate various other command line arguments.`

passwords = {}

pbex = PlaybookExecutor(playbooks=[playbook_path], inventory=inventory, variable_manager=variable_manager, loader=loader, options=options, passwords=passwords)

results = pbex.run()