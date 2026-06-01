def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:

	iter_num = 0
	
	centroids = initial_centroids
	dimensions = len(initial_centroids[0])

	while iter_num < max_iterations:

		clusters = {}

		# assign each point to nearest centroid
		for pointidx in range(len(points)):
			point = points[pointidx]
			nearest_centroid_dist = float("inf")
			for centroididx in range(len(centroids)):
				centroid = centroids[centroididx]
				dist_point_centroid = funcdistcompute(point, centroid, dimensions)
				if dist_point_centroid < nearest_centroid_dist:
					nearest_centroid_dist = dist_point_centroid
					nearest_centroid_idx = centroididx
			
			if nearest_centroid_idx not in clusters:
				clusters[nearest_centroid_idx] = []
			clusters[nearest_centroid_idx].append(point)
		
		# recompute centroids for each cluster
		for cluster in clusters.keys():
			points_in_cluster = clusters[cluster]
			if len(points_in_cluster) == 0:
				continue
			new_centroid = [None]*len(initial_centroids[0])
			for dimidx in range(dimensions):
				dim_sum = 0
				for point in points_in_cluster:
					dim_sum += point[dimidx]
				new_centroid[dimidx] = dim_sum / len(points_in_cluster)
			centroids[cluster] = tuple(new_centroid)
		
		iter_num += 1

	return centroids

def funcdistcompute(point1, point2, dimensions):
	euc_dist_sqd = 0
	for dimidx in range(dimensions):
		euc_dist_sqd += (point1[dimidx] - point2[dimidx])**2
	return euc_dist_sqd
