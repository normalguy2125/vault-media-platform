import os
import subprocess

def clone_repository(repo_url, destination):
    """Clone a Git repository to the specified destination."""
    try:
        subprocess.run(["git", "clone", repo_url, destination], check=True)
        print(f"Successfully cloned {repo_url} to {destination}._")
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository: {e}")

def setup_environment(destination):
    """Perform additional setup steps, if needed."""
    # Example: installing dependencies if a requirements.txt file exists
    requirements_file = os.path.join(destination, "requirements.txt")
    if os.path.isfile(requirements_file):
        subprocess.run(["pip", "install", "-r", requirements_file], check=True)
        print("Dependencies installed successfully.")

if __name__ == "__main__":
    REPO_URL = "https://github.com/your/repo.git"  # Replace with the desired repository URL
    DESTINATION = "destination_path"  # Replace with your local path

    clone_repository(REPO_URL, DESTINATION)
    setup_environment(DESTINATION)