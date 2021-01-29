'''
Script that downloads zip files from an S3 Bucket, unzips them and reuploads them to a different bucket.
@Author Carlos Avalos
 Access key or secret key not needed if the bucket is public.
'''

import boto3
import sys
import os
from zipfile import ZipFile

def Upload(fileName, bucketTwo):
    placeFiles = sys.path[0]+"\\"+"unzipped"
    print("########### Starting Upload Of All Unzipped Files#############")
    for root,dirs,files in os.walk(placeFiles):
        for file in files:
            bucketTwo.upload_file(os.path.join(root,file),file)
    print("############ Upload Complete #############")
            
    print("###### Removing Zip File ##########")
    
    os.remove(sys.path[0]+"//"+fileName)
    
    print("########### Removing Files #############")
    
    os.remove(placeFiles)
    
    print("######### File Removed,Upload Succesfull, Script Complete########")



def download(bucketOne):
    for keys in bucketOne.objects.all():
      placeFiles = sys.path[0]+"\\"+"unzipped"
      bucketOne.download_file(keys.key, placeFiles)
      #zip = ZipFile(sys.path[0]+"\\"+defaultName,'r')
      #zip.extractall(placeFiles)
      #zip.close() Uncomment if files are zipped




accessKey = '' 
secret = ''


s3 = boto3.resource('s3', aws_access_key_id=accessKey , aws_secret_access_key=secret)

defaultName=  'unzipped.zip'

bucketOne = s3.Bucket('')#Bucket One

bucketTwo = s3.Bucket('') #Bucket Two            
            

download(bucketOne)
Upload(defaultName,bucketTwo)
