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

# Leaf
s1_dpid = '110'
s2_dpid = '120'
s3_dpid = '130'
s4_dpid = '140'

# Spine
s5_dpid = '1010'
s6_dpid = '1020'
s7_dpid = '1030'
s8_dpid = '1040'

ofc_ip = '127.0.0.1'
ofc_port = 6641
ofp_ver_str = 'OpenFlow13'

def ofp_version(switch, protocols):
    protocols_str = ','.join(protocols)
    command = 'ovs-vsctl set Bridge %s protocols=%s' % (switch,protocols_str)
    switch.cmd(command)

def myTopo():
    net = Mininet(switch=OVSKernelSwitch)
    net.addController('controller01',controller=RemoteController,ip=ofc_ip, port=ofc_port)

    # Define Switch
    # Leaf
    s1 = net.addSwitch('leaf1', dpid=s1_dpid)
    s2 = net.addSwitch('leaf2', dpid=s2_dpid)
    s3 = net.addSwitch('leaf3', dpid=s3_dpid)
    s4 = net.addSwitch('leaf4', dpid=s4_dpid)

    # Spine
    s5 = net.addSwitch('spine1', dpid=s5_dpid)
    s6 = net.addSwitch('spine2', dpid=s6_dpid)
    s7 = net.addSwitch('spine3', dpid=s7_dpid)
    s8 = net.addSwitch('spine4', dpid=s8_dpid)

    # Define Host
    leaf1_hosts = [ net.addHost( 'l1_h%d' % i ) for i in range(1, 36+1) ]
    leaf2_hosts = [ net.addHost( 'l2_h%d' % i ) for i in range(1, 36+1) ]
    leaf3_hosts = [ net.addHost( 'l3_h%d' % i ) for i in range(1, 36+1) ]
    leaf4_hosts = [ net.addHost( 'l4_h%d' % i ) for i in range(1, 36+1) ]

    # Define Links
    for host in leaf1_hosts:
        net.addLink( s1, host ) 
    for host in leaf2_hosts:
        net.addLink( s2, host ) 
    for host in leaf3_hosts:
        net.addLink( s3, host ) 
    for host in leaf4_hosts:
        net.addLink( s4, host ) 

    net.addLink(s1, s5) 
    net.addLink(s1, s6) 
    net.addLink(s1, s7) 
    net.addLink(s1, s8) 
    net.addLink(s2, s5) 
    net.addLink(s2, s6) 
    net.addLink(s2, s7) 
    net.addLink(s2, s8) 

    net.start()

    ofp_version(s1, ['OpenFlow13']) 
    ofp_version(s2, ['OpenFlow13']) 
    ofp_version(s3, ['OpenFlow13']) 
    ofp_version(s4, ['OpenFlow13']) 
    ofp_version(s5, ['OpenFlow13']) 
    ofp_version(s6, ['OpenFlow13']) 
    ofp_version(s7, ['OpenFlow13']) 
    ofp_version(s8, ['OpenFlow13']) 

    print "Dumping node connections"
    dumpNodeConnections(net.switches)
    dumpNodeConnections(net.hosts)

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    myTopo()

