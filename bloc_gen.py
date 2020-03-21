import sys
import os
import shutil


def changeContent(post, pack='template', cls='Template'):
    pack_dir = '%s_page' % pack
    read_f = '%s/template_%s.dart' % (pack_dir, post)
    write_f = '%s/%s_%s.dart' % (pack_dir, pack, post)
    with open(read_f, 'r') as r_f:
        with open(write_f, 'w') as w_f:
            for line in r_f:
                text = line.replace('template', pack)
                text = text.replace('Template', cls)
                w_f.write(text)
    os.remove(read_f)


def main():
    print("Starting Bloc Template Generator")
    pack = input("Enter package name: ")
    if type(pack) is not str:
        print("Invalid Package Name")
        sys.exit(1)
    cls = input("Enter class name: ")
    if type(cls) is not str:
        print("Invalid Class Name")
        sys.exit(1)

    # Copy files
    shutil.copytree('template_page', '%s_page' % pack)
    print("Copying files completed...")

    # Change Content
    changeContent('event', pack, cls)
    changeContent('bloc', pack, cls)
    changeContent('state', pack, cls)
    changeContent('page', pack, cls)
    changeContent('view', pack, cls)
    changeContent('provider', pack, cls)
    print("Changing context completed...")


if __name__ == "__main__":
    main()

