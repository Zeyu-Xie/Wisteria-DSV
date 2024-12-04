# L7 - Regression

Definition: Statistical measure thay attempts to determine the relationship between the dependent variable $Y$ and a set of independent variables $X = (X_1, X_2, \cdots, X_p)$

Usage: Predicting the next value of the independent $Y$ through $X$

## Simple Linear Regression

- Simplest mathematical relationship - linear relationship

- Cause-and-Effect Relationship: $X$-cause, $Y$-effect

- Goal: To find the line best describes the data:
  $$
  Y_i = \hat{\beta_0}+\hat{\beta_1}X_i
  $$

### Squared differences: Ordinary Least Squares (OLS)

- Most common method for fitting a regression line.

- minimizes the residual sum of squares (RSS) of observed values to the straight-line:
  $$
  \begin{aligned}
  \text{RSS} &= \sum_{i=1}^n(Y_i-\hat{Y_i})^2 \\
  &= \sum_{i=1}^n(Y_i-\hat{\beta_0}-\hat{\beta_1}X_i)^2 \\
  &= \sum_{i=1}^n\hat{\epsilon_i}^2
  \end{aligned}
  $$

- Coefficient Equations:

  - Y-Intercept:
    $$
    \hat{\beta_0} = \overline{Y}-\hat{\beta_1}\overline{X}
    $$

  - Slope:
    $$
    \hat{\beta_1} = \frac{\sum_{i=1}^n(X_i-\overline{X})(Y_i-\overline{Y})}{\sum_{i=1}^n(X_i-\overline{X})^2}
    $$

  - Prediction Equation:
    $$
    \hat{Y_i} = \hat{\beta_0}+\hat{\beta_1}X_i
    $$
    where $\overline{Y}$ and $\overline{X}$ are the average of the $Y_i$ and $X_i$ respectively.

- Example: Cognitive Function

- Multiple Linear Regression: $X^T = (X_1, X_2, \cdots, X_p)$, then te regression is referred to as Multiple Linear Regression
  $$
  \hat{Y} = \hat{\beta_0}+\sum_{j=1}^p\hat{\beta_j}{X_j}
  $$

- Assumptions:

  - The observations are independent (random sampling)
  - The relationship of $Y$ with $X$ and the error term is linear
  - $Y$ is normally distributed at each value of $X$
  - The error term is normally distributed with mean $0$ and constant variance
  - The $X$ variables are independent - no multicollinearity (only to multiple linear regression)

## Gradient Descent

- Optimization algorithm that finds the linear regression coefficients iteratively

- Uses Gradient Descent to update the coefficient values in order to reduce cost function $J$ (minimizing RSS) and achieve the best fit line

- A good wat to ensure that gradient descent is working correctly: make sure the error decreases for each iteration.

- How well the model fit the training data? $R^2$ measure.
  $$
  \begin{aligned}
  R^2 &= \frac{\text{Variance Explained by the Model}}{\text{Total Variance}} \\
  &= 1 - \frac{SS_{res}}{SS_{tot}} \\
  &= 1-\frac{\sum(Y-\hat{Y})^2}{\sum(Y-\overline{Y})^2}
  \end{aligned}
  $$

- Problems: Over-fitting & Under-fitting

## Regularization

## Ridge Regression

- Defination: Shrinks the regression coefficients by imposing a penalty on their size

- The ridge coefficients minimize a penalized residual sum of squares:
  $$
  \sum_{i=1}^n(Y_i-\hat{Y_i}^2) = \sum_{i=1}^n(Y_i-\hat{\beta_0}-\sum_{j=1}^p\hat{\beta_j}X_{ij})^2 + \lambda \sum_{j=1}^p\hat{\beta_j}^2
  $$
  Where $\lambda\geq 0$ is a complexity parameter that controls the amount of shrinkage: $\lambda \uparrow, \, \text{Shrinkage Amount}\uparrow$

- Equvalent wat to write the ridge problem:
  $$
  \sum_{i=1}^n (Y_i-\hat{\beta_0}-\sum_{j=1}^p \hat{\beta_j}X_{ij})^2\quad \text{s.t.}\quad \sum_{j=1}^p\hat{\beta_j}^2\leq t
  $$
  which makes explicit the size constraint on the coefficients.

- Ridge regression shrinks the coefficients toward $0$. ($L_2$ Ridge Penalty)

- When $\lambda\to 0$ the cost function becomes similar to the linear regression cost function.

- Example: Credit Card Debt

## Lasso Regression

- Defination: Shrinkage method like Ridge. The only difference is instead of taking the square of the coefficients, magnitudes are taken into account.
  $$
  \sum_{i=1}^n(Y_i-\hat{Y_i}^2) = \sum_{i=1}^n(Y_i-\hat{\beta_0}-\sum_{j=1}^p\hat{\beta_j}X_{ij})^2 + \lambda \sum_{j=1}^p|\hat{\beta_j}|
  $$

- Equivalent way to write Lasso Problem:
  $$
  \sum_{i=1}^n (Y_i-\hat{\beta_0}-\sum_{j=1}^p \hat{\beta_j}X_{ij})^2\quad \text{s.t.}\quad \sum_{j=1}^p|\hat{\beta_j}|\leq t
  $$

- The type of regularization ($L_1$) can lead to zero coefficients.

- Lasso Regression performs feature selection.

- Like Ridge Regression, the $\lambda$ parameter can be controlled:

  - $\lambda\to 0$, the cost function becomes similar to the linear regression  cost function.
  - When $\lambda$ sufficiently large, some Lasso coefficients will equal zero

- Example: Credit Card Debt

## Evaluation Metrices

Canoot calculate accuracy for a linear regression model. The performance of the model must be reported as an error for the predictions.

Four error metris that are commonly used for evaluating and reporting the performance of a linear regression model:

- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)
- Mean Absolute Percentage Error (MAPE)

### Mean Squared Error

$$
\text{MSE} = \frac{1}{n} \sum_{i=1}^n (Y_i-\hat{Y_i})^2
$$

### Root Mean Squared Error

$$
\text{RMSE} = \sqrt{\frac{1}{n}\sum_{i=1}^n(Y_i-\hat{Y_i})^2}
$$

### Mean Absolute Error

$$
\text{MAE} = \frac{1}{n}\sum_{i=1}^n|Y_i-\hat{Y_i}|
$$

### Mean Absolute Percentage Error

$$
\text{MAPE} = \frac{100\%}{n}\sum_{i=1}^n\frac{|Y_i-\hat{Y_i}|}{Y_i}
$$

### Comparation

| Acronym | Full Name                      | Residual Operation | Robust to Outliers |
| ------- | ------------------------------ | ------------------ | ------------------ |
| MSE     | Mean Squared Error             | Square             | No                 |
| RMSE    | Root Mean Squared Error        | Square             | No                 |
| MAE     | Mean Absolute Error            | Absolute Value     | Yes                |
| MAPE    | Mean Absolute Percentage Error | Absolute Value     | Yes                |

