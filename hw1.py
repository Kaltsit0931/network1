from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel

class MyTopo(Topo):
    def build(self):
        # Create switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        # Create hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        # Add links with specified bandwidth
        self.addLink(s1, s2, bw=15)  # Link between s1 and s2
        self.addLink(s2, s3, bw=15)  # Link between s2 and s3
        self.addLink(s1, h1)
        self.addLink(s2, h2)
        self.addLink(s3, h3)
        self.addLink(s2, h4)

def run():
    setLogLevel('info')
    topo = MyTopo()
    net = Mininet(topo=topo, link=TCLink)
    net.start()

    # Test TCP throughput between h1 and h3
    print("Testing TCP throughput between h1 and h3")
    net.iperf((net.get('h1'), net.get('h3')))

    # Test TCP throughput between h2 and h4
    print("Testing TCP throughput between h2 and h4")
    net.iperf((net.get('h2'), net.get('h4')))

    CLI(net)
    net.stop()

if __name__ == '__main__':
    run()
