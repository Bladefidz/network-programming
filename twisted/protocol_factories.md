# Protocol Factories

When a connection occured, the instance of `Protocol` will be created and fade away when connection closed.

Persistance configuration of connection keeped by `protocol.Factory` and `protocol.ClientFactory`. A factory's `buildprotocol()` creates a protocol for each new connection, which gets passed to the reactor to register callbacks.