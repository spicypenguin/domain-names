import json


def main():
    domains = [
        'in',
        'me',
        'us',
        'de',
        'ca',
        'eu',
        'be',
        'ch',
        'im',
        'it',
        'nl',
        'sh'
    ]

    with open('words/combined.json', 'r') as f:
        words = json.load(f)

    generated_domains = set()
    for word in words:
        for domain in domains:
            if word.endswith(domain):
                text = word.replace(domain, '')
                if len(text) >= 6:
                    full_domain = f"{text}.{domain}"
                    generated_domains.add(full_domain)

    for domain in sorted(
        generated_domains,
        key=lambda i: (len(i), i),
        reverse=True
    ):
        print(domain)

    with open('domains/combined_domains.json', 'w') as f:
        json.dump(list(generated_domains), f)


if __name__ == '__main__':
    main()
