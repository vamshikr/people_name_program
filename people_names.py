import argparse
from collections import Counter


def get_all_names(file_path: str) -> list:
    """
    Get all the names from the given filepath into a list and returns the list
    Args:
        file_path:

    Returns:

    """
    all_names = []

    with open(file_path) as fptr:
        for line in fptr:
            if "--" in line:
                full_name = line.partition("--")[0]
                last_name, _, first_name = full_name.partition(",")
                all_names.append((last_name.strip(), first_name.strip()))
    return all_names


def cardinality(all_names: list):
    """
    Prints the cardinality of each the three sets of full, last, and first names
    Args:
        all_names:

    Returns:

    """
    print("### Cardinality")
    print("Number of unique full names: %s" % len(set(all_names)))
    print("Number of unique last names: %s" % len(set((last_name for last_name, _ in all_names))))
    print("Number of unique first names: %s" %
          len(set((first_name for _, first_name in all_names))))


def most_common_first_names(all_names: list, max_count: int):
    """
    Prints 'max_count' most common last names sorted in descending order, including the count of
    these names
    Args:
        all_names:
        max_count:

    Returns:

    """
    print("### most common first names sorted in descending order")
    first_names = Counter((first_name for _, first_name in all_names))

    for name, count in first_names.most_common(max_count):
        print("%s: %d" % (name, count))


def most_common_last_names(all_names: list, max_count: int):
    """
    Prints 'max_count' most common first names sorted in descending order, including the count of
    these names
    Args:
        all_names:
        max_count:

    Returns:

    """
    print("### most common last names sorted in descending order")
    last_names = Counter((last_name for last_name, _ in all_names))

    for name, count in last_names.most_common(max_count):
        print("%s: %d" % (name, count))


def get_unique_names(all_names: list, max_count: int) -> list:
    """
    Prints and returns a list of the first 'max_count' names from the file where the following
    is true:
    . No previous name has the same first name.
    . No previous name has the same last name.

    Args:
        all_names:
        max_count:

    Returns:

    """
    print("### Unique (last name, first name) set")
    recent_fist_names = set()
    recent_last_names = set()

    unique_names = list()
    count = 0
    for last_name, first_name in all_names:

        if last_name not in recent_last_names and first_name not in recent_fist_names:
            recent_fist_names.add(first_name)
            recent_last_names.add(last_name)
            unique_names.append((last_name, first_name))
            count += 1

        if count == max_count:
            break

    for last_name, first_name in unique_names:
        print("%s, %s" % (last_name, first_name))

    return unique_names


def modify_names(unique_names: list):
    """
    Rotates a first_names in the list by one and makes a new list by joining with last_names
    Args:
        unique_names:

    Returns:

    """
    print("### Modified (last name, first name) set")
    last_names = [last_name for last_name, _ in unique_names]
    first_names = [first_name for _, first_name in unique_names]

    # Rotate the first_names list
    first_item = first_names.pop(0)
    first_names.append(first_item)

    for last_name, first_name in zip(last_names, first_names):
        print("%s, %s" % (last_name, first_name))


def main(file_path: str, max_count: int):
    """
    Main method that calls all the methods tha address the functionality
    Args:
        file_path:
        max_count:

    Returns:

    """
    all_names = get_all_names(file_path)
    cardinality(all_names)
    most_common_last_names(all_names, max_count)
    most_common_first_names(all_names, max_count)
    unique_names = get_unique_names(all_names, max_count)
    modify_names(unique_names)


def cli_parser():
    """
    Command line options parser
    Returns:

    """
    parser = argparse.ArgumentParser(description='People Name Program 1.0')
    parser.add_argument('--max-count', dest='max_count', default="25",
                        help='Number of names to display, default is 25')
    parser.add_argument('--names-file', dest='filepath', required=True,
                        help="File that contains people's names")

    return parser.parse_args()


if __name__ == "__main__":
    args = cli_parser()
    main(args.filepath, int(args.max_count))
