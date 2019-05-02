import numpy as np


class KMeans:
    
    def __init__(self, k=2, tol=0.001, max_iter=300):
        self.k = k # колличество кластеров
        self.tol = tol # точность
        self.max_iter=max_iter # максимальное колличество итераций
        
        
    def fit(self, data):
        self.centroids = {} # центроид (центры кластеров)
        
        for i in range(self.k):
            self.centroids[i] = data[i]
            
        print('centroid:', self.centroids)
            
        for i in range(self.max_iter):
            self.classifications = {}
            
            for i in range(self.k):
                self.classifications[i] = []
                
            for featureset in X:
                distances = [np.linalg.norm(featureset - self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(featureset)
            
            prev_centroids = dict(self.centroids)
            
            # уточняем центроид
            for classification in self.classifications:
                print('-'*100)
                print(self.classifications[classification])
                print(np.average(self.classifications[classification], axis=0))
                print('-'*100)
                self.centroids[classification] = np.average(self.classifications[classification], axis=0)

            optimized = True

            # когда остановить алгоритм
            for c in self.centroids:
                original_cetroid = prev_centroids[c]
                current_centroid = self.centroids[c]

                if np.sum((current_centroid-original_cetroid) / original_cetroid * 100.0) > self.tol:
                    optimized = False

            if optimized:
                break

    def predict(self, featureset):
        distances = [np.linalg.norm(featureset) - self.centroids[centroid] for centroid in self.centroids]
        classification = distances.index(min(distances))
        return classification