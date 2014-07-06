from switchyard.lib.packet import *
from switchyard.lib.address import EthAddr, IPAddr
from switchyard.lib.topo.util import *
from switchyard.lib.topo.topobuild import *
import unittest 

class TopologyTests(unittest.TestCase):
    def testHumanizeCap(self):
        self.assertEqual(humanize_bandwidth(100), "100 bits/s")
        self.assertEqual(humanize_bandwidth(1000), "1 Kb/s")
        self.assertEqual(humanize_bandwidth(10000), "10 Kb/s")
        self.assertEqual(humanize_bandwidth(150000), "150 Kb/s")
        self.assertEqual(humanize_bandwidth(1500000), "1.5 Mb/s")
        self.assertEqual(humanize_bandwidth(10000000), "10 Mb/s")
        self.assertEqual(humanize_bandwidth(100000000), "100 Mb/s")
        self.assertEqual(humanize_bandwidth(900000000), "900 Mb/s")
        self.assertEqual(humanize_bandwidth(1000000000), "1 Gb/s")
        self.assertEqual(humanize_bandwidth(100000000000), "100 Gb/s")
        self.assertEqual(humanize_bandwidth(2000000000000), "2 Tb/s")

    def testUnhumanizeCap(self):
        self.assertEqual(unhumanize_bandwidth("100 bits/s"), 100)
        self.assertEqual(unhumanize_bandwidth("1 Kb/s"), 1000)
        self.assertEqual(unhumanize_bandwidth("1 KB/s"), 8000)
        self.assertEqual(unhumanize_bandwidth("  1  KByte per sec"), 8000)
        self.assertEqual(unhumanize_bandwidth("  1.0  KByte per sec"), 8000)
        self.assertEqual(unhumanize_bandwidth("10 Kb/s"), 10000)
        self.assertEqual(unhumanize_bandwidth("150 Kb/s"), 150000)
        self.assertEqual(unhumanize_bandwidth("1.5 Mb/s"), 1500000)
        self.assertEqual(unhumanize_bandwidth("10 Mb/s"),  10000000)
        self.assertEqual(unhumanize_bandwidth("100 Mb/s"), 100000000)
        self.assertEqual(unhumanize_bandwidth("900 Mb/s"), 900000000)
        self.assertEqual(unhumanize_bandwidth("1 Gb/s"),    1000000000)
        self.assertEqual(unhumanize_bandwidth("100 Gb/s"),100000000000)
        self.assertEqual(unhumanize_bandwidth("2 Tb/s"), 2000000000000)
        self.assertEqual(unhumanize_bandwidth("100000"), 100000)
        self.assertEqual(unhumanize_bandwidth("100000  "), 100000)
        
    def testHumanizeDelay(self):
        self.assertEqual(humanize_delay(0.1), "100 milliseconds")
        self.assertEqual(humanize_delay(0.01), "10 milliseconds")
        self.assertEqual(humanize_delay(0.001), "1 millisecond")
        self.assertEqual(humanize_delay(0.002), "2 milliseconds")
        self.assertEqual(humanize_delay(0.0002), "200 microseconds")
        self.assertEqual(humanize_delay(1), "1 second")
        self.assertEqual(humanize_delay(1.5), "1500 milliseconds")

    def testUnhumanizeDelay(self):
        self.assertEqual(unhumanize_delay("100 milliseconds"), 0.1)
        self.assertEqual(unhumanize_delay("10 milliseconds"), 0.01)
        self.assertEqual(unhumanize_delay("1 millisecond"), 0.001)
        self.assertEqual(unhumanize_delay("2 milliseconds"), 0.002)
        self.assertEqual(unhumanize_delay("200 microseconds"), 0.0002)
        self.assertEqual(unhumanize_delay("1 second"), 1)
        self.assertEqual(unhumanize_delay("1.5 seconds"), 1.5)
        self.assertEqual(unhumanize_delay("0.1"), 0.1)

    def test_serunser(self):
        t = Topology()
        h1 = t.addHost()
        h2 = t.addHost()
        s1 = t.addSwitch()
        t.addLink(h1, s1, 10000000, 0.05)
        t.addLink(h2, s1, 10000000, 0.05)

        x = t.serialize()
        tprime = Topology.unserialize(x)
        y = t.serialize()

        self.assertListEqual(sorted(t.nodes.keys()), sorted(tprime.nodes.keys()))
        self.assertListEqual([str(v) for v in t.nodes.values()], [str(v) for v in tprime.nodes.values()])
        self.assertDictEqual(t.links, tprime.links)


if __name__ == '__main__':
    unittest.main()