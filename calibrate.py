from UndistortFishEye import fisheye_module
import argparse


# Python script to launch calibration process from terminal
# Usage: calibrate.py "folder_of_calibration_images" "output_path"
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "image_folder",
        help="Folder where the calibration images are stored"
    )

    parser.add_argument(
        "-o",
        dest="output_file_path",
        default="calibration.txt",
        help="Path where the calibration file will be saved"
    )

    parser.add_argument(
        "-s",
        dest="save_detection",
        default=False,
        help="Path where the calibration file will be saved"
    )

    args = parser.parse_args()
    if not args.image_folder:
        raise RuntimeError("Folder of calibration images is required")

    k, d, dims = fisheye_module.calibrate("fisheye", True)
    print('----- Calibration results -----')
    print("Dimensions =" + str(dims))
    print("K = np.array(" + str(k.tolist()) + ")")
    print("D = np.array(" + str(d.tolist()) + ")")
    result_path = "E:\\source\\PycharmProjects\\FishEyeModel\\result"
    print("output_file_path {}".format(result_path))
    fisheye_module.save_calibration(result_path, k, d, dims)
    print("Calibration file saved successfully")

