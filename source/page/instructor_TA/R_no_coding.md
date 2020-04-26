# R Questions (without coding)

This page is specific to the **R** questions (**without coding**). The objective is:

- Use the necessary R function in the `server.py` to generate the solutions, and grade the questions
- Specify the randomized variables in the `server.py`
- Specify the specific files (e.g., **figure**) in the `server.py`

## Overview

The easiest way to create a R question (without coding) is by copying an existing R question, and change certain files. Then you don't need to create the [UUID](https://www.uuidgenerator.net/) by yourself.

Note: Each UUID will be assigned to a question only.

## Step 1: Copy a R question

* Follow the Step 1 to Step 4 in the **[Routine work](https://pl-cee202-docs.readthedocs.io/en/latest/page/setup.html#routine-work)**. Then click **PrarieLearn** logo (next to **Admin**) in the upper left.

* Click a course such as **`CEE 202: Engineering Risk & Uncertainty`** in the `Courses` (not `Course instances`) list.

* Click the `Questions` (next to `Issues`) on the top line.

* Find a question you want to copy (for example: `AS4_Prob5_2020_AngTang`).

* Click `Settings` between `Preview` and `Statistics`.

* Click `Make a copy of this question`

* Click `Change QID`

## Step 2: Modify the questions

Before you modifying the question, I strongly suggest creating a **spreadsheet** to keep track of the questions (including title, topic, tags) and corresponding UUID.

Note: Each question folder contain the following files

| Folder/File Name                 | Usage                                                        |
| -------------------------------- | ------------------------------------------------------------ |
| info.json                        | The information of the question such as title, topic, tags, and uuid. |
| question.html                    | The main body of the question                                |
| server.py                        | The solution to the question, but it also species            |
| clientFilesQuestion              | Save the figures for the question.                           |
| clientFilesQuestion<br>/dist.png | The figure needes to be added to the question                |

### info.json

* Click `Edit` under `Settings`
* Define the `title`, `topic`, `tags`, and `type`

### server.py

* Click `Files` (under `PrairieLearn` in the upper left) &rightarrow; `Edit` the `server.py`, then you need to finish the following tasks:

```python
import rpy2.robjects as robjects
import prairielearn as pl

def generate(data):
    # here is the start the R function
    values = robjects.r("""
    # prob 1
    #a_r = 4.0
    a_r = sample(seq(3.8,4.3,0.1),1)
    ans_a_r = 1 + a_r
    
    # Export
    list(  
         ans = list(a=a_r,
                    answer_a=ans_a_r)
       )
    """)
    # here is the end of the R function
    ans = values[0]
    # Convert from R lists to python dictionaries
    ans = { key : ans.rx2(key)[0] for key in ans.names }
    # Setup output 
    data['correct_answers'] = ans
    # Setup randomized variables
    data["params"] = ans
    # define the figure name
    image_name = "dist.png"
    data["params"]["image"] = image_name
```

* Change the randomized variable using `a_r=sample(seq(start,end,interval),1)`

* Change the answers (`ans_a_r`, `ans_b_r`, ...), and export  (`list(...)`)

Note: `a` corresponds to `${{params.a}}$`, `answer_a` corresponds to `answers-name="answer_a"` in the `question.html`

* Change the `image_name`

### question.html

* Click `Files` (under `PrairieLearn` in the upper left) &rightarrow; `Edit` the `question.html`, then you need to finish the following tasks:

```html
<pl-question-panel>
	<p> 
	This is the problem statement.
	</p>
	<pl-figure file-name={{params.image}} directory="clientFilesQuestion"></pl-figure>
</pl-question-panel>

<pl-question-panel><hr></pl-question-panel>
<pl-question-panel>
	<p>
	    (a) Determine the probability that the settlement will exceed ${{params.a}}$ cm.
	</p>
</pl-question-panel>

<div class="card my-2">
  <div class="card-body">
    <pl-question-panel>
      <p>The answer is: (0.XX)</p>
    </pl-question-panel>
    <pl-number-input answers-name="answer_a" weight = "3" comparison="relabs" rtol="0.01" atol="0.01"></pl-number-input>
  </div>
</div>
```

* Replace "This is the problem statement." with your **problem statement**
* Replace `${{params.a}}$` with your randomized variable from `server.py` 
* Replace `"answer_a"` with your answer from `server.py`
* Define the tolerance. Sotiria suggests that: 
  * for the answer (0.XX), `comparison="relabs" rtol="0.01" atol="0.01"`
  * for the answer (0.XXX), `comparison="relabs" rtol="0.001" atol="0.001"`

## Step 3: Test your questions

* Click `Preview` to test

* Click `New variant` to have another test

## Step 4: Commit and push the changes

* Using Git to commit and push the changes

Note: You may do this after you finish all the questions

## Step 5: Sync and test 

* Log in the website https://prairielearn.engr.illinois.edu/pl/, and select your course
* Click `Sync`, then `Pull from remote git repository`
* Find your questions by clicking `Questions` and test them again