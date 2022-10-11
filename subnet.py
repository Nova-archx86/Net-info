"""
TODO: Implement a way to ping a range of hosts (probably by using nmap)
"""

import math
from ip_address import IpAddress


class Subnet:

    def __init__(self, host: IpAddress, subnet: str):
        self.host = host
        self.subnet_prefixes = {
            '/0': '0.0.0.0', '/1': '128.0.0.0', '/2': '192.0.0.0',
            '/3': '224.0.0.0', '/4': '240.0.0.0', '/5': '248.0.0.0',
            '/6': '252.0.0.0', '/7': '254.0.0.0', '/8': '255.0.0.0',
            '/9': '255.128.0.0', '/10': '255.192.0.0', '/11': '255.224.0.0',
            '/12': '255.240.0.0', '/13': '255.248.0.0', '/14': '255.252.0.0',
            '/15': '255.254.0.0', '/16': '255.255.0.0', '/17': '255.255.128.0',
            '/18': '255.255.192.0', '/19': '255.255.224.0', '/20': '255.255.240',
            '/21': '255.255.248.0', '/22': '255.255.252.0', '/23': '255.255.254.0',
            '/24': '255.255.255.0', '/25': '255.255.255.128', '/26': '255.255.255.192',
            '/27': '255.255.255.224', '/28': '255.255.255.240', '/29': '255.255.255.248',
            '/30': '255.255.255.252', '/31': '255.255.255.254', '/32': '255.255.255.255',
        }
        self.subnet = subnet

    def is_valid(self):
        cidr = self.subnet.split('/')
        try:
            if len(cidr) == 1:
                return False
            if int(cidr[1]) > 32 or int(cidr[1]) < 0:
                return False
        except ValueError:
            return False

    def get_hosts(self):
        subnet_mask = IpAddress(self.subnet_prefixes[self.subnet])
        bin_mask = subnet_mask.to_binary()

        counter = 0
        for bit in range(0, len(bin_mask)):
            if bin_mask[bit] == '0':
                counter += 1

        num_hosts = math.pow(2, counter) - 2
        return num_hosts

    # A bit of a messy implementation
    # uses bitwise operators to get the network id and
    # broadcast address.

    def get_net_id(self):
        subnet_mask = IpAddress(self.subnet_prefixes[self.subnet])
        sub = subnet_mask.to_octets()
        addr = self.host.to_octets()
        net_id = [str(x & y) for x, y in zip(sub, addr)]

        return '.'.join(net_id)

    def get_broadcast_addr(self):
        subnet_mask = IpAddress(self.subnet_prefixes[self.subnet])
        net_id = IpAddress(self.get_net_id())
        net_id_octs = net_id.to_octets()
        sub = subnet_mask.to_octets()
        broad_addr = [str((x | ~y) & 0xff) for x, y in zip(net_id_octs, sub)]

        return '.'.join(broad_addr)
