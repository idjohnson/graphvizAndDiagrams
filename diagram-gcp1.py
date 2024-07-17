# diagram.py
from diagrams import Diagram
from diagrams.gcp.compute import GCE 
from diagrams.gcp.database import SQL
from diagrams.gcp.network import LoadBalancing

with Diagram("Web Service", show=True, direction="LR"):
        LoadBalancing("External LB") >> GCE ("uMIG backend pool") >> GCE("VM") >> SQL("CloudSQL")
        SQL("CloudSQL") >> GCE("VM") 