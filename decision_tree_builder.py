import math
from collections import Counter

def calculate_entropy(labels: list) -> float:
    """Calculate the entropy of a list of labels."""
    # Your code here
    count_label = {}
    for label in labels:
        if label not in count_label:
            count_label[label] = 1
        else:
            count_label[label] += 1
    entropy = 0
    for label in count_label.keys():
        p_label = count_label[label]/len(labels)
        entropy += p_label*math.log2(p_label) 
    return -entropy 

def calculate_information_gain(examples: list[dict], attr: str, target_attr: str) -> float:
    """Calculate the information gain of splitting on attr."""
    # Your code here
    targets = []
    feat_labels = {}
    for example in examples:
        feature_value = example[attr]
        target_value = example[target_attr]
        if feature_value not in feat_labels:
            feat_labels[feature_value] = []
        feat_labels[feature_value].append(target_value)
        targets.append(target_value)
    entropy_parent_node = calculate_entropy(targets)
    wt_entropy_children = 0
    for featval in feat_labels.keys():
        ent_child_node = calculate_entropy(feat_labels[featval])
        weight_child_node = len(feat_labels[featval])
        wt_entropy_children += (weight_child_node*ent_child_node)
    wt_entropy_children = wt_entropy_children / len(examples)
    info_gain = entropy_parent_node - wt_entropy_children
    return info_gain

def majority_class(examples: list[dict], target_attr: str) -> str:
    """Return the majority class. Break ties alphabetically."""
    # Your code here
    max_attr = None
    max_attr_count = 0
    target_counts = {}
    for example in examples:
        target_val = example[target_attr]
        if target_val not in target_counts:
            target_counts[target_val] = 1 
        else:
            target_counts[target_val] += 1

        if target_counts[target_val] > max_attr_count:
            max_attr_count = target_counts[target_val]
            max_attr = target_val
    
    count_max_attr_count = 0
    tie_found = False 
    tie_labels = []
    for label in target_counts.keys():
        if target_counts[label] == max_attr_count:
            tie_labels.append(label)
            count_max_attr_count += 1
            if count_max_attr_count > 1:
                tie_found = True 
    
    if tie_found == True:
        tie_labels.sort()
        return tie_labels[0]

    return max_attr

def learn_decision_tree(examples: list[dict], attributes: list[str], target_attr: str) -> dict:
    """Build a decision tree using the ID3 algorithm."""
    decision_tree_model = {} 
    decision_tree_recursion(examples, attributes, target_attr, decision_tree_model)
    return decision_tree_model


def decision_tree_recursion(examples, attributes, target_attr, decision_tree_model):
    if len(attributes) == 0:
        return 

    # get the best attribute to split on that has maximum IG 
    max_ig_val = float("-inf")
    best_attr = None 
    for attribute in attributes:
        ig_attr_val = calculate_information_gain(examples, attribute, target_attr)
        if ig_attr_val > max_ig_val:
            max_ig_val = ig_attr_val
            best_attr = attribute 
    
    decision_tree_model[best_attr] = {}
    # get the attribute's values (these will be the branches)
    for idx in range(len(examples)):
        example = examples[idx]
        example_best_attr_val = example[best_attr]
        example_target_val = example[target_attr]

        if example_best_attr_val not in decision_tree_model[best_attr]:
            decision_tree_model[best_attr][example_best_attr_val] = {}

    # assign either - pure nodes (or) split recursively -- for each of the attribute values for this attribute
    for attribute_val in sorted(decision_tree_model[best_attr].keys()):
        attribute_val_examples = []
        count_labels = {}
        for idx in range(len(examples)):
            example = examples[idx]
            target_val = example[target_attr]
            if example[best_attr] == attribute_val:
                attribute_val_examples.append(example)
                if target_val not in count_labels:
                    count_labels[target_val] = 1 
                else:
                    count_labels[target_val] += 1
        
        if len(count_labels) > 1:
            remaining_attributes = [x for x in attributes if x != best_attr]
            if len(remaining_attributes) > 0:
                decision_tree_recursion(attribute_val_examples, 
                    remaining_attributes, target_attr, decision_tree_model[best_attr][attribute_val])
            elif len(remaining_attributes) == 0:
                majority_label = majority_class(attribute_val_examples, target_attr)
                decision_tree_model[best_attr][attribute_val] = majority_label
        elif len(count_labels) == 1:
            leaf_node_label = list(count_labels.keys())[0]
            decision_tree_model[best_attr][attribute_val] = leaf_node_label
