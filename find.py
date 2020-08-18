import json
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d',
        dest='domain',
        help='provide an integer (default: 2)'
    )
    args = parser.parse_args()

    with open('candidate_domains.json', 'r') as f:
        data = json.load(f)

    matched_domains = set()
    for word, domains in data.items():
        for domain in domains:
            split_domain = domain.split('.')
            if len(split_domain[0]) >= 3:
                if args.domain and split_domain[1] == args.domain:
                    matched_domains.add(domain)

    for domain in sorted(matched_domains, key=lambda i: (len(i), i), reverse=True):
        print(domain)


if __name__ == '__main__':
    main()
