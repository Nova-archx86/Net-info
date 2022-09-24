class IpAddress:

    def __init__(self, addr: str):
        self.addr = addr

    def to_octets(self):
        addr = self.addr.split('.')
        try:
            octets = [int(x) for x in addr]
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
