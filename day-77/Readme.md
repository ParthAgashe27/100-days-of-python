# Day 77 — NumPy & N-Dimensional Arrays

## What this notebook covers
- **ndarray basics**: 1D/2D/3D arrays, `.ndim`, `.shape`, indexing and slicing across multiple axes
- **NumPy mini-challenges**: `arange`, slicing tricks, `flip`, `nonzero`, `random`, `linspace`
- **Vectors vs Python lists**: why `ndarray + ndarray` does element-wise math while `list + list` concatenates
- **Broadcasting**: scalar operations (`array + 10`, `array * 5`) applied across an entire array without loops
- **Matrix multiplication**: `.matmul()` vs the `@` operator, with shape-compatibility reasoning
- **Images as ndarrays**: loading `scipy.datasets.face()` (the standard sample image) as a 3D array (height × width × RGB channels), converting to grayscale using the sRGB luminance formula, flipping/rotating/inverting images via pure array operations (`np.flip`, `np.rot90`, `255 - img`)
- **Using your own image**: loading a custom image with PIL, converting to a NumPy array, and manipulating it the same way

## Note
`scipy.misc.face()` is deprecated/removed in current SciPy — used `scipy.datasets.face()` instead, which is the current replacement for the same sample image.

## Requirements
```
numpy
matplotlib
scipy
pillow
```
