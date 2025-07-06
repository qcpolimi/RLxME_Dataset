import zipfile


def extract_zip(zip_path, extract_path):
    with zipfile.ZipFile(zip_path, "r") as zipf:
        zipf.extractall(extract_path)


def extract_graphs_set(root, set_name):
    set_path = f"{root}/{set_name}.zip"
    set_extract = f"{root}/{set_name}/"
    extract_zip(set_path, set_extract)


def extract_all_graphs(root):
    extract_graphs_set(root, "training")
    extract_graphs_set(root, "testing")


extract_all_graphs("./dataset")
