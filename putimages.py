import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('image1.jpg','Elon Musk'),
      ('image2.jpg','Elon Musk'),
      ('image3.jpg','Bill Gates'),
      ('image4.jpg','Bill Gates'),
      ('image5.jpg','Sundar Pichai'),
      ('image6.jpg','Sundar Pichai'),
      ('image7.png','Satyam Arya')
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('satyam-recognition-bucket','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]})