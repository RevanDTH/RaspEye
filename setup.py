from os import system,getcwd,chmod

### Setup code that runs once
print("Installing RaspEye on your device . . .")

print("Installing dependencies . . .")
system("pip install -r ./requirements.txt")

system_service = input("Do you want RaspEye to create a service for the agent? (Y/N)")

match system_service.lower:
    case "y":
        agent_location = getcwd() + "/agent.py"
        shell_string = f"""
#!/bin/bash

python {agent_location}
        """

        with open("/raspEye-agent-runner.sh","a+") as f:
            f.write(shell_string)
        
        chmod("/raspEye-agent-runner.sh", 0o755)

        runner_location = getcwd + "/raspEye-agent-runner.sh"
        service_string = f"""
[Unit]
Description=RaspEye Agent Service
After=network.target

[Service]
Type=simple
ExecStart={runner_location}
Restart=always

[Install]
WantedBy=multi-user.target
"""
        with open("/etc/systemd/system/raspEye-agent.service") as f:
            f.write(service_string)
        
        system("sudo systemctl daemon-reload")
        system("sudo systemctl enable raspEye-agent.service")
        system("sudo systemctl start raspEye-agent.service")

        print("Setup run successfully!")
    case "n":
        print("Setup run successfully!")