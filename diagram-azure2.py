from graphviz import Digraph

# Create a new directed graph
dot = Digraph()

# Define nodes
dot.node('U', 'User', shape='ellipse')
dot.node('ALB', 'Azure\nLoad Balancer')
dot.node('WAS', 'Web App\nService')
dot.node('ASD', 'Azure SQL\nDatabase')
dot.node('ARC', 'Azure Redis\nCache')
dot.node('AS', 'Azure\nStorage')

# Define edges
dot.edge('U', 'ALB', label='HTTP/HTTPS')
dot.edge('ALB', 'WAS', label='Route traffic')
dot.edge('WAS', 'ASD', label='Read/Write Data')
dot.edge('WAS', 'ARC', label='Cache Data')
dot.edge('WAS', 'AS', label='Store Files')

# Print the dot graph
print(dot.source)
