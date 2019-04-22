import re, subprocess

def tracertIP(ip):
    p = subprocess.Popen(['tracert', ip], stdout=subprocess.PIPE)
    while True:
        line = p.stdout.readline()
        if not line:
            break
        print(line)

if __name__ == '__main__':
    tracertIP('192.168.2.1')