from twisted.internet import reactor, protocol

class EchoClient(protocol.Protocol):
    def connectionMade(self):
        """The EchoClient protocol will send the data to the
        server, sends it 'Hello, world!', and then terminate
        the connection"""
        self.transport.write("Hello, world!".encode('utf-8'))
    
    def dataReceived(self, data):
        """Write anything from server"""
        print("Server said: ", data)
        self.transport.loseConnection()

class EchoFactory(protocol.ClientFactory):
    """The CLientFactory provides 'reactor.connect*' method
    that call lower-level connection APIs"""
    def buildProtocol(self, addr):
        """Build a protocol to listen in given address"""
        return EchoClient()
    
    def clientConnectionFailed(self, connector, reason):
        """Stop client when connection can not established"""
        print("Connection failed.")
        reactor.stop()
    
    def clientConnectionLost(self, connector, reason):
        """Called when connection was made and the disconnected"""
        print("Connection lost.")
        reactor.stop()

reactor.connectTCP("localhost", 8000, EchoFactory())
reactor.run()