
MoinMoin
========

MoinMoin an an FCGI under Lighttpd.

Data is stored under /srv/wiki, so you likely want to do something like:

  docker run -d -t -p $PORT:80 -v $WIKIDATA:/srv/wiki pjzz/moinmoin

Note that MoinMoin is fairly stupid URL-wise, using absolute URLs throughout,
so if you locate it anywhere other than / - even through a reverse proxy
on your Host - you'll need to set the url_prefix_static in the wikiconfig.py
that gets written to your $WIKIDATA dir.

