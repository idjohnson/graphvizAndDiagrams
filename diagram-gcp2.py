from diagrams import Cluster, Diagram
from diagrams.gcp.network import LoadBalancing
from diagrams.gcp.compute import GKE
from diagrams.onprem.network import Istio
from diagrams.k8s.network import SVC
from diagrams.k8s.compute import Pod

with Diagram("GCP Architecture", show=True):
    load_balancer = LoadBalancing("Load Balancer")

    with Cluster("GKE Cluster"):
        gke = GKE("GKE")
        istio = Istio("Istio")
        istio2 = Istio("Istio")

        with Cluster("Services"):
            svc_group = [SVC("service1"), SVC("service2")]

        with Cluster("Pods"):
            pod_group = [Pod("pod1"), Pod("pod2")]

    load_balancer >> gke >> istio >> svc_group >> istio2 >> pod_group
   