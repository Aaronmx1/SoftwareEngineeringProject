# SoftwareEngineeringProject
Project meant to satisfy Software Engineering course requirement

Clear instructions for how to programmatically REQUEST data from the microservice you implemented. Include an example call.
  - To request data from the microservice the user must directly call my microservice in order to pass the microservice a
    dictionary value (example provided) or string value (not shown here), depending on which user is using my microservice.
    Example call:
      To convert temperature values pass dictionary containing temperature values to microservice which are then converted
      dictionary = {{'maxTemperature_0': '41.11', 'minTemperature_0': '30.00', 'maxTemperature_1': '44.44', 'minTemperature_1': '30.56'}
      socket.send(json.dumps(min_max_dict).encode())

Clear instructions for how to programmatically RECEIVE data from the microservice you implemented.
  - In order to receive converted dictionary data from microservice the user must receive data through the same socket
    bound and json.load(message) which was received in order to maintain data in dictionary format.
  The main program component receiving the dictionary would look like such:
  message = socket.recv()
  print("json.loads(message): ", json.loads(message))
