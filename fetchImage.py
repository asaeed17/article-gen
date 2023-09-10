import requests
import streamlit as st

def fetchImage(query):
    #pexels api key
    apiKey = "" 

    #pexels url
    url = "https://api.pexels.com/v1/search" #search endpoint as we search for an image based on a query

    #req/resp header to pass info
    headers = {
        'Authorization' : apiKey    #spelling should be "authorization"
    }

    params = {
        'query': query,
        'per_page': 1
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        #request successful
        data = response.json()
        images = data.get('photos', []) #'photos' not 'images'
        # print("images: ", images)

        if images:
            #only need the image url to fetch it
            imageUrl = images[0]['src']['original']
            print("imageUrl: ", imageUrl)
            
            return imageUrl
        else:
            # print("No images found!")
            st.write("No images found for the given topic")
    else:
        # print("error: ", {response.status_code}, {response.text})
        st.write(f"error: {response.status_code}, {response.text}")

    return None

# #test images
# query = "Airplane"

# #imageUrl for image on Pexels
# imageUrl = fetchImage(query)

# if imageUrl:
#     print(f"image url for '{query}' : {imageUrl}")
