# K-Means Clustering

## Overview
This project implements the K-Means clustering algorithm from scratch and applies it to a 2D dataset. The implementation demonstrates the core concepts of unsupervised learning through iterative centroid updates and point assignments.

## Dataset
- `k-means-dataset.csv`: 2D data points (x, y coordinates) for clustering

## Custom Implementation
The project includes a custom `MyKMeans` class with the following features:
- **Initialization**: Random centroid placement within data range
- **Euclidean Distance**: Calculates distance between points and centroids
- **Iterative Fitting**: Updates centroids until convergence
- **Clustering**: Assigns each point to nearest centroid

## Algorithm
1. Initialize k random centroids within the data range
2. Assign each point to the nearest centroid
3. Recalculate centroid positions based on cluster members
4. Repeat steps 2-3 until convergence (no changes in assignments)

## Key Components
- **n_clusters**: Number of clusters to form
- **clustered_data**: List containing points in each cluster
- **centroids**: Current centroid positions
- **iterations**: Counter for convergence tracking
- **ecludian_distance()**: Computes L2 distance between points

## Visualization
- Scatter plots showing data points and cluster assignments
- Centroid visualization
- Iterative cluster formation process

## Usage
Open `K-Means-Test.ipynb` in Jupyter Notebook to explore the K-Means clustering algorithm and visualizations.

## Requirements
- pandas
- numpy
- matplotlib
