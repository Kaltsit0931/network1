#!/bin/bash

# 停止所有交换机的流
ovs-vsctl --all destroy

# 添加流规则以防止环路
# 这里需要根据你的网络配置添加具体的流规则
# 示例：
sudo ovs-ofctl add-flow s1 "in_port=1,actions=output:2"
sudo ovs-ofctl add-flow s2 "in_port=1,actions=output:2"
sudo ovs-ofctl add-flow s2 "in_port=2,actions=output:1"
sudo ovs-ofctl add-flow s3 "in_port=1,actions=output:2"
