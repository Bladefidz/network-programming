from twisted.internet import protocol, reactor

class Echo(protocol.Protocol):
    """Echo Protocol will be instanciated in memory every time a connection occured.
    
    The Twisted protocol handling data asynchronously"""
    def dataReceived(self, data):
        """Write event data when it arrived, but not send response"""
        self.transport.write(data)

class EchoFactory(protocol.Factory):
    """This is Factory class to persist connection configuration"""
    def buildProtocol(self, addr):
        """Build a Echo protocol on given address"""
        return Echo()

reactor.listenTCP(8000, EchoFactory())
reactor.run()