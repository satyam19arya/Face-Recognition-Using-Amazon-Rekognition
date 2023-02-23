# Commands
- Install aws-shell
```
pip install aws-shell
```

- Configure
```
aws configure
```

- Create a collection on aws rekognition
```
aws rekognition create-collection --collection-id facerecognition_collection --region us-east-1
```

- Create table on DynamoDB
```
aws dynamodb create-table --table-name myfacerecognition --attribute-definitions AttributeName=RekognitionId,AttributeType=S --key-schema AttributeName=RekognitionId,KeyType=HASH --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 --region us-east-1
```

- Create S3 bucket
```
aws s3 mb s3://bucket-name --region us-east-1
```

- Run to put images in S3 bucket
```
python .\putimages.py
```
```
cd test
python .\testing.py
```

Enter path of the image to check😎