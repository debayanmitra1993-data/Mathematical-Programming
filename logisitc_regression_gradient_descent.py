import numpy as np
import math 

def train_logreg(X: np.ndarray, y: np.ndarray, learning_rate: float, iterations: int) -> tuple[list[float], ...]:
	"""
	Gradient-descent training algorithm for logistic regression, optimizing parameters with Binary Cross Entropy loss.
	"""
	X = X.tolist()
	Y = y.tolist()
	n_rows = len(X)
	n_cols = len(X[0])

	Y_hat = [0]*n_rows

	iter_count = 0
	weights = [0]*n_cols
	bias = 0
	loss_lst = []

	while iter_count < iterations:
		
		# compute Y_hat 
		for rowidx in range(n_rows):
			y_pred = 0
			for dimidx in range(n_cols):
				y_pred += (weights[dimidx] * X[rowidx][dimidx])
			y_pred += bias 
			y_pred = sigmoid(y_pred)
			Y_hat[rowidx] = y_pred 

		# compute loss
		loss_val = bceloss(Y_hat, Y)
		loss_lst.append(loss_val)

		# compute gradients of all weights and gradient of the bias 
		gradient_weights = [0]*n_cols
		for dimidx in range(n_cols):
			gradient_weights[dimidx] = compute_grad_weight(Y_hat, Y, dimidx, X)
			weights[dimidx] = weights[dimidx] - (learning_rate * gradient_weights[dimidx])
		gradient_bias = compute_grad_bias(Y_hat, Y)
		bias = bias - (gradient_bias * learning_rate)

		iter_count += 1
	
	return ([bias] + weights, loss_lst)

def compute_grad_weight(Y_hat, Y, dimidx, X):
	grad_term = 0
	for rowidx in range(len(Y)):
		grad_term += ((Y_hat[rowidx] - Y[rowidx])*X[rowidx][dimidx])
	return grad_term / len(Y)

def compute_grad_bias(Y_hat, Y):
	grad_term = 0
	for rowidx in range(len(Y)):
		grad_term += (Y_hat[rowidx] - Y[rowidx])
	return grad_term / len(Y)

def sigmoid(x):
	return 1 / (1 + np.exp(-x)) 

def bceloss(Y_hat, Y):
	bce = 0
	for rowidx in range(len(Y)):
		y = Y[rowidx]
		y_hat = Y_hat[rowidx]
		bce += ((y*math.log(y_hat)) + ((1 - y)*math.log(1 - y_hat)))
	return -bce / len(Y)



	
