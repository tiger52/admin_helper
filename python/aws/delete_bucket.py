#!/usr/bin/env python3
"""
This script delete all versions of all files and after that delete bucket
It should use when bucket has VERSIONING
"""
import boto3

def del_bucket(BUCKET):
    print("=== {} ===".format(BUCKET))
    print("Removing all versions from {}".format(BUCKET))
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(BUCKET)
    bucket.object_versions.delete()
    print("versions deleted")
    # if you want to delete the now-empty bucket as well, uncomment this line:
    print("start delete bucket".format(BUCKET))
    bucket.delete()
    print("bucket has been deleted")


bucket_list_decaf=[
    "bucket1",
    "bucket2"
]

for bucket in bucket_list_decaf:
    del_bucket(bucket)
