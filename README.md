# Localization Data Service Test

This code writes Spot's positional data to a .csv every time the client code is run when the service is running.

Open a terminal and define 3 system variables:

```export BOSDYN_CLIENT_USERNAME=user```
```export BOSDYN_CLIENT_PASSWORD=password```
```export BOSDYN_CLIENT_HOSTNAME=spotip```

Start the service with the command: ```hello_world_mission_service.py local --port 1234```

Open another termal and run the client with: ```python remote_mission_client.py --hello-world local --host-ip localhost --port 1234```

Once the client has run you should see a .csv file written to the script directory with a single data point.

The "hello world" service should be available as a custom action on the Spot Tablet, but I have not tested it with the tablet yet.


```remote_mission_client.py``` is the unmodified example code provided by Boston Dynamics.

I added two lines to the ```hello_world_mission_service.py``` example code which are both preceeded by the comment "added by Noah". The two lines are:

```import os``` added at the top of the file.

```os.system("python localization_test.py")``` added to the Tick function definition.
