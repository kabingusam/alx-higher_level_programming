#!/usr/bin/python3
if __name__ == "__main__":
    '''addition of all arguments'''
    import sys
    count = len(sys.argv)

    for i in range((sys.argv)- 1):
        sum =+ int(sys.argv[i + 1])
    print("{}".format(sum))