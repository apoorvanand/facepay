import boto3

azureblob = boto3.resource('s3')

# Get list of objects for indexing
images=[('image27.jpg','x1'),
      ('image1.jpg','x2'),
      ('image2.jpg','x3'),
      ('image7.jpg','x4'),
     ('image3.jpg','x5'),
     ('image4.jpg','x6'),
     ('image5.jpg','x7'),
     ('image8.jpg','x8'),
     ('image9.jpg','x9'),
     ('image10.jpg','x10')
#image.png    image_2.png  image_4.png  image_6.png  import.py
#image_1.png  image_3.png  image_5.png  image_7.png


      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = azureblob.Object('hacknightaz111','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]}
                    )