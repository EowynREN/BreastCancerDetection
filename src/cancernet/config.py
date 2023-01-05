import os

INPUT_DATASET = "../datasets/original"

BASE_PATH = "../datasets/idc"
TRAIN_PATH = os.path.sep.join([BASE_PATH, "training"])
VAL_PATH = os.path.sep.join([BASE_PATH, "validation"])
TEST_PATH = os.path.sep.join([BASE_PATH, "testing"])

TRAIN_SPLIT = 0.8  # leaves 20% for test set
VAL_SPLIT = 0.1  # of training set, 10% for validation

