from sklearn.datasets import fetch_olivetti_faces

def loadData():

    faces = fetch_olivetti_faces()

    data = faces.data
    images = faces.images
    labels = faces.target

    return data, images, labels

