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

        response = requests.post(url, json=data, stream=True)

        # Measure the time taken for the POST request
        duration = time.time() - start_time

        # Check for successful response
        if response.status_code == 200:
            answer = ""
            # Iterate over each line in the response
            for line in response.iter_lines():
                if line:  # If line is not empty
                    json_line = line.decode('utf-8')  # Decode bytes to string
                    response_data = json.loads(json_line)
                    answer += response_data.get("response", "")  # Accumulate response parts

            print(f"Time taken for POST request: {duration:.2f} seconds")
            return answer.strip()
        else:
            return f"Error: {response.status_code}, {response.text}"

    except requests.exceptions.RequestException as e:
        return f"Connection error: {e}"


if __name__ == "__main__":
    question = input("Ask Ollama: ")
    answer = ask_ollama(question)
    print(f"Ollama's answer: {answer}")
