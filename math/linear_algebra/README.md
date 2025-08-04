# Linear Algebra

This project covers the fundamentals of linear algebra in Python, including vector and matrix operations, array manipulation, and NumPy functionality.

## Learning Objectives

At the end of this project, you should be able to explain:

- What is a vector and matrix
- What is a transpose and matrix shape
- What is an axis and slice
- How to slice vectors/matrices
- Element-wise operations
- Vector/matrix concatenation
- Dot product and matrix multiplication
- NumPy basics and broadcasting
- Parallelization concepts

## Requirements

- **Python Version**: 3.9
- **NumPy Version**: 1.25.2
- **OS**: Ubuntu 20.04 LTS
- **Style**: pycodestyle (version 2.11.1)
- All files must be executable
- All functions must have proper documentation

## Project Structure

### Basic Python Operations (Tasks 0-8)
- `0-slice_me_up.py` - Array slicing operations
- `1-trim_me_down.py` - Matrix column extraction using loops
- `2-size_me_please.py` - Calculate matrix shape recursively
- `3-flip_me_over.py` - 2D matrix transposition
- `4-line_up.py` - Element-wise array addition
- `5-across_the_planes.py` - Element-wise 2D matrix addition
- `6-howdy_partner.py` - Array concatenation
- `7-gettin_cozy.py` - 2D matrix concatenation along specified axis
- `8-ridin_bareback.py` - Matrix multiplication implementation

### NumPy Operations (Tasks 9-14)
- `9-let_the_butcher_slice_it.py` - Advanced NumPy array slicing
- `10-ill_use_my_scale.py` - NumPy array shape calculation
- `11-the_western_exchange.py` - NumPy array transposition
- `12-bracin_the_elements.py` - NumPy element-wise operations
- `13-cats_got_your_tongue.py` - NumPy array concatenation
- `14-saddle_up.py` - NumPy matrix multiplication

## Key Concepts Covered

### Vectors and Matrices
- Vector: 1D array of numbers
- Matrix: 2D array of numbers arranged in rows and columns
- Shape: Dimensions of a matrix (rows × columns)

### Operations
- **Transpose**: Flipping matrix over its diagonal
- **Element-wise**: Operations applied to corresponding elements
- **Dot Product**: Sum of products of corresponding elements
- **Matrix Multiplication**: Rows of first matrix × columns of second matrix

### NumPy Features
- **Broadcasting**: Operations between arrays of different shapes
- **Vectorization**: Applying operations to entire arrays at once
- **Parallelization**: Utilizing multiple CPU cores for faster computation

## Usage Examples

```python
# Basic matrix operations
from matrix_shape import matrix_shape
mat = [[1, 2], [3, 4]]
print(matrix_shape(mat))  # [2, 2]

# NumPy operations
import numpy as np
from np_matmul import np_matmul
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])
result = np_matmul(mat1, mat2)
```

## Testing

Each file can be tested with the provided main files:
```bash
./0-main.py  # Test slicing operations
./2-main.py  # Test matrix shape function
# ... etc
```

## Author

This project is part of the Holberton School Machine Learning curriculum.
