import sys

# python file.py filename

if len(sys.argv) != 2:
    print("Usage: file.py filename", file=sys.stderr)
    sys.exit(1)

try:
    with open(sys.argv[1]) as f:
        for line in f:
            comment_split = line.split("#")
            num = comment_split[0].strip()

            if num == "":
                continue

            x = int(num, 2)
            print(f"{x:08b}: {x:d}")
            # could also do below
            # commands.append(num)
        # print(commands)
        # print([int(c, 2) for c in commands ])

except FileNotFoundError:
    print(f"{sys.argv[0]}: {sys.argv[1]} not found")
    sys.exit(2)