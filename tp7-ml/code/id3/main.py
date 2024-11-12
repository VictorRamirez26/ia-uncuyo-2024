import pandas as pd
import tree  

def display_tree(decision_tree, level=0, prefix=""):
    if isinstance(decision_tree, dict):
        for attribute, subtree in decision_tree.items():
            print(f"{prefix}├── {attribute}")
            # Llamada recursiva para imprimir el subárbol
            new_prefix = prefix + "│   "
            display_tree(subtree, level + 1, new_prefix)
    else:
        print(f"{prefix}└── -> {decision_tree}")

if __name__ == "__main__":
    data = pd.read_csv("https://raw.githubusercontent.com/sjwhitworth/golearn/master/examples/datasets/tennis.csv")
    
    feature_columns = list(data.columns)
    feature_columns.remove("play")
    target_column = "play"

    decision_tree_model = tree.learn_decision_tree(data, feature_columns, data, target_column)
    display_tree(decision_tree_model)
