import os

print(__file__)


def get_prompt():
    data_folder = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data"
    )
    filepath = os.path.join(data_folder, "prompt.txt")
    with open(filepath, "r") as f:
        prompt = f.read()
    return prompt


def get_text(file_name="text.txt"):
    data_folder = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data"
    )
    print(data_folder)
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    filepath = os.path.join(data_folder, file_name)
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    return text
