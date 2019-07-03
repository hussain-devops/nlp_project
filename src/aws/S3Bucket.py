import boto3

class S3Bucket:
    def getBuckets(self):
        # Let's use Amazon S3
        s3 = boto3.resource('s3')

        # Print out bucket names
        for bucket in s3.buckets.all():
            print(bucket.name)

#    def uploadFile(self):
#    def deleteFile(self):