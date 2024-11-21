#!/bin/bash
# 添加流规则以允许h1到h2、h3、h4的流量
# h1 -> s1 -> s2 -> h2
ovs-ofctl add-flow s1 "in_port=1,actions=output:2"  # h1 to s1
ovs-ofctl add-flow s2 "in_port=1,actions=output:2"  # s2 to h2

# h1 -> s1 -> s3 -> h3
ovs-ofctl add-flow s1 "in_port=2,actions=output:1"  # s1 to h1
ovs-ofctl add-flow s3 "in_port=1,actions=output:2"  # s3 to h3

# h1 -> s1 -> s3 -> h4
ovs-ofctl add-flow s3 "in_port=2,actions=output:3"  # s3 to h4

# 添加s2和s3之间的新链接的流规则
# s2 <-> s3
ovs-ofctl add-flow s2 "in_port=2,actions=output:1"  # s2 to s3
ovs-ofctl add-flow s3 "in_port=1,actions=output:2"  # s3 to s2

# 添加h2和h3之间的流规则
# h2 -> s2 -> s3 -> h3
ovs-ofctl add-flow s2 "in_port=2,actions=output:1"  # h2 to s2
ovs-ofctl add-flow s3 "in_port=1,actions=output:2"  # s3 to h3

# 添加h3和h4之间的流规则
# h3 -> s3 -> h4
ovs-ofctl add-flow s3 "in_port=2,actions=output:3"  # h3 to s3
ovs-ofctl add-flow s3 "in_port=1,actions=output:2"  # s3 to h4

# 添加h1和h4之间的流规则
# h1 -> s1 -> s3 -> h4
ovs-ofctl add-flow s1 "in_port=1,actions=output:2"  # h1 to s1
ovs-ofctl add-flow s3 "in_port=2,actions=output:3"  # s3 to h4