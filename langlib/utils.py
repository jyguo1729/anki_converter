import pandas as pd
import re
import requests
import os
from openai import OpenAI
from langlib.reader import get_prompt, get_text

api_key = "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"
os.environ["OPENAI_API_KEY"] = api_key
client = OpenAI()


def test_fun(x):
    return pd.DataFrame(1, index=[1, 2], columns=["a", "b"])


def clean_response(res):
    pattern = re.compile(
        r"([\u3040-\u9fff]+)\W+([\u3040-\u309F]+)\W+([\u4E00-\u9fff]+)\W+", re.UNICODE
    )
    decks = []
    for n in re.findall(pattern, res.content):
        word, pron, mean = n
        deck = dict(
            word=word,
            pron=pron,
            mean=mean,
        )

        decks.append(pd.Series(deck))
    decks = pd.concat(decks, axis=1).T
    return decks


def create_dict(text_file, output_file, output_dir=None):
    if output_dir is None:
        output_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data"
        )
    text = get_text(text_file)
    prompt = get_prompt()
    res = get_raw_res(prompt + text)
    if not output_file.endswith(".csv"):
        output_file += ".csv"
    tmp_df = clean_response(res)
    tmp_df.to_csv(os.path.join(output_dir, output_file))


def get_raw_res(content):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "你是一个日语老师。"},
            {"role": "user", "content": content},
        ],
    )
    return response.choices[0].message
