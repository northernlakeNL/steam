from github import Github

g = Github("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")

g = Github(base_url="https://api.github.com/user/repos", login_or_token="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")

for repo in g.get_user().get_repos():
    print(repo.name)