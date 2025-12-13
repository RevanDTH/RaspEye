# RaspEye
![raspEye-logo](./frontend/static/img/logo.png)
A monitoring tool for your raspberry pi to check system performance and health of your raspberry pi. RaspEye runs as a Agent in the background und provides system metrics to the backend that forwards everything to the frontend. The frontend is kept very simple but I plan to make it a little bit more complex. 



## Before installing

Please make sure that you have the docker engine installed on your Raspberry Pi in order to run the two containers containing the backend and the frontend. If you don't know how to install docker, please follow this [guide](https://docs.docker.com/engine/install/debian/) that guides you trough that. You also need to have the git client installed in order to pull the latest version of the repository. If you don't want to install the git client, you can also pull the latest release with curl and unpack it yourself :). You also need to have python installed on your Raspberry Pi, preferably the latest version.


## Installation guide

1. Clone the latest version of RaspEye from Github
`git pull https://github.com/RevanDTH/RaspEye.git` 

2. Navigate to the downloaded directory
`cd RaspEye`

3. Run setup.py and follow the instructions
`python setup.py`

4. (Optional) After the setup your agent should already be running but you can check the state of the agent by entering the following command
`sudo systemctl status raspEye-agent.service`

5. Build both docker containers (and the network)
`docker compose build`

6. Start both containers in detached mode
`docker compose up -d`

Now you're ready and you can access RaspEye with the local IP-Adresse of your Raspberry Pi.