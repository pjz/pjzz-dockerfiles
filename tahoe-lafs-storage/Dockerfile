FROM pjzz/base

# Install tahoe
RUN apt-get install -y build-essential python-pip libcrypto++-dev python-dev libssl-dev libffi-dev
RUN pip install twisted allmydata-tahoe

RUN mkdir -p /tahoe
RUN chown -R daemon:daemon /tahoe

# /etc/tahoe.cfg.tmpl used by tahoe-setup
ADD tahoe.cfg /etc/tahoe.cfg.tmpl

# port 34567 specified in tahoe-setup
EXPOSE 34567

# our setup/wrapper script
ADD tahoe-setup /usr/local/bin/tahoe-setup
RUN chmod +x /usr/local/bin/tahoe-setup

USER daemon
ENTRYPOINT /usr/local/bin/tahoe-setup


