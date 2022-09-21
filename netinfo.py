import math


class Subnet:

    def __init__(self, host, subnet):
        self.host = host
        self.subnet = subnet
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

    @staticmethod
    def to_octets(addr):
        addr = addr.split('.')
        octets = []
        try:
            for octet in addr:
                octets.append(int(octet))
            return octets
        except ValueError:
            print('Error: Invalid ip address!')
            exit(-1)

    @staticmethod
    def to_binary(octets):
        bin_octets = []
        for octet in octets:
            bin_octets.append(f'{octet:08b}')

        return '.'.join(bin_octets)

    def get_all_hosts(self):
        subnet_mask = self.subnet_prefixes[self.subnet]
        octets = self.to_octets(subnet_mask)
        bin_mask = self.to_binary(octets)

        counter = 0
        for bit in range(0, len(bin_mask)):
            if bin_mask[bit] == '0':
                counter += 1

        num_hosts = math.pow(2, counter) - 2
        return num_hosts

    def get_broadcast_addr(self, bin_addr):
        pass

    def get_net_id(self):
        pass
