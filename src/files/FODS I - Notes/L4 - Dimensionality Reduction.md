# L4 - Dimensionality Reduction

## Background

### Unsupervised Learning

Typically concerns the ability to output useful characterizations (or groupings) of objects.

Objects for which no class labels have been given.

Valuable set of tools for exploratory analysis.

Bring out patterns and structure within datasets.

### Data Understanding - Dimensions

- Data Dimensionality: The number of features or attributes that each data point has.

- High-Dimensional Data: e.g. Images (pixels), Text (words), Genomics (genes). Each feature represents a dimension in a mathematical space.

- Increasing the number of features should lead to better performance
- The inclusion of more features leads to worse performance
- Need an exponential number of training examples as dimensionality increases
- The complexity of learning algorithms depends on the number of input dimensions, as well as the size of the data sample.

### The curse of dimensionality (高维灾难)

The volume of the space increase exponentially with the number of dimensions, making data sparse.

Adding a dimension "stretches" the points across that dimension, making them "further apart" - high dimensional data is extremely sparse.

More dimensions can lead to models that are too complex and fit noise rather than the underlying pattern.

### Dimensionality Reduction

Significant improvments can be achieved by first mapping the data into a lower-dimensional space
$$
\begin{equation}
x = \begin{bmatrix}
a_1 \\
a_2 \\
\cdots \\
a_N
\end{bmatrix} \to \text{reduce dimensionality} \to y = \begin{bmatrix}
b_1 \\
b_2 \\
\cdots \\
b_K
\end{bmatrix}, \quad K<<N
\end{equation}
$$
Dimensionality can be reduced by:

- Feature extraction
- Feature selection

## Feature Selection

### Filter Methods

Statistical techniques to evaluate the importance of features independently of any learning algorithm

- Fast, simple, independent of any learning algorithm
- Correlation coefficient, Chi-Suqared test ($\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}$)

### Wrapper Methods

Predictive models to evaluate the combination of features

- Takes feature interations into account, computationally expensive
- Forward selection, backward elimination

### Embedded Methods

During the model training process

- Incorporates feature selection in the model building process, more efficient than wrapper methods
- Feature importance using tree-based methods like decision trees.

> Question: How to find the "best" low dimensional space that conveys maximum useful information?
>
> Answer: Find "principal components"

## Feature Extraction

### Algorithm 1 - Principal Components Analysis (PCA)

Rotates a multivariate dataset into a new configuration which is easier to interpret.

Purpose: 

1. Simply D ?

Breaks down a multidimensional dataset into set of orthogonal components. (使用正交基表示？)

These components can explain almost all of the dataset variance.

These components deliver an abbreviated description of the dataset.

Dramatically reduces the dimensionality of a large data.

#### Basic Steps

1. Standardize data
2. Calculate the covariance matrix of the data
3. Calculate the eigenvectors and eigenvalues of the covariance matrix
4. Choose the principal components
5. Project data onto principal components

#### Step 1 - Standardization

The principal components are dependent on the units used to measure the original variables as well as on the range of values they assume.

Different measurements can have different ranges. (e.g. range in cm and weight in kg)

Data should always be standardized prior to using PCA.

A common standardzation method:
$$
\begin{equation}\label{standardization}
\frac{x_i-u}{\sigma}
\end{equation}
$$
Example: 

| Flower | Sepal Length (cm) | Sepal Width (cm) | Petal Length (cm) | Petak Width (cm) | Species |
| ------ | ----------------- | ---------------- | ----------------- | ---------------- | ------- |
| 0      | 5.1               | 3.5              | 1.4               | 0.2              | 0       |
| 1      | 4.9               | 3.0              | 1.4               | 0.2              | 0       |
| 2      | 4.7               | 3.2              | 1.3               | 0.2              | 0       |
| 3      | 4.6               | 3.1              | 1.5               | 0.2              | 0       |
| 4      | 5.0               | 3.6              | 1.4               | 0.2              | 0       |
| 5      | 5.4               | 3.9              | 1.7               | 0.4              | 0       |
| 6      | 4.6               | 3.4              | 1.4               | 0.3              | 0       |
| 7      | 5.0               | 3.4              | 1.5               | 0.2              | 0       |
| 8      | 4.4               | 2.9              | 1.4               | 0.2              | 0       |
| 9      | 4.9               | 3.1              | 1.5               | 0.1              | 0       |
| 10     | 5.4               | 3.7              | 1.5               | 0.2              | 0       |

use $\ref{standardization}$ and we can get

| Flower | Sepal Length (cm) | Sepal Width (cm) | Petal Length (cm) | Species |
| ------ | ----------------- | ---------------- | ----------------- | ------- |
| 0      | 5.1               | 3.5              | 1.4               | 0       |
| 1      | 4.9               | 3.0              | 1.4               | 0       |
| 2      | 4.7               | 3.2              | 1.3               | 0       |
| 3      | 4.6               | 3.1              | 1.5               | 0       |
| 4      | 5.0               | 3.6              | 1.4               | 0       |
| 5      | 5.4               | 3.9              | 1.7               | 0       |
| 6      | 4.6               | 3.4              | 1.4               | 0       |
| 7      | 5.0               | 3.4              | 1.5               | 0       |
| 8      | 4.4               | 2.9              | 1.4               | 0       |
| 9      | 4.9               | 3.1              | 1.5               | 0       |
| 10     | 5.4               | 3.7              | 1.5               | 0       |

#### Step 2 - Covariance Matrix

This matrix shows how the variables change together. For example if height and weight increase together, their covariance will be positive.
$$
\begin{equation}
\sigma_{jk} = \frac{1}{n} \sum_{i=1}^{n}\left(x_j^{(i)}-\mu_j\right)\left(x_k^{(i)}-\mu_k\right)
\end{equation}
$$

A positive covariance between two features indicated that the features increase or decrease together.

e.g. The covariance matrix of three features can be written as follows:
$$
\begin{equation}
\Sigma = \begin{bmatrix}
\sigma_1^2 & \sigma_{12} & \sigma_{13} \\
\sigma_{21} & \sigma_2^2 & \sigma_{23} \\
\sigma_{31} & \sigma_{32} & \sigma_3^2
\end{bmatrix}
\end{equation}
$$

#### Step 3 - Eigenvectors and eigenvalues

How should we determine the "best" lower dimensional space?

~ can be determined by the "best" eigenvectors of the covariance matrix of the data. (i.e. The eigenvectors corresponding to the "largest" eigenvalues - also called "Principal Components")

- Eigenvectors: Directions in which data varies the most
- Usage: to calculate the proportion of variance represented by each eigenvector.

The eigenvectors of the covariance matrix represent the principal components, whereas the corresponding eigenvalues will define their magnitude.

#### Step 4 - Choose the Principal Components

We only select the subset of the eigenvectors (principal components) that contains most of the information (variance)

Eigenvalues define the magnitude of the eigenvectors, so we have to sort the eigenvalues by decreasing magnitude.

We are interested in the top $k$ eigenvectors based on the values of their corresponding eigenvalues.

Variance explained ratio: of an eigenvalue $\lambda_j$ is simply the fraction of an eigenvalue $\lambda_j$ and the total sum of the eigenvalues:
$$
\begin{equation}
\frac{\lambda_j}{\sum_{i=1}^d \lambda_i}
\end{equation}
$$

#### Step 5 - Project onto principal components

$k$ largest eigenvalues, which are the dimensionality of the new feature subspace $k \times d$.

- Construct a projection matrix $W$ from the "top" $k$ eigenvalues.
- Transform the $d$-dimensional input dataset $X$ using the projection matrix to obtain the new $k$-dimensional feature subspaces

#### Note - Loss of Information

Always lose some amount of information.

This lossiness is typically minimal.

Perforing PCA, always appropriate to consider: how many components will be necessary...

### Algorithm 2 - Multi-Dimensional Scaling (MDS)

> Different from clustering, MDS is for simplify the data, while clustering is for dividing clusters.

Defination: a set of data analysis techniques used to explore similarities or dissimilarities.

Create a spatial representation of data, distances between points reflect the original dissmilarities.

Distance is the prime concept in MDS.

#### High-Level View of the MDS Algorithm

Input: matrix of dissimilarities

Output: A spatial configuration where similar objects are closer together.

Process:

1. Start with a distance matrix
2. Choose a number of dimensions for the output space
3. Optimize the positions of objects to best preserve the original distances.

Distance Matrix $D$: An $n\times n$ matrix representing distances between $n$ objects.

Configuration Matrix $X$: A $n\times p$ matrix. representing $n$ objects in $p$-dimensional space

Objective: Minimize the stress function:
$$
\begin{equation}
\sqrt{
\frac{\sum_{i<j}(d_{ij}-\delta_{ij})^2}{\sum_{i<j}d_{ij}^2}
}
\end{equation}
$$
$d_{ij}$:Original dissmilarity between objects $i$ and $j$.

$\delta_{ij}$: Distance between objects $i$ and $j$ in the MDS configuration

#### Limitations of MDS

1. Computationally intensive for large datasets.
2. Output dimensions can affect the interpretability.
3. Axes in the MDS plot may not have a clear interpretation.

### Algorithm 3 - $t$-Distributed Stochastic Neighbor Embedding ($t$-SNE)

- Make complex data more understandable
- Captures complex patterns that other linear methods (like PCA) might miss.
- Preserves local structure
- captures global patterns
- stochastic (随机的？)

#### Properties

- Start with similarity
- Probability Distributions
- Low-Dimensional Mapping

#### Some notices

- Perplexity: A parameter that controls the balance between local and global structure. (Effective nearest neighbors)

- Non-Deterministic: Random nature, thus $t$-SNE may produce slightly different results.

#### Limitations

- Computationally Intensive (慢)
- Interpretation Challenges: The axes in $t$-SNE plots don't have a specific meaning

### Differences - PCA vs MDS vs $t$-SNE

| **Method** | **Objective**                                                | **Visualization**                                            | **Applicability**                                            | **Interpretation**                                           |
| ---------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| PCA        | Reduce dimensionality by transforming data into a new set of orthogonal axes (principal components) that capture the most variance. | Produces linear projections that are often visualized in 2D or 3D scatter plots. | Useful for datasets where variance is important, and data is linearly related. Suitable for noise reduction and feature extraction. | Components have a mathematical interpretation. The direction of each axis represents a combination of original features. |
| MDS        | Find a spatial configuration of data points in a lower dimensional space that preserves pairwise distances. | Provides spatial visualization, usually in 2D or 3D, that reflects dissimilarities between data points. | Best for datasets where the main concern is preserving distance relationships between points. Applicable in psychology, market research, etc. | Axes do not have a clear interpretation; focus is on the relative distances between points rather than specific features. |
| $t$-SNE    | Visualize high dimensional data by preserving local structure and neighborhood relationships. | Creates visualizations that highlight clusters and local groupings, typically in 2D or 3D. | Ideal for complex datasets with nonlinear structures, such as image data, text data, and biological data. | Axes are not interpretable; emphasis is on the layout and clustering of points rather than specific features or dimensions. |
