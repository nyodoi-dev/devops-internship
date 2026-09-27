# Docker Debugging Lab Notes

# Port Already in Use
* Symptom: I tried to run my container with 'sudo docker run', but I got an error saying "port is already allocated". 
* Commands used:'sudo docker ps' to see what was currently running.
* Root Cause: I forgot I already had another container (or app) running on port 8000 on my laptop. Two things can't share the same host port.
* Fix:I just need to pick a different port for my computer to use. Changing the run command to '-p 8081:8000' fixed it.

# Missing Environment Variable
* Symptom: The container started, but then crashed and shut down.
* Commands used: 'sudo docker ps -a' to find the dead container, and 'sudo docker logs' to read the error message inside.
* Root Cause:The Python app was expecting a specific variable to work, but I didn't pass it into the container when I started it, so the code crashed.
* Fix: Add the '-e' flag to the run command to pass the variable in

# Container Exits/Vanishes Immediately
* Symptom: I ran the container, but when I typed 'sudo docker ps', it wasn't on the list. It just vanished.
* Commands used: 'sudo docker ps -a' (to see containers that stopped) and 'sudo docker logs'.
* Root Cause: I realized that a container only stays alive as long as its main job is running. If the 'CMD' in the Dockerfile is just a quick script that finishes instantly, the container thinks its job is done and turns itself off.
* Fix: Make sure the 'CMD' in the Dockerfile is running something that stays open continuously, like our FastAPI web server ('uvicorn').
