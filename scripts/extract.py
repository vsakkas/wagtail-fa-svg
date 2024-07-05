import glob
import os

from bs4 import BeautifulSoup
from tqdm import tqdm

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FA_VERSIONS = [
    "5.15.4",
    "6.5.2",
]
FA_DIRECTORIES = ["brands", "regular", "solid"]
APP_NAME = "wagtail_fa_svg"


def process_svg(src_filename: str, directory: str, version: str) -> None:
    """
    Process an SVG file by modifying its content and saving it to a target directory.

    Args:
        src_filename: str
            Path to the source SVG file.
        directory: str
            Directory name ('brands', 'regular', or 'solid').
        version: str
            FontAwesome version.
    """
    # Open and parse the source SVG file.
    with open(src_filename, "r") as src_file:
        soup = BeautifulSoup(src_file.read(), "html.parser")
        tag = soup.find("svg")

        # Modify the SVG tag to add an `id` attribute.
        filename = os.path.basename(src_filename)
        id = os.path.splitext(filename)[0]
        tag["id"] = f"icon-{id}"

        # Determine target file path and directory.
        major_version = version.split(".")[0]
        target_filename = os.path.join(
            BASE_DIR,
            APP_NAME,
            "templates",
            APP_NAME,
            f"v{major_version}",
            directory,
            filename,
        )
        target_dir = os.path.dirname(target_filename)

        # Write modified SVG to the target path.
        os.makedirs(target_dir, exist_ok=True)
        with open(target_filename, "w", encoding="utf-8") as target_file:
            target_file.write(str(tag))


def main() -> None:
    """
    Main function to iterate over FontAwesome versions and directories,
    processing SVG files.
    """
    for version in FA_VERSIONS:
        total_files = 0

        # Calculate total number of SVG files to process.
        for directory in FA_DIRECTORIES:
            src_path = f"fontawesome-free-{version}-web/svgs/{directory}/*.svg"
            svg_files = glob.glob(src_path)
            total_files += len(svg_files)

        progress_bar = tqdm(
            total=total_files,
            desc=f"Extracting FA {version}",
            bar_format="{l_bar}{bar}|{n_fmt}/{total_fmt}",
        )

        # Process SVGs files per FA version.
        for directory in FA_DIRECTORIES:
            src_path = f"fontawesome-free-{version}-web/svgs/{directory}/*.svg"
            svg_files = glob.glob(src_path)

            for src_filename in svg_files:
                process_svg(src_filename, directory, version)
                progress_bar.update(1)

        progress_bar.close()


if __name__ == "__main__":
    main()
