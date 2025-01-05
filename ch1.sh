#!/bin/bash

echo "Checking VM1 Network Configuration..."

# 检查 IP 地址和网络掩码
IP_ADDRESS=$(ifconfig h1-eth0 | grep 'inet ' | awk '{print \$2}')
NETMASK=$(ifconfig h1-eth0 | grep 'inet ' | awk '{print \$4}')
if [ "$IP_ADDRESS" != "10.0.0.1" ] || [ "$NETMASK" != "255.0.0.0" ]; then
    echo "Warning: h1-eth0 IP or netmask is not correctly set."
    echo "Expected: 10.0.0.1/255.0.0.0, Found: $IP_ADDRESS/$NETMASK"
else
    echo "h1-eth0 IP and netmask are correctly set."
fi

# 检查 s1 接口
s1_ip=$(ifconfig s1 | grep 'inet ' | awk '{print \$2}')
if [ "$s1_ip" != "10.0.0.2" ]; then
    echo "Warning: s1 IP is not correctly set."
    echo "Expected: 10.0.0.2, Found: $s1_ip"
else
    echo "s1 IP is correctly set."
fi

# 检查 br1 接口
br1_ip=$(ifconfig br1 | grep 'inet ' | awk '{print \$2}')
if [ "$br1_ip" != "192.168.118.3" ]; then
    echo "Warning: br1 IP is not correctly set."
    echo "Expected: 192.168.118.3, Found: $br1_ip"
else
    echo "br1 IP is correctly set."
fi

# 检查默认网关
default_gw=$(ip route | grep default | awk '{print \$3}')
if [ "$default_gw" != "192.168.118.201" ]; then
    echo "Warning: Default gateway is not correctly set."
    echo "Expected: 192.168.118.201, Found: $default_gw"
else
    echo "Default gateway is correctly set."
fi

# 检查 VXLAN 接口
vxlan1_status=$(ovs-vsctl list Interface vxlan1)
if [ -z "$vxlan1_status" ]; then
    echo "Warning: vxlan1 interface is not created."
else
    echo "vxlan1 interface is created."
fi

echo "VM1 Network Configuration Check Completed."