#!/usr/bin/env python

import paramiko

# openstack.enable_logging(debug=True)

# conn = openstack.connect(auth_url='http://122.166.176.47:5000/v3', username='admin', password='admin@123', project_name='default')

# images = conn.get_image_by_id('4e61b124-1893-49de-9d1d-e946c1672cb6')

# print(images)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.load_system_host_keys()
ssh.connect(hostname='122.166.176.45', username='root', password='titan@123', port=4500)
print('Connection successful')
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('echo $OS_REGION_NAME')
print(ssh_stdout.readlines())  # print the output of ls command

# print(alldata.decode())

ssh_stdin_1, ssh_stdout_1, ssh_stderr_1 = ssh.exec_command('sh opnstack_env.sh')
ssh_stdin_2, ssh_stdout_2, ssh_stderr_2 = ssh.exec_command('/usr/bin/openstack flavor list', timeout=20000,
                                                           environment={'OS_USERNAME': 'admin',
                                                                        'OS_PASSWORD': '\'admin123\'',
                                                                        'OS_REGION_NAME': 'RegionOne',
                                                                        'OS_AUTH_URL': 'http://192.168.1.201:5000/v3',
                                                                        'OS_PROJECT_NAME': 'admin',
                                                                        'OS_USER_DOMAIN_NAME': 'Default',
                                                                        'OS_PROJECT_DOMAIN_NAME': 'Default',
                                                                        'OS_IDENTITY_API_VERSION': '3'})

ssh_stdin_3, ssh_stdout_3, ssh_stderr_3 = ssh.exec_command('pwd')
ssh_stdin_4, ssh_stdout_4, ssh_stderr_4 = ssh.exec_command('echo $OS_REGION_NAME')

print("ssh_stdout_1", ssh_stdout_1.readlines())
print("ssh_stdout_3", ssh_stdout_3.readlines())
print("ssh_stderr_3", ssh_stderr_3.readlines())
print("ssh_stdout_4", ssh_stdout_4.readlines())
print("ssh_stderr_4", ssh_stderr_4.readlines())

ssh.close()
