class FileHelper():
    @staticmethod
    def write_to_file(filename, payload):
        with open(filename, 'w+') as file:
            file.write(payload)
