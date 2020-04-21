# Maintain Website

## Prerequisites

- Clone the GitHub from `https://github.com/zzheng93/pl-cee202-docs`
- Have the markdown file `*.md` ready. This file will be a page for this website

## Step 1: Include your markdown file

- Include your markdown file in the folder `pl-cee202-docs/source/page/`

  Note: if your markdown file name is `"intro.md"`, then the directory of this file is `pl-cee202-docs/source/page/intro.md`

## Step 2: Update the index.rst

**\**Important: `Heading 1`** of your markdown file (**not your markdown file name**) will be the section name showing on the webpage.**\****

1. Use text editor (such as [Notepad++](https://notepad-plus-plus.org/) on **Windows** or [Sublime Text](https://www.sublimetext.com/3) on **MacOS/Linux**) to open the `index.rst` (by the directory `pl-cee202-docs/source/index.rst`)
2. Find the following contents (note: the name will be slightly different)

```rst
Contents
--------
.. toctree::
   :maxdepth: 2
   :caption: Students

	 page/<*.md>

.. toctree::
   :maxdepth: 2
   :caption: Instructors/TAs

	 page/<*.md>
   
.. toctree::
   :maxdepth: 2
   :caption: Website Developers

   page/markdown_intro.md
   page/maintain_site.md
```

3. If you want to add your file `intro.md` under the `"Website Develops"` section, add the name `page/intro.md` under the corresponding section `:caption: Website Developers`. Note the difference.

```rst
Contents
--------
.. toctree::
   :maxdepth: 2
   :caption: Students
	 
	 page/<*.md>

.. toctree::
   :maxdepth: 2
   :caption: Instructors/TAs

   page/<*.md>
   
.. toctree::
   :maxdepth: 2
   :caption: Website Developers

   page/markdown_intro.md
   page/maintain_site.md
   page/intro.md
```

## Step 3: Commit and push to Github

- You need to have the permission to do so.