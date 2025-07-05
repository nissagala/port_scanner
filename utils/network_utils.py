import ipaddress
import socket

class NetworkUtils: 

    """A utility class which contains supporting methods find required IPs for the scan"""

    def find_ips(self, target: str) -> tuple[str, ...]: 

        """Find the IP/s based on the target passed.
        Args: 
            target: target to find ips. This can be a IP or CIDR or Hostname    

        Returns: tuple of IP addresses
        """

        if(self.is_ip(target)): 

            return (target,)
        
        elif(self.is_cidr(target)): 

            return self.cidr_to_ips(target)
        
        else: 

            return self.hostname_to_ips(target)

    def is_ip(self, target: str) -> bool: 
        """Check whether the provided target value is a IP
        Args: 
            target: string value to check if a ip
        
        Returns: boolean, True if IP, False if not a IP
        """

        try: 

            ipaddress.ip_address(target)
            return True
        
        except ValueError: 

            return False
        
        
    def is_cidr(self, target: str) -> bool: 
        """Check whether the provided target value is a CIDR
        Args: 
            target: string value to check if a CIDR

        Retruns: boolean, True if CIDR, False if not a CIDR
        """
        try: 

            ipaddress.ip_network(target, strict=False)
            return True

        except ValueError: 

            return False
        
        
    def cidr_to_ips(self, cidr: str) -> tuple[str, ...]: 
        """Converts CIDR in to a tuple of IPs
        Args: 
            cidr: string CIDR value

        Returns: tuple of IPs
        """

        network = ipaddress.ip_network(cidr, strict=False) 

        return tuple(str(host) for host in network.hosts())


    def hostname_to_ips(self, hostname: str) -> tuple[str, ...]: 
        """Finds ips of a hostname
        Args: 
            hostname: string hostname value
        Returns: tuple of IPs
        """

        try: 

            ips = socket.getaddrinfo(hostname, None)

            unique_ips = tuple({ip[4][0] for ip in ips})

            return unique_ips
        
        except socket.gaierror:

            return ()