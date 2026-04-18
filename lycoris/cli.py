import typer

from lycoris.modules import audit, monitor, network, templates, users

app = typer.Typer(
    name="lycoris",
    help="Lycoris — gestión de seguridad para servidores Debian/Ubuntu.",
    no_args_is_help=True,
)

app.add_typer(users.app, name="users")
app.add_typer(network.app, name="network")
app.add_typer(audit.app, name="audit")
app.add_typer(monitor.app, name="monitor")
app.add_typer(templates.app, name="templates")

if __name__ == "__main__":
    app()
