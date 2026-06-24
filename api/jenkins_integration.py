import requests
from requests.auth import HTTPBasicAuth
import os

JENKINS_URL = os.getenv("JENKINS_URL", "http://jenkins:8080")
JENKINS_USER = os.getenv("JENKINS_USER", "admin")
JENKINS_TOKEN = os.getenv("JENKINS_TOKEN", "your-jenkins-api-token")

def attach_to_jenkins_build(build_number, file_path, result):
    """
    Attach QA results as artifact to Jenkins build
    Also update build description with QA result
    """
    try:
        # 1. Upload artifact to Jenkins build
        with open(file_path, 'rb') as f:
            response = requests.post(
                f"{JENKINS_URL}/job/your-pipeline/{build_number}/artifact",
                auth=HTTPBasicAuth(JENKINS_USER, JENKINS_TOKEN),
                files={'file': (os.path.basename(file_path), f)}
            )
        
        # 2. Update build description with QA result
        requests.post(
            f"{JENKINS_URL}/job/your-pipeline/{build_number}/submitDescription",
            auth=HTTPBasicAuth(JENKINS_USER, JENKINS_TOKEN),
            data={
                'description': f"QA Result: {result} | See artifacts for details"
            }
        )
        
        return True
    except Exception as e:
        print(f"Failed to attach to Jenkins: {e}")
        # Still save locally even if Jenkins attachment fails
        return False