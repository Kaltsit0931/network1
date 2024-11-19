#!/bin/bash

# Add flow rules to prevent broadcast storms
ovs-ofctl add-flow s2 "in_port=1,actions=output:2"  # h1 to s2
ovs-ofctl add-flow s2 "in_port=2,actions=output:1"  # s2 to h1
ovs-ofctl add-flow s2 "in_port=3,actions=output:4"  # h2 to s2
ovs-ofctl add-flow s2 "in_port=4,actions=output:3"  # s2 to h2
ovs-ofctl add-flow s2 "in_port=5,actions=output:6"  # h4 to s2
ovs-ofctl add-flow s2 "in_port=6,actions=output:5"  # s2 to h4
