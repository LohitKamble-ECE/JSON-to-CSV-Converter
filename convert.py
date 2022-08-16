import argparse
import json
import csv
import collections


def parser():
    """Parse the command and return its arguments."""
    my_parser = argparse.ArgumentParser(
        description='Convert a data stored in JSON file format to CSV file format.')

    my_parser.add_argument('-i', '--input', metavar='file',
                           help='input JSON filename', required=True)
    my_parser.add_argument('-o', '--output', metavar='file',
                           help='ouput CSV filename', default='output.csv')

    return my_parser.parse_args()


def read_json(input, fill_na=None):
    """Read the json file and return data stored as dictionary of lists."""
    result = collections.defaultdict(list)
    with open(input, 'r') as file:
        raw = json.loads(file.read())
        for num, adict in enumerate(raw):
            for key, val in adict.items():
                if key not in result.keys():
                    result[key].extend([fill_na] * num)
                result[key].append(val)
            for key in [x for x in result.keys() if x not in adict.keys()]:
                result[key].append(fill_na)
    return result


def write_csv(raw, output):
    """Write a raw data (dictionary of lists) into the ouput csv file."""
    with open(output, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(raw.keys())
        for line in zip(*raw.values()):
            writer.writerow(line)


def main():
    args = parser()
    raw = read_json(args.input, 'NA')
    write_csv(raw, args.output)


if __name__ == '__main__':
    main()
