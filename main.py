import argparse

from netinfo import Subnet


def main(args):
    nf = Subnet(args.host, args.subnet)
    octs = nf.to_octets(args.host)

    for octet in octs:
        if octet > 255 or octet < 0:
            print('Error Invalid Ip address!')
            exit(-1)

    bin_addr = nf.to_binary(octs)
    num_hosts = nf.get_all_hosts()
    print(f'Address provided: \n{args.host}\n')
    print(f'Address in binary: \n{bin_addr}\n')
    print(f'Subnet mask: \n{nf.subnet_prefixes[args.subnet]}\n')
    print(f'# of hosts (minus netid and broadcast address): \n{int(num_hosts)}\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This script automates the tedious task of subnetting and other tools '
                                                 'to get more information about a network')
    parser.add_argument('--host', metavar='-ip', type=str, help='The host address to calculate', required=True)
    parser.add_argument('--subnet', metavar='-sn', type=str, help='The subnet mask in CIDR', required=True)
    arguments = parser.parse_args()
    main(arguments)
