import requests
import time
import json

def ask_ollama(question):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "llama2:latest",
        "prompt": question
    }

    try:
        start_time = time.time()  # Start timing

        # Send the POST request without streaming
        response = requests.post(url, json=data, stream=False)

        # Measure the time taken for the POST request
        duration = time.time() - start_time
        print(f"Time taken for POST request: {duration:.2f} seconds")

        # Check for successful response
        if response.status_code == 200:
            # Split the response into lines and parse each line as JSON
            answer = ""
            for line in response.text.splitlines():
                if line.strip():  # Ignore empty lines
                    try:
                        response_data = json.loads(line)
                        answer += response_data.get("response", "")
                    except json.JSONDecodeError:
                        print(f"Skipping invalid JSON line: {line}")

            duration = time.time() - start_time
            print(f"TOTAL : {duration:.2f} seconds")
            return answer.strip()
        else:
            return f"Error: {response.status_code}, {response.text}"

    except requests.exceptions.RequestException as e:
        return f"Connection error: {e}"

if __name__ == "__main__":
    question = input("Ask Ollama: ")
    answer = ask_ollama(question)
    print(f"Ollama's answer: {answer}")
