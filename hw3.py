from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel

class CustomTopo(Topo):
    def build(self):
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        self.addLink(h1, s1)
        self.addLink(h2, s2)
        self.addLink(h3, s3)
        self.addLink(h4, s3)
        self.addLink(s1, s2) 
        self.addLink(s2, s3) 
        self.addLink(s2, s3) 

def run():
    topo = CustomTopo()
    net = Mininet(topo=topo, link=TCLink)
    net.start()
    
    print("Testing connectivity between all hosts...")

    net.pingAll()
    
    CLI(net) 
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
