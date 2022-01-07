import fire
from script.portInfo import getPortInfo 
def portChecker(port):
    '''try main.py --port <what port> to know what port is?'''
    port,description = getPortInfo(port,"https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers")
    print(f'''
    Port: {port}
    description: {description}
    ''')
if __name__ == "__main__":
    fire.Fire(portChecker)