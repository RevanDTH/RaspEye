from pathlib import Path
import os
import subprocess
from sys import executable


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def uninstall(project_dir: Path) -> int:
    print("Uninstalling RaspEye . . .")

    service_name = "raspEye-agent.service"
    service_path = Path("/etc/systemd/system") / service_name
    runner_path = Path("/usr/local/bin/raspEye-agent-runner.sh")
    venv_dir = project_dir / ".venv"

    if service_path.exists():
        run(["systemctl", "stop", service_name])
        run(["systemctl", "disable", service_name])
        service_path.unlink()
        run(["systemctl", "daemon-reload"])

    if runner_path.exists():
        runner_path.unlink()

    if venv_dir.exists():
        subprocess.run(["rm", "-rf", str(venv_dir)], check=True)

    print("RaspEye successfully uninstalled.")
    return 0


def main() -> int:
    project_dir = Path.cwd()

    uninstall_prompt = input(
        "Do you want to uninstall RaspEye? (Y/N) "
    ).strip().lower()

    if uninstall_prompt == "y":
        return uninstall(project_dir)
    elif uninstall_prompt != "n":
        print("Invalid input. Please enter Y or N.")
        return 2

    print("Installing RaspEye on your device . . .")

    venv_dir = project_dir / ".venv"
    venv_python = venv_dir / "bin" / "python"
    venv_pip = [str(venv_python), "-m", "pip"]

    run([executable, "-m", "venv", str(venv_dir)])

    print("Installing dependencies . . .")
    run(venv_pip + ["install", "--upgrade", "pip"])
    run(venv_pip + ["install", "-r", str(project_dir / "requirements.txt")])

    system_service = input(
        "Do you want RaspEye to create a service for the agent? (Y/N) "
    ).strip().lower()

    if system_service == "y":
        agent_location = project_dir / "agent.py"

        runner_path = Path("/usr/local/bin/raspEye-agent-runner.sh")
        runner_content = f"""#!/bin/bash
set -e
exec "{venv_python}" "{agent_location}"
"""
        runner_path.write_text(runner_content)
        os.chmod(runner_path, 0o755)

        service_path = Path("/etc/systemd/system/raspEye-agent.service")
        service_content = f"""[Unit]
Description=RaspEye Agent Service
After=network.target

[Service]
Type=simple
ExecStart={runner_path}
Restart=always
RestartSec=2

[Install]
WantedBy=multi-user.target
"""
        service_path.write_text(service_content)

        run(["systemctl", "daemon-reload"])
        run(["systemctl", "enable", "--now", "raspEye-agent.service"])

    elif system_service != "n":
        print("Invalid input. Please enter Y or N.")
        return 2

    print("Setup run successfully!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())