from google.cloud import storage


class GCSFileManager:
    def __init__(self):
        self.client = storage.Client()
        self.bucket = self.client.bucket('<bucket_name>')

    def upload_file(self, file_path: str, filename: str):
        try:
            blob = self.bucket.blob(filename)
            with open(file_path, 'rb') as csv_data:
                blob.upload_from_file(csv_data)
        except Exception as err:
            print(err)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gcs_object = GCSFileManager()
    gcs_object.upload_file(file_path='data/demo_data.csv', filename='demo_data.csv')
