import psutil

times = psutil.cpu_times()

print('Time spent by normal processes executing in user mode:\n', times.user)

print('Time spent by processes executing in kernel mode:\n', times.system)

print('Time when system was idle: \n', times.idle)

print('Time spent by priority processes executing in user mode:\n', times.nice)

print('Time spent waiting for I/O to complete:\n', times.iowait)

print('Time spent for servicing hardware interrupts:\n', times.irq)

print('Time spent for servicing software interrupts:\n', times.softirq)

print('Time spent by other operating systems running in a virtualized environment:\n', times.steal)

print('Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel:\n', times.guest)