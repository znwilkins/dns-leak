# dns-leak
Query in Wireshark
```
udp and udp.port == 53 and dns.qry.name contains "94fc460d-be55-4d38-82a2-b7761a1e31b3.com" and dns.flags == 0x0100
```
then export to dns.csv and run
```bash
cat dns.csv | cut -d ',' -f 7 | cut -d ' ' -f 5 | sed -n '1~2!p' - | cut -d '.' -f 2 | base64 --decode
```
