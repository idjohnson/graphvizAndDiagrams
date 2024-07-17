from graphviz import Digraph

# Create a new directed graph
dot = Digraph('aws_diagram')

# Add nodes for ELB, EC2, and RDS
dot.node('A', 'ELB')
dot.node('B', 'EC2')
dot.node('C', 'RDS')

# Add edges between the nodes
dot.edges(['AB', 'BC'])

# Save the diagram to a file
dot.render('aws_diagram.gv', view=True)

