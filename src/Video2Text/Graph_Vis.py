import streamlit as st
import graphviz
import random

# Create a graphlib graph object
graph = graphviz.Digraph()
graph.attr()

def addEdge(origin, destination):
    graph.edge(origin, destination)

def addNode(topic):
    graph.node(topic, color='transparent')

def add_layer(new_dict, old_dict):
    new_topics = new_dict.keys()
    for topic in new_topics:
        if topic in old_dict.keys():
            topic_name = topic + str(random.uniform(0.0,1.0))
            addNode(topic_name)
            addEdge(topic, topic_name)
        else:
            addNode(topic)
            addEdge(topic, list(old_dict.keys())[0])

def create_graph(list_of_dicts):

    # Create first layer
    for topic in list_of_dicts[0].keys():
        addNode(topic)
    
    for i in range(len(list_of_dicts) - 1):
        add_layer(list_of_dicts[i], list_of_dicts[i+1])

    st.graphviz_chart(graph)



# graph.node('run', color='transparent')
# graph.node('intr', color='transparent')
# graph.node('runbl', color='transparent')

# graph.edge('run', 'intr', label='run')
# graph.edge('intr', 'runbl')
# graph.edge('runbl', 'run')
# graph.edge('run', 'kernel')
# graph.edge('kernel', 'zombie')
# graph.edge('kernel', 'sleep')
# graph.edge('kernel', 'runmem')
# graph.edge('sleep', 'swap')
# graph.edge('swap', 'runswap')
# graph.edge('runswap', 'new')
# graph.edge('runswap', 'runmem')
# graph.edge('new', 'runmem')
# graph.edge('sleep', 'runmem')



