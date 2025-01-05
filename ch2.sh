#!/bin/bash

echo "Checking VM2 Network Configuration..."

# 检查 IP 地址和网络掩码
IP_ADDRESS=$(ifconfig h2-eth0 | grep 'inet ' | awk '{print \$2}')
NETMASK=$(ifconfig h2-eth0 | grep 'inet ' | awk '{print \$4}')
if [ "$IP_ADDRESS" != "10.0.0.4" ] || [ "$NETMASK" != "255.0.0.0" ]; then
    echo "Warning: h2-eth0 IP or netmask is not correctly set."
    echo "Expected: 10.0.0.4/255.0.0.0, Found: $IP_ADDRESS/$NETMASK"
else
    echo "h2-eth0 IP and netmask are correctly set."
fi

# 检查 s2 接口
s2_ip=$(ifconfig s2 | grep 'inet ' | awk '{print \$2}')
if [ "$s2_ip" != "10.0.0.3" ]; then
    echo "Warning: s2 IP is not correctly set."
    echo "Expected: 10.0.0.3, Found: $s2_ip"
else
    echo "s2 IP is correctly set."
fi

# 检查 br1 接口
br1_ip=$(ifconfig br1 | grep 'inet ' | awk '{print \$2}')
if [ "$br1_ip" != "192.168.118.4" ]; then
    echo "Warning: br1 IP is not correctly set."
    echo "Expected: 192.168.118.4, Found: $br1_ip"
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
vxlan2_status=$(ovs-vsctl list Interface vxlan2)
if [ -z "$vxlan2_status" ]; then
    echo "Warning: vxlan2 interface is not created."
else
    echo "vxlan2 interface is created."
fi

echo "VM2 Network Configuration Check Completed."
