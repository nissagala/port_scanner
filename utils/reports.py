import json

class Reports: 

    def generate_json_report(targets: dict): 

        targetstr = []
        for target in targets: 

            ports = target.get_ports()
            portstr = []
            for port_num, port_obj in ports.items(): 
                current_port = {}
                current_port['number'] = port_num

                port_status = port_obj.get_status()

                if(port_status['tcp'] != ''): 
                    current_port['tcp'] = port_status['tcp']

                if(port_status['udp'] != ''): 
                    current_port['udp'] = port_status['udp']       

                portstr.append(current_port)

            current_target = {
                'target': target.get_ip(),
                'ports': portstr
            }

            targetstr.append(current_target)


        print(json.dumps(targetstr, indent=4))



    def generate_text_report(targets: dict): 

        targetstr = []
        for target in targets: 
            print(f"\nTarget: {target.get_ip()}")
            print("-" * 30)
            ports = target.get_ports()
            portstr = []
            for port_num, port_obj in ports.items(): 
                current_port = []
                current_port.append('Port: ' + str(port_num))

                port_status = port_obj.get_status()

                if(port_status['tcp'] != ''): 
                    current_port.append('TCP: ' + port_status['tcp'])

                if(port_status['udp'] != ''): 
                    current_port.append('UDP: ' + port_status['udp'])    

                print(' | '.join(current_port))
                # portstr.append(current_port)

            current_target = {
                'target': target.get_ip(),
                'ports': portstr
            }

            targetstr.append(current_target)

