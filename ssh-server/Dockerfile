FROM ubuntu:22.04@sha256:3ba65aa20f86a0fad9df2b2c259c613df006b2e6d0bfcc8a146afb8c525a9751

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    openssh-server=1:8.9p1-3ubuntu0.13 \
    curl=7.81.0-1ubuntu1.21 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Create SSH directory
RUN mkdir -p /var/run/sshd

# Create a non-root user for SSH access
RUN useradd -m -s /bin/bash sshuser && \
    passwd -d sshuser

# Configure SSH server for passwordless authentication
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    sed -i 's/UsePAM yes/UsePAM no/' /etc/ssh/sshd_config && \
    echo 'PermitEmptyPasswords yes' >> /etc/ssh/sshd_config

# Expose SSH port
EXPOSE 22

# Run as non-root where possible (SSH daemon needs root to bind to port 22)
# Start SSH service in foreground
CMD ["/usr/sbin/sshd", "-D", "-e"]
