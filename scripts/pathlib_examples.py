from pathlib import Path
from datetime import datetime
import zipfile

# p1 = Path("../data")
# # print(list(p1.iterdir()))
#
# p2 = Path("../data/test.txt")
#
# if not p2.exists():
#     with open(p2, 'w') as f:
#         f.write("Data Content")
#
# # print(p2.name, p2.stem, p2.suffix)
#
# # Lambda function
# # x = lambda a, b: a * b
# # print(x(5, 6))
#
#
# # rename the files with prefix
# dir = Path('../data/testdatas3/nba1')
# # print(Path.cwd())
# for path in dir.iterdir():
#     # print(path)
#     new_filename = "new-" + path.stem + path.suffix
#     # print(new_filename)
#     new_filepath = path.with_name(new_filename)
#     # print(new_filepath)
#     path.rename(new_filepath)
#
#
# # Rename All Files Based on Folder - adding folders name as prefix
#
# root_dir = Path('../data/Months')
# file_paths = root_dir.glob("**/*")
#
# for path in file_paths:
#     # print(path)
#     if path.is_file():
#         # print(path)
#         parent_folder = path.parts[-2]
#         # print(parent_folder)
#         new_filename = parent_folder + '-' + path.name
#         # print(new_filename)
#         new_filepath = path.with_name(new_filename)
#         # print(new_filepath)
#         path.rename(new_filepath)
#
#
# # Rename All Files Based on Sub-Sub-Folders
# root_dir = Path('../data/year-month')
# # print(root_dir)
# file_paths = root_dir.glob("**/*")
#
# for path in file_paths:
#     # print(path)
#     if path.is_file():
#         # print(path)
#         path_parts = path.parts
#         # print(path_parts)
#         sub_folders = path_parts[3:-1]
#         # print(sub_folders)
#
#         new_filename = "-".join(sub_folders) + "-" + path.name
#         # print(new_filename)
#         new_filepath = path.with_name(new_filename)
#         # print(new_filepath)
#         path.rename(new_filepath)
#
# # Access file created date-time and then convert it to string
# path = Path('../data/Months-date/January/report.txt')
# stats = path.stat()
# second_created = stats.st_ctime
# date_created = datetime.fromtimestamp(second_created)
# date_created_str = date_created.strftime("%Y-%m-%d_%H:%M:%S")
#
# print(second_created)
# print(date_created)
# print(date_created_str)
#
#
# # Add Created Date to All Filenames in Folder
# root_dir = Path('../data/Months-date')
# file_paths = root_dir.glob("**/*")
#
# for path in file_paths:
#     # print(path)
#     if path.is_file():
#
#         # get created date
#         stats = path.stat()
#         second_created = stats.st_ctime
#         date_created = datetime.fromtimestamp(second_created)
#         date_created_str = date_created.strftime("%Y-%m-%d_%H:%M:%S")
#
#         new_filename = date_created_str + '_' + path.name
#         # print(new_filename)
#         new_filepath = path.with_name(new_filename)
#         # print(new_filepath)
#         path.rename(new_filepath)


# Change File Extensions
# root_dir = Path('../data/testdatas3/nba2')
# file_paths = root_dir.rglob("*.csv")
#
# for path in file_paths:
#     # print(path)
#     if path.is_file():
#
#         new_filepath = path.with_suffix(".txt")
#         path.rename(new_filepath)


# Create Empty Files
# root_dir = Path('../data/testdatas3/nba2')
#
# for i in range(10, 15):
#     filename = str(i) + ".txt"
#     filenpath = root_dir / Path(filename)
#     filenpath.touch()

# Create Archive from Files
# root_dir = Path('../data/testdatas3/nba2')
# archive_path = root_dir / Path('archive.zip')
#
# with zipfile.ZipFile(archive_path, 'w') as zf:
#     for path in root_dir.rglob("*.txt"):
#         zf.write(path)

# Extract All ZIP Files
# root_dir = Path('../data/testdatas3/nba2')
# destination_path = root_dir / Path('destination')
#
# for path in root_dir.glob("*.zip"):
#     with zipfile.ZipFile(path, 'r') as zf:
#         final_path = destination_path / Path(path.stem)
#         zf.extractall(path=final_path)

# Search File in Computer
# root_dir = Path('../data/testdatas3/nba2')
# search_term = '12'
#
# for path in root_dir.rglob("*"):
#     if search_term in path.stem:
#         print(path.absolute())


# Destroy files forever
root_dir = Path('../data/testdatas3/nba2')

for path in root_dir.glob("*.txt"):
    with open(path, 'wb') as f:
        f.write(b'')
    path.unlink()

