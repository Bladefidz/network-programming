# Protocols

* Protocols* describe how to proccess network events asynchronously. Twisted maintains implementations for many popular application protocols, including HTTP, Telnet, DNS, and IMAP. Protocols implement the `IProtocol` interface, which has the following methods:

* `makeConnection()`: Create a connection between two endpoints across a transport.
* `connectionMade()`: Called when connection to another endpoint is made.
* `dataReceived()`: Called when data is received across a transport.
* `connectionLost()`: Called when the connection is shut down.