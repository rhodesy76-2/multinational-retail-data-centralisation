class DataExtractor():
    def extract_from_csv(self, filename):
        '''Returns a list of records from the csv file given as a parameter''' 
        # Assumes that the file is stored in the same directory

        # Code to extract data from CSV goes here
    
    def extract_from_API(self, endpoint):
        '''Returns the data returned by making an API call to the specified endpoint'''
        # For example on how to make an API request in Python
        # refer to this link https://realpython.com/python-requests/
        
        # Code to extract data from API goes here

    def extract_from_s3_bucket(self, bucket_name, path):
        '''Returns the file stored under the mentioned bucket and path'''
        # bucket name is the bucket in which the file will be stored
        # and path is the object key of that particular file.
        # For example on how to download files from s3 buckets in Python
        # refer to this link https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.download_file

        # Code to extract data from S3 bucket goes here
