import subprocess

var5 = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]

for ping_now in var5:

    ping_process = subprocess.Popen(ping_now, stdout=subprocess.PIPE)

    i = 0

    for line in ping_process.stdout:

        if i < 10:
            print(line)
            line = line.decode('cp866').encode('utf-8')
            print(line.decode('utf-8'))
            i += 1
        else:
            print('#' * 30)
            break
