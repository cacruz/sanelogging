#!/usr/bin/env python

from sanelogging import log

log.info("starting up!")

log.error("something went wrong.")

log.die("bailing out") # exits

print("no soup for you.")
