import requests

def ask_ollama(question):
    url = "http://localhost:11434/api/generate"  # Ollama's local API endpoint
    data = {
        "model": "llama2",  # Specify the model you're using
        "prompt": question
    }

    try:
        response = requests.post(url, json=data)

        if response.status_code == 200:
            return response.json().get("text").strip()
        else:
            return f"Error: {response.status_code}, {response.text}"

    except requests.exceptions.RequestException as e:
        return f"Connection error: {e}"

if __name__ == "__main__":
    question = input("Ask Ollama: ")
    answer = ask_ollama(question)
    print(f"Ollama's answer: {answer}")
