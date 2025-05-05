class TextLoader:
    @staticmethod
    def can_load(file_path):
        return file_path.lower().endswith('.txt')  # Check if the file is a text file

    @staticmethod
    def load(file_path):
        with open(file_path, 'r') as file: # The 'r' mode used in open() is for reading text files
            data = file.read()  # Read the text file content
        return data  # Return the text data