import platform
from datetime import datetime

print("Hello from my Docker container!")
print(f"Python version: {platform.python_version()}")
print(f"Current time: {datetime.now():%Y-%m-%d %H:%M:%S}")
