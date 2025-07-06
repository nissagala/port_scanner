class Port: 
    """This is Port class which is scanning main attribute of a target
    Attributes: 
        port_number: int number of the port
        status: dict contains tcp and udp status
    """

    port_number: int
    status: dict

    def __init__(self, port_number: int):
        self.port_number = port_number
        self.status = {
            'tcp': '',
            'udp': ''
        }

    def get_port_number(self) -> int: 

        return self.port_number
    
    def set_status(self, status: str, proto: str): 

        self.status[proto] = status

    def get_status(self) -> dict: 

        return self.status