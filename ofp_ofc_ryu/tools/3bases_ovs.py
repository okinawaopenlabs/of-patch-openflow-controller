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

# Sites SW
s1_dpid = '1'

# AG SW
s2_dpid = '2'
s3_dpid = '3'
s4_dpid = '4'

#Kanekadan has not Spine
# IT sinryo park Spine
s5_dpid = '44c'
s6_dpid = '4b0'

# Jicchaku Spine
s7_dpid = '834'
s8_dpid = '898'

#Kanekadan Leaf
s9_dpid = '3e9'

# IT sinryo park Leaf
s10_dpid = '7d1'
s11_dpid = '7d2'
s12_dpid = '7d3'
s13_dpid = '7d4'
s14_dpid = '7d5'
s15_dpid = '7d6'
s16_dpid = '7d7'
s17_dpid = '7d8'

# Jicchaku Leaf
s18_dpid = 'bb9'
s19_dpid = 'bba'
s20_dpid = 'bbb'
s21_dpid = 'bbc'
s22_dpid = 'bbd'
s23_dpid = 'bbe'

ofc_ip = '127.0.0.1'
ofc_port = 6641
ofp_ver_str = 'OpenFlow13'

# l2sw_ofc_ip = '127.0.0.1'
# l2sw_ofc_port = 6640

def ofp_version(switch, protocols):
    protocols_str = ','.join(protocols)
    command = 'ovs-vsctl set Bridge %s protocols=%s' % (switch,protocols_str)
    switch.cmd(command)

def l2_mode(switch):
    command = 'ovs-ofctl add-flow %s actions=normal -O OpenFlow13' % (switch)
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
    s5 = net.addSwitch('sp_its1', dpid=s5_dpid)
    s6 = net.addSwitch('sp_its2', dpid=s6_dpid)
    s7 = net.addSwitch('sp_jic1', dpid=s7_dpid)
    s8 = net.addSwitch('sp_jic2', dpid=s8_dpid)

    # Leaf
    s9 = net.addSwitch('le_kane1', dpid=s9_dpid)
    s10 = net.addSwitch('le_its1', dpid=s10_dpid)
    s11 = net.addSwitch('le_its2', dpid=s11_dpid)
    s12 = net.addSwitch('le_its3', dpid=s12_dpid)
    s13 = net.addSwitch('le_its4', dpid=s13_dpid)
    s14 = net.addSwitch('le_its5', dpid=s14_dpid)
    s15 = net.addSwitch('le_its6', dpid=s15_dpid)
    s16 = net.addSwitch('le_its7', dpid=s16_dpid)
    s17 = net.addSwitch('le_its8', dpid=s17_dpid)
    s18 = net.addSwitch('le_jic1', dpid=s18_dpid)
    s19 = net.addSwitch('le_jic2', dpid=s19_dpid)
    s20 = net.addSwitch('le_jic3', dpid=s20_dpid)
    s21 = net.addSwitch('le_jic4', dpid=s21_dpid)
    s22 = net.addSwitch('le_jic5', dpid=s22_dpid)
    s23 = net.addSwitch('le_jic6', dpid=s23_dpid)

    # Host
    kane_hosts = [ net.addHost( 'k_h%d' %n) for n in range(1,48)]

    its_leaf1_hosts = [ net.addHost( 'i_h%d' %n) for n in range( 1,36)]
    its_leaf2_hosts = [ net.addHost( 'i_h%d' %n) for n in range(37,72)]
    its_leaf3_hosts = [ net.addHost( 'i_h%d' %n) for n in range(73,108)]
    its_leaf4_hosts = [ net.addHost( 'i_h%d' %n) for n in range(109,144)]
    its_leaf5_hosts = [ net.addHost( 'i_h%d' %n) for n in range(145,180)]
    its_leaf6_hosts = [ net.addHost( 'i_h%d' %n) for n in range(181,216)]
    its_leaf7_hosts = [ net.addHost( 'i_h%d' %n) for n in range(217,252)]
    its_leaf8_hosts = [ net.addHost( 'i_h%d' %n) for n in range(253,288)]

    jic_leaf1_hosts = [ net.addHost( 'j_h%d' %n) for n in range( 1,36)]
    jic_leaf2_hosts = [ net.addHost( 'j_h%d' %n) for n in range(37,72)]
    jic_leaf3_hosts = [ net.addHost( 'j_h%d' %n) for n in range(73,108)]
    jic_leaf4_hosts = [ net.addHost( 'j_h%d' %n) for n in range(109,144)]
    jic_leaf5_hosts = [ net.addHost( 'j_h%d' %n) for n in range(145,180)]
    jic_leaf6_hosts = [ net.addHost( 'j_h%d' %n) for n in range(181,216)]

    # Define Links
    # Note:
    # mininet port number must match DB port number.
    # following "addlink" is sorted.  

    # Leaf -> Host
    # Kanekadan
    for h in kane_hosts:
      net.addLink(s9, h)

    # IT Sinryo park
    for h in its_leaf1_hosts:
      net.addLink(s10, h)

    for h in its_leaf2_hosts:
      net.addLink(s11, h)

    for h in its_leaf3_hosts:
      net.addLink(s12, h)

    for h in its_leaf4_hosts:
      net.addLink(s13, h)

    for h in its_leaf5_hosts:
      net.addLink(s14, h)

    for h in its_leaf6_hosts:
      net.addLink(s15, h)

    for h in its_leaf7_hosts:
      net.addLink(s16, h)

    for h in its_leaf8_hosts:
      net.addLink(s17, h)

    # IT Jichchaku
    for h in jic_leaf1_hosts:
      net.addLink(s18, h)

    for h in jic_leaf2_hosts:
      net.addLink(s19, h)

    for h in jic_leaf3_hosts:
      net.addLink(s20, h)

    for h in jic_leaf4_hosts:
      net.addLink(s21, h)

    for h in jic_leaf5_hosts:
      net.addLink(s22, h)

    for h in jic_leaf6_hosts:
      net.addLink(s23, h)

    # Spine -> Leaf
    net.addLink(s5, s10)
    net.addLink(s5, s11)
    net.addLink(s5, s12)
    net.addLink(s5, s13)
    net.addLink(s5, s14)
    net.addLink(s5, s15)
    net.addLink(s5, s16)
    net.addLink(s5, s17)
    net.addLink(s6, s10)
    net.addLink(s6, s11)
    net.addLink(s6, s12)
    net.addLink(s6, s13)
    net.addLink(s6, s14)
    net.addLink(s6, s15)
    net.addLink(s6, s16)
    net.addLink(s6, s17)

    net.addLink(s7, s18)
    net.addLink(s7, s19)
    net.addLink(s7, s20)
    net.addLink(s7, s21)
    net.addLink(s7, s22)
    net.addLink(s7, s23)
    net.addLink(s8, s18)
    net.addLink(s8, s19)
    net.addLink(s8, s20)
    net.addLink(s8, s21)
    net.addLink(s8, s22)
    net.addLink(s8, s23)
 
    # AG_SW -> Leaf, Spine
    net.addLink(s2, s9)
    net.addLink(s2, s6)

    net.addLink(s3, s5)
    net.addLink(s3, s6)

    net.addLink(s4, s7)
    net.addLink(s4, s8)

    # SItes_SW -> AG_SW
    net.addLink(s1, s2)
    net.addLink(s1, s3)
    net.addLink(s1, s4)

    print "*** Starting network"
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
    ofp_version(s13, ['OpenFlow13'])
    ofp_version(s14, ['OpenFlow13'])
    ofp_version(s15, ['OpenFlow13'])
    ofp_version(s16, ['OpenFlow13'])
    ofp_version(s17, ['OpenFlow13'])
    ofp_version(s18, ['OpenFlow13'])
    ofp_version(s19, ['OpenFlow13'])
    ofp_version(s20, ['OpenFlow13'])
    ofp_version(s21, ['OpenFlow13'])
    ofp_version(s22, ['OpenFlow13'])
    ofp_version(s23, ['OpenFlow13'])
 
    l2_mode(s1)
    l2_mode(s2)
    l2_mode(s3)
    l2_mode(s4)

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    myTopo()

