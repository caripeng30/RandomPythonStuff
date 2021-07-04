class file_creator(Exception):
    def file_create(string, filename):
        texts = string.split(':')
        with open(filename + ".dat", 'w') as f:
            for text in texts:
                f.write(text + ":")


