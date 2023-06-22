from flask import Flask, request, jsonify
import csv
import os
from collections import OrderedDict


app = Flask(__name__)


# Checking if the lines contain a comma
def validate_csv(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        # Check if the first line contains headers
        headers = []
        headers = lines[0].strip().split(",")
        if headers[0].strip() == "product" and headers[1].strip() == "amount":
            return True
        else:
            return False    

# Reading the file to calculate sum
def calculate_sum(file_path, product):
    with open(file_path, "r") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        headers = csv_reader.fieldnames
        total_sum = 0
        for row in csv_reader:
            print(row)
            if row[headers[0]] == product:
                total_sum += int(row[headers[1]].strip())
    return str(total_sum)


# Receives the POST request from Container 1 and performs operations [1,2]
@app.route("/result", methods=["POST"])
def receive_payload():
    if request.method == "POST":
        try:
            json_payload = request.get_json()
            print("Received payload:")
            print(json_payload)

            # Extracting file_name and product column
            file_name = json_payload.get("file")
            product = json_payload.get("product")

            current_directory = "/Alagappan_PV_dir/"
            file_path = os.path.join(current_directory, file_name)

            if not validate_csv(file_path):
                response_data = OrderedDict(
                    [("file", file_name), ("error", "Input file not in CSV format.")]
                )
                return jsonify(response_data)

            sum = calculate_sum(file_path, product)

            response_data = {"file": file_name, "sum": sum}
            return jsonify(response_data)

        except Exception as e:
            print("Error processing payload2:", str(e))
            return "Error processing payload2", 500
    else:
        return "Method Not Allowed", 405


# Runs on port 8080
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
