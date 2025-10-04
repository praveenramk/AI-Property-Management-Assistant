from typing import Any, Dict
import requests

class LLMClient:
    def __init__(self, api_key: str, endpoint: str):
        self.api_key = api_key
        self.endpoint = endpoint

    def generate_response(self, prompt: str, **kwargs: Any) -> Dict[str, Any]:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "prompt": prompt,
            **kwargs
        }
        response = requests.post(self.endpoint, headers=headers, json=data)
        response.raise_for_status()
        return response.json()