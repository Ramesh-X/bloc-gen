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
    if type(t) is not str:
        print("Invalid Variable Type")
        sys.exit(1)
    v = input("Enter variable name (as myText): ")
    if type(t) is not str:
        print("Invalid Variable Name")
        sys.exit(1)

    i = 1
    text = ''
    with open(path, 'r') as r_f:
        for line in r_f:
            text += line
            if line.strip().endswith('{'):
                if i == 1:
                    i += 1
                    text += 'final %s %s;\n' % (t, v)
                elif i == 2:
                    i += 1
                    text += '@required this.%s,\n' %v
                elif i == 4:
                    i += 1
                    text += '%s %s,\n' % (t, v)
            elif line.strip().endswith('('):
                if i == 3:
                    i += 1
                    text += '%s: null,\n' %v
                elif i == 5:
                    i += 1
                    text += '%s: %s ?? this.%s,\n' % (v, v, v)

    with open(path, 'w') as w_f:
        w_f.write(text)



if __name__ == "__main__":
    main()

