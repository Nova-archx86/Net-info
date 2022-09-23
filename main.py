"""
TODO:
    1. Add more commandline options to specify a specific output
    2. Refactor
"""

import argparse

from netinfo import IpAddress, Subnet


def main(args):
    ip = IpAddress(args.host)
    sn = Subnet(ip, args.subnet)

    if ip.is_valid() is False:
        print('Error: invalid ip address!')
        exit(-1)

    if sn.is_valid() is False:
        print('Error: invalid subnet prefix! [ Make sure to include a / ]')
        exit(-1)

    bin_addr = ip.to_binary()
    num_hosts = sn.get_hosts()
    net_id = sn.get_net_id()
    broad_addr = sn.get_broadcast_addr()
    print('---------- Network Details ----------')
    print(f'Address provided: \n{args.host}\n')
    print(f'Address in binary: \n{bin_addr}\n')
    print(f'Network id: \n{net_id}\n')
    print(f'Broadcast address: \n{broad_addr}\n')
    print(f'Subnet mask: \n{sn.subnet_prefixes[args.subnet]}\n')
    print(f'# of usable hosts: \n{int(num_hosts)}\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This script automates the tedious task of subnetting and uses '
                                                 'other tools '
                                                 'to get more information about a network')
    parser.add_argument('--host', metavar='|--host ip Ex: 192.168.0.1|', type=str, help='The host address to calculate',
                        required=True)
    parser.add_argument('--subnet', metavar='|--subnet prefix Ex: /24|', type=str, help='The subnet mask in CIDR',
                        required=True)
    arguments = parser.parse_args()
    main(arguments)
