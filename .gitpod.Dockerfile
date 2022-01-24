FROM gitpod/workspace-full

RUN brew install docker-compose git-secret lefthook
RUN mkdir -p ~/.docker/cli-plugins && \
    ln -sfn /home/linuxbrew/.linuxbrew/opt/docker-compose/bin/docker-compose ~/.docker/cli-plugins/docker-compose
