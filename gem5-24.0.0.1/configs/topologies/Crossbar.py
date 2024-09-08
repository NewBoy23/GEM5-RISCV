# Copyright (c) 2010 Advanced Micro Devices, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met: redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer;
# redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution;
# neither the name of the copyright holders nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
from topologies.BaseTopology import SimpleTopology

from m5.objects import *
from m5.params import *


class Crossbar(SimpleTopology):
    description = "Crossbar"

    def makeTopology(self, options, network, IntLink, ExtLink, Router):
        # default values for link latency and router latency.
        # Can be over-ridden on a per link/router basis
        link_latency = options.link_latency  # used by simple and garnet
        router_latency = options.router_latency  # only used by garnet

        # Create an individual router for each controller plus one more for
        # the centralized crossbar.  The large numbers of routers are needed
        # because external links do not model outgoing bandwidth in the
        # simple network, but internal links do.
        # For garnet, one router suffices, use CrossbarGarnet.py

        routers = [Router(router_id=i) for i in range(len(self.nodes) + 1)]
        xbar = routers[
            len(self.nodes)
        ]  # the crossbar router is the last router created
        network.routers = routers

        ext_links = [
            ExtLink(
                link_id=i,
                ext_node=n,
                int_node=routers[i],
                latency=link_latency,
            )
            for (i, n) in enumerate(self.nodes)
        ]
        network.ext_links = ext_links

        link_count = len(self.nodes)

        int_links = []
        for i in range(len(self.nodes)):
            int_links.append(
                IntLink(
                    link_id=(link_count + i),
                    src_node=routers[i],
                    dst_node=xbar,
                    latency=link_latency,
                )
            )

        link_count += len(self.nodes)

        for i in range(len(self.nodes)):
            int_links.append(
                IntLink(
                    link_id=(link_count + i),
                    src_node=xbar,
                    dst_node=routers[i],
                    latency=link_latency,
                )
            )

        network.int_links = int_links
"""
# Copyright (c) 2010 Advanced Micro Devices, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met: redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer;
# redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution;
# neither the name of the copyright holders nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""
from topologies.BaseTopology import SimpleTopology

from m5.objects import *
from m5.params import *


class Crossbar(SimpleTopology):
    description = "Crossbar"

    def makeTopology(self, options, network, IntLink, ExtLink, Router):
        # default values for link latency and router latency.
        # Can be over-ridden on a per link/router basis
        link_latency = options.link_latency  # used by simple and garnet
        router_latency = options.router_latency  # only used by garnet

        # Create an individual router for each controller plus one more for
        # the centralized crossbar.  The large numbers of routers are needed
        # because external links do not model outgoing bandwidth in the
        # simple network, but internal links do.
        # For garnet, one router suffices, use CrossbarGarnet.py

        routers = [Router(router_id=i) for i in range(len(self.nodes) + 1)]
        xbar = routers[
            len(self.nodes)
        ]  # the crossbar router is the last router created
        network.routers = routers

        ext_links = [
            ExtLink(
                link_id=i,
                ext_node=n,
                int_node=routers[i],
                latency=link_latency,
            )
            for (i, n) in enumerate(self.nodes)
        ]
        network.ext_links = ext_links

        link_count = len(self.nodes)

        int_links = []
        for i in range(len(self.nodes)):
            int_links.append(
                IntLink(
                    link_id=(link_count + i),
                    src_node=routers[i],
                    dst_node=xbar,
                    latency=link_latency,
                )
            )

        link_count += len(self.nodes)

        for i in range(len(self.nodes)):
            int_links.append(
                IntLink(
                    link_id=(link_count + i),
                    src_node=xbar,
                    dst_node=routers[i],
                    latency=link_latency,
                )
            )

        network.int_links = int_links
"""
# Copyright (c) 2010 Advanced Micro Devices, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met: redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer;
# redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution;
# neither the name of the copyright holders nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from topologies.BaseTopology import SimpleTopology

from m5.objects import *
from m5.params import *


class Crossbar(SimpleTopology):
    description = "Crossbar"

    def makeTopology(self, options, network, IntLink, ExtLink, Router):
        # default values for link latency and router latency.
        # Can be over-ridden on a per link/router basis
        link_latency = options.link_latency  # used by simple and garnet
        router_latency = options.router_latency  # only used by garnet

        # Create an individual router for each controller plus one more for
        # the centralized crossbar.  The large numbers of routers are needed
        # because external links do not model outgoing bandwidth in the
        # simple network, but internal links do.
        # For garnet, one router suffices, use CrossbarGarnet.py

        routers = [Router(router_id=i) for i in range(len(self.nodes) + 1)]
        xbar = routers[
            len(self.nodes)
        ]  # the crossbar router is the last router created

        dir_router = [routers[len(self.nodes)-1],routers[len(self.nodes)-2]]
        network.routers = routers
        # for (i,node) in enumerate(self.nodes):
            # print(f"第{i}个节点为{node},它的类型为{type(node)}")
        # 连接每个node和路由器
        ext_links = [
            ExtLink(
                link_id=i,
                ext_node=n,
                int_node=routers[i],
                latency=link_latency,
            )
            for (i, n) in enumerate(self.nodes)
        ]
        network.ext_links = ext_links

        link_count = len(self.nodes)

        # 连接每个node到xbar路由器节点
        """
        int_links = []
        for i in range(len(self.nodes)):
            int_links.append(
                IntLink(
                    link_id=(link_count + i),
                    src_node=routers[i],
                    dst_node=xbar,
                    latency=link_latency,
                )
            )
            link_count += len(self.nodes)
        for i in range(len(self.nodes)):
            int_links.append(
                IntLink(
                    link_id=(link_count + i),
                    src_node=xbar,
                    dst_node=routers[i],
                    latency=link_latency,
                )
            )

        network.int_links = int_links
        """
        # 连接特定node到xbar路由器节点
        print(f"**************************连接特定节点到指定路由器****************************")
        print(f"**********************************start***********************************")
        int_links = []
        cnt_dir = 0
        for i in range(len(self.nodes)):
            # 连接: l0cache,l1cache,l2cache --> router_xbar
            if type(self.nodes[i]) != Directory_Controller:
                print(f"{type(self.nodes[i])} --> R_xbar")
                int_links.append(
                    IntLink(
                        link_id=link_count,
                        src_node=routers[i],
                        dst_node=xbar,
                        latency=link_latency,
                    )
                )
                link_count += 1
            # 连接: l2cache --> router_dir
            if type(self.nodes[i]) == L2Cache_Controller:
                print(f"{type(self.nodes[i])} --> R_dir{cnt_dir}")
                int_links.append(
                    IntLink(
                        link_id=link_count,
                        src_node=routers[i],
                        dst_node=dir_router[cnt_dir],
                        latency=link_latency,
                    )
                )
                cnt_dir += 1
                link_count += 1
        cnt_dir = 0
        print(f"**********************************next************************************") 
        for i in range(len(self.nodes)):
            # 连接: router_xbar --> l0cache,l1cache,l2cache
            print(f"R_xbar --> {type(self.nodes[i])}")
            if type(self.nodes[i]) != Directory_Controller:
                int_links.append(
                    IntLink(
                        link_id=link_count,
                        src_node=xbar,
                        dst_node=routers[i],
                        latency=link_latency,
                    )
                )
                link_count += 1
            # 连接: router_dir --> l2cache
            if type(self.nodes[i]) == L2Cache_Controller:
                print(f"R_dir{cnt_dir} --> {type(self.nodes[i])}")
                int_links.append(
                    IntLink(
                        link_id=link_count,
                        src_node=dir_router[cnt_dir],
                        dst_node=routers[i],
                        latency=link_latency,
                    )
                )
                link_count += 1
                cnt_dir += 1
        print(f"**********************************end*************************************")    
        network.int_links = int_links
        
        


        


