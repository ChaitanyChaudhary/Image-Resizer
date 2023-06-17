import cv2

print("\nWelecome to Image-Resizer. Created by Chaitany\n")

# Ask for user input
source = input("Enter your input image name with extension: ")
destination = input("Enter your output image name with extension: ")
new_width = int(input("Enter your image width: "))
new_height = int(input("Enter your image height: "))

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow("title", src)

# resize image
output = cv2.resize(src, (new_width, new_height),  interpolation=cv2.INTER_AREA)

cv2.imwrite(destination, output)

# cv2.waitKey(0)