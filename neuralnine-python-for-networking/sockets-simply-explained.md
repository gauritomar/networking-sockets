## Sockets

Sockets are communication endpoints that can facilitate various types of communication. They don't necessarily need to be internet sockets; they can also be used for other types of communication protocols.

In addition to internet sockets, there are other types of sockets such as Bluetooth sockets (SOCKET.AF_BLUETOOTH) and various system-level sockets like OS sockets and Kernel sockets.

### Differences between SOCK_STREAM (TCP) and SOCK_DGRAM (UDP) Sockets

| Feature                    | SOCK_STREAM (TCP)                                                                   | SOCK_DGRAM (UDP)                                                                   |
|----------------------------|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| Connection                | Connection-based: Connection is established before data transfer.                    | Connectionless: No connection establishment; each packet is independent.            |
| Reliability               | Reliable: Ensures data delivery, detects and retransmits lost packets.               | Unreliable: No guarantee of data delivery or detection of lost packets.              |
| Ordering                  | Ordered: Data packets are delivered in the order they were sent.                     | Unordered: Data packets may arrive out of order.                                     |
| Packet Loss               | Detects and retransmits lost packets.                                                | No detection or retransmission of lost packets.                                     |
| Use Cases                 | Ideal for applications requiring reliable, ordered, and error-checked delivery.      | Suitable for real-time applications, multimedia streaming, and situations where some packet loss is acceptable. |
| Overhead                  | Higher overhead due to connection setup, reliability mechanisms, and flow control.   | Lower overhead, as there is no connection setup and no reliability mechanisms.       |


## Skype: Use Case

- Skype utilizes a combination of TCP and UDP protocols for different aspects of its communication:

1. **UDP for Call Transmission**: Skype employs UDP (User Datagram Protocol) for the actual transmission of calls. UDP is preferred for real-time communication like voice and video calls due to its lower latency and reduced overhead compared to TCP.

2. **TCP for Call Requests and Messages**: However, the initiation of calls, transmission of emojis, and exchange of text messages in Skype are handled over TCP (Transmission Control Protocol). TCP provides reliable, ordered, and error-checked delivery, which is essential for ensuring that call requests and messages are delivered accurately.

3. **Streaming Video via TCP**: Additionally, Skype has the capability to stream video over TCP. Although TCP introduces more overhead due to its connection-oriented nature, it can be advantageous for streaming video content where reliability and ordered delivery are prioritized over minimal latency.

By leveraging both TCP and UDP, Skype optimizes its communication platform to provide a seamless user experience while balancing the requirements of reliability, real-time responsiveness, and efficiency.
