import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('image01.jpeg','Albert Einstein'),
      ('image02.jpeg','Albert Einstein'),
      ('image03.jpeg','Albert Einstein'),
      ('image04.jpeg','Niels Bohr'),
      ('image05.jpeg','Niels Bohr'),
      ('image06.jpeg','Niels Bohr')
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('rekognition-pictures','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]}
                    )