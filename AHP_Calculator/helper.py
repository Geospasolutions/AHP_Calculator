import pandas as pd

def total(matrix, num_of_params):
#     mat_T = matrix.transpose()
    tot = np.full((num_of_params), 0, dtype=float)
    for i in range(num_of_params):
        for j in range(num_of_params):
            tot[i] = tot[i] + matrix[j,i]
    return(tot)
sum_column = total(mat, num)
sum_column

def normalization(array_1d, matrix, num_of_params):
    norm = np.full((num_of_params, num_of_params), 1, dtype=float)
    for i in range(num_of_params):
        for j in range(num_of_params):
            norm[i,j] = matrix[j,i]/tot[i]
    norm_t = norm.transpose()
    return (norm_t)
normalized_value = normalization(sum_column, mat, num)
normalized_value

def weight(norm_2d, num_of_params):
    li = []
    for i in range(num_of_params):
        wt = np.sum(norm_2d[[i]])/num_of_params
        li.append(wt)
    return(li)
weight_list = weight(normalized_value, num)
weight_list

def consistency_check(total, weight, num_of_params):
    #Lambda value
    lmda = 0
    for i in range(num):
        lmda = lmda + tot[i] * weight[i]
    
    #Consistency Index
    CI = (lmda-num_of_params)/(num_of_params-1)
    
    #Random Index
    df = pd.read_csv('random_index.csv')
    fnd = df[df["Size of matrix (n)"]==num_of_params]
    RI = fnd.iloc[0]["Random Index (RI)"]
    
    #Consistency Ratio
    CR = CI/RI
    to_return = {
        "Consistency Index: " : CI,
        "Random Index" : RI,
        "Consistency Ratio: " : CR       
    }
    if(CR<0.1):
        to_return ["Consistency"] = "The data is consistent"
    else:
        to_return ["Consistency"] = "The data is inconsistent. Iterate the process by changing comparison value"
        
    return (to_return)
consistency_check(sum_column, weight_list, num)       