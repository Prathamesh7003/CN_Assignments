#  NAME     : Prathamesh Agawane
#  Mis      : 142203001
#  Branch   : Computer
#  Division : 2nd
#  Batch    : T4


import ipaddress


def calculate_subnet_info(ip_class, ip_address):
    if ip_class == 'A':
        subnet_mask = '255.0.0.0'
    elif ip_class == 'B':
        subnet_mask = '255.255.0.0'
    elif ip_class == 'C':
        subnet_mask = '255.255.255.0'
    else:
        return "Invalid IP class"

    network = ipaddress.IPv4Network(f'{ip_address}/{subnet_mask}', strict=False)

    num_subnets = 2 ** (32 - network.prefixlen)
    num_hosts_per_subnet = 2 ** (32 - network.prefixlen) - 2  # Subtract 2 for network and broadcast addresses

    subnet_info = []
    for subnet in network.subnets():
        subnet_info.append({
            'Network ID': subnet.network_address,
            'Broadcast ID': subnet.broadcast_address,
            'Range': f'{subnet.network_address + 1} - {subnet.broadcast_address - 1}'
        })

    return {
        'Number of Subnets': num_subnets,
        'Number of Hosts per Subnet': num_hosts_per_subnet,
        'Subnet Information': subnet_info,
        'Subnet Mask': subnet_mask
    }


ip_class = input("Enter IP class (A, B, or C): ").upper()
ip_address = input("Enter IP address: ")

subnet_info = calculate_subnet_info(ip_class, ip_address)
if subnet_info == "Invalid IP class":
    print(subnet_info)

else:
    print("\nSubnet Information:")
    print(f"Subnet Mask: {subnet_info['Subnet Mask']}")
    print(f"Number of Subnets: {subnet_info['Number of Subnets']}")
    print(f"Number of Hosts per Subnet: {subnet_info['Number of Hosts per Subnet']}")
    print("\nNetwork ID, Broadcast ID, and Range of each network:")
    for subnet in subnet_info['Subnet Information']:
        print(f"Network ID: {subnet['Network ID']}, Broadcast ID: {subnet['Broadcast ID']}, Range: {subnet['Range']}")