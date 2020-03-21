import sys
import os
import shutil


def main():
    args = sys.argv
    if len(args) <= 1:
        print("Give the filepath as input")
        sys.exit(1)

    path = args[1]
    t = input("Enter variable Type (as String): ")
    v = input("Enter variable name (as myText): ")
    i = 0
    text = ''
    with open(path, 'r') as r_f:
        for line in r_f:
            text += line
            if line.trim().endswith('{'):
                i += 1
                if i == 1:
                    text += 'final %s %s;' % (t, v)
                elif i == 2:
                    text += '@required this.%s,' %v
                elif i == 3:
                    text += '%s %s,' % (t, v)
            elif line.trim().endswith('(') and i == 3:
                i += 1
                text += '%s: %s ?? this.%s,' % (v, v, v)
    with open(path, 'w') as w_f:
        w_f.write(text)



if __name__ == "__main__":
    main()

