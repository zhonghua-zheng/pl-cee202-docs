# Maintain Website

## Prerequisites

- Clone the GitHub from `https://github.com/zzheng93/pl-cee202-docs`
- Have the markdown file `*.md` ready. This file will be a page for this website

## Step 1: Include your markdown file

- Include your markdown file in the folder `pl-cee202-docs/source/page/`

  Note: if your Markdown file name is `intro.md`, and you want this page to be under the section `WEBSITE DEVELOPERS`, then the directory of this file is `pl-cee202-docs/source/page/web/intro.md`. 

## Step 2: Update the index.rst

**Important: `Heading 1`** of your markdown file (**not your markdown file name**) will be the section name showing on the webpage.

* Use text editor (such as [Notepad++](https://notepad-plus-plus.org/) on **Windows** or [Sublime Text](https://www.sublimetext.com/3) on **MacOS/Linux**) to open the `index.rst` (by the directory `pl-cee202-docs/source/index.rst`)
* Find the following contents (note: the name will be slightly different). 

```rst
Contents
--------
.. toctree::
   :maxdepth: 2
   :caption: Students

   page/student/<*.md>

.. toctree::
   :maxdepth: 2
   :caption: Instructors/TAs

   page/instructor_TA/<*.md>
   
.. toctree::
   :maxdepth: 2
   :caption: Website Developers

   page/web/markdown_intro.md
   page/web/maintain_site.md
```

* If you want to add your page under the `"Website Develops"` section in the left panel, add the name `page/web/intro.md` under the corresponding section `:caption: Website Developers`. Note the difference. Here you don't need to include the path prefix `"pl-cee202-docs/source/"`, because you only need to define the [relative path](https://support.dtsearch.com/webhelp/dtsearch/relative_paths.htm).

```rst
Contents
--------
.. toctree::
   :maxdepth: 2
   :caption: Students
   
   page/student/<*.md>

.. toctree::
   :maxdepth: 2
   :caption: Instructors/TAs
   
   page/instructor_TA/<*.md>
   
.. toctree::
   :maxdepth: 2
   :caption: Website Developers

   page/web/markdown_intro.md
   page/web/maintain_site.md
   page/web/intro.md
```

## Step 3: Commit and push to Github

- You need to have the GitHub permission to do so.