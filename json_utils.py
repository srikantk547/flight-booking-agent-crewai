import json
import re


def parse_json_response(response):

    text = str(response)

    try:
        return json.loads(text)

    except Exception:

        match = re.search(r'\{.*\}', text, re.DOTALL)

        if match:
            return json.loads(match.group())

        raise ValueError(
            f"Unable to parse JSON:\n{text}"
        )