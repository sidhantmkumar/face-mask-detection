from tensorflow.keras.preprocessing import image

img_path = "test.jpg"  # upload file in colab

img = image.load_img(img_path, target_size=(64,64))
img_array = image.img_to_array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)

prediction = model.predict(img_array)

if prediction[0][0] > 0.5:
    print("No Mask ❌")
else:
    print("Mask ✅")