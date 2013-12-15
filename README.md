# TriggerQueue


## Introduction
TriggerQueue maintains a queue for all triggered events.

## requirement:
- zeromq(pyzmq)
- django 1.6

## example:
1. trigger a new instant event to queue:
	POST /new-event/ HTTP/1.1
    type=instant

2. add a periodly event to queue, then TriggerQueue will call it later:
	POST /new-event/ HTTP/1.1
    type=period

3. add a url difference event to queue, then TriggerQueue will call it later:
	POST /new-event/ HTTP/1.1
    type=page

