import fire
from script.wport import wport

def portChecker(port):
    '''try main.py --port <what port> to know what port is?'''
    wport("Searching port Information...",port)
    print(f'''
    Port: {port}
    description: {description}
    ''')
if __name__ == "__main__":
    fire.Fire(portChecker)