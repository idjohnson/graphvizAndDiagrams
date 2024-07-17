from diagrams import Cluster, Diagram
from diagrams.azure.compute import AKS
from diagrams.azure.network import LoadBalancers, VirtualNetworks
from diagrams.azure.security import KeyVaults
from diagrams.onprem.network import Istio
from diagrams.k8s.compute import Pod
from diagrams.k8s.network import SVC

with Diagram("Azure Architecture", show=True):
    load_balancer = LoadBalancers("Load Balancer")
    virtual_network = VirtualNetworks("Virtual Network")
    key_vault = KeyVaults("AKV")

    with Cluster("AKS Cluster"):
        aks = AKS("AKS")
        istio = Istio("Istio")

        with Cluster("Node Pools"):
            node_pools = [Pod("Node Pool 1"), Pod("Node Pool 2")]

        with Cluster("Services"):
            svc_group = [SVC("service1"), SVC("service2")]

    load_balancer >> virtual_network >> aks >> node_pools >> istio >> svc_group >> key_vault
