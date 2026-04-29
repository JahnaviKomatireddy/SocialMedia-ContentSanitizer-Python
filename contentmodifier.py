# Social Media Content Sanitizer
import re

n = int(input("Enter number of posts: "))
posts = []

for i in range(n):
    user = input("Enter username: ")
    post = input("Enter post: ")
    posts.append((user, post))
bannedwords = ["bad", "toxic", "hate", "bully", "spam", "worst", "useless", "dumb", "bullied"]

totalPosts = len(posts)
postscleaned = 0
cleanposts = 0
user_flags = {}
links_file = open("links_found.txt", "w")

pattern = r'\b(' + '|'.join(bannedwords) + r')\b'
def mask(match):
    return "*" * len(match.group())

print("\nPosts:")

for user, post in posts:
    original = post
    if user not in user_flags:
        user_flags[user] = 0

    new_post = re.sub(pattern, mask, post, flags=re.IGNORECASE)
    if new_post != post:
        postscleaned += 1
        user_flags[user] += 1
    else:
        cleanposts += 1

    words = original.split()
    for w in words:
        if w.startswith("http"):
            links_file.write(w + "\n")
    print(f"{user}: {new_post}")

links_file.close()

print("\nFinal Report:")
print(f"Total Posts Screened: {totalPosts}")
print(f"Cleaned Posts: {postscleaned}")
print(f"Clean Posts: {cleanposts}")

print("\nUser Flag Summary:")
print(user_flags)