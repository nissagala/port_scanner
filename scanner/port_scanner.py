from abc import ABC, abstractmethod
from .target_host import *
from scapy.all import *

class PortScanner(ABC): 

    timeout = 2
    target_host: TargetHost

    PORT_STATUS_OPEN = 'open'
    PORT_STATUS_CLOSED = 'closed'

    def set_target_host(self, target_host: TargetHost): 

        self.target_host = target_host



    @abstractmethod
    def scan(self): 
        pass

class TCPPortScanner(PortScanner): 

    PORT_STATUS_NO_RESPONSE = 'filtered'

    def scan(self): 

        ports = self.target_host.get_ports()

        if(len(ports) > 0): 

            for port_num, port_obj in ports.items():

                t = self.target_host.get_ip()
                print(f'Scanning {t} for TCP port {port_num}')

                syn_packet = IP(dst=self.target_host.get_ip()) / TCP(dport=port_num, flags="S")

                response = sr1(syn_packet, timeout=self.timeout, verbose=0)

                port_status = self.PORT_STATUS_CLOSED

                if response is None:
                    port_status = self.PORT_STATUS_NO_RESPONSE

                elif response.haslayer(TCP):
                    if response[TCP].flags == 0x12:  
                        
                        rst_packet = IP(dst=self.target_host.get_ip()) / TCP(dport=port_num, flags="R")

                        send(rst_packet, verbose=0)

                        port_status = self.PORT_STATUS_OPEN

                    elif response[TCP].flags == 0x14:  
                        port_status = self.PORT_STATUS_CLOSED


                self.target_host.set_tcp_port_status(port_num, port_status)

class UDPPortScanner(PortScanner): 

    PORT_STATUS_NO_RESPONSE = 'open/filtered'

    def scan(self): 

        ports = self.target_host.get_ports()

        if(len(ports) > 0): 

            for port_num, port_obj in ports.items():

                t = self.target_host.get_ip()
                print(f'Scanning {t} for UDP port {port_num}')

                udp_packet = IP(dst=self.target_host.get_ip()) / UDP(dport=port_num)

                response = sr1(udp_packet, timeout=self.timeout, verbose=0)

                port_status = self.PORT_STATUS_CLOSED

                if response is None:
           
                    port_status = self.PORT_STATUS_NO_RESPONSE
                elif response.haslayer(ICMP):
                    
                    port_status = self.PORT_STATUS_CLOSED
                else:
                    
                    port_status = self.PORT_STATUS_OPEN

                self.target_host.set_udp_port_status(port_num, port_status)