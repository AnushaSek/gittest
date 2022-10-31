import git

local_repo_path = '/Users/ahamed.musthafa/Documents/testgit/gittest/' #config['LOCAL_REPO_PATH']
author = 'amrs-saama' #config['AUTHOR']
my_repo =  git.Repo(local_repo_path)
branch = 'test' #config['GIT_BRANCH']
my_repo.git.checkout(branch)
origin = my_repo.remote(name='origin')
print(origin.pull('test'))
if my_repo.is_dirty():
    my_repo.git.add('--all')
    my_repo.git.commit('-m', 'second commit', author=author)
    origin = my_repo.remote(name='origin')
    origin.push()
