import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('image.png','x1'),
      ('image1.png','x2'),
      ('image2.png','x3'),
      ('image7.png','x4'),
     ('image3.png','x5'),
     ('image4.png','x6'),
     ('image5.png','x7'),
     ('image8.jpg','x8'),
     ('image9.jpg','x9'),
     ('imaage')
#image.png    image_2.png  image_4.png  image_6.png  import.py
#image_1.png  image_3.png  image_5.png  image_7.png


      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('hacknightaz111','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]}
                    )