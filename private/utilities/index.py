import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)

import requests
from requests.auth import HTTPBasicAuth

def create_github_repo(token, repo_name, description="", private=False):
    api_url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository. Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Ganti dengan Personal Access Token (PAT) Anda
    github_token = "YOUR_GITHUB_TOKEN"

    # Ganti dengan nama repositori yang diinginkan
    repository_name = "placeholder-repo"

    # Ganti dengan deskripsi yang diinginkan
    repository_description = "This is a placeholder repository created using GitHub API."

    # Apakah repositori ini akan bersifat private (True/False)
    is_private = False

    create_github_repo(github_token, repository_name, repository_description, is_private)