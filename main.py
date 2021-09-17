from simple_image_download import simple_image_download as simp

response = simp()

keywords = "medical bonnet"
limit = 100
#extensions={'.jpg', '.png', '.jpeg'}
response.download(keywords, limit, extensions={'.png'})