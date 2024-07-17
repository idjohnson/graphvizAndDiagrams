from diagrams import Diagram
from diagrams.gcp.compute import GKE
from diagrams.gcp.network import FirewallRules, LoadBalancing
from diagrams.onprem.client import User
from diagrams.onprem.network import  Internet
from diagrams.gcp.database import SQL

with Diagram("GCP Load Balancer with Istio on GKE", direction="TB", show=True):
    users = User("Users")
    internet = Internet("Internet")
    firewall = FirewallRules("FirewallRules")
    lb = LoadBalancing("Load Balancer")
    gke = GKE("GKE Cluster")
    istio = gke >> GKE("Istio")
    virtual_service = istio >> GKE("Virtual Service")
    service_a = istio >> GKE("Service A")
    service_b = istio >> GKE("Service B")
    database = SQL("SQL")

    users >> internet
    internet >> firewall >> lb
    lb >> virtual_service
    virtual_service >> service_a
    virtual_service >> service_b
    service_a >> database
    service_b >> database
