# Review of autograding example R notebook

By Advai Podduturi (Department of CS, University of Illinois, Urbana-Champaign, IL, USA)

## About

This guide will cover how to write a deploy an R notebook as an autogradable assignment on Prairielearn. 

## Directory Structures
```bash
WSXX_Example_Topic
|   info.json
|   question.html
|
|___tests
|   points.json
|   |   ans1.R
|   |   ans2.R
|   |   ans3.R
|   |___tests
|   |   |   test1.R
|   |   |   test2.R
|   |   |   test3.R
|   |
|___workspace
|   | Workbook.ipynb
|   
```

## Explaining the files

`info.json` 

```python
{
    "uuid": "09b1ad17-f022-4189-b5ce-250743b8f969",
    "title": "WSXX Example Topic",
    "topic": "Basic R Notebook",
    "tags": [
        "Spring2022",
        "Sotiria",
        "Priyam",
        "CLT",
        "Jupyter"
    ],
    "type": "v3",
    "singleVariant": true,
    "workspaceOptions": {
        "image": "prairielearn/workspace-jupyterlab",
        "port": 8080,
        "home": "/home/jovyan",
        "rewriteUrl": false,
        "gradedFiles": [
            "Workbook.ipynb"
        ]
    },
    "gradingMethod": "External",
    "externalGradingOptions": {
        "enabled": true,
        "image": "advai/grader-r-advai",
        "serverFilesCourse": [
            "r_autograder/"
        ],
        "entrypoint": "/grade/serverFilesCourse/r_autograder/run.sh",
        "timeout": 20
    }
}

```

If you are coding a new problem while using the same autograder, the things to change would be the `uuid`, `title`, `topic`, `tags`, and `timeout` under the `externalGradingOptions`. The `timeout` is the time in seconds that is allowed for each student submission to be processed. Submission is considered incorrect  if it runs longer than the `timeout` duration. Try to keep it minimum (typically 5 to 10 seconds for a small problem, simulations take longer). 

The R notebook autograder image is stored under advai/grader-r-advai. 

`question.html`

I typically use the same template for this that just displays the button for opening the Prairielearn Jupyter interface. 

```html
<pl-question-panel>
  <p>This is a workspace question with an in-browser <a href="https://jupyter.org">JupyterLab</a>.
  </p>

  <p>
      In this worksheet, you will be learning about and understanding "Example Topic". 
  </p>

  <p>
      Once in the JupyterLab environment, please, open workbook called <b>Workbook.ipynb</b>. After you complete your code in it, save the workbook and come back to this Prairie Learn question window to click Save and Grade button. Ignore the other .ipynb workspace you see. </p>

  <pl-external-grader-variables params-name="names_from_user"></pl-external-grader-variables>

  <pl-workspace></pl-workspace>
</pl-question-panel>

<pl-submission-panel>
  <pl-external-grader-results></pl-external-grader-results>
  <pl-file-preview></pl-file-preview>
</pl-submission-panel>

```
## Subdirectory: `tests`
`points.json`

You can define any number of tests you want by just creating more test files under tests/tests. To assign points to these tests, you need to edit the points.json. 

```python
[
    {
        "name":"Test 1",
        "file":"test1.R",
        "max_points":1
    },
    
    {
        "name":"Test 2",
        "file":"test2.R",
        "max_points":3
    },
    
    {
        "name":"Test 3",
        "file":"test3.R",
        "max_points":5
    }
]
```
`ans1.R`
```R
#grade {p1_t0, p1_ta, p1_pvalue}
#1) Fixed probability track 
#calculate the t-statistic from the data
p1_alpha<- 0.05 # Alpha Value
p1_xbar <- 1.9 # Sample Mean of 25 trips
p1_mu<- 2.0 # Traditional fuel intensity
p1_s<- 0.2 # Standard deviaion
p1_n<- 25 # Sample size
p1_t0 <- round((p1_xbar - p1_mu)/ (p1_s/p1_n^0.5), 3) # critical value of null

#find the t-value for the significance level 0.05 with n-1 dof
p1_ta <- round(qt(p1_alpha, (p1_n-1), lower.tail=TRUE, log.p=FALSE), 3) # critical value of alternative

p1_pvalue <- round(pt(p1_t0, (p1_n-1), lower.tail=TRUE, log.p=FALSE), 3) # P value

```
Here we can see that all the supporting variables for the p1_t0, p1_ta, and p1_pvalue computations are available in the ans1.R file. Not including the right variables is a common way to make bugs when autograding R notebooks. **Use unique variable names across testX/ansX.R files or they will clash and cause one of the tests to fail.**

`tests/test1.R`
I will only go over one test for brevity but consult the tests folder of any question in the PL-CEE202 question bank for more examples of tests. I will highlight three important notes
1. All of the student's code from the notebook gets written to `/grade/student/stcode.R` so be sure to source from that location. 
2. Be sure to add #grade tags to all essential cells so that all the important supporting data is written to `grade/student/stcode.R`. 
3. Use unique variable names across tests or they will clash. A common approach is "pX_variable". 

You test code by sourcing the student's value for a variable and then sourcing the correct value from the `ansX.R` file. You can compare them using expect_equivalent_with_diff() as shown below. 

```R
Sys.chmod("/grade/student/stcode.R", mode="0664")
student_p1_t0 <- unix::eval_safe({source("/grade/student/stcode.R"); p1_t0}, uid=1001)
student_p1_ta <- unix::eval_safe({source("/grade/student/stcode.R"); p1_ta}, uid=1001)
student_p1_pvalue <- unix::eval_safe({source("/grade/student/stcode.R"); p1_pvalue}, uid=1001)

source("/grade/tests/ans1.R")
correct_p1_t0 <- p1_t0
correct_p1_ta <- p1_ta
correct_p1_pvalue <- p1_pvalue

using(ttdo)
expect_equivalent_with_diff(student_p1_t0, correct_p1_t0, mode="unified", format="ansi256")
expect_equivalent_with_diff(student_p1_ta, correct_p1_ta, mode="unified", format="ansi256")
expect_equivalent_with_diff(student_p1_pvalue, correct_p1_pvalue, mode="unified", format="ansi256")
```
## Subdirectory `workspace`
`Workbook.ipynb`

It is imperative that the notebook be named "Workbook.ipynb" or the autograder will not pick it up. Typically, notebooks are designed as lesson plans. To grade a cell in the notebook, simply add 
```python
#grade
```
to the top of the cell. Note: if a problem uses variables across multiple cells, then you need #grade tags in all those cells. 

# Testing gradability of your R Notebook
The intial set up is the hardest/longest part. After that, developing in a local PL env is very easy. 

## Setting up local development environment
1. [Install docker](https://docs.docker.com/get-docker/)
2. [Clone the PL CEE Repo](https://github.com/PrairieLearn/pl-cee202)
Now you should be able to launch a local PL instance by running 
```bash
./runMe.sh
```
## Adding notebook to course directory
Create a new folder in `questions/` for your worksheet and fill out all the relevant content descirbed above. Then you can navigate to [http://localhost:3000/](http://localhost:3000/) to view your question. 

You should also create a copy of the folder and add `_filled` to the end of the folder name. This is where you safely store your filled notebook without risk of leaking it to students. **Make sure to change the uuid in the `info.json` or it will clash with the original problem in PL.**

## Testing
It's important to test that each individual question grades since students will work incrementally. Launch the question and replace each cell block with the filled cell block and grade to ensure the question is being graded properly. 

## Deploying to live PL

# Final Thoughts
`questions/WS13_Central_Limit_Theorem` is a great example question to reference. 
