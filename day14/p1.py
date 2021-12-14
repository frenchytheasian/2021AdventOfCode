def parse_data():
    template = ""
    rules = []
    with open('in.txt', 'r') as f:
        data_raw = f.read().split('\n\n')
        template = data_raw[0].strip()

        rules_raw = data_raw[1].strip().split('\n')
        for rule_raw in rules_raw:
            rule_raw = rule_raw.strip().split('->')


def main():
    template, rules = parse_data()
    print(data)

if __name__ == "__main__":
    main()