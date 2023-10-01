from utils import read_yaml_file
from logger import get_logger
import requests
from requests import RequestException

class GithubHelper:
    def __init__(self):
        api_config = read_yaml_file("api_config.yaml")["github_api"]
        self.username = api_config["username"]
        self.token = api_config["token"]
        config = read_yaml_file("config.yaml")
        self.repo_owner = config["repo_owner"]
        self.logger = get_logger(__name__)

    def make_get_request(self, repo_name):
        api_url = self.build_api_url(repo_name)
        headers = self.get_headers()
        try:
            self.logger.info(f"Sending request to {api_url}...")
            response = requests.get(api_url, headers=headers)
            if response.status_code == 200:
                self.logger.info(f"Request successful")
                return response.json()
            else:
                self.logger.warning(f"Request failed - status code: {response.status_code}")
        except RequestException as e:
            self.logger.error(e)

    def build_api_url(self, repo_name):
        return f"https://api.github.com/repos/{self.repo_owner}/{repo_name}"

    def get_headers(self):
        return {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }
    
    def __str__(self):
        return f"api username: {self.username}, repo_owner: {self.repo_owner}"
