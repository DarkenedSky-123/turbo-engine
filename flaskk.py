import git

# Assuming your git repository is located in the same directory as your Python code
repo = git.Repo('.')

# Open your data.txt file in append mode
with open("./data.txt", "a") as f:
    f.write("Hello\n")

# Stage the changes made to the file
repo.index.add(["data.txt"])

# Commit the changes with a custom commit message
repo.index.commit("Added content to data.txt")
