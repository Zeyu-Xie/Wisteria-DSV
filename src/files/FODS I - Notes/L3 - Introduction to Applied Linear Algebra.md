# Introduction to Applied Linear Algebra

## Vectors

A vector is an ordered list of numbers. Written as:
$$
\begin{equation}
\begin{bmatrix}
-1.1 \\
0.0 \\
3.6 \\
-7.2
\end{bmatrix}
\end{equation}
$$
or:
$$
\begin{equation}
\begin{pmatrix}
-1.1 \\
0.0 \\
3.6 \\
-7.2
\end{pmatrix}
\end{equation}
$$

- Numbers in the list: elements (entries, coefficients, components)

- Vector Size: dimension, length

- Entry: the third entry is 3.6

- $n$-vector: A vector of size $n$

- Scalar: numbers ?
- Block vectors: $a$ has size $m+n+p$

$$
\begin{equation}
a = \begin{bmatrix}
b \\
c \\
d \\
\end{bmatrix}
\end{equation}
$$

- Zero: $n$-vector with all entries $0$, denoted $0n$ or just $0$

- Ones: $n$-vector with all entries $1$, denoted $1n$ or just $1$

- Unit Vector: one entry $1$ and all others $0$, denoted $e_i$ where $i$ is entry that is $1$

- Sparse vector: A vector is sparse if many of its entries are $0$ (e.g. zero vectors, unit vectors)

- Examples: 

  - $2$-vector $(x_1, x_2)$ can represent a location of a displacement in 2-D

  - Color $(R;G;B)$

  - Word count vectors:
    $$
    \begin{equation}
    \begin{bmatrix}
    \text{word} \\
    \text{in} \\
    \text{number} \\
    \text{horse} \\
    \text{the} \\
    \text{document}
    \end{bmatrix} = \begin{bmatrix}
    3 \\
    2 \\
    1 \\
    0 \\
    4 \\
    2
    \end{bmatrix}
    \end{equation}
    $$

- Vector Addition: 

  - commutative: $a+b = b+a$

  - associative: $(a+b)+c = a+(b+c)$

  - $a+0=0+a=a$

  - $a-a=0$

- Adding Displacements: vectors $a$ and $b$ are displacements, $a+b$ is the sum displacement

- Scalar-Vector Multiplication: Scalar $\beta$ and $n$-vector can be multiplied

  - Associative: $(\beta\gamma)a = \beta(\gamma a)$
  - Left Distribute: $(\beta+\gamma)a = \beta a+\gamma a$
  - Right Distribute: $\beta(a+b) = \beta a+\beta b$

- Linear Functions: $f:\mathbb{R}^n\to\mathbb{R}$ satisfies the superposition property if
  $$
  \begin{equation}
  f(\alpha x+\beta y) = \alpha f(x) + \beta f(y)
  \end{equation}
  $$
  holds for all numbers $\alpha$ and $\beta$, and all $n$-vectors $x$ and $y$
  
- Euclidean Norm (or just norm): of an $n$-vector $x$ is
  $$
  \begin{equation}
  \norm{x} = \sqrt{x_1^2+x_2^2+\cdots+x_n^2}
  \end{equation}
  $$

  - Homogeneity: $\norm{\beta x} = \abs{\beta} \norm{x}$
  - Nonenegativity: $\norm{x}\geq 0$
  - Definiteness: $\norm{x} = 0 \iff x=0$


## Matrices

A matrix is a rectangular array of numbers
$$
\begin{equation}
\begin{bmatrix}
0 &1 &-2.3 &0.1 \\
1.3 &4 &-0.1 &0 \\
4.1 &-1 &0 &1.7
\end{bmatrix}
\end{equation}
$$

- Size: $\text{row dimension}\times\text{column dimension}$, in the matrix above is $3\times 4$

- Entries (coefficients): Elements

- $i,j$ element: $b_{ij}$ is the $i,j$ element of matrix $B$

- Equal: they are the same size and corresponding entries are equal

- Column and Row Vectors:

  - $n\times 1$ matrix is an $n$-vector
  - $1\times 1$ matrix is a number
  - $1\times n$ matrix is called a row vector ($\neq$ (column) vector)

- Examples: image / feature matrix

- Special Matrices: 

  - Zero: $m\times n$ zero matrix has all entries zero, written as $0_{m\times n}$ or just $0$

  - Identity Matrix: square matrix with $I_{ii} - 1$ and $I_{ij} = 0$ for $i\neq j$
    $$
    \begin{equation}
    \begin{bmatrix}
    1 &0 \\
    0 &1
    \end{bmatrix}
    \end{equation}
    $$
    
  - Sqarse Matrix: most entries are zero

- Diagonal and Tringular Matrices:

  - Diagonal Matrix: Square Matrix with $D_{ij}=0$ for $i\neq j$, written as $\text{diag}\left(a_1, a_2, \cdots, a_n\right)$ 

  - lower traingular matrix: $A_{ij}=0$ for $i< j$
    $$
    \begin{equation}
    \begin{bmatrix}
    1 &-1 &0.7 \\
    0 &1.2 &-1.1 \\
    0 &0 &3.2
    \end{bmatrix}
    \end{equation}
    $$
    
  - upper  traingular matrix: $A_{ij} = 0$ for $i>j$
    $$
    \begin{equation}
    \begin{bmatrix}
    -0.6 &0 \\
    -0.3 &3.5
    \end{bmatrix}
    \end{equation}
    $$

- Transpose: denoted $A^T$, defined by:
  $$
  \begin{equation}
  (A^T)_{ij} = A_{ji}, \quad i = 1,2,\cdots,n,\quad j=1,2,\cdots, m
  \end{equation}
  $$
  
  - Converts column to row vectors
  - $(A^T)^T = A$
  
- Addition, Subtraction, Scalar Multiplication

- Matrix-Vector Product: Matrix-vector product of $m\times n$ matrix $A$ and $n$-vector $x$, denoted by $y=Ax$

- Linear functions: 

  - $f:\mathbb{R}^n\to\mathbb{R}^m$ means $f$ is a function mapping $n$-vectors to $m$-vectors
  - ...

- Row Aspect: ...

- Column Aspect: ...

- Properties:
  - $(AB)C = A(BC)$
  - $A(B+C) = AB+AC$
  - $(AB)^T = B^T A^T$
  - $AI = A$

## Derivatives

- Differentiation
- Secant Line (割线): The secant to the function $f(x)$ through the points $(a, f(a))$ and $(x, f(x))$ is the line passing through these points
- Tangent Line (切线): The tangent line of a curve at a given point is a line thatt touches the curve (function at that point)
- Properties of the differential operator:
  - Sum: $\frac{d}{dx}(f+g) = \frac{df}{dx} + \frac{dg}{dx}$
  - Differences: $\frac{d}{dx}(f-g) = \frac{df}{dx} - \frac{dg}{dx}$
  - Products: $\frac{d}{dx}(f\cdot g) = f\frac{dg}{dx} + \frac{df}{dx} g$
  - Quotients: $\frac{d}{dx}\left(\frac{f}{g}\right) = \frac{\left(g\frac{df}{dx} - f\frac{dg}{dx}\right)}{g^2}$
  - Power Rule: $\frac{d}{dx} = (x^n) = nx^{n-1}$


## Gradients

?? Is the vector or the row vector 👇??

The gratient of a function is a vector that contains the partial derivatives of the function with respect to each variable. For function $f(x_1, x_2, \cdots, x_n)$
$$
\begin{equation}
\nabla f(x_1, x_2, \cdots, x_n) = \left(\frac{\part f}{\part x_1}, \frac{\part f}{\part x_2}, \cdots, \frac{\part f}{\part x_n}\right)
\end{equation}
$$

- The gradient points in the direction of the steepest ascent of the function

### Derivative of a matrix

Consider a function $f$ that maps an $n$-dimensional vector $x$ to an $m$-dimensional vector $f(x)$
$$
\begin{equation}
f: \mathbb{R}^n\to\mathbb{R}^m, \quad f(x) = \begin{pmatrix}
f_1(x) \\
f_2(x) \\
\vdots \\
f_m(x)
\end{pmatrix}
\end{equation}
$$
Each $f_i(x)$ is a scalar-valued function of the vector $x$

Patrial derivatives matrix for element $J_{ij}$ will be like
$$
\begin{equation}
J_{ij} = \frac{\part f_i(x)}{\part x_j}
\end{equation}
$$
And thus $J$ Will be like
$$
\begin{equation}
J = \begin{pmatrix}
J_{11} &J_{12} &\cdots &J_{1n} \\
J_{21} &J_{22} &\cdots &J_{2n} \\
\vdots &\vdots &\ddots &\vdots \\
J_{m1} &J_{m2} &\cdots &J_{mn}
\end{pmatrix} = \begin{pmatrix}
\frac{\part f_1}{\part x_1} &\frac{\part f_1}{\part x_2} &\cdots &\frac{\part f_1}{\part x_n} \\
\frac{\part f_2}{\part x_1} &\frac{\part f_2}{\part x_2} &\cdots &\frac{\part f_2}{\part x_n} \\
\vdots &\vdots &\ddots &\vdots \\
\frac{\part f_m}{\part x_1} &\frac{\part f_m}{\part x_2} &\cdots &\frac{\part f_m}{\part x_n}
\end{pmatrix}
\end{equation}
$$
