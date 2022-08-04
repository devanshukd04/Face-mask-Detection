# Face-mask-Detection-1

## Inspiration
- COVID-19 is an infectious disease caused by the SARS-CoV2 virus, but anyone can become seriously ill from COVID-19, regardless of their age. 
- When an infected person coughs, sneezes, speaks, sings, or breathes, small liquid particles spread the virus. 
- Having a mask on is an effective way to reduce the spread of the COVID-19 virus. This project will assist local authorities in monitoring public areas for public safety. 

## What it does
- The task of ensuring everyone wears a facemask is not an easy one. 
- The application recognizes human faces and determines whether they are wearing face masks or not.
- Face recognition and mask detection is performed in real-time in this application. 

## How we built it
- It contains 10000 images for training and 400 images for validation taken from the Kaggel website 
- As the dataset used consists of images with different colors, sizes, and orientations, the images are converted to grayscale and normalized. 
- Data is augmented to provide robustness for the model and to avoid overfitting.
- A CNN model is then built over the processed data. It is found that the model is 97.5% accurate
- Using openCV, the model was tested in real-time and deployed over the web.
