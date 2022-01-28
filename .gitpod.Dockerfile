FROM gitpod/workspace-full

RUN brew install docker-compose git-secret lefthook

# Install docker compose v2
RUN mkdir -p ~/.docker/cli-plugins && \
    ln -sfn /home/linuxbrew/.linuxbrew/opt/docker-compose/bin/docker-compose ~/.docker/cli-plugins/docker-compose

# Install oh-my-bash
RUN curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh
