from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI

class ChatTopo(Topo):
    def build(self):
        # Create four hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        # Create three switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        # Connect hosts to switches
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s2)
        self.addLink(h4, s3)

        # Connect switches
        self.addLink(s1, s2)
        self.addLink(s1, s3)

def run():
    topo = ChatTopo()
    net = Mininet(topo=topo)
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    run()
