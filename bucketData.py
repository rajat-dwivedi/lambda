import boto
import boto.s3.connection
import sys
import boto3
from boto3.session import Session

access_key = <access key>
secret_key = <secret key>

conn = boto.connect_s3(
        aws_access_key_id = access_key,
        aws_secret_access_key = secret_key
        )

bucketNames = []
for bucket in conn.get_all_buckets():
        print("{name}\t{created}".format(
                name = bucket.name,
                created = bucket.creation_date,
        ))
        bucketNames.append(bucket.name)


session = Session(aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)

s3 = session.resource('s3')

s3bucket = s3.Bucket(bucketNames[0])
size = 0
totalCount = 0

for key in s3bucket.objects.all():
    totalCount += 1
    size += key.size

print(bucketNames[0])
print('total size:')
print("%.3f GB" % (size*1.0/1024/1024/1024))
print('total count:')
print(totalCount)
