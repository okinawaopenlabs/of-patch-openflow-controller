#
# usage
#   sudo python mininet_3sw4host_topo.py
#
from mininet.cli import CLI
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import Link
from mininet.node import RemoteController,OVSKernelSwitch
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import Lagopus

s1_dpid = '10'

ofc_ip = '127.0.0.1'
ofc_port = 6641
ofp_ver_str = 'OpenFlow13'

def myTopo():
    net = Mininet(switch=Lagopus)
    net.addController('controller01',controller=RemoteController,ip=ofc_ip, port=ofc_port)

    # Define Switch
    # Leaf
    s1 = net.addSwitch('leaf1', dpid=s1_dpid)

    # Define Host
    hosts = [ net.addHost( 'h%d' % i ) for i in range(0+1,48+1) ]

    # Define Links
    for host in hosts:
        net.addLink( s1, host ) 

    net.start()

    print "Dumping node connections"
    dumpNodeConnections(net.switches)
    dumpNodeConnections(net.hosts)

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    myTopo()

