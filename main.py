import shutil

# extract folder

shutil.unpack_archive(
    "/workspaces/codespaces-flask/tf_model.zip",
    "/workspaces/codespaces-flask/model/tf_model_folder",
    "zip",
)
