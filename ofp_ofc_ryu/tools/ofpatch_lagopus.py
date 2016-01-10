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

s1_dpid = '1'
s2_dpid = '2'
s3_dpid = '3'
s4_dpid = '4'
s5_dpid = '5'
s6_dpid = '6'
s7_dpid = '7'
s8_dpid = '8'
s9_dpid = '9'
s10_dpid = '16'
s11_dpid = '17'
s12_dpid = '18'


ofc_ip = '127.0.0.1'
ofc_port = 6641
ofp_ver_str = 'OpenFlow13'

l2sw_ofc_ip = '127.0.0.1'
l2sw_ofc_port = 6640

def myTopo():
    net = Mininet(switch=Lagopus)
    c1 = net.addController('controller_l2sw',controller=RemoteController,ip=l2sw_ofc_ip, port=l2sw_ofc_port)
    c2 = net.addController('controller01',controller=RemoteController,ip=ofc_ip, port=ofc_port)

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

    #net.start()
    print "*** Starting network"
    net.build()
    c1.start()
    c2.start()
    s1.start( [ c1 ] )
    s2.start( [ c1 ] )
    s3.start( [ c1 ] )
    s4.start( [ c1 ] )
    s5.start( [ c2 ] )
    s6.start( [ c2 ] )
    s7.start( [ c2 ] )
    s8.start( [ c2 ] )
    s9.start( [ c2 ] )
    s10.start( [ c2 ] )
    s11.start( [ c2 ] )
    s12.start( [ c2 ] )

    print "Dumping node connections"
    dumpNodeConnections(net.switches)
    dumpNodeConnections(net.hosts)

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    myTopo()

