import urllib.request


def calculate(url):
    with urllib.request.urlopen(url) as r:
        d = r.read().decode('utf-8')

    x = y = n = 0.0

    for l in d.splitlines():
        if not l.strip():
            continue
        a, b = l.replace(',', '.').split()
        x += float(a)
        y += float(b)
        n += 1

    print(x / n, y / n)


file_url = "https://cloud.physics.itmo.ru/s/pY68e5CrdtQHF6M/download"
calculate(file_url)