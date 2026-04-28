try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


def get_models(key, url):
    headers = {"Authorization": f"Bearer {key}"}
    resp = requests.get(
        f"{url.rstrip('/')}/models",
        headers=headers,
        timeout=10
    )
    data = resp.json()

    models = []
    if "data" in data:
        models = [m.get("id") for m in data["data"]]
    elif "models" in data:
        models = [m.get("name") or m.get("model") for m in data["models"]]

    return models


