import torch

# ===== Create a simple tensor data object with 2 rows and 3 columns =====

data = [[1, 2, 3], [4, 5, 6]]
tensor_data = torch.tensor(data)
print("A simple tensor data object: ", tensor_data)

# ========================================================================

# ===== Create a simple tensor data object with 4 rows and 5 columns =====

shape = (4, 5)

zeros = torch.zeros(shape)  # an object with 4 rows and 5 columns of ZEROS
ones = torch.ones(shape)  # an object with 4 rows and 5 columns of ONES
# an object with 4 rows and 5 columns of RANDOM NUMBERS
randoms = torch.rand(shape)

print("ZEROS: ", zeros)
print("ONES: ", ones)
print("RANDOM NUMBERS: ", randoms)

# ========================================================================

# ===== Tensor is running on? =====

print(f"This torch is running on: {randoms.device}")

# =================================

# ===== Element-wise multiplication =====

ewm_data1 = torch.tensor([[1, 2], [3, 4]])
ewm_data2 = torch.tensor([[10, 20], [30, 40]])

ewm_result = ewm_data1 * ewm_data2  # 1*10 | 2*20 | 3*30 | 4*40
# NOTE: both elements MUST have the same shape. In this case both have 2 rows and 2 columns
print("EWM Result: ", ewm_result)

# =======================================

# ======= Matrix multiplication ========

mx_data1 = torch.tensor([[1, 2, 3], [4, 5, 6]])
mx_data2 = torch.tensor([[10, 20], [30, 40], [50, 60]])

mx_result = mx_data1 @ mx_data2
# NOTE: number of columns on the frist data MUST BE THE SAME as number of rows on the second data
print("Matrix Result: ", mx_result)

# ======================================

# ================= mean() ==================

# mean() only works with float32 type not int
scores = torch.tensor([[12., 16.], [13., 20.]])

average_score = scores.mean()  # (12 + 16 + 13 + 20) / 4

print("Average Score: ", average_score)
# ===========================================

# ================= dim ==================

# dim basically crushes crushes data vertically or horizontally
scores = torch.tensor([[10., 20., 30.], [1., 2., 3.]])

# result: [((10 + 1) / 2), ((20 + 2) / 2), ((30 + 3) / 2)] = [ 5.5000, 11.0000, 16.5000]
average_score_vert = scores.mean(dim=0)
# result: [((10 + 20 + 30) / 3), ((1 + 2 + 3) / 3)] = [20.,  2.]
average_score_horz = scores.mean(dim=1)

print("Average Score Vertically: ", average_score_vert)
print("Average Score Horizontally: ", average_score_horz)
# ===========================================

# ================= Indexing ==================

indexing_data = torch.arange(12).reshape(3, 4)
# tensor([[ 0,  1,  2,  3],
#         [ 4,  5,  6,  7],
#         [ 8,  9, 10, 11]])
coln_2 = indexing_data[:, 2]  # tensor([ 2,  6, 10])
print(coln_2)

# ===========================================

# ================= argmax() ==================

random_ints = (torch.rand(3, 4) * 10000).int()
print("random_ints: ", random_ints)

argmax = torch.argmax(random_ints, dim=1)
print("argmax: ", argmax)

# ===========================================

# ================= gather() ==================

data = torch.tensor([
    [10., 11., 12., 13.,],
    [20., 21., 22., 23.,],
    [30., 31., 32., 33.,]
])
indices_to_select = torch.tensor([[2], [0], [3]])

selected_values = torch.gather(data, dim=1, index=indices_to_select)
print("Select index 2 on row 1, index 0 on row 2, index 3 on row 3: ", selected_values)

# ===========================================