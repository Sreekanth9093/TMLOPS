import boto3

# Let's use Amazon S3
s3_client = boto3.resource('s3')

bucket_name = 'iriscloudbt-mlapp'  # Replace with your bucket name
file_key = 'model/model.pkl'  # Replace with your file key    
local_file_path = 'local_rental_prediction_mode.pkl'  # Replace with your local path

# Print out bucket names
def print_bucket_names():
    print("Listing Amazon S3 buckets:")
    for bucket in s3_client.buckets.all():
        print(f" - {bucket.name}")


# 
def upload_file(bucket_name, file_key, local_file_path):
    """
    Upload a file to an S3 bucket.
    
    :param bucket_name: Name of the S3 bucket
    :param file_key: Key under which the file will be stored in the S3 bucket
    :param local_file_path: Local path of the file to be uploaded
    """
    try:
        s3_client.Bucket(bucket_name).upload_file(local_file_path, file_key)
        print(f"Uploaded {local_file_path} to {bucket_name}/{file_key}")
    except Exception as e:
        print(f"Error uploading file: {e}")

def download_file(bucket_name, file_key, local_file_path):
    """
    Download a file from an S3 bucket to a local path.
    
    :param bucket_name: Name of the S3 bucket
    :param file_key: Key of the file in the S3 bucket
    :param local_file_path: Local path where the file will be saved
    """
    try:
        s3_client.Bucket(bucket_name).download_file(file_key, local_file_path)
        print(f"Downloaded {file_key} from {bucket_name} to {local_file_path}")
    except Exception as e:
        print(f"Error downloading file: {e}")
    
# Call the function to print bucket names
#print_bucket_names()

# 
upload_file(bucket_name, file_key, local_file_path)

# Call the function to download the file
#download_file(bucket_name, file_key, local_file_path)


print("File Upload successfully.")

