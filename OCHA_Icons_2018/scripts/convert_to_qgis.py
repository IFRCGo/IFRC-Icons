import os

sourceDir = '../original_un_blue_versions/svg'
destDir = '../qgis_versions/svg'

files = os.listdir(sourceDir)
for file in files:
    sourceFile = os.path.join(sourceDir, file)
    destFile = os.path.join(destDir, file)
    #print(sourceFile)
    #print(destFile)

    with open(sourceFile) as file:
        s = file.read()
    s = s.replace('<path class="cls-1"', '<path fill="param(fill)" stroke="param(outline)" stroke-width="param(outline-width) 0" ')
    s = s.replace('<polygon class="cls-1"', '<polygon fill="param(fill)" stroke="param(outline)" stroke-width="param(outline-width) 0" ')
    s = s.replace('<circle class="cls-1"', '<circle fill="param(fill)" stroke="param(outline)" stroke-width="param(outline-width) 0" ')
    s = s.replace('<circle class="cls-2"', '<circle fill="param(fill)" stroke="param(outline)" stroke-width="param(outline-width) 0" ')
    s = s.replace('<rect class="cls-1"', '<rect fill="param(fill)" stroke="param(outline)" stroke-width="param(outline-width) 0" ')
    with open(destFile, "w") as file:
        file.write(s)
