import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('image.png','Harish Kumar'),
      ('image_1.png','Ram Kahnanna'),
      ('image_2.png','Hema K'),
      ('image_7.png','Simaran Kaur'),
     ('image_3.jpeg','Jon Doe'),
     ('image_4.jpeg','Niels Bohr')
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