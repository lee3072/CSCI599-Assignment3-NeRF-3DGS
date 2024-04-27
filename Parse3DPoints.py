import read_write_model

# Create a dictionary to store the sum of errors and counts for each image
image_errors = {}
image_counts = {}

# Process each line in the points3D.txt file
with open('data/nerfstudio/LivingRoom/colmap/sparse/0/points3D.txt', 'r') as file:
    for line in file:
        if line.startswith('#'):
            continue
        parts = line.split()
        error = float(parts[7])
        track_data = parts[8:]  # This will contain pairs of (IMAGE_ID, POINT2D_IDX)

        # Iterate through each pair
        for i in range(0, len(track_data), 2):
            image_id = int(track_data[i])
            # We ignore POINT2D_IDX because we're summing errors based on image_id only
            
            if image_id not in image_errors:
                image_errors[image_id] = 0
                image_counts[image_id] = 0
            
            image_errors[image_id] += error
            image_counts[image_id] += 1

# Calculate average error per image
average_errors = {image_id: image_errors[image_id] / image_counts[image_id] for image_id in image_errors if image_counts[image_id] > 0}

if average_errors:
    overall_average_error = sum(average_errors.values()) / len(average_errors)
else:
    overall_average_error = 0

print("COLMAP - Overall average reprojection error across all images:", overall_average_error)

