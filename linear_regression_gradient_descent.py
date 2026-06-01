import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    """
    Perform linear regression using gradient descent.

    Args:
        X: Feature matrix of shape (m, n) where first column is all ones (for intercept)
        y: Target vector of shape (m,)
        alpha: Learning rate
        iterations: Number of gradient descent iterations
    
    Returns:
        Learned weights as a 1D array of shape (n,)
    """

    X = X.tolist()
    Y = y.tolist()

    iter_count = 0

    n_rows = len(X)
    n_cols = len(X[0])

    weights = [0]*(n_cols)
    Y_hat = [0]*n_rows

    while iter_count < iterations:
        
        for rowidx in range(n_rows):
            y_pred = 0
            for dimidx in range(n_cols):
                y_pred += (weights[dimidx]*X[rowidx][dimidx])
            Y_hat[rowidx] = y_pred 

        gradient_weights = [0]*(n_cols)
        for dimidx in range(n_cols):
            gradient_weights[dimidx] = compute_gradient_weight(X, Y, dimidx, Y_hat)
            weights[dimidx] = weights[dimidx] - (alpha * gradient_weights[dimidx])

        iter_count += 1
    return np.array(weights)

def compute_gradient_weight(X, Y, dimidx, Y_hat):
    sum_grad = 0
    for rowidx in range(len(X)):
        point_grad = (Y_hat[rowidx] - Y[rowidx])*X[rowidx][dimidx]
        sum_grad += point_grad 
    return sum_grad/len(X)
