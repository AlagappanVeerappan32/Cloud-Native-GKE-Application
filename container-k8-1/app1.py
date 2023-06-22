from flask import Flask, request, jsonify, Response
import os
import requests, json
from collections import OrderedDict


app = Flask(__name__)
app.json.sort_keys = False

# Container 2 listening port 8080

container2_url = "http://container2-service:3000/result"


# container2_url = "http://127.0.0.1:3000/result"


Invalid_error_messgae = "Invalid JSON input."
File_error_message = "File not found."


# This method validates the file is not null and exists in the mounted volume
def validate(json_payload):
    # Taking JSON input and checking if it contains a valid name or null
    file_name = json_payload.get("file")
    if file_name is None or file_name == "null":
        response = OrderedDict([("file", None), ("error", Invalid_error_messgae)])
        return False, response

    # Checking if the file name is not empty
    if file_name == "":
        response = OrderedDict([("file", None), ("error", Invalid_error_messgae)])
        return False, response

    # Checking if the file exists in the current directory
    current_directory = "/Alagappan_PV_dir/"
    file_path = os.path.join(current_directory, file_name)
    if not os.path.isfile(file_path):
        response = OrderedDict([("file", file_name), ("error", File_error_message)])
        return False, response

    return True, file_name


# This method sends the transformed payload to container 2
def communicate_with_container2(payload):
    response = requests.post(container2_url, json=payload)
    return response


# This method takes the response from container 1 and 2, extracts the JSON data, and sends it back
def send_response_to_user(response):
    response_data = response.json()
    # json_response = json.dumps(response_data)
    return jsonify(response_data)



# Receives the POST request and calls the respective functions to send the response back [1,2]
@app.route("/calculate", methods=["POST"])
def listen():
    if request.method == "POST":
        try:
            json_payload = request.get_json()
            print("Received JSON payload:")
            print(json_payload)

            is_valid, file_name = validate(json_payload)
            if not is_valid:
                return jsonify(file_name)

            payload = OrderedDict(
                [("file", file_name), ("product", json_payload.get("product"))]
            )

            # If the file name is correct, it communicates with container 2
            if file_name:
                response_from_container2 = communicate_with_container2(payload)
                if response_from_container2 is not None:
                    print("Response from Container 2:")
                    print(response_from_container2.content)
                    return send_response_to_user(response_from_container2)
                else:
                    return "Error communicating with Container 2"

        except Exception as e:
            print("Error processing JSON payload1:", str(e))
            return "Error processing JSON payload1"

    return "Method Not Allowed", 405


def validate_store_file(json_payload):
    file_name = json_payload.get("file")
    if file_name is None or file_name == "null":
        response = OrderedDict([("file", None), ("error", Invalid_error_messgae)])
        return False, response

    # Checking if the file name is not empty
    if file_name == "":
        response = OrderedDict([("file", None), ("error", Invalid_error_messgae)])
        return False, response

    return True, file_name


@app.route("/store-file", methods=["POST"])
def store_file():
    try:
        file_to_store_data = request.get_json()
    except Exception as e:
        return {
            "file": None,
            "error": Invalid_error_messgae
        }
    
    try:
        file_name = file_to_store_data["file"]
        if file_name is None: raise
    except Exception as e:
        response = {
            "file": None,
            "error": Invalid_error_messgae,
        }
        return response
    try:
        file_data = file_to_store_data["data"]
        print("Received JSON payload:")
        print(file_to_store_data)

        is_valid, file_name = validate_store_file(file_to_store_data)
        if not is_valid:
            return jsonify(file_name)

        current_directory = "/Alagappan_PV_dir/"
        file_path = os.path.join(current_directory, file_name)

        if not file_data:
            response = {
                "file": file_name,
                "error": "Error while storing the file to the storage.",
            }
            return jsonify(response)

        try:
            # Write the file data to GKE persistent storage
            with open(file_path, "w") as file:
                file.write(file_data)
        except Exception as e:
            response = {
                "file": file_name,
                "error": "Error while storing the file to the storage.",
            }
            return jsonify(response)

        response = {"file": file_name, "message": "Success."}
        return jsonify(response)

    except Exception as e:
        print("Error processing JSON payload at store-file:", str(e))
        return "Error processing JSON payload store-file"



# Runs on port 6000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
