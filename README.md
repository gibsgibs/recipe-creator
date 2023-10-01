# recipe-creator

## GitHub API Config File
You will need to create a file called `api_config.yaml` at the root of the project. The file should be structured as follows:
```yaml
github_api:
  username: <your-github-username>
  token: <your-personal-access-token>
```

## General Use
Add all of the GitHub repository names to the `repo_names.yaml` file, then run `python app.py`. The result should be a properly formatted output file called `recipes.yaml`.

The repo owner name and header information are located in `config.yaml`.
