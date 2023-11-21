import streamlit as st
import os
from PIL import Image
from datetime import datetime
import pandas as pd

# Upload files

# When give directory name and file
# save the file at that directory
def save_uploaded_file(directory, file):
    # 1. Is that directory actually exist?
    #    If not, create new directory
    #    If yes, do nothing
    if not os.path.exists(directory):
        os.makedirs(directory)
    # 2. If directory is actually exist,
    #    Save this file in this directory
    with open(os.path.join(directory, file.name), 'wb') as f:
        f.write(file.getbuffer())
    # 3. If file save gone success, show web screen to users
    return st.success('Successfully save the file in '+directory+' , what named '+file.name)

# save_uploaded_file('tmp', file)

def main():
    st.header('File upload Project')

    # set Sidebar and use if to selcet upload file type
    choice = st.sidebar.selectbox('Menu', ['Image','CSV'])


    if choice == 'Image':
        st.subheader('Image file upload')

        file = st.file_uploader('Upload Image file now', type =['jfif','jpg', 'jpeg','png', 'webp'])

        if file is not None:
            # How to manage file name consistently
            # In company, they have file naming rules

            # If combine datetime with file name
            # The file name gonna have unique name
            current_time = datetime.now()

            print( current_time.isoformat().replace(':','_').replace('.','_') + '.jpg')

            file.name = current_time.isoformat().replace(':','_').replace('.','_') + '.jpg'

            # If file have uploaded, save the file
            save_uploaded_file('tmp',file)
            # Show saved file on web screen
            img = Image.open(file)
            st.image(img)


    elif choice == 'CSV':
        st.subheader('CSV file upload')

        file = st.file_uploader('CSV File upload', type = ['csv'])

        if file is not None:
            # Make file name unique
            current_time = datetime.now()

            print( current_time.isoformat().replace(':','_').replace('.','_') + '.csv')

            file.name = current_time.isoformat().replace(':','_').replace('.','_') + '.csv'

            # save csv file
            save_uploaded_file('csv',file)

            # Save csv file as pandas dataframe
            # And show web screen
            df = pd.read_csv(file)
            
            st.dataframe(df)


if __name__ == '__main__':
    main()