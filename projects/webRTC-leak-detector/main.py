from scapy.all import *
import sys

# CLI things
CYAN    = "\033[96m"
BLACK   = '\033[30m'
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"

class Detector:
    magic_tokens = dict(
        STUN = b'\x21\x12\xa4\x42',
    )

    @staticmethod
    def alert(packet: list, protocol: str, method: str) -> None:
        print(f"{BOLD}{RED}[!] ALERT: {WHITE}WebRTC -p {RED}{protocol}{WHITE} -m {RED}{method}{WHITE} Handshake Detected!{RESET}")
        print(f"   {BOLD}{RED}>{RESET} Protocol : {protocol}")
        print(f"   {BOLD}{RED}>{RESET} Method : {method}")
        print(f"   {BOLD}{RED}>{RESET} Direction: {packet[IP].src}:{packet.sport} -> {packet[IP].dst}:{packet.dport}")
        print("")

    @staticmethod
    def stun_method(packet: list, protocol: str, payload: bytes) -> None:
        if len(payload) <= 20:
            return # a STUN header is at least 20 bytes long
        
        payload_offset = payload[4:8] # STUN offset

        if payload_offset == Detector.magic_tokens["STUN"]:
            Detector.alert(packet, protocol, "STUN")

def analyze_packet(packet):
    try:
        if packet.haslayer(UDP):
            payload = bytes(packet[UDP].payload)
            protocol = "UDP"
        elif packet.haslayer(TCP):
            payload = bytes(packet[TCP].payload)
            protocol = "TCP"
        else:
            return

        Detector.stun_method(packet, protocol, payload)

    except Exception:
        pass
        
if __name__ == "__main__":
    print(f"{BOLD}{GREEN}[*]{RESET} initializing WebRTC sniffer...")
    print(f"{BOLD}{GREEN}[*]{RESET} monitoring all network TCP and UDP protocols for signatures...\n")

    sniff(filter="udp or tcp", prn=analyze_packet, store=0)