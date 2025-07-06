class TargetHost: 
    """This is the target of the scan
    Attribute: 
        ip: string ip of the target
    """

    ip: str
    ports: dict

    def __init__(self, ip):
        self.ip = ip
        self.ports = {}
    
    def set_ports(self, ports: dict): 

        self.ports = ports

    def get_ip(self) -> str: 

        return self.ip

    def get_ports(self) -> dict: 

        return self.ports
    
    def set_tcp_port_status(self, port_number: int, status: str): 

        self.ports[port_number].set_status(status, 'tcp')

    def set_udp_port_status(self, port_number: int, status: str): 

        self.ports[port_number].set_status(status, 'udp')