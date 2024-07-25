import pydot
from IPython.display import Image, display

# Create the Graph with a top-to-bottom direction
graph = pydot.Dot(graph_type='digraph', rankdir='TB')

# Define the glycolysis enzyme steps in the order they occur
steps = [
    "Hexokinase",
    "Phosphoglucose Isomerase",
    "Phosphofructokinase-1",
    "Aldolase",
    "Triose Phosphate Isomerase",
    "Glyceraldehyde-3-Phosphate Dehydrogenase",
    "Phosphoglycerate Kinase",
    "Phosphoglycerate Mutase",
    "Enolase",
    "Pyruvate Kinase"
]

# Define the reactions associated with each enzyme
reactions = {
    "Hexokinase": "Phosphorylation of Glucose",
    "Phosphoglucose Isomerase": "Isomerization of Glucose-6-Phosphate",
    "Phosphofructokinase-1": "Phosphorylation of Fructose-6-Phosphate",
    "Aldolase": "Cleavage of Fructose-1,6-Bisphosphate",
    "Triose Phosphate Isomerase": "Isomerization of Dihydroxyacetone Phosphate",
    "Glyceraldehyde-3-Phosphate Dehydrogenase": "Oxidation and Phosphorylation of Glyceraldehyde-3-Phosphate",
    "Phosphoglycerate Kinase": "Substrate-Level Phosphorylation to Produce ATP",
    "Phosphoglycerate Mutase": "Rearrangement of 3-Phosphoglycerate",
    "Enolase": "Dehydration of 2-Phosphoglycerate",
    "Pyruvate Kinase": "Substrate-Level Phosphorylation to Produce Pyruvate"
}

# Add nodes to the graph
for enzyme in steps:
    label = enzyme
    # Add enzyme node
    enzyme_node = pydot.Node(enzyme, label=label, shape="rect", style="filled", fillcolor="lightblue")
    graph.add_node(enzyme_node)
    # Add reaction node
    reaction = reactions[enzyme]
    reaction_node = pydot.Node(reaction, label=reaction, shape="ellipse", style="filled", fillcolor="lightgreen")
    graph.add_node(reaction_node)
    # Add edge between enzyme and reaction
    graph.add_edge(pydot.Edge(enzyme, reaction))

# Add edges between successive enzymes
for i in range(len(steps) - 1):
    start = steps[i]
    end = steps[i + 1]
    graph.add_edge(pydot.Edge(reactions[start], reactions[end]))

# Save the graph as a PNG file
file_name = "glycolysis_steps_with_arrows.png"
graph.write_png(file_name)

# Display the graph
display(Image(file_name))

