import sys

def main():
    # Make sure there is a twitter handle specified
    if len(sys.argv) != 2:
        print("Error: Invalid arguments")
        print("Syntax: main.py <twitterHandle>")
        return

    # Get the twitter handle from the command line
    twitterHandle = sys.argv[1]
    print("Monitoring twitter handle {0}".format(twitterHandle))

if __name__ == "__main__":
    main()