# -*- coding: utf-8 -*-

import csv
import os
import gzip


class File:
    def read(self, path, **kwargs):
        path = os.path.join(kwargs.get('root_path', ''), path)
        content_type = kwargs.get('content_type', 'txt')

        if content_type == 'txt':
            with file(path, 'r') as f:
                content = f.read()
            yield content
        elif content_type == 'gz':
            with gzip.open(path, 'r') as f:
                content = f.read()
            yield content
        elif content_type == 'csv':
            with open(path, 'rU') as f:
                reader = csv.reader(f)
                for line in reader:
                    yield line
        else:
            raise Exception('Bad file type')

    def write(self, path, content, **kwargs):
        path = os.path.join(kwargs.get('root_path', ''), path)
        content_type = kwargs.get('content_type', 'txt')

        if content_type == 'txt':
            with file(path, 'wb') as f:
                f.write(content)
        elif content_type == 'gz':
            with gzip.open(path, 'w') as f:
                f.write(content)
        elif content_type == 'csv':
            with open(path, 'wb') as f:
                writer = csv.writer(f)
                for c in content:
                    if c['type'] == 'single':
                        writer.writerow(c['data'])
                    elif c['type'] == 'multi':
                        writer.writerows(c['data'])
                    else:
                        raise Exception('Row type must be specified')
        else:
            raise Exception('Bad file type')

    def exists(self, path):
        return os.path.exists(path)
