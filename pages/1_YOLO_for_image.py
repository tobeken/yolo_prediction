import streamlit as st
from yolo_predictions import YOLO_Pred
from PIL import Image
import numpy as np




st.set_page_config(page_title="YOLO object detection",layout="wide",page_icon='./images/object.png')

st.title('YOLO へようこそ')
st.write("予測用のデータをアップロードしてください")


with st.spinner('Please wait while your model is loading'):
    yolo = YOLO_Pred(onnx_model='./models/best.onnx',
                    data_yaml='./models/data.yaml')
    # st.balloons()

def upload_image():

    #upload image
    image_file = st.file_uploader(label='アップロード')
    if image_file is not None:
        size_mb = image_file.size/(1024**2)
        file_details ={"filename":image_file.name,
                        "filetype":image_file.type,
                        "filesize":"{:,.2f}MB".format(size_mb)
        }
        #st.json(file_details)
        #validate file
        if file_details['filetype'] in ('image/png','image/jpeg'):
            st.success('VALID IMAGE file type (png or jpeg)')
            return {"file":image_file,
                    "details":file_details}

        else:
            st.error('INVALID Image file type')
            st.error('upload only png,jpeg,jpg')
            return None

def main():
    object = upload_image()

    if object:
        prediction = False
        image_obj = Image.open(object['file'])

        col1,col2 = st.columns(2)
       

        with col1:
            st.info('Preview of Image')
            st.image(image_obj)
        with col2:
            st.subheader('check below for file details')
            st.json(object['details'])
            button = st.button('YOLOで予測')
            if button:
                with st.spinner("""
                予測中です。しばらくお待ちください
                                """):
                    image_array = np.array(image_obj)
                    pred_img = yolo.predictions(image_array)
                    pred_img_obj = Image.fromarray(pred_img)
                    prediction = True

        if prediction:
            st.subheader('Predicted Image')
            st.caption('Object detection from YOL v5 model')
            st.image(pred_img_obj)

                




if __name__ == "__main__":
    main()


