FROM jenkins/jenkins:lts

USER root

# Install required base packages
RUN apt-get update && \
    apt-get install -y ca-certificates curl gnupg python3 python3-pip && \
    install -m 0755 -d /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg && \
    chmod a+r /etc/apt/keyrings/docker.gpg

# Add Docker official repo
RUN echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo $VERSION_CODENAME) stable" \
  > /etc/apt/sources.list.d/docker.list

# Install Docker + Compose plugin (modern way ✅)
RUN apt-get update && \
    apt-get install -y docker-ce docker-ce-cli docker-compose-plugin && \
    apt-get clean

# Add jenkins user to docker group
RUN usermod -aG docker jenkins

USER jenkins
