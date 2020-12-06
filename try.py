import win32com.client
import pandas as pd
import os
from conf import Intro_and_End_DIR, DOWNLOADED_IMAGE_DIR
from photoshop import Session
from PIL import Image

psApp = win32com.client.Dispatch("Photoshop.Application")
psApp.Open(os.path.join(Intro_and_End_DIR, "Intro.psd"))
active_doc = psApp.Application.ActiveDocument


# saveAs JPEG:
def saveAsJEPG(folder_path, filename):  # provide filename as string
    option = win32com.client.Dispatch("Photoshop.ExportOptionsSaveForWeb")
    option.Format = 6
    option.Quality = 100

    export_path_parent_folder = folder_path  # provide folder path
    export_path = export_path_parent_folder + "\\" + filename + ".jpg"
    active_doc.Export(ExportIn=export_path, ExportAs=2, Options=option)


# saveAs PNG:
def saveAsPNG(folder_path, filename):  # provide filename as string
    option = win32com.client.Dispatch("Photoshop.ExportOptionsSaveForWeb")
    option.Format = 13
    option.PNG8 = False

    export_path_parent_folder = folder_path  # provide folder path
    export_path = export_path_parent_folder + "\\" + filename + ".png"
    active_doc.Export(ExportIn=export_path, ExportAs=2, Options=option)


def paragraph(layer_name, text_input, fontSize):
    layerText_main = active_doc.ArtLayers(layer_name)
    text_of_layerText_main = layerText_main.TextItem
    text_of_layerText_main.contents = text_input
    text_of_layerText_main.size = fontSize


def auto_font_size(string):
    if len(string) >= 310:
        return 12
    elif 310 > len(string) >= 190:
        return 15
    else:
        return 20


def replace_image_in_layer(image_to_beReplaced_file_path, layer_name):
    """replaces image in an existing layer. Ex. if a layer called 'background' needs image to be replaced
    from ..folder/folder/image.jpg , use argument: (r"..folder/folder/image.jpg", "background)

    >> import requirement: from photoshop import Session"""

    active_doc.ActiveLayer = (active_doc.ArtLayers[layer_name])
    with Session() as ps:
        replace_contents = ps.app.stringIDToTypeID("placedLayerReplaceContents")
        desc = ps.ActionDescriptor
        idnull = ps.app.charIDToTypeID("null")
        desc.putPath(idnull, image_to_beReplaced_file_path)
        ps.app.executeAction(replace_contents, desc)


def image_same_size_maker(image_path, output_size):
    """output_size: takes a tuple. Ex: (1900, 1200)"""
    if image_path.endswith(".jpg"):
        im = Image.open(image_path)
        original_size = im.size
        if original_size != output_size:
            im = im.resize(output_size)
            im.save(image_path)


if __name__ == '__main__':

    background_image_list = os.listdir(DOWNLOADED_IMAGE_DIR)
    background_image_list_paths = [os.path.join(DOWNLOADED_IMAGE_DIR, fname) for fname in background_image_list if
                                   fname.endswith(".jpg")]
    for i in background_image_list_paths:
        replace_image_in_layer(i, "BG")
