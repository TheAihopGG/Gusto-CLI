from typer import Typer

app = Typer(no_args_is_help=True)
apps = []
[app.add_typer(_) for _ in apps]

if __name__ == "__main__":
    app()
