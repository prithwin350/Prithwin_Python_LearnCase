def get_input(prompt, data_type=str):
    while True:
        try:
            return data_type(input(prompt))
        except ValueError:
            print(f"Please enter a valid {data_type.__name__}.")


def print_table(headers, rows):
    if not rows:
        print("\nNo records found.")
        return

    # Calculate the width of each column
    widths = []

    for i, header in enumerate(headers):
        width = len(header)

        for row in rows:
            width = max(width, len(str(row[i])))

        widths.append(width)

    # Print header
    header_row = " | ".join(
        header.ljust(widths[i])
        for i, header in enumerate(headers)
    )

    print()
    print(header_row)
    print("-" * len(header_row))

    # Print rows
    for row in rows:
        print(
            " | ".join(
                str(value).ljust(widths[i])
                for i, value in enumerate(row)
            )
        )