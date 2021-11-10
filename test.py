import glob
import cv2
from UndistortFishEye import fisheye_module
import argparse


# Python script to launch calibration process from terminal
# Usage: calibrate.py "folder_of_calibration_images" "output_path"
if __name__ == '__main__':

    # images = glob.glob("E:\\source\\PycharmProjects\\FishEyeModel\\fisheye\\" + '/*.jpg')
    # for filename in images:
    #     img = cv2.imread(filename)
    #     newFileName = filename[0:-4]+".png"
    #     cv2.imwrite(newFileName, img)

    img_folder = "fisheye\\img"

    k, d, dims = fisheye_module.calibrate(img_folder, True)

    print('----- Calibration results -----')
    print("Dimensions =" + str(dims))
    print("K = np.array(" + str(k.tolist()) + ")")
    print("D = np.array(" + str(d.tolist()) + ")")
    # fisheye_module.save_calibration(result_path, k, d, dims)
    print("Calibration file saved successfully")

    images = glob.glob(img_folder + '/*.png')
    for filename in images:

        undistorted_img = fisheye_module.undistort_from_file(filename, k, d, dims)
        # save_img = filename[0:-4]+"_result.png"
        # fisheye_module.save_image(undistorted_img, save_img)