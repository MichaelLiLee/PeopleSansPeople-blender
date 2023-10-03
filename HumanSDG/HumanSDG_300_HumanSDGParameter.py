class HumanSDGParameter:
    """ A configuration class to configure this blender-based synthetic data generator pipeline.

    Attributes
    ----------
    gen_num (int): The quantity of synthetic images needed to be generated.
    blender_exe_path (str): The path to the blender executable[1].
    asset_background_object_folder_path (str): The path to background object assets.
    asset_foreground_object_folder_path (str): The path to foreground object assets.
    asset_occluder_folder_path (str): The path to occlusion object assets.
    asset_ambientCGMaterial_folder_path (str): The path to the downloaded ambientCG PBR materials.
    asset_hdri_lighting_folder_path (str): The path to the downloaded Poly Haven HDRIs.
    asset_animation_folder_path (str): The path to the animation assets directory.
    output_img_path (str): The path where rendered images will be saved.
    output_annotation_path (str): The path where MSCOCO format bounding box and skeleton keypoints annotations will be saved.
    background_poisson_disk_sampling_radius (float): Background objects separation distance.
    num_foreground_object_in_scene_range (dict of str: int): The distribution of the number of virtual humans within the blender scene.
    foreground_area (list of float): Spatial distribution area of foreground objects.
    foreground_poisson_disk_sampling_radius (float): Foreground objects separation distance.
    num_occluder_in_scene_range (dict of str: int): The distribution of the number of occlusion objects within the blender scene.
    occluder_area (list of float): Spatial distribution area of occlusion objects.
    occluder_poisson_disk_sampling_radius (float): Occlusion objects separation distance.
    bg_obj_scale_ratio_range (dict of str: float): The distribution of the scale ratio of background objects within the blender scene.
    fg_obj_scale_ratio_range (dict of str: float): The distribution of the scale ratio of foreground objects within the blender scene.
    occluder_scale_ratio_range (dict of str: float): The distribution of the scale ratio of occluder objects within the blender scene.
    hdri_lighting_strength_range (dict of str: float): The distribution of the strength factor for the intensity of the HDRI scene light.
    camera_focal_length (int): Perspective Camera focal length value in millimeters.
    img_resolution_x (int): Number of horizontal pixels in the rendered image.
    img_resolution_y (int): Number of vertical pixels in the rendered image.
    max_samples (int): Number of samples to render for each pixel.
    chromatic_aberration_probability (float): Probability of chromatic aberration effect being enabled.
    blur_probability (float): Probability of blur effect being enabled.
    motion_blur_probability (float): Probability of motion blur effect being enabled.
    exposure_probability (float): Probability of exposure adjustment being enabled.
    noise_probability (float): Probability of noise effect being enabled.
    white_balance_probability (float): Probability of white balance adjustment being enabled.
    brightness_probability (float): Probability of brightness adjustment being enabled.
    contrast_probability (float): Probability of contrast adjustment being enabled.
    hue_probability (float): Probability of hue adjustment being enabled.
    saturation_probability (float): Probability of saturation adjustment being enabled.
    chromatic_aberration_value_range (dict of str: float): The distribution of the value of Lens Distortion nodes input-Dispersion, which simulates chromatic aberration.
    blur_value_range (dict of str: float): The distribution of the value of Blur nodes input-Size, which controls the blur radius values.
    motion_blur_value_range (dict of str: float): The distribution of the value of Vector Blur nodes input-Speed, which controls the direction of motion.
    exposure_value_range (dict of str: float): The distribution of the value of Exposure nodes input-Exposure, which controls the scalar factor to adjust the exposure.
    noise_value_range (dict of str: float): The distribution of the value of brightness of the noise texture.
    white_balance_value_range (dict of str: float): The distribution of the value of WhiteBalanceNode input-ColorTemperature, which adjust the color temperature.
    brightness_value_range (dict of str: float): The distribution of the value of Bright/Contrast nodes input-Bright, which adjust the brightness.
    contrast_value_range (dict of str: float): The distribution of the value of Bright/Contrast nodes input-Contrast, which adjust the contrast.
    hue_value_range (dict of str: float): The distribution of the value of Hue Saturation Value nodes input-Hue, which adjust the hue.
    saturation_value_range (dict of str: float): The distribution of the value of Hue Saturation Value nodes input-Saturation, which adjust the saturation.

    References
    ----------
    [1]https://docs.blender.org/manual/en/latest/advanced/blender_directory_layout.html

    """
    
    def __init__(self):
        self.gen_num = 400
        self.blender_exe_path = "C:/program Files/Blender Foundation/Blender 3.3/blender"
        self.asset_background_object_folder_path = 'C:/Users/user/Documents/project/synthDet/Asset/background_object'
        self.asset_foreground_object_folder_path = "F:/ProceduralHuman1500"
        self.asset_occluder_folder_path = "C:/Users/user/Documents/project/synthDet/Asset/occluder"
        self.asset_ambientCGMaterial_folder_path = "C:/Users/user/Documents/project/synthDet/Asset/blenderproc_asset/cc_texture"
        self.asset_hdri_lighting_folder_path = "C:/Users/user/Documents/project/synthDet/Asset/Lighting/HDRI"
        self.asset_animation_folder_path = "C:/Users/user/Documents/project/PeopleSansPeople/Asset/Animation/WIP/Frame250"
        self.output_img_path = "F:/PeopleSansPeople_synth40000/images"
        self.output_annotation_path = "F:/PeopleSansPeople_synth40000/annotations_single"
        self.background_poisson_disk_sampling_radius = 0.5
        self.num_foreground_object_in_scene_range = {"min": 1, "max": 6}
        self.foreground_area = [9, 7, 4]
        self.foreground_poisson_disk_sampling_radius = 1.5
        self.num_occluder_in_scene_range = {"min": 5 , "max": 10}
        self.occluder_area = [2.5, 1.5, 0.5]
        self.occluder_poisson_disk_sampling_radius =  0.25
        self.bg_obj_scale_ratio_range = {"min": 6, "max": 6}
        self.fg_obj_scale_ratio_range = {"min": 0.8, "max": 1.5}
        self.occluder_scale_ratio_range = {"min": 0.5, "max": 1.2}
        self.hdri_lighting_strength_range = {"min": 0.1 , "max": 2}
        self.camera_focal_length = 35
        self.img_resolution_x = 640
        self.img_resolution_y = 480
        self.max_samples = 256
        self.chromatic_aberration_probability = 0.1
        self.blur_probability = 0.1
        self.motion_blur_probability = 0.1 
        self.exposure_probability = 0.15
        self.noise_probability = 0.1
        self.white_balance_probability = 0.15
        self.brightness_probability = 0.15
        self.contrast_probability = 0.15
        self.hue_probability = 0.15
        self.saturation_probability = 0.15
        self.chromatic_aberration_value_range = {"min": 0.1, "max": 1}
        self.blur_value_range = {"min": 2, "max": 4}
        self.motion_blur_value_range = {"min": 2, "max": 7}
        self.exposure_value_range = {"min": -0.5, "max": 2}
        self.noise_value_range = {"min": 1.6, "max": 1.8}
        self.white_balance_value_range = {"min": 3500, "max": 9500}
        self.brightness_value_range = {"min": -1, "max": 1}
        self.contrast_value_range = {"min": -1, "max": 5}
        self.hue_value_range =  {"min": 0.45, "max": 0.55}
        self.saturation_value_range = {"min": 0.75, "max": 1.25}