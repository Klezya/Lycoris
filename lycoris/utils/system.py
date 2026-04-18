import os
import shutil
import subprocess


def is_root() -> bool:
    return os.geteuid() == 0


def require_root() -> None:
    if not is_root():
        import typer
        raise typer.BadParameter(
            "Este comando requiere privilegios de superusuario. Usa sudo."
        )


def command_exists(name: str) -> bool:
    return shutil.which(name) is not None


def run(
    cmd: list[str],
    capture: bool = True,
    check: bool = True,
) -> str | None:
    result = subprocess.run(
        cmd,
        capture_output=capture,
        text=True,
        check=check,
    )
    if capture:
        return result.stdout.strip()
    return None
