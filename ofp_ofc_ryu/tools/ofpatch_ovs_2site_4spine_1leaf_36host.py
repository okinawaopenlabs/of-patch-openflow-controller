#
# usage
#   sudo python .py
#
from mininet.cli import CLI
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import Link
from mininet.node import RemoteController,OVSKernelSwitch
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import Lagopus

ofc_ip = '127.0.0.1'
ofc_port = 6641
ofp_ver_str = 'OpenFlow13'

def ofp_version(switch, protocols):
    protocols_str = ','.join(protocols)
    command = 'ovs-vsctl set Bridge %s protocols=%s' % (switch,protocols_str)
    switch.cmd(command)

def l2_mode(switch):
    command = 'ovs-ofctl add-flow %s actions=normal -O OpenFlow13' % (switch)
    switch.cmd(command)

def myTopo():
    #net = Mininet(switch=Lagopus)
    net = Mininet(switch=OVSKernelSwitch)
    net.addController('controller01',controller=RemoteController,ip=ofc_ip, port=ofc_port)

    # Define Switch
    # Sites_SW
    sites_dpid = "{0:X}".format(1000000)
    sites_sw = net.addSwitch('si_sw', dpid=sites_dpid)

    ag_sw = []
    spine_sw = [[]]
    leaf_sw = [[]]
    hosts = [[[]]]
    for site_num in range(1,2+1):
        # AG_SW
        ag_dpid = "{0:X}".format(100000*site_num)
        ag_sw.append(net.addSwitch('ag%d' % site_num, dpid=ag_dpid))
        net.addLink(sites_sw, ag_sw[site_num-1])

        spine_site_sw = []
        for spine_num in range(1,4+1):
            # Spine
            spie_dpid = "{0:X}".format(site_num * 1000 + spine_num * 100)
            spine_site_sw.append(net.addSwitch('sp%d_site%d' % (spine_num, site_num), dpid=spie_dpid))
            net.addLink(ag_sw[site_num-1], spine_site_sw[spine_num-1])
        spine_sw.append(spine_site_sw)

        leaf_site_sw = []
        hosts_site = [[]]
        for leaf_num in range(1,1+1):
            # Leaf
            leaf_dpid = "{0:X}".format(site_num * 1000 + leaf_num)
            leaf_site_sw.append(net.addSwitch('le%d_si%d' % (leaf_num, site_num), dpid=leaf_dpid))

            hosts_site_leaf = []
            for host_num in range(1,37+1):
                # Host
                leaf_dpid = "{0:X}".format(site_num * 1000 + leaf_num)
                hosts_site_leaf.append(net.addHost('h%d_l%d_si%d' % (host_num, leaf_num, site_num)))
                net.addLink(leaf_site_sw[leaf_num-1], hosts_site_leaf[host_num-1])

        for spine_num in range(1,4+1):
            for leaf_num in range(1,1+1):
                net.addLink(spine_site_sw[spine_num-1], leaf_site_sw[leaf_num-1])

        leaf_sw.append(leaf_site_sw)
        hosts.append(hosts_site)

    net.start()

    print "Dumping node connections"
    dumpNodeConnections(net.switches)
    dumpNodeConnections(net.hosts)

    ofp_version(sites_sw, ['OpenFlow13'])
    l2_mode(sites_sw)

    for ag in ag_sw:
        ofp_version(ag, ['OpenFlow13'])
        l2_mode(ag)

    for spine_site_sw in spine_sw:
        for spine in spine_site_sw:
            ofp_version(spine, ['OpenFlow13'])

    for leaf_site_sw in leaf_sw:
        for leaf in leaf_site_sw:
            ofp_version(leaf, ['OpenFlow13'])

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    myTopo()

