from moviepy.editor import VideoFileClip
from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Controller as MouseController, Button
import pydirectinput
import pyttsx3
import time
import threading

# Initialize the keyboard and mouse controllers
keyboard = KeyboardController()
mouse = MouseController()

# Initialize the TTS engine
tts_engine = pyttsx3.init()

# Function to simulate key press with logging
def press_key(key, timestamp):
    print(f"Pressing {key} at {timestamp} seconds")
    keyboard.press(key)
    time.sleep(0.35)  # Adding a slight delay to ensure the key press is registered
    keyboard.release(key)

# Function to simulate mouse movement with logging
def move_mouse(x, y, timestamp):
    print(f"Moving mouse by ({x}, {y}) at {timestamp} seconds")
    pydirectinput.moveRel(x, y, relative=True)

# Function to simulate left click with logging
def left_click(timestamp):
    print(f"Left click at {timestamp} seconds")
    mouse.click(Button.left, 1)

# Function to handle events
def handle_events(events, start_time):
    for timestamp, event in sorted(events.items()):
        # Calculate the time to wait before the next event
        time_to_wait = timestamp - (time.time() - start_time)
        
        # If the time to wait is positive, wait for that duration
        if time_to_wait > 0:
            time.sleep(time_to_wait)
        
        # Check the type of event and simulate accordingly
        if event[0] == 'key':
            press_key(event[1], timestamp)
        elif event[0] == 'move':
            move_mouse(event[1], event[2], timestamp)
        elif event[0] == 'click':
            left_click(timestamp)

# Load video and resize
video_path = r"C:\Users\super\Desktop\Lightsaber Duel Custom MP3\duelofthefates.mp4"
video = VideoFileClip(video_path).resize(height=360)  # Resize to a height of 360 pixels

# Manually created list of events (keys or mouse clicks) and their times
events = {
    1.75: ('key', 'i'),
    3.55: ('key', 'i'),
    5.29: ('key', 'i'),
    5.45: ('key', 'i'),
    9.00: ('move', -100, 0),
    10.72: ('move', 100, 0),
    11.67: ('key', '1'),
    11.89: ('key', '2'),
    12.60: ('key', 'd'),
    13.20: ('move', -100, 0),
    13.45: ('move', 100, 0),
    13.70: ('key', '2'),
    14.20: ('key', '2'),
    14.72: ('move', 100, 0),
    14.90: ('move', -100, 0),
    15.00: ('key', '2'),
    15.20: ('move', 100, 0),
    16.06: ('key', '2'),
    21.00: ('click',),
    22.00: ('key', 'w'),
    23.00: ('key', '2'),
    25.00: ('move', 100, 0),
    25.50: ('key', '1'), 
    27.50: ('click',),
    31.00: ('key', '2'),
    32.00: ('move', -100, 0),
    32.50: ('key', '1'),
    34.00: ('move', 100, 0),
    34.50: ('key', '2'),
    35.00: ('key', '1'),
    37.00: ('key', 's'),
    49.00: ('move', 100, 0),
    54.00: ('move', -100, 0),
    56.00: ('move', -100, 0),
    57.00: ('key', '2'),
    58.00: ('move', -100, 0),
    59.00: ('move', -100, 0),
    60.00: ('move', 100, 0),
    62.00: ('click',),
    68.50: ('click',),
    69.00: ('click',),
    75.00: ('click',),
    76.50: ('move', -100, 0),
    78.00: ('key', '1'),
    80.00: ('key', 'd'),
    80.50: ('key', '2'),
    81.75: ('key', 'd'),
    87.00: ('key', '2'),
    89.00: ('move', 100, 0),
    90.00: ('key', '2'),
    93.00: ('key', 'w'),
    93.30: ('key', 'i'),
    95.00: ('move', 100, 0),
    95.75: ('key', '2'),
    97.00: ('key', 'w'),
    98.50: ('move', 100, 0),
    105.00: ('move', 100, 0),
    118.30: ('click',),
    138.00: ('key', 'i'),
    140.50: ('key', 'i'),
    141.75: ('move', 100, 0),
    142.00: ('key', '1'),
    142.25: ('key', '2'),
    147.50: ('move', 100, 0),
    148.00: ('move', -100, 0),
    148.25: ('key', '1'),
    153.75: ('key', 'w'),
    154.00: ('key', 's'),
    155.00: ('move', 100, 0),
    156.00: ('key', '1'),
    159.50: ('key', 's'),
    160.00: ('key', 'w'),
    161.00: ('key', 's'),
    162.10: ('key', 'd'),
    167.25: ('move', 100, 0),
    167.50: ('move', -100, 0),
    170.00: ('key', 'w'),
    171.50: ('click',),
    172.00: ('click',),
    189.00: ('key', 'i'),
    189.25: ('key', 'i'),
    189.50: ('key', 'i'),
    192.00: ('move', 100, 0),
    193.00: ('key', '1'),
    194.00: ('key', '1'),
    194.30: ('key', 'd'),
    195.00: ('key', 'd'),
    195.25: ('key', 'a'),
    196.00: ('key', 'w'),
    197.40: ('move', 100, 0),
    197.75: ('key', '2'),
    198.00: ('key', 'd'),
    199.00: ('key', '1'),
    199.50: ('key', '2'),
    199.75: ('key', '1'),
    202.00: ('move', 100, 0),
    202.50: ('key', '2'),
    203.00: ('key', 'i'),
    203.50: ('move', 100, 0),
    204.00: ('key', 'w'),
    204.70: ('key', '2'),
    205.00: ('key', 'd'),
    206.00: ('key', 'a'),
    207.00: ('key', 'w'),
    208.00: ('key', 'd'),
    208.60: ('click',),
    214.50: ('move', 100, 0),
    215.00: ('move', 100, 0),
    215.50: ('click',),
    223.50: ('key', '2'),
    224.00: ('move', 100, 0),
    225.00: ('key', 'w'),
    226.00: ('key', '1'),
    226.50: ('key', '2'),
    227.50: ('key', 'w'),
    230.00: ('click',),
}

# Start time of the video
start_time = time.time()

# Start the thread to handle events
event_thread = threading.Thread(target=handle_events, args=(events, start_time))
event_thread.start()

# Start playing the video
video.preview(fps=24, audio=True, audio_fps=44100, fullscreen=False)

# Wait for the event thread to finish
event_thread.join()