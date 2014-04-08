FROM pjzz/base

# tools
RUN apt-get install -y lighttpd python-moinmoin unzip ssmtp python-flup

# install FixedLeft moinmoin theme
RUN wget "http://moinmo.in/ThemeMarket/FixedLeft?action=AttachFile&do=get&target=FixedLeft197.zip" -q -O /tmp/FixedLeft.zip
RUN cd /tmp && unzip FixedLeft.zip && \
    cp fixedleft.py fixedleftcms.py fixedlefticonbar.py /usr/share/pyshared/MoinMoin/theme && \
    cp /tmp/PageActions.py /usr/share/pyshared/MoinMoin/action && \
    mv /tmp/fixedleft /usr/share/moin/htdocs

# configure lighttpd
ADD 90-moinmoin.conf /etc/lighttpd/conf-available/90-moinmoin.conf
RUN lighttpd-enable-mod fastcgi
RUN lighttpd-enable-mod moinmoin
RUN perl -pi -e's/^#( *.)mod_rewrite/ \1mod_rewrite/' /etc/lighttpd/lighttpd.conf # enable mod_rewrite
EXPOSE 80

# configure moinmoin
ADD moin.fcgi /usr/local/bin/moin.fcgi
ADD wikiconfig.py /usr/local/bin/wikiconfig.py
ADD moin-startup /usr/local/bin/moin-startup
RUN chmod a+rwx /usr/local/bin/moin-startup

ENTRYPOINT /usr/local/bin/moin-startup

