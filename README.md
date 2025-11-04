### 📝 **Instagram Not-Following-Back Checker (Python Script)**

This Python script compares your Instagram followers and following lists to find which accounts you follow that don’t follow you back.

#### **Purpose**

To analyze your Instagram data (in JSON format) and easily see who isn’t following you back.

#### **Required Files**

1. `followers.json`
2. `following.json`

   > Both files can be downloaded from Instagram → *Settings → Accounts Center → Your information and permissions → Download your information → Some of your information → Followers and Following (in JSON format)*

#### **Steps to Use**

1. **Download Instagram Data**

   * Go to your Instagram settings and download your followers/following data in JSON format.
   * Extract the ZIP file sent to your email.
   * Locate `followers.json` and `following.json`.

2. **Save Files and Script**

   * Copy both JSON files into a folder, e.g.
     `C:\Users\admin\OneDrive\Codes_By_Vraj\Instagram\`
   * Create a new Python file named `instagram_checker.py` and paste the code below:

```python
import json
import os

# Paths to your files
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

# Extract usernames safely
def extract_usernames(data):
    usernames = set()
    if isinstance(data, dict) and "relationships_following" in data:
        data = data["relationships_following"]
    for entry in data:
        try:
            usernames.add(entry["string_list_data"][0]["value"])
        except (KeyError, IndexError, TypeError):
            if "username" in entry:
                usernames.add(entry["username"])
            elif "name" in entry:
                usernames.add(entry["name"])
    return usernames

followers = extract_usernames(followers_data)
following = extract_usernames(following_data)

not_following_back = following - followers

print("\n🚫 People not following you back:")
if not not_following_back:
    print("🎉 Everyone you follow follows you back!")
else:
    for user in sorted(not_following_back):
        print(user)
```

3. **Run the Script**

   * Open Command Prompt or PowerShell.
   * Navigate to your script folder:

     ```bash
     cd "C:\Users\admin\OneDrive\Codes_By_Vraj\Instagram"
     ```
   * Run:

     ```bash
     python instagram_checker.py
     ```

4. **View the Result**

   * The console will display:

     ```
     🚫 People not following you back:
     username1
     username2
     ...
     ```
   * If everyone follows you back:

     ```
     🎉 Everyone you follow follows you back!
     ```

#### **Explanation**

* The script reads both JSON files using the `json` module.
* It extracts usernames into Python sets.
* It compares both sets to find users you follow who don’t follow you.
* Results are printed clearly in the terminal.

#### **Optional (Save Output)**

To save results in a text file, add:

```python
with open("not_following_back.txt", "w", encoding="utf-8") as f:
    for user in sorted(not_following_back):
        f.write(user + "\n")
```

---
