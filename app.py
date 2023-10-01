from github_helper import GithubHelper
from utils import read_yaml_file
from utils import write_yaml_file
from utils import append_yaml_file

def main():
    githubHelper = GithubHelper()
    repo_names = read_yaml_file("repo_names.yaml")['repo_names']
    tasks = []
    for repo_name in repo_names:
        repo_data = githubHelper.make_get_request(repo_name)
        task = {
            "action": "download_github",
            "dest": get_dest(repo_data),
            "ref": repo_data.get('default_branch', 'NA'),
            "src": repo_data['url']
        }
        tasks.append(task)
    header = read_yaml_file('config.yaml')['recipe_header']
    write_yaml_file("recipes.yaml", header)
    append_yaml_file("recipes.yaml", tasks)
    
def get_dest(repo_data):
    topics = repo_data.get('topics', [])
    topic = topics[0] if len(topics) > 0 else 'NA'
    return f"./resources/[{topic}]/{repo_data.get('name', 'NA')}"

                        
if __name__ == "__main__":
    main()