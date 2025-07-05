class PortUtils: 

    """A utility class which contains supporting methods find required ports for the scan"""

    ALL_PORTS = 'all'
    WELL_KNOWN_PORTS = 'wp'
    REGISTERED_PORTS = 'rp'
    VALID_PORT_TYPES = {ALL_PORTS, WELL_KNOWN_PORTS, REGISTERED_PORTS}

    LOW_PORT = 1
    HIGH_PORT = 65535

    WELL_KNOWN_HIGH_PORT = 1023
    REGISTERED_LOW_PORT = 1024
    REGISTERED_HIGH_PORT = 49151

    START_LABEL = 'start'
    END_LABEL = 'end'

    VALID_PORT_RANGES = {
        ALL_PORTS: {
            START_LABEL: LOW_PORT,
            END_LABEL: HIGH_PORT
        },
        WELL_KNOWN_PORTS: {
            START_LABEL: LOW_PORT,
            END_LABEL: WELL_KNOWN_HIGH_PORT           
        }, 
        REGISTERED_PORTS: {
            START_LABEL: REGISTERED_LOW_PORT,
            END_LABEL: REGISTERED_HIGH_PORT           
        }
    }


    @staticmethod
    def parse_port(ports: str) -> dict: 
        """Validate the input port value is valid
        Args:
            ports: string of the port range text

        Returns: boolean
        """

        if ports in PortUtils.VALID_PORT_TYPES: 

            return PortUtils.VALID_PORT_RANGES[ports]
        
        elif '-' in ports: 
            try: 
                p_start, p_end = map(int, ports.split('-'))

                if PortUtils.LOW_PORT <= p_start <= p_end <= PortUtils.HIGH_PORT:
                    return {
                        PortUtils.START_LABEL: p_start,
                        PortUtils.END_LABEL: p_end
                    }
                
                raise ValueError('Ports must be 0-65535 and start ≤ end')

            except ValueError:
                raise ValueError('Invalid range format. Use start-end')
            
        else: 

            try: 
                port = int(ports)

                if PortUtils.LOW_PORT <= port <= PortUtils.HIGH_PORT:
                    return {
                        PortUtils.START_LABEL: port,
                        PortUtils.END_LABEL: port
                    }

                raise ValueError('Ports must be 0-65535 and start ≤ end')
            except ValueError: 
                raise ValueError('Invalid port')