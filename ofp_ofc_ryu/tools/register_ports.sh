curl -X POST -H "Content-Type:application/json" -d "{'portName':'spine1-eth1','portNumber':1,'band':'10Gbps'}" "http://localhost:18080/ofpm/device_mng/port/spine1"  
curl -X POST -H "Content-Type:application/json" -d "{'portName':'spine1-eth2','portNumber':2,'band':'10Gbps'}" "http://localhost:18080/ofpm/device_mng/port/spine1"  

curl -X POST -H "Content-Type:application/json" -d "{'portName':'leaf1-eth1','portNumber':1,'band':'10Gbps'}" "http://localhost:18080/ofpm/device_mng/port/leaf1"  
curl -X POST -H "Content-Type:application/json" -d "{'portName':'leaf1-eth2','portNumber':2,'band':'1Gbps'}" "http://localhost:18080/ofpm/device_mng/port/leaf1"  
curl -X POST -H "Content-Type:application/json" -d "{'portName':'leaf1-eth3','portNumber':3,'band':'1Gbps'}" "http://localhost:18080/ofpm/device_mng/port/leaf1"  
curl -X POST -H "Content-Type:application/json" -d "{'portName':'leaf2-eth1','portNumber':1,'band':'10Gbps'}" "http://localhost:18080/ofpm/device_mng/port/leaf2"  
curl -X POST -H "Content-Type:application/json" -d "{'portName':'leaf2-eth2','portNumber':2,'band':'1Gbps'}" "http://localhost:18080/ofpm/device_mng/port/leaf2"  
curl -X POST -H "Content-Type:application/json" -d "{'portName':'leaf2-eth3','portNumber':3,'band':'1Gbps'}" "http://localhost:18080/ofpm/device_mng/port/leaf2"  

curl -X POST -H "Content-Type:application/json" -d "{'portName':'host1-eth0','portNumber':1,'band':'1Gbps'}" "http://localhost:18080/ofpm/device_mng/port/host1"  
curl -X POST -H "Content-Type:application/json" -d "{'portName':'host2-eth0','portNumber':1,'band':'1Gbps'}" "http://localhost:18080/ofpm/device_mng/port/host2"  
curl -X POST -H "Content-Type:application/json" -d "{'portName':'host3-eth0','portNumber':1,'band':'1Gbps'}" "http://localhost:18080/ofpm/device_mng/port/host3"  
curl -X POST -H "Content-Type:application/json" -d "{'portName':'host4-eth0','portNumber':1,'band':'1Gbps'}" "http://localhost:18080/ofpm/device_mng/port/host4"  
