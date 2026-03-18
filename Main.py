import networkx as nx
from sklearn.cluster import KMeans

# Create a simple graph (dummy example)
G = nx.karate_club_graph()

# Convert graph to adjacency matrix
A = nx.to_numpy_array(G)

# Apply KMeans clustering
kmeans = KMeans(n_clusters=2, random_state=0)
labels = kmeans.fit_predict(A)

# Print community labels
print("Community Labels:", labels)