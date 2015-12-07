import os, sys, time, json
from operator import itemgetter

def parse_images(files_dir):
    images = []
    gallery_name = os.path.basename(files_dir)
    for filename in os.listdir(files_dir):
        path = os.path.join(files_dir, filename)
        if os.path.isdir(path) or filename.startswith('.'):
            continue
        dt = time.ctime(os.path.getctime(path))
        images.append({
            'dt': dt,
            'src': "/images/{}/{}".format(gallery_name, filename),
            'thumb': "/images/{}/thumbs/{}".format(gallery_name, filename),
        })
    return sorted(images, key=itemgetter('dt'), reverse=True)


def gen_front_matter(images, title):
    return {
        'images': images,
        'Frontpage': False,
        'date': "2015-12-06T17:12:59-07:00",
        'description': "",
        'title': title,
        'type': "gallery",
    }

def write_front_matter(front_matter, dest_file):
    dest_file.write(json.dumps(front_matter, indent=2))

def parse_and_write_file():
    files_dir = sys.argv[1]
    dest_file_path = sys.argv[2]
    title = sys.argv[3]

    images = parse_images(files_dir)
    front_matter = gen_front_matter(images, title)

    with open(dest_file_path, 'w') as dest_file:
        write_front_matter(front_matter, dest_file)


if __name__ == "__main__":
    parse_and_write_file()
