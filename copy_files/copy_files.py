from os.path import join
from shutil import copy as copy_file
from progress.bar import Bar
import logging
from xml.etree import ElementTree


def copy(path_to_config):
    paths = prepare(open_file(path_to_config))
    for path in paths:
        try:
            src = join(path['source_path'], path['file_name'])
            dst = join(path['destination_path'], path['file_name'])
            with Bar(
                    f"{'Copy '}{src[:70]}{' to '}{dst[:70]}{': '}",
                    max=len(paths) / 100,
                    suffix='%(percent)d%%') as bar_file:
                try:
                    copy_file(src, dst)
                    logging.info(f"{'File copy '}{src}{' to '}{dst}{': '}")
                    bar_file.next()
                except OSError as error:
                    logging.warning('Error copy of file: {a}'.format(a=error))
                    bar_file.next()
                    raise
        except KeyError as error:
            logging.warning('Incorrect discription of file: {a}'.format(a=error))


def open_file(path):
    try:
        with open(path, 'r') as infile:
            content = infile.read()
        logging.info(f'{"Open config-file: "}{path}')
        return content
    except OSError as e:
        logging.error(f'{"Error config-file: "}{e}')
        raise


def prepare(content_xml):
    try:
        root = ElementTree.fromstring(content_xml)
        paths = []
        for child in root:
            paths.append(child.attrib)
        logging.debug(f'{"Prepare of paths files: "}{paths}')
        return paths
    except Exception as e:
        logging.error(f'{"Error of content config file: "}{e}')

