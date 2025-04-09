import sys

from app.main import run as run_cli
from app.tui import run_tui


def main():
    if len(sys.argv) < 2:
        print("Uso: python run.py [cli|tui|api]")
        return

    mode = sys.argv[1]

    if mode == "cli":
        run_cli()
    elif mode == "tui":
        run_tui()
    elif mode == "api":
        import uvicorn

        uvicorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True)
    else:
        print("Modo inválido. Use: cli | tui | api")


if __name__ == "__main__":
    main()
