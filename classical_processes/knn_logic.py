from collections import Counter

def classify(distances, k):
    nearest_neighbors = distances[:k]
    class_votes = [neighbor[1] for neighbor in nearest_neighbors]
    return Counter(class_votes).most_common(1)[0][0]
