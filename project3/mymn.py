"""Custom topology example
Two directly connected switches plus a host for each switch:
   host --- switch --- switch --- host
Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        Host1 = self.addHost( 'h1' )
        Host2 = self.addHost( 'h2' )
        Host3 = self.addHost( 'h3' )
        Host4 = self.addHost( 'h4' )
        Host5 = self.addHost( 'h5' )
        Host6 = self.addHost( 'h6' )

        Switch1 = self.addSwitch( 's1' )
        Switch2 = self.addSwitch( 's2' )
        Switch3 = self.addSwitch( 's3' )
        Switch4 = self.addSwitch( 's4' )

        # Add links
        self.addLink( Switch1, Switch2, bw=1000, loss=5 )
        self.addLink( Switch2, Switch3, bw=1000, loss=5 )
        self.addLink( Switch3, Switch4, bw=1000, loss=5 )

        self.addLink( Switch1, Host1, bw=100 )
        self.addLink( Switch1, Host2, bw=100 )
        self.addLink( Switch2, Host3, bw=100 )
        self.addLink( Switch3, Host4, bw=100 )
        self.addLink( Switch4, Host5, bw=100 )
        self.addLink( Switch4, Host6, bw=100 )

topos = { 'mytopo': ( lambda: MyTopo() ) }