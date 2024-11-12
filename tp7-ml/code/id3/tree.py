import pandas as pd
import numpy as np

def majority_value(dataset, target_col):
    return dataset[target_col].mode()[0]

def calculate_entropy(column):
    entropy_sum = 0
    total_count = len(column)
    value_counts = column.value_counts()
    for count in value_counts:
        probability = count / total_count
        entropy_sum -= probability * np.log2(probability)
    return entropy_sum

def compute_information_gain(data, attribute, target_col):
    total_entropy = calculate_entropy(data[target_col])
    
    weighted_avg_entropy = 0
    for val in data[attribute].unique():
        subset_data = data[data[attribute] == val]
        probability = len(subset_data) / len(data)
        weighted_avg_entropy += probability * calculate_entropy(subset_data[target_col])
    
    info_gain = total_entropy - weighted_avg_entropy
    return info_gain

def learn_decision_tree(data, attributes, parent_data, target_col):

    if data.empty:
        return majority_value(parent_data, target_col)
    elif len(data[target_col].unique()) == 1:
        return data[target_col].iloc[0]
    elif not attributes:
        return majority_value(data, target_col)
    else:
        best_attr = max(attributes, key=lambda attr: compute_information_gain(data, attr, target_col))
        tree = {best_attr: {}}
        for val in data[best_attr].unique():
            subset_data = data[data[best_attr] == val]
            subtree = learn_decision_tree(subset_data, [attr for attr in attributes if attr != best_attr], data, target_col)
            tree[best_attr][val] = subtree
        return tree
