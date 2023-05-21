import os

def generate_file_list(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(file)
    return file_list

def generate_html(file_list, team_name):
    html = f"<h2>{team_name}</h2>\n<ul>\n"
    for file in file_list:
        html += f"  <li><a href='{file}' download>{file}</a></li>\n"
    html += "</ul>\n"
    return html

html = "<!DOCTYPE html>\n<html>\n<head>\n  <title>PDF Files</title>\n</head>\n<body>\n"
html += "<h1>PDF Files</h1>\n"

# Generate file list and HTML for Stuttgart Silver Arrows
ssa_directory = "stats/SSA"
ssa_files = generate_file_list(ssa_directory)
html += generate_html(ssa_files, "Stuttgart Silver Arrows")

# Generate file list and HTML for Albershausen Crusaders
ac_directory = "stats/AC"
ac_files = generate_file_list(ac_directory)
html += generate_html(ac_files, "Albershausen Crusaders")

html += "</body>\n</html>"

# Save the generated HTML code to a file
with open("index.html", "w") as file:
    file.write(html)