import json
from functools import lru_cache

@lru_cache(maxsize=1)
def load_labels():
    """
    Load disease class labels from a JSON file.
    """

    with open("backend/data/labels.json", "r") as file:
        return json.load(file)