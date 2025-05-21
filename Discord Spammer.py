import discum
import time
import threading

# Display author info
print("=" * 50)
print("🔧 Created by MaJiX - Discord Spammer Tool")
print("=" * 50)

# Get user input
TOKEN = input("Enter your Discord token: ").strip()
channel_input = input("Enter channel IDs (comma-separated): ").strip()
MESSAGE = input("Enter the message to send: ").strip()

CHANNEL_IDS = [channel.strip() for channel in channel_input.split(",")]
bot = discum.Client(token=TOKEN, log=False)

# Control flags
is_running = False
should_quit = False

def send_messages():
    count = 0
    global is_running, should_quit
    while not should_quit:
        if is_running:
            for channel_id in CHANNEL_IDS:
                if not is_running or should_quit:
                    break
                bot.sendMessage(channel_id, MESSAGE)
                count += 1
                print(f"\rMessage Sent #{count}", end='', flush=True)
                time.sleep(3)
        else:
            time.sleep(1)

# Thread to handle sending messages
thread = threading.Thread(target=send_messages)
thread.start()

# Main input loop
print("\nCommands:")
print("[s] Start sending")
print("[p] Pause sending")
print("[q] Quit program")

while not should_quit:
    cmd = input("\nEnter command: ").strip().lower()
    if cmd == 's':
        is_running = True
        print("Started sending messages.")
    elif cmd == 'p':
        is_running = False
        print("Paused.")
    elif cmd == 'q':
        should_quit = True
        print("Quitting...")
    else:
        print("Unknown command. Use 's', 'p', or 'q'.")
