"""
TODO: Implement a way to ping a range of hosts (probably by using nmap)
"""

import math


class IpAddress:

    def __init__(self, addr: str):
        self.addr = addr

    def to_octets(self):
        addr = self.addr.split('.')
        octets = []
        try:
            for octet in addr:
                octets.append(int(octet))
            return octets
        except ValueError:
            print(f'Error: invalid ip address')
            exit(-1)

    def to_binary(self):
        octets = self.to_octets()
        bin_octets = [f'{octet:08b}' for octet in octets]

        return '.'.join(bin_octets)

    def is_valid(self):
        octets = self.to_octets()
        for octet in octets:
            if octet > 255 or octet < 0:
                return False


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
        self.subnet = IpAddress(self.subnet_prefixes[subnet])

    def get_hosts(self):
        bin_mask = self.subnet.to_binary()

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
        sub = self.subnet.to_octets()
        addr = self.host.to_octets()
        net_id = [str(x & y) for x, y in zip(sub, addr)]

        return '.'.join(net_id)

    def get_broadcast_addr(self):
        net_id = IpAddress(self.get_net_id())
        net_id_octs = net_id.to_octets()
        sub = self.subnet.to_octets()
        broad_addr = [str((x | ~y) & 0xff) for x, y in zip(net_id_octs, sub)]

        return '.'.join(broad_addr)
