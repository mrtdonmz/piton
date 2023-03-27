
import os


#set the env vairable in 2nd line
os.environ['REPLICATE_API_TOKEN'] = '7b63ad7d84b75864d74799794581e3d441e3b81d'

import replicate
model = replicate.models.get("salesforce/blip")
version = model.versions.get("2e1dddc8621f72155f24cf2e0adbde548458d3cab9f00c0139eea840d0ac4746")
inputs = {
    # Input image
    'image': open("C:\\Users\\mert9\\Desktop\\piton\\demo.jpg", "rb"),

    # Choose a task.
    #'task': "image_captioning",
    'task': "visual_question_answering",

    # Type question for the input image for visual question answering
    # task.
    'question': "how many dogs in the picture",

    # Type caption for the input image for image text matching task.
    # 'caption': ...,
}

output = version.predict(**inputs)
print(output)
