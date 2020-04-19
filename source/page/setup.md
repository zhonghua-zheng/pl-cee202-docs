# How to run PrairieLearn?

For more information, please check [HERE](https://prairielearn.readthedocs.io/en/latest/installing/).

## Install and check (for first time users)

* **Step 1**: Install [Docker Community Edition](https://www.docker.com/community-edition).

* **Step 2**: Open a terminal, such as [iTerm2](https://www.iterm2.com/) (on **MacOS/Linux**), and run PrairieLearn using the example course with

  ```bash
  docker run -it --rm -p 3000:3000 prairielearn/prairielearn
  ```

* **Step 3**: Open a web browser and connect to [http://localhost:3000/pl](http://localhost:3000/pl)
* **Step 4**: Click the button **`Load from disk`** in the upper right, then play with it.
* **Step 5**: When you are finished with PrairieLearn, type `Control-C` on the commandline where your ran the server to stop it.

## Routine work

* **Step 1**: Upgrade your Docker's version on PrairieLearn

  ```bash
  docker pull prairielearn/prairielearn
  ```

* **Step 2**: To use your own course, use the `-v` flag to bind the Docker `/course` directory with your own course directory (replace the precise path with your own). 

  on **Windows**:

  ```sh
  docker run -it --rm -p 3000:3000 -v C:\GitHub\pl-cee202:/course prairielearn/prairielearn
  ```

  or on **MacOS/Linux**:

  ```sh
  docker run -it --rm -p 3000:3000 -v /Users/zzheng25/git/pl-cee202:/course prairielearn/prairielearn
  ```

* **Step 3**: Open a web browser and connect to [http://localhost:3000/pl](http://localhost:3000/pl)
* **Step 4**: Click the button **`Load from disk`** in the upper right, then work on it.
* **Step 5**: When you are finished with PrairieLearn, type `Control-C` on the commandline where your ran the server to stop it.