import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def kMeans_cluster(img):
    # For clustering the image using k-means, need to convert it into a 2-dimensional array
    # (H*W, N) N is channel = 3
    image_2D = img.reshape(img.shape[0]*img.shape[1], img.shape[2])

    kmeans = KMeans(n_clusters=2, random_state=0).fit(image_2D)
    clustOut = kmeans.cluster_centers_[kmeans.labels_]

    # Reshape back the image from 2D to 3D image
    clustered_3D = clustOut.reshape(img.shape[0], img.shape[1], img.shape[2])
    clusteredImg = np.uint8(clustered_3D*255)

    return clusteredImg


def edge_detection(img):
    edges = cv2.Canny(img, 40, 40)
    edges = cv2.dilate(edges, None)
    return edges


def get_bounding_rect(img):
    contours, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # Get the largest rectangle box to get the paper
    rects = [cv2.minAreaRect(cnt) for cnt in contours]
    # Sort all boxes by area
    rects.sort(key=lambda rect: rect[1][0] * rect[1][1])
    return rects[-1] # return largest bounding rect


def draw_bounding_box(img, rect):
    img_copy = np.copy(img)
    box = np.int0(cv2.boxPoints(rect))
    cv2.drawContours(img_copy, [box], 0, (255,0,0), 2)
    return img_copy


def crop_minAreaRect(img, rect):
    # get the parameter of the small rectangle
    center, size, angle = rect[0], rect[1], rect[2]
    center, size = tuple(map(int, center)), tuple(map(int, size))

    # get row and col num in img
    height, width = img.shape[0], img.shape[1]

    # calculate the rotation matrix
    M = cv2.getRotationMatrix2D(center, angle, 1)
    # rotate the original image
    img_rot = cv2.warpAffine(img, M, (width, height))

    # now rotated rectangle becomes vertical, and we crop it
    img_crop = cv2.getRectSubPix(img_rot, size, center)
    # Slightly crop around image
    img_crop = img_crop[50:-50, 50:-50]
    return img_crop


def convert_to_shoe_size(length, width):
    base_length = 21
    base_length_size = 32
    length_size = -1

    while base_length <= 27:
        if length <= base_length:
            length_size = base_length_size
            break
        base_length += 0.5
        base_length_size += 1
    if length_size == -1:
        length_size = 45

    base_width = 8
    base_width_size = 32
    width_size = -1

    while base_width <= 11:
        if width <= base_width:
            width_size = base_width_size
            break
        base_width += 0.5
        base_width_size += 2
    if width_size == -1:
        width_size = 45

    shoe_size = max(length_size, width_size)
    return shoe_size
    
        
if __name__ == "__main__":
    print(convert_to_shoe_size(25.6, 10.2))