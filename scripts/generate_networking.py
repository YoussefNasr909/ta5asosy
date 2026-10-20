# 70 High-Quality Computer Networking Practice Questions
networking_questions = [
    {
        "id": "net-gen-01",
        "topic": "Computer Networking",
        "subtopic": "OSI & TCP/IP Models",
        "question": "Which layer of the OSI model is responsible for syntax conversion, character code translation (e.g., ASCII to EBCDIC), and data encryption/compression?",
        "options": [
            {"id": "A", "text": "Session Layer (Layer 5)"},
            {"id": "B", "text": "Presentation Layer (Layer 6)"},
            {"id": "C", "text": "Application Layer (Layer 7)"},
            {"id": "D", "text": "Transport Layer (Layer 4)"}
        ],
        "correctAnswer": "B",
        "explanation": "The Presentation Layer (Layer 6) handles data representation, formatting, compression (e.g. JPEG, MP3), and encryption/decryption (e.g. SSL/TLS cryptographic formatting).",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-02",
        "topic": "Computer Networking",
        "subtopic": "OSI & TCP/IP Models",
        "question": "In the standard 4-layer TCP/IP reference model (RFC 1122), which layer corresponds to both the Data Link and Physical layers of the OSI model?",
        "options": [
            {"id": "A", "text": "Network Access (Link) Layer"},
            {"id": "B", "text": "Internet Layer"},
            {"id": "C", "text": "Transport Layer"},
            {"id": "D", "text": "Application Layer"}
        ],
        "correctAnswer": "A",
        "explanation": "The Network Access layer (also called Link or Network Interface layer) in the classic TCP/IP model encompasses physical transmission and framing, corresponding to OSI Layers 1 and 2.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-03",
        "topic": "Computer Networking",
        "subtopic": "IP Addressing & Subnetting",
        "question": "A network engineer is given the subnet 192.168.10.64/26. What is the broadcast address for this subnet?",
        "options": [
            {"id": "A", "text": "192.168.10.127"},
            {"id": "B", "text": "192.168.10.128"},
            {"id": "C", "text": "192.168.10.255"},
            {"id": "D", "text": "192.168.10.63"}
        ],
        "correctAnswer": "A",
        "explanation": "A /26 mask has a block size of 2^(32-26) = 64 addresses. For subnet 192.168.10.64, the address range is .64 to .127. The first (.64) is network ID, and the last (.127) is the broadcast address.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-04",
        "topic": "Computer Networking",
        "subtopic": "IP Addressing & Subnetting",
        "question": "How many usable host IP addresses are available in a /28 IPv4 subnet?",
        "options": [
            {"id": "A", "text": "16"},
            {"id": "B", "text": "14"},
            {"id": "C", "text": "30"},
            {"id": "D", "text": "6"}
        ],
        "correctAnswer": "B",
        "explanation": "In a /28 subnet, there are 32 - 28 = 4 host bits. Total addresses = 2^4 = 16. Subtracting 2 (one for the network address, one for the broadcast address) yields 14 usable host addresses.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-05",
        "topic": "Computer Networking",
        "subtopic": "IP Addressing & Subnetting",
        "question": "Which of the following IPv4 address ranges is designated as Private by RFC 1918?",
        "options": [
            {"id": "A", "text": "172.16.0.0 to 172.31.255.255"},
            {"id": "B", "text": "172.0.0.0 to 172.15.255.255"},
            {"id": "C", "text": "192.169.0.0 to 192.169.255.255"},
            {"id": "D", "text": "100.64.0.0 to 100.127.255.255"}
        ],
        "correctAnswer": "A",
        "explanation": "RFC 1918 defines three private ranges: 10.0.0.0/8, 172.16.0.0/12 (172.16.0.0 - 172.31.255.255), and 192.168.0.0/16. (100.64.0.0/10 is CGNAT, RFC 6598).",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-06",
        "topic": "Computer Networking",
        "subtopic": "Transport Layer Protocols",
        "question": "During the TCP 3-way handshake, what sequence of control flags is exchanged between Client and Server?",
        "options": [
            {"id": "A", "text": "SYN -> SYN-ACK -> ACK"},
            {"id": "B", "text": "ACK -> SYN-ACK -> SYN"},
            {"id": "C", "text": "SYN -> ACK -> DATA"},
            {"id": "D", "text": "SYN -> ACK-FIN -> ACK"}
        ],
        "correctAnswer": "A",
        "explanation": "TCP connection establishment begins with the client sending a SYN packet, the server responding with SYN-ACK, and the client acknowledging with ACK.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-07",
        "topic": "Computer Networking",
        "subtopic": "Transport Layer Protocols",
        "question": "Which TCP mechanism prevents a fast sender from overwhelming a slow receiver's buffer?",
        "options": [
            {"id": "A", "text": "Flow Control (Sliding Window)"},
            {"id": "B", "text": "Congestion Window (cwnd)"},
            {"id": "C", "text": "Three-way Handshake"},
            {"id": "D", "text": "Checksum Verification"}
        ],
        "correctAnswer": "A",
        "explanation": "Flow Control uses the Receive Window (rwnd) advertised in TCP headers to limit sender transmissions based on the receiver's available buffer capacity.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-08",
        "topic": "Computer Networking",
        "subtopic": "Transport Layer Protocols",
        "question": "What happens when a TCP sender receives three duplicate ACKs (4 identical ACKs total) for the same packet?",
        "options": [
            {"id": "A", "text": "It triggers Fast Retransmit without waiting for the retransmission timer to expire"},
            {"id": "B", "text": "It terminates the TCP connection with a RST flag"},
            {"id": "C", "text": "It doubles the Advertised Window size"},
            {"id": "D", "text": "It sends an ICMP Source Quench"}
        ],
        "correctAnswer": "A",
        "explanation": "Three duplicate ACKs indicate an out-of-order segment and strongly imply packet loss. Fast Retransmit immediately resends the missing segment prior to RTO expiration.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-09",
        "topic": "Computer Networking",
        "subtopic": "Application Layer Protocols",
        "question": "What are the four chronological steps of the DHCP IP allocation handshake?",
        "options": [
            {"id": "A", "text": "Discover -> Offer -> Request -> Acknowledge (DORA)"},
            {"id": "B", "text": "Demand -> Order -> Receive -> Accept"},
            {"id": "C", "text": "Discover -> Request -> Offer -> Acknowledge"},
            {"id": "D", "text": "Detect -> Open -> Reserve -> Attach"}
        ],
        "correctAnswer": "A",
        "explanation": "DHCP configuration follows the DORA sequence: DHCPDISCOVER (client broadcast), DHCPOFFER (server unicast/broadcast), DHCPREQUEST (client selection), and DHCPACK (server confirmation).",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-10",
        "topic": "Computer Networking",
        "subtopic": "Application Layer Protocols",
        "question": "Which DNS record type maps an IPv6 address to a domain name?",
        "options": [
            {"id": "A", "text": "A Record"},
            {"id": "B", "text": "AAAA Record"},
            {"id": "C", "text": "CNAME Record"},
            {"id": "D", "text": "PTR Record"}
        ],
        "correctAnswer": "B",
        "explanation": "AAAA (quad-A) records map hostnames to 128-bit IPv6 addresses, whereas standard 'A' records map to 32-bit IPv4 addresses.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-11",
        "topic": "Computer Networking",
        "subtopic": "Application Layer Protocols",
        "question": "What is the primary role of a DNS CNAME record?",
        "options": [
            {"id": "A", "text": "To create an alias pointing one domain name to another canonical domain name"},
            {"id": "B", "text": "To specify the authoritative mail exchange server"},
            {"id": "C", "text": "To delegate authority for a DNS subzone"},
            {"id": "D", "text": "To reverse lookup an IP into a hostname"}
        ],
        "correctAnswer": "A",
        "explanation": "A Canonical Name (CNAME) record creates an alias for another domain name (e.g. www.example.com pointing to example.com), rather than resolving directly to an IP.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-12",
        "topic": "Computer Networking",
        "subtopic": "Ports & Protocols",
        "question": "What default port numbers are utilized by the NTP (Network Time Protocol) and SNMP (Simple Network Management Protocol)?",
        "options": [
            {"id": "A", "text": "NTP: UDP 123, SNMP: UDP 161"},
            {"id": "B", "text": "NTP: TCP 123, SNMP: TCP 161"},
            {"id": "C", "text": "NTP: UDP 53, SNMP: UDP 69"},
            {"id": "D", "text": "NTP: TCP 88, SNMP: UDP 389"}
        ],
        "correctAnswer": "A",
        "explanation": "NTP operates over UDP port 123 for clock synchronization, while SNMP agents listen on UDP port 161 for query requests (and port 162 for traps).",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-13",
        "topic": "Computer Networking",
        "subtopic": "Ports & Protocols",
        "question": "Which port does Microsoft Remote Desktop Protocol (RDP) listen on by default?",
        "options": [
            {"id": "A", "text": "3389"},
            {"id": "B", "text": "5900"},
            {"id": "C", "text": "445"},
            {"id": "D", "text": "1433"}
        ],
        "correctAnswer": "A",
        "explanation": "RDP uses TCP (and UDP) port 3389. Port 5900 is typically VNC, 445 is SMB, and 1433 is Microsoft SQL Server.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-14",
        "topic": "Computer Networking",
        "subtopic": "Data Link Layer & Switching",
        "question": "How does an Ethernet switch populate its MAC address table (CAM table)?",
        "options": [
            {"id": "A", "text": "By inspecting the source MAC address of incoming frames on each physical port"},
            {"id": "B", "text": "By sending ARP broadcasts to all connected hosts upon boot"},
            {"id": "C", "text": "By querying the default gateway router"},
            {"id": "D", "text": "By reading destination MAC addresses in received headers"}
        ],
        "correctAnswer": "A",
        "explanation": "Switches perform dynamic MAC learning by recording the source MAC address and ingress port of every frame received.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-15",
        "topic": "Computer Networking",
        "subtopic": "Data Link Layer & Switching",
        "question": "What IEEE standard defines VLAN tagging on Ethernet frames, adding a 4-byte header containing a 12-bit VLAN ID?",
        "options": [
            {"id": "A", "text": "IEEE 802.1Q"},
            {"id": "B", "text": "IEEE 802.1D"},
            {"id": "C", "text": "IEEE 802.3u"},
            {"id": "D", "text": "IEEE 802.11ac"}
        ],
        "correctAnswer": "A",
        "explanation": "IEEE 802.1Q is the industry standard for VLAN trunking, inserting a 4-byte tag into Ethernet frames to differentiate up to 4094 distinct VLANs.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-16",
        "topic": "Computer Networking",
        "subtopic": "Data Link Layer & Switching",
        "question": "What is the primary objective of Spanning Tree Protocol (STP, IEEE 802.1D)?",
        "options": [
            {"id": "A", "text": "To prevent Layer 2 switching loops and broadcast storms in redundant topologies"},
            {"id": "B", "text": "To route packets dynamically across autonomous systems"},
            {"id": "C", "text": "To encrypt traffic between branch offices"},
            {"id": "D", "text": "To aggregate multiple physical links into one logical link"}
        ],
        "correctAnswer": "A",
        "explanation": "STP prevents Layer 2 switching loops and broadcast storms by selectively placing redundant switch ports into a blocking state while maintaining path failover.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-17",
        "topic": "Computer Networking",
        "subtopic": "Routing & Protocols",
        "question": "Which of the following routing protocols is classified as an exterior gateway protocol (EGP) and forms the backbone of global Internet routing?",
        "options": [
            {"id": "A", "text": "BGP (Border Gateway Protocol)"},
            {"id": "B", "text": "OSPF (Open Shortest Path First)"},
            {"id": "C", "text": "RIPv2 (Routing Information Protocol)"},
            {"id": "D", "text": "IS-IS (Intermediate System to Intermediate System)"}
        ],
        "correctAnswer": "A",
        "explanation": "BGP (Border Gateway Protocol) is the de facto Path-Vector Exterior Gateway Protocol used to exchange routing and reachability information between Autonomous Systems (AS) on the Internet.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-18",
        "topic": "Computer Networking",
        "subtopic": "Routing & Protocols",
        "question": "What algorithm does OSPF (Open Shortest Path First) use to compute the shortest loop-free path to all destinations?",
        "options": [
            {"id": "A", "text": "Dijkstra's Shortest Path First (SPF) algorithm"},
            {"id": "B", "text": "Bellman-Ford algorithm"},
            {"id": "C", "text": "Diffie-Hellman algorithm"},
            {"id": "D", "text": "Kruskal's Minimum Spanning Tree"}
        ],
        "correctAnswer": "A",
        "explanation": "OSPF is a link-state routing protocol that maintains a topology database and executes Dijkstra's SPF algorithm to calculate cost-effective loop-free routes.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-19",
        "topic": "Computer Networking",
        "subtopic": "Routing & Protocols",
        "question": "What is the maximum hop count allowed by RIP (Routing Information Protocol) before a route is considered unreachable?",
        "options": [
            {"id": "A", "text": "15 hops (16 is infinity)"},
            {"id": "B", "text": "255 hops"},
            {"id": "C", "text": "100 hops"},
            {"id": "D", "text": "32 hops"}
        ],
        "correctAnswer": "A",
        "explanation": "RIP uses hop count as its sole metric with a maximum limit of 15 hops; a hop count of 16 indicates an unreachable network (infinity) to mitigate count-to-infinity routing loops.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-20",
        "topic": "Computer Networking",
        "subtopic": "IP Addressing & Subnetting",
        "question": "In IPv4 packet headers, what field prevents packets from circulating indefinitely in a routing loop?",
        "options": [
            {"id": "A", "text": "Time to Live (TTL)"},
            {"id": "B", "text": "Total Length"},
            {"id": "C", "text": "Header Checksum"},
            {"id": "D", "text": "Differentiated Services (DiffServ)"}
        ],
        "correctAnswer": "A",
        "explanation": "The 8-bit TTL field is decremented by 1 at every router hop. When TTL reaches 0, the packet is discarded and an ICMP Time Exceeded message is returned.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-21",
        "topic": "Computer Networking",
        "subtopic": "IP Addressing & Subnetting",
        "question": "What is the IPv6 equivalent of IPv4's Time to Live (TTL) field?",
        "options": [
            {"id": "A", "text": "Hop Limit"},
            {"id": "B", "text": "Traffic Class"},
            {"id": "C", "text": "Flow Label"},
            {"id": "D", "text": "Next Header"}
        ],
        "correctAnswer": "A",
        "explanation": "In IPv6 headers, the TTL field was renamed to Hop Limit to accurately describe its function: decrementing by 1 per forwarding hop.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-22",
        "topic": "Computer Networking",
        "subtopic": "IP Addressing & Subnetting",
        "question": "Which prefix identifies an IPv6 Link-Local address automatically configured on every active interface?",
        "options": [
            {"id": "A", "text": "fe80::/10"},
            {"id": "B", "text": "fc00::/7"},
            {"id": "C", "text": "2001::/16"},
            {"id": "D", "text": "ff02::/16"}
        ],
        "correctAnswer": "A",
        "explanation": "Link-Local addresses begin with fe80::/10 (fe80 to febf) and are non-routable addresses used exclusively for communication on the local physical link.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-23",
        "topic": "Computer Networking",
        "subtopic": "IP Addressing & Subnetting",
        "question": "How does IPv6 replace IPv4's broadcast mechanism for address resolution and discovery?",
        "options": [
            {"id": "A", "text": "By using Multicast groups with ICMPv6 Neighbor Discovery Protocol (NDP)"},
            {"id": "B", "text": "By using Anycast ARP frames"},
            {"id": "C", "text": "By sending unicast queries directly to root DNS"},
            {"id": "D", "text": "By flooding all ports on the default VLAN"}
        ],
        "correctAnswer": "A",
        "explanation": "IPv6 eliminates broadcast addressing entirely, utilizing Solicited-Node Multicast addresses and ICMPv6 Neighbor Discovery Protocol (NDP) for MAC resolution.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-24",
        "topic": "Computer Networking",
        "subtopic": "Routing & NAT",
        "question": "What type of NAT specifically maps multiple internal private IP addresses to a single public IP address using distinct layer 4 port numbers?",
        "options": [
            {"id": "A", "text": "PAT (Port Address Translation / NAT Overload)"},
            {"id": "B", "text": "Static NAT (1:1)"},
            {"id": "C", "text": "Dynamic NAT Pool"},
            {"id": "D", "text": "Carrier-Grade IPv6 NAT"}
        ],
        "correctAnswer": "A",
        "explanation": "Port Address Translation (PAT, also called NAT Overload) maps thousands of private sockets to one public IP address by tracking source port numbers.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-25",
        "topic": "Computer Networking",
        "subtopic": "Network Troubleshooting & Utilities",
        "question": "How does the `traceroute` (or `tracert`) command determine the path and intermediate routers between source and destination?",
        "options": [
            {"id": "A", "text": "By sending packets with sequentially incrementing TTL values starting at 1"},
            {"id": "B", "text": "By querying the central BGP route server for AS paths"},
            {"id": "C", "text": "By inspecting OSPF link-state advertisements along the path"},
            {"id": "D", "text": "By executing ARP requests at every intermediate hop"}
        ],
        "correctAnswer": "A",
        "explanation": "Traceroute sends packets starting with TTL=1. Each successive router drops the packet when TTL expires, returning an ICMP Time Exceeded message that reveals that hop's IP.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-26",
        "topic": "Computer Networking",
        "subtopic": "Network Security & Protocols",
        "question": "What is the primary difference between a Stateless Firewall and a Stateful Inspection Firewall?",
        "options": [
            {"id": "A", "text": "A stateful firewall tracks the state of active network connections in a state table, whereas a stateless firewall evaluates each packet in isolation against static ACL rules"},
            {"id": "B", "text": "Stateless firewalls operate at Layer 7, while stateful firewalls only operate at Layer 2"},
            {"id": "C", "text": "Stateful firewalls cannot inspect TCP flags"},
            {"id": "D", "text": "Stateless firewalls decrypt HTTPS payloads"}
        ],
        "correctAnswer": "A",
        "explanation": "Stateful firewalls maintain a dynamic connection state table (tracking TCP sequence numbers, SYN/ACK handshake states, and UDP flows), permitting return packets automatically.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-27",
        "topic": "Computer Networking",
        "subtopic": "Network Security & Protocols",
        "question": "In an ARP Spoofing (ARP Poisoning) attack, what malicious action does the attacker execute?",
        "options": [
            {"id": "A", "text": "Sends gratuitous or unsolicited ARP replies linking the attacker's MAC address with a legitimate IP address (e.g. Default Gateway)"},
            {"id": "B", "text": "Sends SYN packets with spoofed source IPs to consume server memory"},
            {"id": "C", "text": "Injects false DNS records into a recursive resolver's cache"},
            {"id": "D", "text": "Floods a switch with random MACs to fill the CAM table"}
        ],
        "correctAnswer": "A",
        "explanation": "ARP Spoofing exploits the trust of ARP by broadcasting forged ARP replies that associate the attacker's MAC address with a target host's IP (often the gateway), enabling Man-in-the-Middle eavesdropping.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-28",
        "topic": "Computer Networking",
        "subtopic": "Network Security & Protocols",
        "question": "What is the difference between an IDS (Intrusion Detection System) and an IPS (Intrusion Prevention System)?",
        "options": [
            {"id": "A", "text": "An IDS is passive (out-of-band) and alerts on suspicious traffic, while an IPS is active (in-line) and drops malicious packets in real time"},
            {"id": "B", "text": "An IDS inspects encrypted traffic, while an IPS can only inspect plaintext"},
            {"id": "C", "text": "An IPS only runs on client workstations, while an IDS runs on routers"},
            {"id": "D", "text": "An IDS alters routing tables, while an IPS simply logs events"}
        ],
        "correctAnswer": "A",
        "explanation": "IDS detects threats via tapped network traffic and sends alerts without interrupting traffic flow, whereas IPS sits inline with the data path and actively drops malicious packets.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-29",
        "topic": "Computer Networking",
        "subtopic": "Transport Layer Protocols",
        "question": "What is the standard Maximum Transmission Unit (MTU) size for standard Ethernet frames?",
        "options": [
            {"id": "A", "text": "1500 bytes"},
            {"id": "B", "text": "9000 bytes"},
            {"id": "C", "text": "64 bytes"},
            {"id": "D", "text": "576 bytes"}
        ],
        "correctAnswer": "A",
        "explanation": "Standard Ethernet has an MTU of 1500 bytes (payload size excluding the 14-byte Ethernet header and 4-byte CRC). Frames larger than 1500 bytes are known as Jumbo Frames (up to 9000 bytes).",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-30",
        "topic": "Computer Networking",
        "subtopic": "Transport Layer Protocols",
        "question": "If an IP packet's 'Don't Fragment' (DF) flag is set to 1 and the packet exceeds the outgoing link's MTU, what action does the router take?",
        "options": [
            {"id": "A", "text": "Discards the packet and sends back an ICMP 'Fragmentation Needed and DF set' message"},
            {"id": "B", "text": "Fragments the packet regardless of the flag"},
            {"id": "C", "text": "Compresses the packet payload and forwards it"},
            {"id": "D", "text": "Stores the packet in buffer until the link expands"}
        ],
        "correctAnswer": "A",
        "explanation": "If DF=1, the router cannot fragment the packet; it drops the packet and responds with an ICMP Type 3, Code 4 message, enabling Path MTU Discovery (PMTUD).",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-31",
        "topic": "Computer Networking",
        "subtopic": "Application Layer Protocols",
        "question": "In HTTP/1.1 vs HTTP/2, what major performance improvement did HTTP/2 introduce to solve head-of-line blocking at the application layer?",
        "options": [
            {"id": "A", "text": "Binary framing and multiplexing of multiple requests/responses over a single TCP connection"},
            {"id": "B", "text": "Replacing TCP with raw UDP datagrams without flow control"},
            {"id": "C", "text": "Requiring plain text uncompressed ASCII headers"},
            {"id": "D", "text": "Opening 6 parallel TCP connections per host by default"}
        ],
        "correctAnswer": "A",
        "explanation": "HTTP/2 uses a binary framing layer that breaks transactions into independent frames, multiplexing concurrent streams over a single TCP connection without application-layer head-of-line blocking.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-32",
        "topic": "Computer Networking",
        "subtopic": "Application Layer Protocols",
        "question": "HTTP/3 differs fundamentally from HTTP/1.1 and HTTP/2 because it operates on top of which transport protocol?",
        "options": [
            {"id": "A", "text": "QUIC (built on top of UDP)"},
            {"id": "B", "text": "SCTP (Stream Control Transmission Protocol)"},
            {"id": "C", "text": "Enhanced TCP with MPTCP extensions"},
            {"id": "D", "text": "Raw IP sockets"}
        ],
        "correctAnswer": "A",
        "explanation": "HTTP/3 runs over QUIC, a transport protocol built on UDP that incorporates built-in TLS 1.3, independent multiplexed streams, and 0-RTT connection resumption.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-33",
        "topic": "Computer Networking",
        "subtopic": "Ports & Protocols",
        "question": "What is the standard TCP port for secure LDAP (LDAPS) directory services?",
        "options": [
            {"id": "A", "text": "636"},
            {"id": "B", "text": "389"},
            {"id": "C", "text": "88"},
            {"id": "D", "text": "53"}
        ],
        "correctAnswer": "A",
        "explanation": "Plain LDAP uses TCP port 389, while LDAPS (LDAP over SSL/TLS) uses TCP port 636.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-34",
        "topic": "Computer Networking",
        "subtopic": "Ports & Protocols",
        "question": "Which port does Kerberos authentication utilize for Key Distribution Center (KDC) authentication services?",
        "options": [
            {"id": "A", "text": "Port 88"},
            {"id": "B", "text": "Port 53"},
            {"id": "C", "text": "Port 110"},
            {"id": "D", "text": "Port 179"}
        ],
        "correctAnswer": "A",
        "explanation": "Kerberos utilizes port 88 (both UDP and TCP) for ticket granting service (TGS) requests and authentications.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-35",
        "topic": "Computer Networking",
        "subtopic": "Transmission Media",
        "question": "What is the maximum rated segment distance for standard twisted-pair Ethernet cables (Cat5e, Cat6) using 1000BASE-T without repeaters?",
        "options": [
            {"id": "A", "text": "100 meters (approx. 328 feet)"},
            {"id": "B", "text": "500 meters"},
            {"id": "C", "text": "50 meters"},
            {"id": "D", "text": "1000 meters"}
        ],
        "correctAnswer": "A",
        "explanation": "The TIA/EIA standard specifies a maximum cable channel run of 100 meters (90 meters solid horizontal cable plus 10 meters of stranded patch cables).",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-36",
        "topic": "Computer Networking",
        "subtopic": "Transmission Media",
        "question": "Which optical fiber type features a narrow core (approx 9 micrometers) and allows light to travel along a single direct path, minimizing modal dispersion over long distances?",
        "options": [
            {"id": "A", "text": "Single-Mode Fiber (SMF)"},
            {"id": "B", "text": "Multi-Mode Fiber (MMF)"},
            {"id": "C", "text": "Shielded Twisted Pair (STP)"},
            {"id": "D", "text": "RG-6 Coaxial Cable"}
        ],
        "correctAnswer": "A",
        "explanation": "Single-Mode Fiber (SMF) has a very small core (~9 µm) that supports only one propagation mode, making it ideal for high-speed, long-distance telecommunication (up to tens of kilometers).",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-37",
        "topic": "Computer Networking",
        "subtopic": "Network Troubleshooting & Utilities",
        "question": "Which command-line utility displays active TCP connections, listening ports, ethernet statistics, and the IP routing table on Windows and Linux?",
        "options": [
            {"id": "A", "text": "netstat"},
            {"id": "B", "text": "nslookup"},
            {"id": "C", "text": "tracert"},
            {"id": "D", "text": "arp"}
        ],
        "correctAnswer": "A",
        "explanation": "`netstat` (network statistics) is the standard utility to view network connections, routing tables, interface statistics, and listening sockets.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-38",
        "topic": "Computer Networking",
        "subtopic": "Network Troubleshooting & Utilities",
        "question": "What is the primary purpose of the `tcpdump` command in Unix/Linux environments?",
        "options": [
            {"id": "A", "text": "Capturing and analyzing raw packet traffic traversing network interfaces"},
            {"id": "B", "text": "Resetting the host's TCP stack and socket buffers"},
            {"id": "C", "text": "Configuring static IP addresses on network cards"},
            {"id": "D", "text": "Testing DNS query speed against public resolvers"}
        ],
        "correctAnswer": "A",
        "explanation": "`tcpdump` is a command-line packet analyzer using libpcap to capture, filter, and inspect network traffic in real time.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-39",
        "topic": "Computer Networking",
        "subtopic": "IP Addressing & Subnetting",
        "question": "Given the IP address 10.200.15.70 with subnet mask 255.255.255.192, what is the network address?",
        "options": [
            {"id": "A", "text": "10.200.15.64"},
            {"id": "B", "text": "10.200.15.0"},
            {"id": "C", "text": "10.200.15.32"},
            {"id": "D", "text": "10.200.15.128"}
        ],
        "correctAnswer": "A",
        "explanation": "255.255.255.192 is /26 (block size 64). Subnets are .0, .64, .128, .192. Host .70 falls between .64 and .127, so the network address is 10.200.15.64.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-40",
        "topic": "Computer Networking",
        "subtopic": "Data Link Layer & Switching",
        "question": "What is a broadcast domain, and which networking device delimits (breaks up) broadcast domains by default?",
        "options": [
            {"id": "A", "text": "A network boundary where broadcast frames are forwarded; routers delimit broadcast domains"},
            {"id": "B", "text": "A physical collision zone; unmanaged switches delimit broadcast domains"},
            {"id": "C", "text": "A group of devices sharing one IP address; hubs delimit broadcast domains"},
            {"id": "D", "text": "A single wireless channel; repeaters delimit broadcast domains"}
        ],
        "correctAnswer": "A",
        "explanation": "A broadcast domain includes all nodes reachable by a Layer 2 broadcast. Routers (and Layer 3 switches) do not forward Layer 2 broadcasts, thereby separating broadcast domains.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-41",
        "topic": "Computer Networking",
        "subtopic": "Data Link Layer & Switching",
        "question": "In Ethernet carrier sensing, what collision resolution mechanism is employed in CSMA/CD when a collision is detected on a shared coaxial medium?",
        "options": [
            {"id": "A", "text": "Nodes send a Jam signal and execute a randomized Truncated Binary Exponential Backoff algorithm"},
            {"id": "B", "text": "Nodes immediately retransmit with doubled signal power"},
            {"id": "C", "text": "Nodes drop the connection and request a token from the master node"},
            {"id": "D", "text": "The switch disconnects the offending physical port"}
        ],
        "correctAnswer": "A",
        "explanation": "When CSMA/CD detects a collision, transmitting nodes broadcast a jam signal to ensure all nodes detect it, then calculate a random backoff time using truncated binary exponential backoff.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-42",
        "topic": "Computer Networking",
        "subtopic": "Transport Layer Protocols",
        "question": "What is the primary function of the TCP Window Scale option (RFC 1323)?",
        "options": [
            {"id": "A", "text": "To expand the 16-bit receive window field up to 30 bits, enabling high-bandwidth latency-rich links"},
            {"id": "B", "text": "To increase maximum segment size (MSS) to 65535 bytes"},
            {"id": "C", "text": "To encrypt TCP payloads with TLS keys"},
            {"id": "D", "text": "To calculate round trip time without timestamps"}
        ],
        "correctAnswer": "A",
        "explanation": "The standard TCP window header is 16 bits (max 65,535 bytes). Window Scale introduces a scale factor, allowing receive buffers up to 1 Gigabyte on high-bandwidth-delay product networks.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-43",
        "topic": "Computer Networking",
        "subtopic": "Network Security & Protocols",
        "question": "In TLS 1.3, how many round trips (RTT) are required for a standard full handshake between client and server before application data can be sent?",
        "options": [
            {"id": "A", "text": "1-RTT (and 0-RTT for resumed connections)"},
            {"id": "B", "text": "2-RTT"},
            {"id": "C", "text": "3-RTT"},
            {"id": "D", "text": "0-RTT for all connections"}
        ],
        "correctAnswer": "A",
        "explanation": "TLS 1.3 optimized the handshake by combining key exchange and cipher negotiation into the ClientHello/ServerHello exchange, reducing latency to 1-RTT (or 0-RTT on resumption).",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-44",
        "topic": "Computer Networking",
        "subtopic": "Network Security & Protocols",
        "question": "Which IPsec protocol provides data confidentiality (encryption) as well as data integrity and authentication for IP packets?",
        "options": [
            {"id": "A", "text": "ESP (Encapsulating Security Payload)"},
            {"id": "B", "text": "AH (Authentication Header)"},
            {"id": "C", "text": "IKE (Internet Key Exchange)"},
            {"id": "D", "text": "Diffie-Hellman"}
        ],
        "correctAnswer": "A",
        "explanation": "ESP (IP protocol 50) provides confidentiality through encryption, plus integrity and origin authentication. AH (protocol 51) provides integrity and authentication but does NOT encrypt data.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-45",
        "topic": "Computer Networking",
        "subtopic": "Routing & Protocols",
        "question": "What is an Autonomous System (AS) in Internet routing terminology?",
        "options": [
            {"id": "A", "text": "A connected group of IP networks and routers under the administrative control of a single entity with a common routing policy"},
            {"id": "B", "text": "A router that updates its firmware automatically without human intervention"},
            {"id": "C", "text": "A local broadcast domain bounded by a firewall"},
            {"id": "D", "text": "A server rack running automated high-availability clustering"}
        ],
        "correctAnswer": "A",
        "explanation": "An Autonomous System (AS) is an identified collection of IP networks managed by a single organization (ISP, enterprise, university) that presents a unified routing policy via BGP.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-46",
        "topic": "Computer Networking",
        "subtopic": "Routing & Protocols",
        "question": "What metric does the Administrative Distance (AD) value represent in Cisco and general multi-protocol routing engines?",
        "options": [
            {"id": "A", "text": "The trustworthiness and priority of the routing information source (lower AD is preferred)"},
            {"id": "B", "text": "The total physical cable distance in kilometers between routers"},
            {"id": "C", "text": "The packet propagation delay across the interface"},
            {"id": "D", "text": "The total number of BGP autonomous systems traversed"}
        ],
        "correctAnswer": "A",
        "explanation": "Administrative Distance is an integer ranking route believability when multiple protocols advertise the same destination. Connected = 0, Static = 1, OSPF = 110, RIP = 120 (lower is preferred).",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-47",
        "topic": "Computer Networking",
        "subtopic": "Network Devices",
        "question": "At which layer of the OSI model does a traditional unmanaged Layer 2 Ethernet switch make its forwarding decisions?",
        "options": [
            {"id": "A", "text": "Data Link Layer (Layer 2)"},
            {"id": "B", "text": "Network Layer (Layer 3)"},
            {"id": "C", "text": "Physical Layer (Layer 1)"},
            {"id": "D", "text": "Transport Layer (Layer 4)"}
        ],
        "correctAnswer": "A",
        "explanation": "Layer 2 switches parse destination MAC addresses encapsulated within the Ethernet frame header at the Data Link layer.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-48",
        "topic": "Computer Networking",
        "subtopic": "Network Devices",
        "question": "What is the primary difference between a Layer 2 Switch and a Layer 3 Switch (Multilayer Switch)?",
        "options": [
            {"id": "A", "text": "A Layer 3 switch has hardware ASIC routing capabilities allowing it to forward packets across IP subnets and VLANs at wire speed"},
            {"id": "B", "text": "A Layer 2 switch can route between VLANs while Layer 3 cannot"},
            {"id": "C", "text": "Layer 3 switches do not support MAC address tables"},
            {"id": "D", "text": "Layer 3 switches only operate on wireless Wi-Fi signals"}
        ],
        "correctAnswer": "A",
        "explanation": "A Layer 3 switch combines high-speed switching with hardware-accelerated IP packet routing, enabling fast inter-VLAN routing without bottle-necking an external router.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-49",
        "topic": "Computer Networking",
        "subtopic": "Network Topologies",
        "question": "If a network has 8 computers connected in a Full Mesh topology, how many physical point-to-point links are required?",
        "options": [
            {"id": "A", "text": "28 links"},
            {"id": "B", "text": "56 links"},
            {"id": "C", "text": "16 links"},
            {"id": "D", "text": "8 links"}
        ],
        "correctAnswer": "A",
        "explanation": "The formula for full mesh links is n * (n - 1) / 2. For 8 computers: 8 * 7 / 2 = 28 links.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-50",
        "topic": "Computer Networking",
        "subtopic": "Network Topologies",
        "question": "What happens in a Bus topology if the terminating resistor at either end of the shared coaxial cable is damaged or disconnected?",
        "options": [
            {"id": "A", "text": "Electrical signals reflect back across the bus (signal reflection), causing collisions and bringing down network communications"},
            {"id": "B", "text": "The network automatically transitions into a Star topology"},
            {"id": "C", "text": "Traffic speed drops by exactly 50% without dropping packets"},
            {"id": "D", "text": "Only the computer nearest the break is disconnected"}
        ],
        "correctAnswer": "A",
        "explanation": "Terminators absorb the electrical signal energy at the wire endpoints. Without proper termination, signal reflection bounces back along the line, creating collisions that cripple the bus.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-51",
        "topic": "Computer Networking",
        "subtopic": "Application Layer Protocols",
        "question": "What is the difference between POP3 and IMAP email retrieval protocols?",
        "options": [
            {"id": "A", "text": "POP3 downloads emails and usually deletes them from the server, while IMAP synchronizes folders and maintains emails on the mail server"},
            {"id": "B", "text": "POP3 encrypts emails while IMAP sends them in plaintext"},
            {"id": "C", "text": "POP3 is for sending outgoing emails while IMAP is for receiving"},
            {"id": "D", "text": "IMAP can only be accessed by one client device simultaneously"}
        ],
        "correctAnswer": "A",
        "explanation": "POP3 (port 110/995) downloads messages locally, while IMAP (port 143/993) maintains mail state centrally on the server, syncing read/unread flags across multiple devices.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-52",
        "topic": "Computer Networking",
        "subtopic": "Application Layer Protocols",
        "question": "In FTP (File Transfer Protocol) Active Mode, which port does the client listen on for data connection initiated by the server?",
        "options": [
            {"id": "A", "text": "A random high unprivileged port (> 1023) sent via the PORT command"},
            {"id": "B", "text": "Port 21"},
            {"id": "C", "text": "Port 20"},
            {"id": "D", "text": "Port 80"}
        ],
        "correctAnswer": "A",
        "explanation": "In Active FTP, the control connection is established to port 21. The client tells the server via PORT command which high-order port to connect back to from server port 20.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-53",
        "topic": "Computer Networking",
        "subtopic": "Transport Layer Protocols",
        "question": "Which TCP control flag is used to abruptly terminate and reset a malformed, invalid, or unauthorized TCP connection?",
        "options": [
            {"id": "A", "text": "RST (Reset)"},
            {"id": "B", "text": "FIN (Finish)"},
            {"id": "C", "text": "URG (Urgent)"},
            {"id": "D", "text": "PSH (Push)"}
        ],
        "correctAnswer": "A",
        "explanation": "The RST (Reset) flag forcefully and immediately aborts a TCP connection without waiting for graceful four-way teardown handshakes.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-54",
        "topic": "Computer Networking",
        "subtopic": "Transport Layer Protocols",
        "question": "Why is UDP preferred over TCP for live video streaming, VoIP calls, and online gaming?",
        "options": [
            {"id": "A", "text": "UDP has minimal header overhead (8 bytes vs 20+ bytes) and does not incur latency delays from retransmission and acknowledgments"},
            {"id": "B", "text": "UDP guarantees packet delivery with lower CPU usage"},
            {"id": "C", "text": "UDP encrypts audio streams at the socket layer"},
            {"id": "D", "text": "UDP automatically adjusts link bandwidth"}
        ],
        "correctAnswer": "A",
        "explanation": "Real-time interactive media prioritizes low latency and timeliness over 100% reliability; retransmitted audio packets arriving 500ms late are useless and create jitter.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-55",
        "topic": "Computer Networking",
        "subtopic": "IP Addressing & Subnetting",
        "question": "What is the network address and default subnet mask for an IPv4 APIPA (Automatic Private IP Addressing) address?",
        "options": [
            {"id": "A", "text": "169.254.0.0/16 (255.255.0.0)"},
            {"id": "B", "text": "192.168.0.0/16"},
            {"id": "C", "text": "10.0.0.0/8"},
            {"id": "D", "text": "127.0.0.0/8"}
        ],
        "correctAnswer": "A",
        "explanation": "When a DHCP client fails to receive a lease, Windows and other OSs assign a link-local address in the range 169.254.0.1 - 169.254.255.254 (/16).",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-56",
        "topic": "Computer Networking",
        "subtopic": "IP Addressing & Subnetting",
        "question": "How many bits are borrowed from the host portion to create 6 subnets from a Class C network?",
        "options": [
            {"id": "A", "text": "3 bits"},
            {"id": "B", "text": "2 bits"},
            {"id": "C", "text": "4 bits"},
            {"id": "D", "text": "5 bits"}
        ],
        "correctAnswer": "A",
        "explanation": "To create at least 6 subnets, we need 2^n >= 6. For n=2, 2^2=4 (insufficient). For n=3, 2^3=8 (supports 6 subnets with 2 remaining).",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-57",
        "topic": "Computer Networking",
        "subtopic": "Data Link Layer & Switching",
        "question": "What is the purpose of Port Security on managed enterprise switches?",
        "options": [
            {"id": "A", "text": "Restricting ingress traffic on an interface by limiting and binding learned source MAC addresses"},
            {"id": "B", "text": "Blocking outgoing HTTP traffic on TCP port 80"},
            {"id": "C", "text": "Encrypting all payloads passing through physical RJ-45 jacks"},
            {"id": "D", "text": "Preventing unauthorized SSH logins to the switch CLI"}
        ],
        "correctAnswer": "A",
        "explanation": "Switch Port Security prevents unauthorized devices and MAC flooding attacks by limiting the number and identity of MAC addresses permitted on each physical access switch port.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-58",
        "topic": "Computer Networking",
        "subtopic": "Data Link Layer & Switching",
        "question": "What is a broadcast storm, and what commonly causes it in enterprise LANs?",
        "options": [
            {"id": "A", "text": "An endless loop of broadcast frames circling redundant Layer 2 links without STP, consuming all available bandwidth"},
            {"id": "B", "text": "A severe lightning strike damaging outdoor coaxial cables"},
            {"id": "C", "text": "A high volume of legitimate DNS queries during peak business hours"},
            {"id": "D", "text": "A router sending BGP updates to 100 peers simultaneously"}
        ],
        "correctAnswer": "A",
        "explanation": "Because Ethernet frames lack a TTL field, any Layer 2 loop will duplicate and circulate broadcast frames indefinitely, saturating switch backplanes and crashing the network.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-59",
        "topic": "Computer Networking",
        "subtopic": "Network Security & Protocols",
        "question": "Which protocol protects DNS integrity by cryptographically signing DNS records with public key cryptography?",
        "options": [
            {"id": "A", "text": "DNSSEC (DNS Security Extensions)"},
            {"id": "B", "text": "DoH (DNS over HTTPS)"},
            {"id": "C", "text": "DoT (DNS over TLS)"},
            {"id": "D", "text": "mDNS (Multicast DNS)"}
        ],
        "correctAnswer": "A",
        "explanation": "DNSSEC adds cryptographic signatures (RRSIG, DNSKEY, DS records) to authenticate the origin and verify the integrity of DNS records, preventing cache poisoning.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-60",
        "topic": "Computer Networking",
        "subtopic": "Network Security & Protocols",
        "question": "In a SYN Flood denial-of-service attack, what server resource is exhausted by the attacker?",
        "options": [
            {"id": "A", "text": "The TCP half-open connection backlog queue (SYN queue)"},
            {"id": "B", "text": "The router's ARP cache memory"},
            {"id": "C", "text": "The local hard drive partition space"},
            {"id": "D", "text": "The DNS root hints configuration file"}
        ],
        "correctAnswer": "A",
        "explanation": "SYN floods transmit countless SYN packets from spoofed addresses without completing the final ACK. The server allocates memory in its SYN queue for each half-open state until memory is exhausted.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-61",
        "topic": "Computer Networking",
        "subtopic": "OSI & TCP/IP Models",
        "question": "Which layer of the OSI model coordinates dialog control, token management, and synchronization checkpoints between applications?",
        "options": [
            {"id": "A", "text": "Session Layer (Layer 5)"},
            {"id": "B", "text": "Presentation Layer (Layer 6)"},
            {"id": "C", "text": "Transport Layer (Layer 4)"},
            {"id": "D", "text": "Application Layer (Layer 7)"}
        ],
        "correctAnswer": "A",
        "explanation": "The Session Layer establishes, manages, and terminates conversational sessions between endpoints, providing checkpoints to resume interrupted file transfers.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-62",
        "topic": "Computer Networking",
        "subtopic": "Ports & Protocols",
        "question": "What is the standard port used by Syslog for system logging messages?",
        "options": [
            {"id": "A", "text": "UDP 514"},
            {"id": "B", "text": "TCP 53"},
            {"id": "C", "text": "UDP 69"},
            {"id": "D", "text": "TCP 443"}
        ],
        "correctAnswer": "A",
        "explanation": "Syslog standard message logging traditionally operates over UDP port 514 (RFC 5424 also allows TLS over TCP port 6514).",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-63",
        "topic": "Computer Networking",
        "subtopic": "Ports & Protocols",
        "question": "What port and transport protocol is utilized by TFTP (Trivial File Transfer Protocol)?",
        "options": [
            {"id": "A", "text": "UDP port 69"},
            {"id": "B", "text": "TCP port 21"},
            {"id": "C", "text": "TCP port 69"},
            {"id": "D", "text": "UDP port 20"}
        ],
        "correctAnswer": "A",
        "explanation": "TFTP is a simple file transfer protocol running over UDP port 69, commonly used for bootstrap netbooting (PXE) and saving router firmware configs.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-64",
        "topic": "Computer Networking",
        "subtopic": "Transmission Media",
        "question": "Why are copper wire pairs in Category cables (Cat5, Cat6) twisted together at varying twist rates?",
        "options": [
            {"id": "A", "text": "To cancel out electromagnetic interference (EMI) and crosstalk from adjacent pairs via differential signaling"},
            {"id": "B", "text": "To make the physical cable more flexible and less prone to breaking"},
            {"id": "C", "text": "To slow down the velocity of propagation"},
            {"id": "D", "text": "To increase the electrical resistance of the wire"}
        ],
        "correctAnswer": "A",
        "explanation": "Twisting the pairs causes external electromagnetic fields to affect both wires equally; differential signal receivers subtract the noise, canceling EMI and near-end crosstalk (NEXT).",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-65",
        "topic": "Computer Networking",
        "subtopic": "Network Troubleshooting & Utilities",
        "question": "If a host can ping 127.0.0.1 and its own local IP address 192.168.1.50, but cannot ping its default gateway 192.168.1.1, which problem is most likely?",
        "options": [
            {"id": "A", "text": "A physical link or Layer 2 connectivity problem between the host and the local switch or router"},
            {"id": "B", "text": "The local TCP/IP protocol stack is uninstalled or corrupt"},
            {"id": "C", "text": "The public DNS servers are offline"},
            {"id": "D", "text": "The external internet service provider has suffered an outage"}
        ],
        "correctAnswer": "A",
        "explanation": "Pinging 127.0.0.1 verifies the local TCP/IP stack works. Pinging the local IP verifies the NIC driver is active. Inability to reach the gateway points directly to a local physical or Layer 2 link issue.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-66",
        "topic": "Computer Networking",
        "subtopic": "Routing & Protocols",
        "question": "What is the purpose of VRRP (Virtual Router Redundancy Protocol) or HSRP (Hot Standby Router Protocol)?",
        "options": [
            {"id": "A", "text": "Providing default gateway redundancy by presenting a virtual IP and virtual MAC address shared between redundant routers"},
            {"id": "B", "text": "Balancing web server requests at Layer 7"},
            {"id": "C", "text": "Dynamic bandwidth allocation for internet links"},
            {"id": "D", "text": "Encrypting traffic between branch routers"}
        ],
        "correctAnswer": "A",
        "explanation": "First Hop Redundancy Protocols (HSRP/VRRP) provide high availability for hosts by sharing a virtual gateway IP/MAC; if the master router fails, the standby router immediately takes over.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-67",
        "topic": "Computer Networking",
        "subtopic": "Network Security & Protocols",
        "question": "What security mechanism helps mitigate Rogue DHCP servers on an enterprise access switch?",
        "options": [
            {"id": "A", "text": "DHCP Snooping"},
            {"id": "B", "text": "Dynamic ARP Inspection (DAI)"},
            {"id": "C", "text": "Spanning Tree BPDU Guard"},
            {"id": "D", "text": "MAC Flapping Protection"}
        ],
        "correctAnswer": "A",
        "explanation": "DHCP Snooping classifies switch ports as trusted or untrusted, dropping rogue DHCP server messages (DHCPOFFER, DHCPACK) arriving on untrusted user ports.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-68",
        "topic": "Computer Networking",
        "subtopic": "IP Addressing & Subnetting",
        "question": "In Classful IPv4 addressing, what is the default network class and leading bit pattern for the IP address 210.150.25.1?",
        "options": [
            {"id": "A", "text": "Class C (Leading bits: 110)"},
            {"id": "B", "text": "Class B (Leading bits: 10)"},
            {"id": "C", "text": "Class A (Leading bits: 0)"},
            {"id": "D", "text": "Class D (Leading bits: 1110)"}
        ],
        "correctAnswer": "A",
        "explanation": "Class C addresses range from 192.0.0.0 to 223.255.255.255, with the high-order bits 110 (binary 110xxxxx). 210 falls in Class C.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-69",
        "topic": "Computer Networking",
        "subtopic": "IP Addressing & Subnetting",
        "question": "What is the multicast address range designated in IPv4?",
        "options": [
            {"id": "A", "text": "224.0.0.0 to 239.255.255.255 (Class D)"},
            {"id": "B", "text": "240.0.0.0 to 255.255.255.254 (Class E)"},
            {"id": "C", "text": "192.0.0.0 to 223.255.255.255 (Class C)"},
            {"id": "D", "text": "128.0.0.0 to 191.255.255.255 (Class B)"}
        ],
        "correctAnswer": "A",
        "explanation": "Class D addresses (224.0.0.0 to 239.255.255.255) are reserved for multicast groups (e.g. 224.0.0.5 for OSPF routers). Class E (240.0.0.0+) is experimental.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "net-gen-70",
        "topic": "Computer Networking",
        "subtopic": "Network Troubleshooting & Utilities",
        "question": "What Wireshark display filter isolates all DNS query responses containing errors or NXDOMAIN results?",
        "options": [
            {"id": "A", "text": "dns.flags.rcode != 0"},
            {"id": "B", "text": "dns.port == 53 && error"},
            {"id": "C", "text": "ip.proto == dns && failed"},
            {"id": "D", "text": "tcp.flags.reset == 1"}
        ],
        "correctAnswer": "A",
        "explanation": "In DNS protocol headers, the Return Code (RCODE) field indicates status: 0 is NoError, 3 is NXDomain. Thus, `dns.flags.rcode != 0` filters all non-successful DNS responses.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    }
]
