pv /div/zero
3.87GiB 0:00:06 [47.6MiB/s] [          <=>                                                                             ]
pv /dev/zero > /dev/null
3GiB 0:00:04 [16.4GiB/s] [      <=>]
pv /dev/random > /dev/null
57GiB 0:00:04 [391MiB/s] [      <=>]
pv /dev/urandom > /dev/null
70GiB 0:00:07 [398MiB/s] [            <=>]
dd if=/dev/zero of=bigfile.txt bs=1M count=1024
pv bigfile.txt > /tmp/bigfile_copy.txt
