# Do not forget to pin down the version
FROM jupyterhub/jupyterhub:0.9.4

# Copy the JupyterHub configuration in the container
COPY jupyterhub_config.py .

# Download script to automatically stop idle single-user servers
RUN wget https://raw.githubusercontent.com/jupyterhub/jupyterhub/0.9.4/examples/cull-idle/cull_idle_servers.py

# Install dependencies (for advanced authentication and spawning)
RUN pip install \
    dockerspawner==0.10.0 \
    oauthenticator==0.8.0 \
    notebook>=0.4.0


# We make additions here.
# These represent our system users. They exist on the same machine jupyterhub is on.

RUN useradd michael -m -s /bin/bash -d /home/michael
RUN touch /home/michael/test.md
RUN echo "michael:test" | chpasswd michael
RUN echo "Created user Michael"

RUN useradd troy -m -s /bin/bash -d /home/troy
RUN echo "troy:test" | chpasswd troy

RUN useradd joe -m -s /bin/bash -d /home/joe
RUN echo "joe:test" | chpasswd joe

