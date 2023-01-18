import os


class DownloadListener:
    def __init__(self, download_dir: str = None, files_names_iterator=None):
        if not files_names_iterator:
            raise ValueError("files_names_iterator is required")
        self.files_names_iterator = files_names_iterator
        self.download_dir = download_dir if download_dir else os.getcwd()

        os.chdir(self.download_dir)

    def get_file_list(self) -> "list[str]":
        return os.listdir(self.download_dir)

    def adjust_iterator(self, current_name: str = None, files_list: "list[str]" = None):
        try:
            if isinstance(files_list, list) and len(files_list) == 0:
                return

            current_list = self.get_file_list() if not files_list else files_list

            current = (
                next(self.files_names_iterator) if not current_name else current_name
            )
            found = False
            for file in current_list:
                if file == current + ".pdf":
                    current_list.remove(f"{current}.pdf")
                    current = next(self.files_names_iterator)
                    found = True
                    break
            if not found:
                current = next(self.files_names_iterator)
            self.adjust_iterator(current, current_list)
        except StopIteration:
            return

    def rename_file_to_next_name(self, file_name_to_listen: str):
        new_name = self.files_names_iterator.current_str
        os.rename(
            os.path.join(self.download_dir, file_name_to_listen),
            os.path.join(self.download_dir, new_name + ".pdf"),
        )
        print("Renamed file to " + new_name + ".pdf")
        next(self.files_names_iterator)

    def listen(self, file_name_to_listen: str):
        try:
            self.adjust_iterator()
            print(f"Listening for file on {self.download_dir}")
            print("Waiting for file...")
            while True:
                if file_name_to_listen in self.get_file_list():
                    print(f"{file_name_to_listen} found")
                    self.rename_file_to_next_name(file_name_to_listen)
                    print("Waiting for file...")
        except KeyboardInterrupt:
            print("Exiting...")
        except StopIteration:
            print("All months downloaded")
