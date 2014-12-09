import argparse
import sys


def find_course_data(course_file, search_term):
    course_data = open(course_file, 'r')
    found = False
    course_ids = []
    for line in course_data:
        if "data-course-key=" in line:
            if search_term.rstrip() in line:
                line = line.split("data-course-key=", 1)[1]
                course_ids.append(line[:-2].rstrip().replace('"', '').strip())
                found = True
    if found:
        course_id_file = open("course_ids", "a")
        if len(course_ids) == 1:
            for id in course_ids:
                course_id_file.write(id+"\n")
        print search_term.rstrip(), ":", course_ids
    if not found:
        print search_term.rstrip(), ": Not found"


def main():
    parser = argparse.ArgumentParser()
    parser.usage = '''
    {cmd} -d path/to/data -c course_key
    '''.format(cmd=sys.argv[0])
    parser.add_argument('-d', '--file', help='Path to data', default='')
    parser.add_argument('-c', '--course', help='Course key', default='')
    parser.add_argument('-i', '--courses', type=argparse.FileType('rb'), default=None)

    args = parser.parse_args()

    if not (args.course or args.courses) and args.file:
        parser.print_usage()
        return

    course_keys = args.courses or [args.course]
    for course_key in course_keys:
        find_course_data(args.file, course_key)
    pass

if __name__ == "__main__":
    main()
