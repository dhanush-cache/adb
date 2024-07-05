""" Module to execute adb commands. """

from pathlib import Path
import subprocess


def run_adb_command(command: list) -> subprocess.CompletedProcess:
    return subprocess.run(command, check=True, capture_output=True, text=True)


def pair(url: str, pairing_code: str) -> None:
    command = ["adb", "pair", url, pairing_code]
    run_adb_command(command)


def extract(package_name: str, target: Path) -> None:
    command = ["adb", "shell", "pm", "path", package_name]
    result = run_adb_command(command)
    apk_path = result.stdout.strip().replace("package:", "").split("\n")[0]
    if apk_path:
        command = ["adb", "pull", apk_path, f"{target}/{package_name}.apk"]
        run_adb_command(command)


def connect(url: str) -> None:
    command = ["adb", "connect", url]
    run_adb_command(command)


def is_connected() -> bool:
    command = ["adb", "devices"]
    result = run_adb_command(command)
    devices = result.stdout.splitlines()[1:]
    return any("device" in device for device in devices)


def is_installed(package_name: str) -> bool:
    command = ["adb", "shell", "pm", "list", "packages", package_name]
    result = run_adb_command(command)
    return package_name in result.stdout


def is_enabled(package_name: str) -> bool:
    command = ["adb", "shell", "pm", "list", "packages", "-e"]
    result = run_adb_command(command)
    return package_name in result.stdout


def install(apk_path: Path) -> None:
    command = ["adb", "install", str(apk_path)]
    run_adb_command(command)


def clear_data(package_name: str) -> None:
    command = ["adb", "shell", "pm", "clear", package_name]
    run_adb_command(command)


def uninstall(package_name: str) -> None:
    try:
        command = ["adb", "uninstall", package_name]
        run_adb_command(command)
    except:
        pass
    finally:
        command = ["adb", "uninstall", "--user", "0", package_name]
        run_adb_command(command)


def enable(package_name: str) -> None:
    command = ["adb", "shell", "pm", "enable", package_name]
    run_adb_command(command)


def disable(package_name: str) -> None:
    try:
        command = ["adb", "uninstall", package_name]
        run_adb_command(command)
    except:
        pass
    finally:
        command = ["adb", "shell", "pm", "disable-user", package_name]
        run_adb_command(command)
