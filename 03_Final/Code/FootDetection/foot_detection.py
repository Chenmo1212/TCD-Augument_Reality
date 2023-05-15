import streamlit as st
from PIL import Image
import numpy as np
import cv2
from utils import kMeans_cluster, edge_detection, get_bounding_rect, draw_bounding_box, crop_minAreaRect, convert_to_shoe_size


TRUE_A4_WIDTH = 21
TRUE_A4_LENGTH = 29.7


def load_image(image_file):
	img = Image.open(image_file)
	return img

st.header("Foot Size Measurement")
st.subheader("Upload image")
st.markdown(
    """The uploaded image must satisfy the following requirements:
- Foot should be on an A4 paper, with the heel touching 1 edge of the paper
- Floor color should not be white
- Paper must be completly visible (all 4 corners are visible)"""
)
uploaded_file = st.file_uploader("Choose an image", type=["png","jpg","jpeg"])
if uploaded_file is not None:
    img = load_image(uploaded_file)
    img = np.array(img)
    st.subheader("Original Image")
    st.image(img)

    st.subheader("Step 1: Segment image into 2 clusters")
    segmented_img = kMeans_cluster(img)
    st.image(segmented_img)

    st.subheader("Step 2: Detect edges of the image")
    edges = edge_detection(segmented_img)
    st.image(edges)

    st.subheader("Step 3: Detect bouding box of the A4 paper")
    rect = get_bounding_rect(edges)
    edges_color = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
    edges_box = draw_bounding_box(edges_color, rect)
    st.image(edges_box)

    st.subheader("Step 4: Crop the the A4 paper from image")
    edges_crop = crop_minAreaRect(edges, rect)
    st.image(edges_crop)

    st.subheader("Step 5: Detect bouding box around the foot")
    foot_rect = get_bounding_rect(edges_crop)
    edges_crop = cv2.cvtColor(edges_crop, cv2.COLOR_GRAY2RGB)
    foot_box = draw_bounding_box(edges_crop, foot_rect)
    st.image(foot_box)

    st.subheader("Step 6: Calculate length and width of the foot")
    a4_width = min(rect[1])
    a4_length = max(rect[1])
    foot_width = min(foot_rect[1])
    foot_length = max(foot_rect[1])
    true_foot_width = round(TRUE_A4_WIDTH * foot_width / a4_width, 1)
    true_foot_length = round(TRUE_A4_LENGTH * foot_length / a4_length, 1)
    st.write("Foot Length: " + str(true_foot_length) + " cm")
    st.write("Foot Width: " + str(true_foot_width) + " cm")
    shoe_size = convert_to_shoe_size(true_foot_length, true_foot_width)
    st.write("Shoe Size: " + str(shoe_size))