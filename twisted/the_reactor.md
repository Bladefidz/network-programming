# The Reactor

The core of Twisted is the reactor event loop. The reactor knows about network, file-system, and timer events. It waits on and demultiplexes these events and dispatches them to waiting event handlers. Twisted takes care of abstracting away paltform-specific behavior and using the underlying nonblocking APIs correctly. Twisted presents a common interface to the various event sources so tha responding to events anywhere in the network stack is easy.

The reactor essentially accomplishes the following:

```
while True:
    timeout = time_until_next_timed_event()
    events = wait_for_events(timeout)
    events += timed_events_until(now())
    for event in events:
        event.process()
```

In the [echo serve and client](echo-server-client), the reactor's listen `TCP` and `connectTCP` methods take care of registering callbacks with the reactor to ge notified when data is available to read from a TCP socket on port 8000.

After those callbacks have been registered, we start the reactor's event loop with `reactor.run`. Once running, the reactor will poll for and dispatch events forever or untul `reactor.stop` is called.