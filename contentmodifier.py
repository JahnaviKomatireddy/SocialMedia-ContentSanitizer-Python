
n = int(input("Enter number of posts: "))
posts = []
for i in range(n):
    user = input("Enter username: ")
    post = input("Enter post: ")
    posts.append((user, post))

bannedwords = ["bad", "toxic", "hate","bully","spam","worst","useless","dumb"]
totalPosts = len(posts)
postscleaned = 0
cleanposts = 0
user_flags = {}
links_file = open("../links_found.txt", "w")

print("\nPosts:")
for user, post in posts:
    original = post
    flagged = False
    if user not in user_flags:
        user_flags[user] = 0
    for word in bannedwords:
        if word in post.lower():
            post = post.replace(word, "***")
            flagged = True
    words = original.split()
    for w in words:
        if w.startswith("http"):
            links_file.write(w + "\n")
    if flagged:
        postscleaned += 1
        user_flags[user] += 1
    else:
        cleanposts += 1
    print(f"{user}: {post}")

links_file.close()
print("Final Report:")
print(f"Total Posts Screened: {totalPosts}")
print(f"Cleaned Posts: {postscleaned}")
print(f"Clean Posts: {cleanposts}")

print("Number of times a user post have been modified or flagged")
print(user_flags)