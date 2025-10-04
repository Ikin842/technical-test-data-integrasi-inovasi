from typing import Optional
import typer
from controller import (
    engine
)

__app_name__ = "Streaming-Template"
__version__ = "0.0.1"

app = typer.Typer()
app.add_typer(engine.app, name="engine")

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.callback()
def main(version: Optional[bool] = typer.Option(
    None,
    "--version",
    "-v",
    help="Show the application's version and exit.",
    callback=_version_callback,
    is_eager=True,
)
) -> None:
    return

if __name__ == '__main__':
    app()