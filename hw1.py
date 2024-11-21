from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.node import OVSController
import time

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
        self.addLink(s1, s2, bw=15)  
        self.addLink(s2, s3, bw=15) 

def run():
    topo = CustomTopo()
    net = Mininet(topo=topo, controller=OVSController, link=TCLink)
    net.start()
    
    print("Starting iperf3 tests...")
    
    h1 = net.get('h1')
    h3 = net.get('h3')
    
    h1.cmd('iperf3 -s &')
    print("Testing TCP throughput from h1 to h3...")
    print(h3.cmd('iperf3 -c ' + h1.IP() + ' -t 10'))

    
    h2 = net.get('h2')
    h4 = net.get('h4')
    
    h2.cmd('iperf3 -s &')
    print("Testing TCP throughput from h2 to h4...")
    print(h4.cmd('iperf3 -c ' + h2.IP() + ' -t 10'))
    
    CLI(net) 
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
