from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.node import RemoteController
from mininet.link import TCLink


def chooseRequirement():
    print("Choose the plan you want to avail:")
    print("1 - High data requirement, Standard reliable channel, Low latency, Few number of devices needed to be connected")
    print("2 - Average data requirement, Extremely high reliable channel, Very low latency, Few number of devices needed to be connected")
    print("3 - Small data requirement, Standard reliable channel, Can tolerate latency, Many devices needed to be connected")
    print("Enter the corrresponding number of the plan required")
    plan = int(input())
    if (plan == 1):
        print("Your requirement is enhanced Mobile Broadband")
        return 1
    elif (plan == 2):
        print("Your requirement is Ultra-Reliable and Low Latency Communications")
        return 2
    elif (plan == 3):
        print("Your requirement is Massive Machine Type Communications")
        return 3
    else:
        print("Invalid plan chosen")
        return 0


def planRequirements():
    plan = chooseRequirement()
    if (plan == 1):
        print("Enter the bandwidth required between 100Mbps to 500Mbps:")
        bw = int(input())
        print("Enter latency requirement between 10-20ms:")
        latency = int(input())
        print("Enter number of devices you want to connect between 1 to 5:")
        devices = int(input())

    if (plan == 2):
        print("Enter the bandwidth required between 10Mbps to 50Mbps:")
        bw = int(input())
        print("Enter latency requirement between 0.5ms to 1ms:")
        latency = int(input())
        print("Enter number of devices you want to connect between 5 to 10:")
        devices = int(input())

    if (plan == 3):
        print("Enter the bandwidth required between 0.1Mbps to 2Mbps:")
        bw = int(input())
        print("Enter latency requirement between 1ms to 30ms:")
        latency = int(input())
        print("Enter number of devices you want to connect between 10 to 20:")
        devices = int(input())

    return (bw, latency, devices, plan)



class CustomTopology(Topo):
    def build(self):
        # Separating the 3 networks
        embb_switch = self.addSwitch('s1', cls = OVSSwitch)
        mmtc_switch = self.addSwitch('s2', cls=OVSSwitch) 
        urlcc_switch = self.addSwitch('s3', cls=OVSSwitch)

        # Adding few hosts
        h1 = self.addHost('h1', ip='10.0.1.1/24')
        h2 = self.addHost('h2', ip='10.0.1.2/24')
        h3 = self.addHost('h3', ip='10.0.2.1/24')
        h4 = self.addHost('h4', ip='10.0.2.2/24')
        h5 = self.addHost('h5', ip='10.0.3.1/24')
        h6 = self.addHost('h6', ip='10.0.3.2/24')

        self.addLink(embb_switch, h1, bw=150, delay=15)
        self.addLink(embb_switch, h2, bw=150, delay=15)
        self.addLink(urlcc_switch, h3, bw=10, delay=0.5)
        self.addLink(urlcc_switch, h4, bw=10, delay=0.5)
        self.addLink(mmtc_switch, h5, bw=1, delay=25)
        self.addLink(mmtc_switch, h6, bw=1, delay=25)

        self.addLink(embb_switch, urlcc_switch)
        self.addLink(urlcc_switch, mmtc_switch)

        n_devices = 6

        bw_h, latency, devices, plan = planRequirements()
        if (plan == 1):
            for i in range(devices):
                host = "h" + str(n_devices+i+1)
                ipHost = "10.0.1." + str(n_devices+i+1) + "/24"
                host = self.addHost(host, ip=ipHost)
                self.addLink(embb_switch, host, bw=bw_h, delay=latency)

        if (plan == 2):
            for i in range(devices):
                host = "h" + str(n_devices+i+1)
                ipHost = "10.0.2" + str(n_devices+i+1) + "/24"
                host = self.addHost(host, ip=ipHost)
                self.addLink(urlcc_switch, host, bw=bw_h, delay=latency)  

        if (plan == 3):
            for i in range(devices):
                host = "h" + str(n_devices+i+1)
                ipHost = "10.0.3." + str(n_devices+i+1) + "/24"
                host = self.addHost(host, ip=ipHost)
                self.addLink(mmtc_switch, host, bw=bw_h, delay=latency)


def run():
    topo = CustomTopology()
    controller = RemoteController('c0', ip='127.0.0.1', port=6633)
    net = Mininet(topo=topo, controller=controller)
    net.start()
    embb_switch = net.get('s1')
    urlcc_switch = net.get('s2')
    mmtc_switch = net.get('s3')

    CLI(net)
    net.stop()


if __name__== '__main__':
    setLogLevel('info')
    run()
