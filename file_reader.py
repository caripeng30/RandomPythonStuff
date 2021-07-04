class file_reader(Exception):
    def file_reader(filename):
        with open(filename + ".dat") as f:
            data = f.read()
        f.close()
        splitted = data.split(":")
        returned_value = ""
        for split in splitted:
            if split == '': pass
            else:
                if returned_value == "":
                    returned_value = returned_value +  split
                else:
                    returned_value = returned_value + " " + split
        return returned_value
