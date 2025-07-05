import argparse
from utils.network_utils import *
from utils.port_utils import *
from scanner.port import *
from scanner.target_host import *
from scanner.port_scanner import *
from utils.reports import *

LABEL_UDP = 'udp'
LABEL_TCP = 'tcp'
LABEL_ALL = 'all'
REPORT_TYPE_TEXT = 'text'
REPORT_TYPE_JSON = 'json'

def main():

    parser = argparse.ArgumentParser(description='Network port scanner')
    parser.add_argument('-t', '--target', help='Target IP address/CIDR or hostname', required=True)
    parser.add_argument('-p', '--port', type=PortUtils.parse_port, help='Port(s) to scan: number(80), range(443-987) or category(wp=well-known, rp=registered, all=all ports)', required=True)
    parser.add_argument('-proto', '--protocol', help='tcp/udp/all', choices=['tcp', 'udp', 'all'], required=True)
    parser.add_argument('-o', '--output', help='Output format (text or json)', choices=['text', 'json'], default='json', required=False)

    args = parser.parse_args()

    network_utils = NetworkUtils()

    ips = network_utils.find_ips(args.target)

    port_range = args.port

    if(len(ips) > 0): 

        target_list = []

        for ip in ips: 
        
            target_host = TargetHost(ip)

            ports = {}
            for port_num in range(port_range[PortUtils.START_LABEL], port_range[PortUtils.END_LABEL] + 1): 
                
                ports[port_num] = Port(port_num)


            target_host.set_ports(ports)

            if(args.protocol == LABEL_ALL): 

                tcp_scanner = TCPPortScanner()
                tcp_scanner.set_target_host(target_host)
                tcp_scanner.scan()


                udp_scanner = UDPPortScanner()
                udp_scanner.set_target_host(target_host)
                udp_scanner.scan()

            elif(args.protocol == LABEL_TCP): 

                tcp_scanner = TCPPortScanner()
                tcp_scanner.set_target_host(target_host)
                tcp_scanner.scan()

            elif(args.protocol == LABEL_UDP): 

                udp_scanner = UDPPortScanner()
                udp_scanner.set_target_host(target_host)
                udp_scanner.scan()
            

            target_list.append(target_host)

        

        if(args.output == REPORT_TYPE_TEXT): 

            Reports.generate_text_report(target_list)

        else: 

            Reports.generate_json_report(target_list)


if __name__ == '__main__':
    main()