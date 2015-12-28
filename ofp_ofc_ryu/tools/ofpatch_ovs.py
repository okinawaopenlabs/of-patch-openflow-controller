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

s1_dpid = '0000000000000001'
s2_dpid = '0000000000000002'
s3_dpid = '0000000000000003'
s4_dpid = '0000000000000004'
s5_dpid = '0000000000000005'
s6_dpid = '0000000000000006'
s7_dpid = '0000000000000007'
s8_dpid = '0000000000000008'
s9_dpid = '0000000000000009'
s10_dpid = '0000000000000010'
s11_dpid = '0000000000000011'
s12_dpid = '0000000000000012'

ofc_ip = '127.0.0.1'
ofc_port = 6641
ofp_ver_str = 'OpenFlow13'

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

    # Define Nodes
    # Sites_SW
    s1 = net.addSwitch('sites_sw', dpid=s1_dpid)

    # AG_SW
    s2 = net.addSwitch('ag_kane', dpid=s2_dpid)
    s3 = net.addSwitch('ag_its', dpid=s3_dpid)
    s4 = net.addSwitch('ag_jic', dpid=s4_dpid)

    # Spine
    s5 = net.addSwitch('sp_kane1', dpid=s5_dpid)
    s6 = net.addSwitch('sp_kane2', dpid=s6_dpid)
    s7 = net.addSwitch('sp_its1', dpid=s7_dpid)
    s8 = net.addSwitch('sp_jic1', dpid=s8_dpid)

    # Leaf
    s9 = net.addSwitch('le_kane1', dpid=s9_dpid)
    s10 = net.addSwitch('le_kane2', dpid=s10_dpid)
    s11 = net.addSwitch('le_its1', dpid=s11_dpid)
    s12 = net.addSwitch('le_jic1', dpid=s12_dpid)

    # Host
    h1 = net.addHost('h_kane1')
    h2 = net.addHost('h_kane2')
    h3 = net.addHost('h_kane3')
    h4 = net.addHost('h_its1')
    h5 = net.addHost('h_jic1')
    hx = net.addHost('h_kane_x')

    # Define Links
    # Note:
    # mininet port number must match DB port number.
    # following "addlink" is sorted.  

    # SItes_SW -> AG_SW
    net.addLink(s1, s2)
    net.addLink(s1, s3)
    net.addLink(s1, s4)

    # Leaf -> Host
    net.addLink(s9, h1)
    net.addLink(s9, h2)

    net.addLink(s10, h3)
    net.addLink(s10, hx)

    net.addLink(s11, h4)

    net.addLink(s12, h5)

    # Spine -> Leaf
    net.addLink(s5, s9)
    net.addLink(s5, s10)
    net.addLink(s6, s9)
    net.addLink(s6, s10)

    net.addLink(s7, s11)

    net.addLink(s8, s12)

    # AG_SW -> Spine
    net.addLink(s2, s5)
    net.addLink(s2, s6)

    net.addLink(s3, s7)

    net.addLink(s4, s8)

    net.start()

    print "Dumping node connections"
    dumpNodeConnections(net.switches)
    dumpNodeConnections(net.hosts)

    ofp_version(s1, ['OpenFlow13'])
    ofp_version(s2, ['OpenFlow13'])
    ofp_version(s3, ['OpenFlow13'])
    ofp_version(s4, ['OpenFlow13'])
    ofp_version(s5, ['OpenFlow13'])
    ofp_version(s6, ['OpenFlow13'])
    ofp_version(s7, ['OpenFlow13'])
    ofp_version(s8, ['OpenFlow13'])
    ofp_version(s9, ['OpenFlow13'])
    ofp_version(s10, ['OpenFlow13'])
    ofp_version(s11, ['OpenFlow13'])
    ofp_version(s12, ['OpenFlow13'])

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    myTopo()

