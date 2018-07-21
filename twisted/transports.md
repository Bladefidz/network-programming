# Transports

A *transport* represent the connection between two endpoints communicating over a network. Transports describe connection details: for example, is this connection stream-oriented (like TCP) or datagram-oriented (like UDP)? TCP, UDP, Unix sockets, and serial ports are example of transports. Transports implement the `ITransport` interface, which has the following methods:

* `write()`: Write data to the physical connection in a nonblocking manner.
* `writeSequence()`: Write a lst of strings to the physical connection. Useful when working with line-oriented protocols.
* `loseConnection()`: Write all pending data and then close the connection.
* `getPeer()`: Get the remote address of the connection.
* `getHost()`: Like `getPeer`, but returns the address of the local side of the connection.