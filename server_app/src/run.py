"""
---- this script run server app (0-0)
"""
from core.startup import StartUp

def main():
    StartUp().start()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        SystemExit, print("[-] Somebody kill this server")