import time
import psutil

count = 0

last_received = psutil.net_io_counters().bytes_recv
last_sent = psutil.net_io_counters().bytes_sent
last_total = last_received + last_sent

while count < 10 :
  bytes_received = psutil.net_io_counters().bytes_recv
  bytes_sent = psutil.net_io_counters().bytes_sent
  bytes_total = last_received + last_sent

  new_received = bytes_received - last_received
  new_sent = bytes_sent - last_sent
  new_total = bytes_total - last_total

  mb_new_received = new_received / 1024/ 1024
  mb_new_sent = new_sent / 1024 / 1024
  mb_new_total = new_total /1024 /1024

  print(f"{mb_new_received:.2f} MB received, {mb_new_sent:.2f} MB sent, {mb_new_total:.2f} MB Total.")

  last_received = bytes_received
  last_sent = bytes_sent
  last_total = bytes_total

  time.sleep(1)
  count += 1

# Caution: If you modify the while loop, it may inifnitely looping
