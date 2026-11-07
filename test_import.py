import sys
print("Python Executable:", sys.executable)

try:
    from moviepy import VideoFileClip
    print("✅ moviepy successfully imported!")
except ModuleNotFoundError as e:
    print("❌ ModuleNotFoundError:", e)
