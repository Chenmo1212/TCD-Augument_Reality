# Foot Measurement
## Web application
Visit https://share.streamlit.io/scinerd68/footdetection/main/foot_detection.py to see the result.
## Approach
- Use k-means to segment the image
- Detect edges on the segmented image
- Detect bouding box around the A4 paper
- Crop the A4 paper from the image
- Detect bounding box around the foot
- Based on length and width of paper's bounding box and foot's bouding box calculate real length and width of the foot (in cm) and output shoe size based on measured length and width
## Image requirements
The uploaded image must satisfy the following requirements
- Foot should be on an A4 paper, with the heel touching 1 edge of the paper
- Floor color should not be white
- Paper must be completly visible (all 4 corners are visible)
## Visualization
Original image:  
![foot image](output/original.png "Original Image")  
Step 1: Segment image  
![segment image](output/segmented.png "Segmented Image")  
Step 2: Detect edges  
![edge image](output/edges.png "Edges Image")  
Step 3: Detect paper bounding box  
![bouding box image](output/paper_rect.png "Paper Bouding Box")  
Step 4: Crop paper  
![cropped image](output/crop.png "Cropped Image")  
Step 5: Detect foot bounding box  
![foot bouding box image](output/foot_rect.png "Foot Bouding Box")
## Convert to shoe size table
| Length (cm) | Width (cm) | Shoe size |
| --- | --- | --- |
| 21          | 7.5 - 8 | 32 |
| 21.1 - 21.5 | 8       | 33 |
| 21.6 - 22   | 8 - 8.5 | 34 |
| 22.1 - 22.5 | 8.5     | 35 |
| 22.6 - 23   |	8.5 - 9 | 36 |
| 23.1 - 23.5 | 9       | 37 |
| 23.6 - 24   |	9 - 9.5 | 38 |
| 24.1 - 24.5 |	9.5     | 39 |
| 24.6 - 25   |	9.5 - 10  | 40 |
| 25.1 - 25.5 |	10        | 41 |
| 25.6 - 26   |	10 - 10.5 | 42 |
| 26.1 - 26.5 |	10.5      | 43 |
| 26.6 - 27   |	10.5 - 11 | 44 |
| > 27        | > 11      | 45 |
