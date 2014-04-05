
Running
=======

This Dockerfile will set up a resolver that will resolve normal DNS as a recursive resolver
and also consider itself canonical for the .bit domain, which it resolves by running
namecoind and the NamecoinToBind scripts.

It should be invoked something like:

  $ docker run -d -t -p 5353:53 -p 5353:53/udp pjzz/namecoindns

How It Works:
=============

Internally it uses supervisord to run multiple processes:

  * namecoind, to keep up to date onthe namecoin blockchain
  * cron, to update /etc/bind/dotbit/* from the blockchain using a script from NamecoinToBind
  * restart_bind.sh (from NamecoinToBind)
  * bind, to be the resolver

If you wish to update the version of NamecoinToBind, you can run:

  $ git clone https://github.com/khalahan/NamecoinToBind.git /tmp/n2b
  $ cd /tmp/n2b && git archive -o /tmp/NamecoinToBind.tar.gz HEAD

and then put the NamecoinToBind.tar.gz from /tmp into this directory.  You'll then have to
rebuild the image, of course.




