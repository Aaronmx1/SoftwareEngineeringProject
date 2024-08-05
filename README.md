# Microservice Project

This project is designed to satisfy the Software Engineering course requirement. The microservice provided converts characters to hexadecimal for authentication key generation and converts Fahrenheit temperatures to Celsius.

## Overview

This microservice is implemented using ZeroMQ for messaging and JSON for data formatting. It can perform the following conversions:
1. Characters to hexadecimal.
2. Fahrenheit temperatures to Celsius.

## Features

- Converts characters to their hexadecimal representation.
- Converts Fahrenheit temperature values to Celsius.

## Prerequisites

- Python 3.x
- ZeroMQ library (`pyzmq`)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name

2. Install the required dependencies:
    pip install pyzmq

**Request Data**
To request data from the microservice, you need to send a JSON-encoded dictionary or string value via a ZeroMQ socket.

**Example Call:**
import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# Example dictionary to convert Fahrenheit to Celsius
temperature_data = {
    'maxTemperature_0': '41.11',
    'minTemperature_0': '30.00',
    'maxTemperature_1': '44.44',
    'minTemperature_1': '30.56'
}

socket.send(json.dumps(temperature_data).encode())

# Receive the converted data
message = socket.recv()
converted_data = json.loads(message)
print("Converted data:", converted_data)

**Receive Data**
To receive the converted data from the microservice, listen on the same socket and decode the JSON message.

   **Example:**
message = socket.recv()
converted_data = json.loads(message)
print("Converted data:", converted_data)
