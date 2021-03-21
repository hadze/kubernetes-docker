import sys

def hello_world():
    return "Hello world!"

def get_version():
    version = sys.version[0]
    return f"This is Python version: {version}"

if __name__ == "__main__":
    print(hello_world())
    print(get_version())