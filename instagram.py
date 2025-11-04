import json
import os

# Paths to your files (update if needed)
followers_path = r"C:\Users\admin\OneDrive\Codes_By_Vraj\Instagram\followers.json"
following_path = r"C:\Users\admin\OneDrive\Codes_By_Vraj\Instagram\following.json"

# Check if files exist
if not os.path.exists(followers_path):
    print("❌ followers.json file not found at:", followers_path)
    exit()
if not os.path.exists(following_path):
    print("❌ following.json file not found at:", following_path)
    exit()

# Load JSON data
with open(followers_path, "r", encoding="utf-8") as f:
    followers_data = json.load(f)

with open(following_path, "r", encoding="utf-8") as f:
    following_data = json.load(f)

# ---- Helper to extract usernames safely ----
def extract_usernames(data):
    usernames = set()
    if isinstance(data, dict) and "relationships_following" in data:
        data = data["relationships_following"]

    for entry in data:
        try:
            # Common format
            usernames.add(entry["string_list_data"][0]["value"])
        except (KeyError, IndexError, TypeError):
            # Fallback for different JSON shapes
            if "username" in entry:
                usernames.add(entry["username"])
            elif "name" in entry:
                usernames.add(entry["name"])
    return usernames

# ---- Extract usernames ----
followers = extract_usernames(followers_data)
following = extract_usernames(following_data)

# ---- Compare ----
not_following_back = following - followers

print("\n🚫 People not following you back:")
if not not_following_back:
    print("🎉 Everyone you follow follows you back!")
else:
    for user in sorted(not_following_back):
        print(user)
