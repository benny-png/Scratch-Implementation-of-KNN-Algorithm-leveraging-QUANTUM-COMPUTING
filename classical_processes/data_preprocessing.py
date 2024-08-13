from sklearn.preprocessing import StandardScaler

def scale_data(X):
    scaler = StandardScaler()
    return scaler.fit_transform(X)
