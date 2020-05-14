#!/usr/bin/env python

import json

import munch
import openstack

# conn = openstack.connect(auth_url='http://192.168.43.125:5000/v3', project_name='admin', username='admin',
# password = 'admin123', region_name = 'RegionOne', app_name = 'Default')


try:
    conn = openstack.connection.Connection(
        region_name='RegionOne',
        auth=dict(
            auth_url='http://192.168.43.125:5000/v3',
            username='admin',
            password='admin123',
            project_id='e0875629f3834e42a941aad3b8823cfc',
            user_domain_id='default'),
        compute_api_version='2',
        identity_interface='internal')
except Exception as e:
    print(e)

# server = conn.create_server('inst-5', image='cirros', flavor='1', auto_ip=True, ips=None, ip_pool=None,
#                            root_volume=None,
#                            terminate_volume=False, wait=False, timeout=180, reuse_ips=True, network='external_network',
#                            boot_from_volume=False, volume_size='50', boot_volume=None, volumes=None,
#                            nat_destination=None,
#                            group=None)

# print(json.loads(munch.toJSON(server))['id'])

print(conn.get_image(name_or_id='cirros'))

# network = conn.create_network(name='network-1', )

router = conn.create_router(name='router-4', ext_gateway_net_id='3a89c8a8-1aa0-4ea8-8755-14def2df5dbb')

if json.loads(munch.toJSON(router))['id']:
    private_network = conn.create_network(name='private-network-3')
    if json.loads(munch.toJSON(private_network))['id']:
        private_subnet = conn.create_subnet(subnet_name='subnet-3', network_name_or_id='private-network-1',
                                            cidr='200.200.10.0/24')
        if json.loads(munch.toJSON(private_subnet))['id']:
            connect1 = conn.add_router_interface(router=router,
                                                 subnet_id=json.loads(munch.toJSON(private_subnet))['id'])
            print(connect1)
            print(private_network)
            print(private_subnet)
            print(router)

conn.close()
