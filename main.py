import asyncio
from telethon import TelegramClient, types

# --- CONFIGURATION ---
API_ID =    # Replace with your API ID
API_HASH = ' '  # Replace with your API Hash
MESSAGE = """
🛑🛑🛑🛑 Your message here🛑🛑🛑🛑
"""
INTERVAL = 10   # Seconds between messages

client = TelegramClient('session_name', API_ID, API_HASH)

async def main():
    await client.start()
    print("✅ Client Authenticated!")

    # 1. Fetch all groups/channels you are in
    print("🔍 Fetching your groups...")
    groups = []
    async for dialog in client.iter_dialogs():
        if dialog.is_group or dialog.is_channel:
            groups.append(dialog)

    # 2. List the groups for the user to choose
    print("\n--- YOUR GROUPS ---")
    for i, g in enumerate(groups):
        print(f"[{i}] {g.name} (ID: {g.id})")

    # 3. User input to select the group
    try:
        index = int(input("\n🔢 Enter the [number] of the group to spam: "))
        target_group = groups[index]
        print(f"🚀 Starting spam in: {target_group.name}")
    except (ValueError, IndexError):
        print("❌ Invalid selection. Exiting.")
        return

    # 4. The Loop
    while True:
        try:
            await client.send_message(target_group, MESSAGE)
            print(f"✔️ Sent at {target_group.name} | Waiting {INTERVAL}s")
            await asyncio.sleep(INTERVAL)
        except Exception as e:
            print(f"🚨 Error: {e}")
            print("Waiting 30 seconds before retrying...")
            await asyncio.sleep(30)

with client:
    client.loop.run_until_complete(main())
